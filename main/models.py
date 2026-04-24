from django.db import models
from django.contrib.auth.models import User


class UserName(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='usernames'
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    from django.db import models
from django.contrib.auth.models import User

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    output = models.ImageField(upload_to='outputs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    