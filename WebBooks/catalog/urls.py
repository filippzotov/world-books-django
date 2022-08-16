from xml.etree.ElementInclude import include
from django.urls import path, re_path

import django.contrib.auth.urls

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors_add/", views.authors_add, name="authors_add"),
    path("authors_add/edit1/<int:id>", views.edit1, name="edit1"),
    path("authors_add/create/", views.create, name="create"),
    path("authors_add/delete/<int:id>/", views.delete, name="delete"),
    re_path(r"^books/$", views.BookListView.as_view(), name="books"),
    re_path(r"book/(?P<pk>\d+)$", views.BookDetailView.as_view(), name="book-detail"),
    re_path(r"^authors/$", views.AuthorListView.as_view(), name="authors"),
    re_path(
        r"^mybooks/$",
        views.LoanedBooksByUserListView.as_view(),
        name="my-borrowed",
    ),
]


