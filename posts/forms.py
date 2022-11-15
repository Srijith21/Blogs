from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={"class":"input",}), label="Tags (comma separated)")

    class Meta:
        model = Post
        exclude = ('author','published_date','is_deleted','categories')

        widgets = {
            "title" : forms.TextInput(attrs={"class":"input"}),
            "time_to_read" : forms.TextInput(attrs={"class":"input"}),
            "short_description" : forms.Textarea(attrs={"class":"input"})
        }

        error_messages={
            "time_to_read" : {
                "required": "Time to read field is required"
            },
            "title" : {
                "required": "Title field is required"
            },
            "short_description" : {
                "required": "Short_description field is required"
            },
            "Description" : {
                "required": " Description field is required"
            },
            "featured_image" : {
                "required": " featured_image field is required"
            },
            "is_draft" : {
                "required": " is_draft field is required"
            },
            "categories" : {
                "required": " categories field is required"
            },

        }