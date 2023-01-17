from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coinbase_commerce.client import Client
from socialmediamarket import settings
from account.models import User 
from core.models import Transaction, DepositPreview

# Create your views here.
def index(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

@login_required(login_url="account:login")
def dashboard(request):
    user = User.objects.get(username=request.user.username)
    tx = len(Transaction.objects.filter(user=user))
    data = {
        "user": user,
        "tx": tx,
    }
    return render(request, "dashboard.html", context=data)

def userServices(request):
    return render(request, "user_services.html")

def orderHistory(request):
    return render(request, "orderhistory.html")

@login_required(login_url="account:login")
def deposit(request):
    if request.method == "POST":
        amount = float(request.POST['amount'])
        userId = request.user.id
        user = User.objects.get(id=userId)
        print(amount)
        deposit_preview = DepositPreview.objects.create(user=user, amount=amount)
        return redirect("core:depositPreview")

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

@login_required(login_url="account:login")
def profileSettings(request):
    user = User.objects.get(username=request.user.username)
    data = {
        "user": user,
    }
    return render(request, "profile-settings.html", context=data)

@login_required(login_url="account:login")
def depositPreview(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    depositpreview = DepositPreview.objects.get(user=user)
    convertedPrice = depositpreview.amount

    # creating a charge
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = "https://iboost.ng/"
    product = {
        'name': 'Iboost Deposit',
        'description': 'funding of iboost account',
        'local_price': {
            'amount': convertedPrice,
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
        'metadata': {
            'customer_id': request.user.id if request.user.is_authenticated else None,
            'customer_username': request.user.username if request.user.is_authenticated else None,
        },
    }
    charge = client.charge.create(**product)
    data = {
        "preview": depositpreview,
        "charge": charge
    }


    return render(request, "deposit-preview.html", context=data)