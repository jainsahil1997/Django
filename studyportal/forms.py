from django import forms

from .models import Department,Subject,Material


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields=['dept_name','code','type','material_desc','material_link','material_file']
