from django import forms
from django.forms import fields
from .models import SubCategories

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model=SubCategories
        fields='__all__'
        
    def __init__(self,*args,**kwargs):
        super(SubCategoryForm,self).__init__(*args,**kwargs)
        self.fields['parent'].empty_label='Select'
