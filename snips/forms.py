from django.contrib.auth.forms import forms
from snips.models import Snippet

class Snippet_Form(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('title', 'language', 'description', 'code', 'tags')