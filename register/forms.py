from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=('name','surname','email','telephone_no','password',)
    
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['telephone_no'].required=False