from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super(BaseModelManager, self).get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=_('modified time'), auto_now=True)
    deleted_time = models.DateTimeField(verbose_name=_('deleted time'), null=True, editable=False)
    deleted = models.BooleanField(verbose_name=_('deleted'), default=False, editable=False)

    objects = BaseModelManager()
    private_manager = models.Manager()

    class Meta:
        abstract = True

    def un_delete(self):
        self.deleted = False
        self.deleted_time = None
        self.save()

    def set_delete(self):
        self.deleted = True
        self.deleted_time = timezone.now()
        self.save()
