# Generated by Django 4.0.5 on 2022-08-12 14:59
from django.apps import apps as applications
from django.core.files import File
from django.db import migrations, transaction

from initial_data.post_data import post_data

User = applications.get_model('user', 'User')
Post = applications.get_model('post', 'Post')
Photo = applications.get_model('post', 'Photo')
Tag = applications.get_model('post', 'Tag')


@transaction.atomic
def create_initial_posts(apps, schema_editor):
    user1 = User.objects.get(username='dafna')
    user2 = User.objects.get(username='richard')

    Post.objects.bulk_create([
        Post(body=post_data['post_body'][0], creator=user1, _order=0),
        Post(body=post_data['post_body'][1], creator=user1, _order=1),
        Post(body=post_data['post_body'][2], creator=user2, _order=0),
        Post(body=post_data['post_body'][3], creator=user2, _order=1)
    ])

    tags = []
    for index, post in enumerate(Post.objects.all()):
        for i, tag_name in enumerate(post_data['tags'][index]):
            tags.append(Tag(tag_name=tag_name, post=post, _order=i))
    Tag.objects.bulk_create(tags)

    photos = []
    for index, post in enumerate(Post.objects.all()):
        index += 1
        photo_file = File(open(f'initial_data/post_data/images/test_photo_{index}.jpeg', 'rb'))
        photos.append(Photo(image=photo_file, post=post, _order=0))
        if index == 4:
            index += 1
            photo_file = File(open(f'initial_data/post_data/images/test_photo_{index}.jpeg', 'rb'))
            photos.append(Photo(image=photo_file, post=post, _order=1))
    Photo.objects.bulk_create(photos)


@transaction.atomic
def revert_create_initial_posts(apps, schema_editor):
    Post.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('post', '0002_initial'),
        ('user', '0002_add_initial_users'),
    ]

    operations = [
        migrations.RunPython(create_initial_posts, revert_create_initial_posts)
    ]
