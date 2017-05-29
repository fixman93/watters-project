from django.contrib import admin
from django.forms import TextInput
from grappelli.forms import GrappelliSortableHiddenMixin
from .models import (Dress, DressImage, Fabric, Collection, Color, Part, Size)


class BaseAdmin(admin.ModelAdmin):
    class Media:
        js = [
            'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            'grappelli/tinymce_setup/tinymce_setup.js',
        ]


class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class ColorAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "hex_code":
            kwargs["widget"] = TextInput({"type": "color",})
        return super().formfield_for_dbfield(db_field, **kwargs)


class DressImageInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = DressImage
    extra = 2


class FabricInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Fabric
    filter_horizontal = ["colors"]
    extra = 2


class PartInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Part
    filter_horizontal = ["colors"]
    extra = 2

class SizeAdmin(admin.ModelAdmin):
    pass


class DressAdmin(BaseAdmin):
    list_filter = ["name", "sku", "style"]
    radio_fields = {"price": admin.HORIZONTAL, "size": admin.HORIZONTAL,}
    list_display = ["name", "style", "collection", "price", "size"]
    inlines = [DressImageInline, FabricInline, PartInline]


admin.site.register(Dress, DressAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
