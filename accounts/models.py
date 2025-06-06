from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 追加したいフィールドがあればここに書けます（任意）
    # 例: bio = models.TextField(blank=True, null=True)
    pass
# Create your models here.
