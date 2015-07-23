from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['blog']
        widgets = {
            #todo pq no puedo cambiar el widget?
            'published_date': forms.DateInput()
        }