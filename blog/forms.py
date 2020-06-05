from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


widgets = {
            
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    
