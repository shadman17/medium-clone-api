from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("You must provide a valid email address."))

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not first_name:
            raise ValueError(_("Users must have a first name."))
        if not last_name:
            raise ValueError(_("Users must have a last name."))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Users must have an email address."))

        user = self.model(
            first_name=first_name, last_name=last_name, email=email, **extra_fields
        )
        user.set_password(password)

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        if not password:
            raise ValueError(_("Superuser must have a password."))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Superuser must have an email address."))

        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user


# from django.contrib.auth.base_user import BaseUserManager
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from django.utils.translation import gettext_lazy as _


# class CustomUserManager(BaseUserManager):
#     def email_validator(self, email):
#         try:
#             validate_email(email)
#             return True
#         except ValidationError:
#             # Keep ValueError to match Django conventions used in managers
#             raise ValueError(_("You must provide a valid email address."))

#     def create_user(self, first_name, last_name, email, password=None, **extra_fields):
#         if not first_name:
#             raise ValueError(_("Users must have a first name."))
#         if not last_name:
#             raise ValueError(_("Users must have a last name."))
#         if not email:
#             raise ValueError(_("Users must have an email address."))

#         email = self.normalize_email(email)
#         self.email_validator(email)

#         # Ensure expected defaults are set BEFORE creating the instance
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         # It's common for users to be active by default; keep if your model expects that
#         extra_fields.setdefault("is_active", True)

#         user = self.model(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             **extra_fields,
#         )
#         if password:
#             user.set_password(password)
#         else:
#             # If you want to enforce password for normal users, replace with a ValueError
#             user.set_unusable_password()

#         user.save(using=self._db)
#         return user

# def create_superuser(self, first_name, last_name, email, password, **extra_fields):
#     extra_fields.setdefault("is_staff", True)
#     extra_fields.setdefault("is_superuser", True)
#     extra_fields.setdefault("is_active", True)

#     if extra_fields.get("is_staff") is not True:
#         raise ValueError(_("Superuser must have is_staff=True."))
#     if extra_fields.get("is_superuser") is not True:
#         raise ValueError(_("Superuser must have is_superuser=True."))
#     if not password:
#         raise ValueError(_("Superuser must have a password."))
#     if not email:
#         raise ValueError(_("Superuser must have an email address."))

#     # no need to normalize or validate email again — create_user handles it
#     return self.create_user(first_name, last_name, email, password, **extra_fields)
