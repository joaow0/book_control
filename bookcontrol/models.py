from django.db import models

from django.db import models


GENRE_CHOICES = (
    ('FICTION', 'Fiction'),
    ('FANTASY', 'Fantasy'),
    ('SCIENCE FICTION', 'Science Fiction'),
    ('THRILLER/SUSPENSE', 'Thriller/Suspense'),
    ('HORROR', 'Horror'),
    ('MYSTERY', 'Mystery'),
    ('ACTION AND ADVENTURE', 'Action and Adventure'),
    ('CLASSICS', 'Classics'),
    ('CHILDREN AND YOUNG ADULT', 'Children and Young Adult'),
    ('SPECULATIVE FICTION', 'Speculative Fiction'),
    ('BIOGRAPHY', 'Biography'),
    ('AUTOBIOGRAPHY', 'Autobiography'),
    ('HISTORY', 'History'),
    ('SCIENCE', 'Science'),
    ('SELF-HELP', 'Self-Help'),
    ('COOKING', 'Cooking'),
    ('GASTRONOMY', 'Gastronomy'),
    ('TRAVEL', 'Travel'),
    ('ECONOMICS', 'Economics'),
    ('ART', 'Art'),
    ('RELIGION', 'Religion'),
    ('POLITICS', 'Politics'),
    ('INVESTIGATIVE JOURNALISM', 'Investigative Journalism'),
    ('ESSAYS', 'Essays'),
    ('MANUALS', 'Manuals'),
)


class Author(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title
