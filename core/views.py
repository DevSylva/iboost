from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def dashboard(request):
    return render(request, "dashboard.html")

def userServices(request):
    return render(request, "user_services.html")

def orderHistory(request):
    return render(request, "orderhistory.html")

def deposit(request):
    return render(request, "order.html")

def depositLog(request):
    return render(request, "orderhistory.html")

def transactions(request):
    return render(request, "transactions.html")

def supportTicket(request):
    return render(request, "support_ticket.html")

def termsAndCondition(request):
    return render(request, "terms_and_conditon")

def refundPolicy(request):
    return render(request, "refund_policy.html")

def privacyProlicy(request):
    return render(request, "privacy_policy.html")