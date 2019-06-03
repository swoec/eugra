# Create your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

User = get_user_model()


class UserProfile(AbstractUser):
    """
    UserProfile
    """
    name = models.CharField(max_length=80, null=True, blank=True, verbose_name="name")
    gender = models.CharField(max_length=6, choices=(("male", "male"), ("female", "female")), default="female",
                              verbose_name="gender")
    birthday = models.DateField(null=True, blank=True, verbose_name="birthday")
    address = models.CharField(max_length=120, null=True, blank=True, verbose_name="address")
    email = models.EmailField(max_length=120, null=True, blank=True, verbose_name="email")
    mobile = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=40, null=False, blank=False, default="anon")
    is_superuser = models.BooleanField(
        default=False,
        help_text=
        'Designates that this user has all permissions without ',

    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=
        'The groups this user belongs to. A user will get all permissions '
        ,
        related_name="userprofile_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="userprofile_set",
        related_query_name="user",
    )

    class Meta:
        permissions = (
            ('forum.comments', 'get comments'),
            ('view_comments', 'view comments'),
        )
        verbose_name = "user Profile"
        verbose_name_plural = verbose_name

    def has_perm(self, perm, obj=None):
        try:
            user_perm = self.user_permissions.get(codename=perm)
        except ObjectDoesNotExist:
            user_perm = False
        if user_perm:
            return True
        else:
            return False

    def permission_required(*perms):
        from django.contrib.auth.decorators import user_passes_test
        return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms), login_url='/login')

    def __str__(self):
        return self.name