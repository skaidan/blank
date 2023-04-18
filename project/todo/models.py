import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from enum import Enum

from enumchoicefield import ChoiceEnum, EnumChoiceField



class TypeOfReadLine(Enum):
        _026 = '026'
        _027 = '027'
        _028 = '028'
        _029 = '029'
        _030 = '030'
        _032 = '032'
        _033 = '033'        

class Read(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeofline = EnumChoiceField(TypeOfReadLine, default=TypeOfReadLine._026, null=False)
    filesource = models.CharField(max_length=256, null=False, blank=True)
    MPAN = models.CharField(max_length=256, null=False, blank=True)
    meterSN = models.CharField(max_length=256, null=False, blank=True)
    datafields = models.JSONField(default=list, blank=True, null=False)
    

