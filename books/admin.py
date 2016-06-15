from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(RateAuthor)
admin.site.register(RateBook)
admin.site.register(Review)

