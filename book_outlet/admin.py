from django.contrib import admin

from .models import Author, Book, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("last_name",)
    list_display = ("full_name", "address")

class AddressAdmin(admin.ModelAdmin):
    list_filter = ("city",)
    list_display = ("street", "postcode", "city")

class CountryDisplayed(admin.ModelAdmin):
    list_display = ("name", "code",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryDisplayed)
