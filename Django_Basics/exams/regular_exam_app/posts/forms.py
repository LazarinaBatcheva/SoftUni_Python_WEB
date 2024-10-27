from django import forms
from posts.models import Post
from regular_exam_app.mixins import LabelAddMixin, ReadOnlyMixin


class PostBaseForm(LabelAddMixin, forms.ModelForm):
    image_label = 'Post Image URL:'

    class Meta:
        model = Post
        exclude = ['updated_at', 'author']


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...'
            })
        }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    pass
