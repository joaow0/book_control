from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    authors_names = forms.CharField(
        label='Author(s)',
        help_text='Separate names with commas',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex: J. K. Rowling, George Orwell'
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'genre']
