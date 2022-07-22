import typing

if typing.TYPE_CHECKING:
    from apps.post import models


class FilePathProcessor:
    """Processor for paths of uploaded images."""

    @classmethod
    def get_photo_path(cls, photo_instance: 'models.Photo', filename: str) -> str:
        """Builds a path for storing post photos."""
        return f'post/photos/post_{photo_instance.post.id}/{filename}'
