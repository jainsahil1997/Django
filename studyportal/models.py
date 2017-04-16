from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey



# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=50)

    def get_absolute_url(self):
         return reverse('studyportal:subject',kwargs={'department_id':self.pk})

    def __str__(self):
        return self.dept_name

class Subject (models.Model):
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    sub_name=models.CharField(max_length=50)
    code=models.CharField(max_length=50)

    def get_absolute_url(self):
         return reverse('studyportal:material',kwargs={'subject_code':self.code})

    def get_books(self):
        return self.material_set.filter(type="books")
    def get_ppt(self):
        return self.material_set.filter(type="ppt")
    def get_pp(self):
        return self.material_set.filter(type="pp")
    def get_lv(self):
        return self.material_set.filter(type="lv")
    def get_notes(self):
        return self.material_set.filter(type="notes")
    def get_others(self):
        return self.material_set.filter(type="others")



    def __str__(self):
        return '{} {}' .format(self.code,self.sub_name)

Material_CHOICES = (
    ('books','Books'),
    ('ppt', 'PPT'),
    ('pp','Past Papers'),
    ('lv','Lecture Video'),
    ('notes','Notes'),
    ('others','Others'),
)

class Material(models.Model):
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    code=ChainedForeignKey(Subject,
                            chained_field="dept_name",
                            chained_model_field="dept_name",
                            show_all=False,
                            auto_choose=False,
                            sort=True,)
    type= models.CharField(max_length=50,choices=Material_CHOICES,default='books')
    material_desc=models.CharField(max_length=50,blank=False,null=False,default='code')
    material_link=models.CharField(max_length=1000,blank=True)
    material_file=models.FileField(blank=True)


    def clean(self):
        if self.material_link=='' and self.material_file is None:
            raise ValidationError(_('Chose any one of Options'))
        if self.material_link is not None and self.material_file is not None:
            raise ValidationError(_('Chose any one of the option'))

    def get_absolute_url(self):
        return '/'


    def __str__(self):
        return 'Course: {} {}'.format(self.code, self.material_desc)
