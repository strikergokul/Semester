from SemApp.models import SemMarks
from django import forms
class SemMarksForm(forms.ModelForm):
        class Meta:
               model=SemMarks
               fields= ('Regno','Maths','Physics','Chemistry')
