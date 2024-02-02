from django.db import models


class CryptoChoices(models.TextChoices):
    ENGLISH = ('ABAN', 'Aban')
    PERSIAN = ('BTC', 'Bitcoin')


