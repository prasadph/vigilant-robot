from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    # adds search bar and decides fields to search
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    # adds fields to display in object list
    list_display = ('title', 'publisher', 'publication_date')
    # adds controls at right to filter
    list_filter = ('publication_date',)
    # adds controls at top to filter by datetime
    date_hierarchy = 'publication_date'
    # select default ordering of object in admin
    ordering = ('-publication_date',)
    # order of fields in editing, can used to not display field
    fields = ('title', 'authors', 'publisher', 'publication_date')
    # new widget for many-many object , vertical objects also
    filter_horizontal = ('authors',)
    # used to added forign key by id, tool provided to decide key
    raw_id_fields = ('publisher',)


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
