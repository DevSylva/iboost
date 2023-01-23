from django.contrib import admin
from .models import *
# Register your models here.


class DepositLogAdmin(admin.ModelAdmin):
    list_display = ("user", "gateway", "status", "time")
    list_filter = ("user", "gateway")

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "time")
    list_filter = ("user",)


admin.site.register(DepositLog, DepositLogAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(InstagramService)
admin.site.register(TiktokService)
admin.site.register(YoutubeService)
admin.site.register(OrderHistory)
admin.site.register(DepositPreview)

