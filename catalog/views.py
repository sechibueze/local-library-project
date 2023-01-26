from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance

# Create your views here.
def index(req):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(req, 'index.html', context)

class BookList(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.all()[:5]
    # template_name = ''

class BookDetails(generic.DetailView):
    model = Book