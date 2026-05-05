from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    # NOTE: the built-in UserManager is imported here but NOT used — our
    # custom UserManager below replaces it entirely. Safe to remove this
    # import later if you want to keep things tidy.
    UserManager,
)


class UserManager(BaseUserManager):
    """Custom manager for the User model.

    Replaces Django's default UserManager so we can use email as the
    login credential instead of a username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a regular user.

        **Why .lower() + normalize_email()?**
        normalize_email() (from BaseUserManager) only lowercases the
        *domain* part of the address (everything after the @).  The local
        part (everything before the @) is technically case-sensitive per
        the RFC, but in practice every mail server treats it as
        case-insensitive — and users certainly expect 'Test@example.com'
        and 'test@example.com' to be the same account.

        So we call .lower() on the whole string first to normalise the
        local part, then pass the result to normalize_email() which
        handles the domain.  Together they guarantee a fully lowercase,
        consistently stored email address.

        **Why **extra_fields?**
        Any keyword arguments beyond email/password (e.g. first_name,
        last_name) are captured here and spread onto the model instance.
        This is required because Django's createsuperuser command collects
        all REQUIRED_FIELDS and forwards them as kwargs — see create_superuser
        below for the full story.
        """
        if not email:
            raise ValueError('Users must have an email address')
        # Step 1 — lowercase the whole address (local part + domain).
        # Step 2 — normalize_email() further cleans up the domain portion.
        email = self.normalize_email(email.lower())
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create, save and return a superuser.

        **Why **extra_fields here?**
        When you run `python manage.py createsuperuser`, Django prompts
        for every field listed in REQUIRED_FIELDS (here: first_name and
        last_name) and then calls:

            create_superuser(email=..., password=...,
                             first_name=..., last_name=...)

        Without **extra_fields in the signature Python raises:
            TypeError: create_superuser() got an unexpected keyword
                       argument 'first_name'

        **extra_fields absorbs those extra kwargs so they flow through
        to create_user() and onto the model instance correctly.

        setdefault() sets is_staff/is_superuser to True only when the
        caller hasn't already supplied them — useful in tests where you
        might want to verify the validation guards by passing False.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username."""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
