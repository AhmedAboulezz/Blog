from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    blog=forms.CharField(label='',
                widget=forms.Textarea(
                        attrs={'placeholder': "Your blog",
                            "class": "form-control"
                            }
                    ))


    def __init__(self,user, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['user'].initial = user



    def clean(self):
        cleaned_data=super(BlogForm, self).clean()
        user=cleaned_data.get(self.user)
        if Blog.objects.filter(user=self.user).count()>=3:
            raise forms.ValidationError("You are allowed to post only 3 blogs")


    class Meta:
        model=Blog
        fields = ['user',
                  'blog',
                 'tags']
        widgets = {'user': forms.HiddenInput()}

    # def clean_blog(self,*args,**kwargs):
    #     content=self.cleaned_data.get('blog')
    #     if content=='abc':
    #         raise forms.ValidationError("SORRRRY")
    #     return content


