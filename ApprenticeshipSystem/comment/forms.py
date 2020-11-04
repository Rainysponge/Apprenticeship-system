#form表单 内容与前端form的name="text"交互
from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
    homework_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget())
