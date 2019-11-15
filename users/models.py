from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_MALE = "male"

    GENDER_CHOICES = {
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
        (GENDER_MALE, "Male"),
    }

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = {(LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean")}

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = {(CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW")}

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=LANGUAGE_KOREAN
    )
    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)

