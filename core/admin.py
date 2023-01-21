from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(DepositLog)
admin.site.register(Transaction)
admin.site.register(InstagramService)
admin.site.register(TiktokService)
admin.site.register(YoutubeService)
admin.site.register(OrderHistory)

