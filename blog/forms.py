from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
	#� model�� �������ϴ��� ��� �˷��ش�
        model = Post
        fields = ('title', 'text',)