from django import forms
from .models import Book,Author


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'authors', 'description', 'count')
        labels = {
            'name': 'Name ob Book',
            'authors': 'Book`s Author',
        }

    def __init__(self, *args, **kwargs):
        super(BookForm,self).__init__(*args, **kwargs)
        self.fields['authors'].required = False