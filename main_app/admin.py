from django.contrib import admin
from .models import Baby, Feeding, Toy

# Register your models here.
admin.site.register(Baby)
admin.site.register(Feeding)
admin.site.register(Toy)