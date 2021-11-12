from django.db import models
from django.contrib.auth.models import User

from textwrap import fill
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=180, verbose_name="biography", null=True, blank=True)
    display_picture = models.ImageField(default='avatar.jpg', upload_to='profile_pics')


    def __str__(self):
        return f"{self.user.username}'s profile."
    
    @property
    def full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}".title()

    @property
    def wrapped_bio(self):
        return fill(self.bio, 52)

    @property
    def posts_count(self):
        """ Returns number of posts a user has """
        posts_count = len(self.user.posts.all())
        return posts_count
    
    def save(self, **kwargs):
        """ Override save to resize profile picture before saving. """
        # open file
        image = Image.open(self.display_picture)
        # limited size should be 300
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.display_picture.path)

        super().save() # call save from super


class Connected(models.Model):
    
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="linked_accounts")
    # Connected accounts
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)


    class Meta:
        verbose_name = "connected"
        verbose_name_plural = 'connected accounts'

    @property
    def data(self):
        return {key: getattr(self, key) for key in self.accounts}

    @property
    def accounts(self):
        return [ i for i in ('facebook', 'instagram', 'twitter', 'github', 'youtube') if getattr(self, i)]

    def __str__(self):
        return f"Connected accounts {self.accounts}"
