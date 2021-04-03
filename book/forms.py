from django import forms
from .models import Book,Author


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'authors', 'description', 'count')
        labels = {
            'name': 'Name of a Book',
            'authors': "Book's Authors",
        }

    def __init__(self, *args, **kwargs):
        super(BookForm,self).__init__(*args, **kwargs)
        self.fields['authors'].required = True
        self.fields['name'].required = True
        self.fields['count'].required = True