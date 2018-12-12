from django.core.exceptions import ValidationError


def min_post_length(text):
    if len(text) < 2:
        raise ValidationError(
            ('Your post is not long enough.')
        )
