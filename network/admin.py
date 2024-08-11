from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import NetworkLink, Product


class ProductInlineModel(admin.TabularInline):
    model = Product
    fields = ['title', 'model', 'release_date']


@admin.action(description="Очистить задолженность")
def debt_cleaner(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'view_supplier',
        'create_date'
    )
    list_filter = ('city',)
    actions = [debt_cleaner,]
    inlines = [ProductInlineModel,]

    def view_supplier(self, obj):
        if obj.supplier:
            url = (
                reverse('admin:network_networklink_changelist')
                + f'{obj.supplier.id}/change/'
            )
            return format_html(f'<a href="{url}">{obj.supplier}</a>')
        return ''

    view_supplier.short_description = "Supplier"
