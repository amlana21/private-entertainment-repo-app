from django.contrib import admin

# Register your models here.

from .models import ItemTypes,ListTypes,SourceType,Items


admin.site.register(ItemTypes)
admin.site.register(ListTypes)
admin.site.register(SourceType)
admin.site.register(Items)
