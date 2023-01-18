from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coinbase_commerce.client import Client
from socialmediamarket import settings
from account.models import User 
from core.models import Transaction, DepositPreview
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site


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


@login_required(login_url="account:login")
def userServices(request):
    return render(request, "user_services.html")


@login_required(login_url="account:login")
def orderHistory(request):
    return render(request, "orderhistory.html")


@login_required(login_url="account:login")
def deposit(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    try:
        DepositPreview.objects.filter(user=user).all().delete()
    except DepositPreview.DoesNotExist:
        pass
    if request.method == "POST":
        amount = float(request.POST['amount'])
        DepositPreview.objects.create(user=user, amount=amount)
        return redirect("core:depositPreview")

    return render(request, "deposit.html")


@login_required(login_url="account:login")
def depositLog(request):
    return render(request, "orderhistory.html")


@login_required(login_url="account:login")
def transactions(request):
    return render(request, "transactions.html")


@login_required(login_url="account:login")
def supportTicket(request):
    return render(request, "support_ticket.html")


def termsAndCondition(request):
    return render(request, "terms_and_condition.html")


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

    # creating a charge
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = get_current_site(request)
    product = {
        'name': 'Iboost Deposit',
        'description': 'funding of iboost account',
        'local_price': {
            'amount': f"{depositpreview.amount}",
            'currency': 'NGN'
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


@login_required(login_url="account:login")
def success(request):
    user = User.objects.get(id=request.user.id)
    depositData = DepositPreview.objects.get(user=user)
    user.balance += depositData.amount
    user.save()
    return HttpResponse(request, "deposit successful")


@login_required(login_url="account:login")
def cancel(request):
    return HttpResponse(request, "deposit failed")