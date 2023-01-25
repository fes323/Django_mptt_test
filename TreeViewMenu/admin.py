from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import TreeMenu_MPTT


class TreeMenu_MPTTAdmin(DraggableMPTTAdmin):
    pass
admin.site.register(
    TreeMenu_MPTT,
    TreeMenu_MPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)


# class TreeMenu_nativeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'parent', 'position']
#     prepopulated_fields = {'slug': ('name',)}
#     list_editable = ['parent', 'position']
# admin.site.register(TreeMenu_native, TreeMenu_nativeAdmin)

