import re

from django import forms


#  生成form的对象

class UserForm1(forms.Form):
    name = forms.CharField(label='用户名',
                           max_length=18,
                           min_length=6,
                           required=False,
                           error_messages={'required': u'必填',
                                           'max_length': '最大为18个字符'
                                           },
                           widget=forms.TextInput(attrs={'placeholder': '请输入用户名'})
                           )
    password = forms.CharField(label='密码',
                               max_length=18,
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))
    city = forms.ChoiceField(choices=[(1, '北京'), (2, '上海'), (3, '武汉')])
    create_date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
    money = forms.DecimalField(label='收入', max_digits=10, decimal_places=2)
    # 文件
    image = forms.ImageField(allow_empty_file=True)
    email = forms.EmailField(label='邮箱',
                             required=True,
                             error_messages={'invalid': u'邮箱格式不正确'},
                             widget=forms.EmailInput(attrs={'placeholder': '请输入邮箱@xxx.com'})
                             )
    is_read = forms.BooleanField(label='同意协议')


from apps.form01 import models


# 数据验证
# 一种全局的验证
# 针对某个字段进行验证

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        # 所有模型的字段都生成
        # fields = '__all__'
        # 只显示某些字段
        fields = ('name', 'password', 'phone')
        # 不显示
        exclude = ()

    # 自定义验证数据
    def clean_phone(self):
        re_com = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        if re.search(re_com, self.cleaned_data.get('phone')):
            return self.cleaned_data
        else:
            raise ValueError('手机格式不正确')

    # 全局验证
    # def clean(self):
    #     if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
    #         raise ValueError('两次输入的密码不一致')
    #     else:
    #         return self.cleaned_data
