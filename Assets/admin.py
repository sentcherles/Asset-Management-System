from django.contrib import admin
from .models import Asset

class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'serialNumber', 'datePurchased', 'qr')
    readonly_fields = ('qr',)

admin.site.register(Asset, AssetAdmin)
