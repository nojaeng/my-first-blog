from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
	#어떤 model이 쓰여야하는지 장고에 알려준다
        model = Post
        fields = ('title', 'text',)