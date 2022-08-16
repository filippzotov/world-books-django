from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "language", "display_author")
    list_filter = ("genre", "author")


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "borrower", "due_back", "id")
    list_filter = ("book", "status")

    fieldsets = (
        (
            None,
            {
                "fields": ("book", "imprint", "inv_nom"),
            },
        ),
        ("Avaiability", {"fields": ("status", "due_back", "borrower")}),
    )
