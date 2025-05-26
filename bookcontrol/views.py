from django.shortcuts import render, redirect
from .form import BookForm
from .models import Book, Author
from django.db.models import Q

def register_books(request):

    query = request.GET.get('q')
    results = []
    
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        ).distinct()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            genre = form.cleaned_data['genre']
            authors_names = form.cleaned_data['authors_names']
            
            book = Book.objects.create(title=title, genre=genre)

            names = [name.strip() for name in authors_names.split(',')]
            
            for name in names:
                author, created = Author.objects.get_or_create(name=name)
                book.authors.add(author)
                
            return redirect('register_books')

    else:
        form = BookForm()

    books = Book.objects.all()

    context = {
        'form': form,
        'books': books,
        'results': results,
        'query': query,
    }

    return render(request, 'book.html', context)
