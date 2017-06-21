from django.contrib import admin
from invoice.models import Company, Suburb, Location, Store, StickerOrder


def mark_printed(modeladmin, request, queryset):
    queryset.update(printed=True)


mark_printed.short_description = "Mark selected as Printed"


def mark_notprinted(modeladmin, request, queryset):
    queryset.update(printed=False)


mark_notprinted.short_description = "Mark selected as NOT Printed"


def mark_signed(modeladmin, request, queryset):
    queryset.update(signed=True)


mark_signed.short_description = "Mark selected as Signed"


def mark_notsigned(modeladmin, request, queryset):
    queryset.update(signed=None)


mark_notsigned.short_description = "Mark selected as NOT Signed"


def mark_unsigned(modeladmin, request, queryset):
    queryset.update(signed=None)


mark_unsigned.short_description = "Mark selected as YET TO BE Signed"


class StickerOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'date', 'stickerstart', 'qty', 'printed', 'signed')
    list_filter = ['printed', 'signed']
    actions = [mark_printed, mark_notprinted, mark_signed, mark_notsigned, mark_unsigned]


admin.site.register(Company)
admin.site.register(Suburb)
admin.site.register(Location)
admin.site.register(Store)
admin.site.register(StickerOrder, StickerOrderAdmin)
