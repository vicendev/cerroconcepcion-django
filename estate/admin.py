from django.contrib import admin
from estate.models import Estate, Business, Structure, EstateImages

# Register your models here.

class EstateAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class BusinessAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class StructureAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    


admin.site.register(Estate, EstateAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(EstateImages)
