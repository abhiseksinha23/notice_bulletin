from django import forms

from .models import queries, addinfo, Notices

class NoticesForm(forms.ModelForm):

    class Meta:
        model = Notices
        fields = ('author','title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea noticecontent'}),
        }


class addinfoForm(forms.ModelForm):

    class Meta:
        model = addinfo
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class queriesForm(forms.ModelForm):
    class Meta:
        model = queries
        fields = ('author','regno','email','contact','subject', 'text')

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
