from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile
from django.test import TestCase

from apps.user.forms import UserUpdateForm
from apps.user.models import User


class TestUserUpdateForm(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', email='t@mail.ru', password='1234')
        self.valid_form_data = {
            'username': 'username',
            'email': 'e@mail.com',
            'first_name': 'user',
            'last_name': 'test',
            'bio': 'Test user bio.'
        }

    def test_valid_data(self):
        """Form validates correct data."""
        form = UserUpdateForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        """Form displays an error if required fields are empty."""
        form_data = {
            'username': '',
            'email': '',
        }
        form = UserUpdateForm(data=form_data)
        self.assertEqual(form.errors['username'], ['Обязательное поле.'])
        self.assertEqual(form.errors['email'], ['Обязательное поле.'])

    def test_already_existing_data(self):
        """Form displays an error if fields are populated with already existing data."""
        form_data = {
            'username': 'test',
            'email': 't@mail.ru',
        }
        form = UserUpdateForm(data=form_data)
        self.assertEqual(form.errors['email'], ['Пользователь с таким Адрес электронной почты уже существует.'])
        self.assertEqual(form.errors['username'], ['Пользователь с таким именем уже существует.'])

    def test_invalid_data(self):
        """Form displays an error if fields are populated with incorrect data."""
        form_data = {
            'email': '111',
            'username': 'x' * 151,
            'first_name': 'y' * 152,
            'last_name': 'z' * 153,
            'bio': 'a' * 1001
        }
        form = UserUpdateForm(data=form_data)
        self.assertEqual(form.errors['email'], ['Введите правильный адрес электронной почты.'])
        self.assertEqual(form.errors['username'],
                         ['Убедитесь, что это значение содержит не более 150 символов (сейчас 151).'])
        self.assertEqual(form.errors['first_name'],
                         ['Убедитесь, что это значение содержит не более 150 символов (сейчас 152).'])
        self.assertEqual(form.errors['last_name'],
                         ['Убедитесь, что это значение содержит не более 150 символов (сейчас 153).'])
        self.assertEqual(form.errors['bio'],
                         ['Убедитесь, что это значение содержит не более 1000 символов (сейчас 1001).'])

    def test_file_data(self):
        """Form validates image files."""
        im = Image.new(mode='RGB', size=(200, 200))
        im_io = BytesIO()
        im.save(im_io, 'JPEG')
        im_io.seek(0)

        image = InMemoryUploadedFile(
            im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None
        )

        file_data = {'avatar': image}

        form = UserUpdateForm(data=self.valid_form_data, files=file_data)
        self.assertTrue(form.is_valid())

    def test_invalid_file_data(self):
        """Form displays an error if image field is populated with incorrect data."""
        loaded_file = BytesIO(b"some data: \x00\x01")
        loaded_file.name = 'test_file_name.xls'
        file = SimpleUploadedFile(loaded_file.name, loaded_file.read())
        file_data = {'avatar': file}
        form = UserUpdateForm(data=self.valid_form_data, files=file_data)
        self.assertEqual(form.errors['avatar'],
                         ['Загрузите правильное изображение. Файл, который вы загрузили, '
                          'поврежден или не является изображением.'])
