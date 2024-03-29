from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {'group': 'Группа', 'text': 'Текст поста'}
        help_texts = {
            'group': 'Группа, к которой будет относиться пост',
            'text': 'Текст нового поста'
        }
