from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import ObjectDoesNotExist
from user.models import Teacher


class ApprenticeForm(forms.Form):
    teacher_id = forms.IntegerField(widget=forms.HiddenInput)
    result = forms.IntegerField(widget=forms.HiddenInput)  # 0表示请求中，1表示请求成功，2表示请求失败

    # def __str__(self):
    #     return '<Profile: %s for %s>' % (self.user, self.teacher)
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        # self.
        super(ApprenticeForm, self).__init__(*args, **kwargs)
        
        
    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')

        # 评论对象验证
        # content_type = self.cleaned_data['content_type']
        teacher_id = self.cleaned_data['teacher_id']
        try:
            # model_class = ContentType.objects.get(model=content_type).model_class()
            teacher = Teacher.objects.get(pk=teacher_id)
            # self.cleaned_data['content_object'] = model_obj
            self.cleaned_data['teacher'] = teacher
        except ObjectDoesNotExist:
            raise forms.ValidationError('对象不存在')

        return self.cleaned_data



