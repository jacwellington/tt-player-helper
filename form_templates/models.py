from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=200) 
    template = models.ForeignKey('FormTemplate')
    def __unicode__(self):
        return self.name
    class Meta:
        abstract = True

class FormTemplate(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name;

    
class NumberField(Field):
    has_plus_sign = models.BooleanField()
    can_be_negative = models.BooleanField()
    is_calculated = models.BooleanField()
    easy_change = models.BooleanField()
    
class StringField(Field):
    easy_change = models.BooleanField()
    max_length = models.IntegerField()

    
class ListField(Field):
    max_length_per_item = models.IntegerField()
    max_number_of_items = models.IntegerField() 

class FieldData(models.Model):
	form = models.OneToOneField(FormTemplate, primary_key=True)
	field_data = models.TextField()
    
