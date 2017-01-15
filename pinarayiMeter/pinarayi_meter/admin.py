from django.contrib import admin

from .models import Promise, ReferenceObj


admin.site.register(Promise)
admin.site.register(ReferenceObj)
