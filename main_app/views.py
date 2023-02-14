from django.shortcuts import render, redirect
from .models import Book, Author
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class BookList(LoginRequiredMixin, ListView):
    model = Book

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'isbn', 'pageCount', 'pubDate', 'genre', 'bookCover']

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        authors = Author.objects.all()
        context['authors'] = authors
        return context

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'isbn', 'pageCount', 'pubDate', 'genre', 'bookCover']

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books/'



class AuthorList(LoginRequiredMixin, ListView):
    model = Author

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'

class AuthorDetail(LoginRequiredMixin, DetailView):
    model = Author

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/authors/'



@login_required
def add_author(request, book_id, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    book.author = author
    book.save()
    return redirect('book_detail', pk=book_id)