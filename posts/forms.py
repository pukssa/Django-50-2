from .models import Post, Category, Tag
from django import forms
from posts.models import Category

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'image', 'rate')

class SearchForm(forms.Form):
    search = forms.CharField
    required = False
    max_length = 100
    widget = forms.TextInput(attrs={'placeholder': 'Search'})


    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False )
    tags =  forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

orderings = (
    'title',
    "-title",
    'rate'
    '-rate',
    'created',
    '-created',
)

ordering = (forms.ChoiceField
            (choices=orderings, widget = forms.Select(attrs={
    'class': 'form-control'
})))