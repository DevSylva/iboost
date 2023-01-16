from django.urls import path 
from . import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="home"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("support-ticket/", views.supportTicket, name="supportTicket"),
    path("user/dashboard/", views.dashboard, name="dashboard"),
    path("user/services", views.userServices, name="userServices"),
    path("user/order/history/", views.orderHistory, name="orderHistory"),
    path("user/deposit/", views.deposit, name="deposit"),
    path("user/deposit/history/", views.depositLog, name="depositHistory"),
    path("user/transactions/", views.transactions, name="transactions"),
    path("terms-and-condition/", views.termsAndCondition, name="termsAndCondition"),
    path("privacy-policy/", views.privacyProlicy, name="privacy"),
    path("refund-policy/", views.refundPolicy, name="refundPolicy"),
]