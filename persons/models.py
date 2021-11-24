from django.db import models
from django.contrib.auth.models import User

"""
    Modelos relacionados a persons:
     - PersonType
     - Person
     - Person Person Type
"""


class PersonType(models.Model):
    id_person_type = models.AutoField(primary_key=True)
    person_type_name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'person_type'


class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=45, blank=True, null=True)
    person_last_name = models.CharField(max_length=45)
    person_address = models.CharField(max_length=45, blank=True, null=True)
    person_phone = models.CharField(max_length=45, blank=True, null=True)
    person_dni = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'person'


class PersonPersonType(models.Model):
    id_person_person_type = models.AutoField(primary_key=True)
    fk_id_person_type = models.ForeignKey(PersonType, models.DO_NOTHING, db_column='fk_id_person_type')
    fk_id_person = models.ForeignKey(Person, models.DO_NOTHING, db_column='fk_id_person')

    class Meta:
        managed = True
        db_table = 'person_person_type'
