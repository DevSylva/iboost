from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coinbase_commerce.client import Client
from socialmediamarket import settings
from account.models import User 
from core.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from rave_python import Rave
from .utils import checkBalance, debitBalance
import requests
import json


# Create your views here.
def index(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


@login_required(login_url="account:login")
def depositLog(request):
    user = User.objects.get(id=request.user.id)
    deposits = DepositLog.objects.filter(user=user)

    data = {
        "deposits": deposits
    }
    
    return render(request, "depositlog.html", context=data)


@login_required(login_url="account:login")
def transactions(request):
    user = User.objects.get(id=request.user.id)
    tx = Transaction.objects.filter(user=user)

    data = {
        "transactions": tx
    }
    return render(request, "transactions.html", context=data)


@login_required(login_url="account:login")
def supportTicket(request):
    return render(request, "support_ticket.html")


def termsAndCondition(request):
    return render(request, "terms_and_condition.html")


def refundPolicy(request):
    return render(request, "refund_policy.html")


def privacyProlicy(request):
    return render(request, "privacy_policy.html")

def newSupportTicket(request):
    user = User.objects.get(id=request.user.id)

    if request.method == "POST":
        ContactSupport.objects.create(
            user=user,
            name = request.POST["name"],
            email = request.POST["email"],
            subject = request.POST["subject"],
            message = request.POST["message"]
        )
        messages.success(request, "message sent")
        return redirect("core:dashboard")

    data = {
        "user": user
    }
    return render(request, "new-ticket.html", context=data)

@login_required(login_url="account:login")
def userServices(request):

    igServices = InstagramService.objects.all()
    tikTokService = TiktokService.objects.all()
    youtubeService = YoutubeService.objects.all()


    if request.method == "POST":
        try:
            # get the user info
            user = User.objects.get(id=request.user.id)
            userBalance = user.balance
            bill = request.POST["price"]

            link = request.POST["link"]
            quantity = request.POST["quantity"]
            serviceId = request.POST["serviceid"]
            
           
            # condition to ensure proper deduction
            chkBal = checkBalance(bill, userBalance)
            if not chkBal:
                messages.warning(request, "Insufficient funds")
                messages.info(request, "Kinldy fund your account")
                return redirect("core:deposit")
            else:
                debitBalance(request.user.id, bill)

                # send api request
                url = "https://fams-up.net/api/v2"

                payload = json.dumps({
                    "key": settings.FAMSUPAPI_KEY,
                    "action": "add",
                    "service": serviceId,
                    "link": link,
                    "quantity": quantity
                })
                
                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                responseData = response.json()
                
                message = ""
                if "error" in responseData:
                    message = "Service Unavailable"
                    user.balance += float(bill[1:-3])
                    user.save()
                else:
                    # create order history
                    OrderHistory.objects.create(
                        user=user,
                        service = serviceId,
                        link = link,
                        quantity = quantity,
                        status = "success"
                    )
                    message = response.json()

                messages.success(request, message)
        except Exception as e:
                messages.warning(request, e)

    data = {
        "igService": igServices,
        "tiktokService": tikTokService,
        "youtubeService": youtubeService
    }
    return render(request, "user_services.html", context=data)


@login_required(login_url="account:login")
def orderHistory(request):
    user = User.objects.get(id=request.user.id)
    orders = OrderHistory.objects.filter(user=user)

    data = {
        "orders": orders
    }
    return render(request, "orderhistory.html", context=data)


@login_required(login_url="account:login")
def deposit(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    try:
        DepositPreview.objects.filter(user=user).all().delete()
    except DepositPreview.DoesNotExist:
        pass
    if request.method == "POST":
        print(request.POST)
        amount = float(request.POST['amount'])
        method = request.POST["method_code"]
        DepositPreview.objects.create(user=user, amount=amount, method=method)
        return redirect("core:depositPreview")

    return render(request, "deposit.html")


@login_required(login_url="account:login")
def profileSettings(request):
    user = User.objects.get(username=request.user.username)

    if request.method == "POST":
        print(request.POST)
        if "image" in request.FILES:
            user.profile_pic = request.FILES["image"]
        if "firstname" in request.POST:
            user.first_name = request.POST["firstname"]
        if "lastname" in request.POST:
            user.last_name = request.POST["lastname"]
        if "mobile" in request.POST:
            user.mobile_number = request.POST["mobile"]
        if "email" in request.POST:
            user.email = request.POST["email"]
        if "zip" in request.POST:
            user.zipcode = request.POST["zip"]
        if "address" in request.POST:
            user.address = request.POST["address"]
        if "city" in request.POST:
            user.city = request.POST["city"]
        if "state" in request.POST:
            user.state = request.POST["state"]

        user.save()
        messages.success(request, "User details successfully updated.")
        return redirect("core:dashboard")
    data = {
        "user": user,
    }
    return render(request, "profile-settings.html", context=data)


@login_required(login_url="account:login")
def paystackDepositPreview(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    try:
        depositpreview = DepositPreview.objects.get(user=user)
    except DepositPreview.DoesNotExist:
        return HttpResponse(request, "Ooops! something's wrong")

    data = {
        "preview": depositpreview,
        "user": user,
        "public_key": settings.PAYSTACK_PUBLIC_API_KEY
    }
    return render(request, "paystack-checkout.html", context=data)

@login_required(login_url="account:login")
def depositPreview(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    depositpreview = DepositPreview.objects.get(user=user)

    # creating a charge
    if depositpreview.method == "506":
        client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
        domain_url = "https://iboost.ng"
        product = {
            'name': 'Iboost Deposit',
            'description': 'funding of iboost account',
            'local_price': {
                'amount': f"{depositpreview.amount}",
                'currency': 'NGN'
            },
            'pricing_type': 'fixed_price',
            'redirect_url': domain_url + '/user/deposit/success/',
            'cancel_url': domain_url + '/user/deposit/cancel/',
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

    else:
        return redirect("core:paystackDepositPreview")


    return render(request, "deposit-preview.html", context=data)


@login_required(login_url="account:login")
def dashboard(request):
    user = User.objects.get(username=request.user.username)
    tx = len(Transaction.objects.filter(user=user))
    data = {
        "user": user,
        "bal": f"{user.balance:,}",
        "tx": tx,
    }
    return render(request, "dashboard.html", context=data)



@login_required(login_url="account:login")
def paystackSuccess(request):
    user = User.objects.get(id=request.user.id)
    depositData = DepositPreview.objects.get(user=user)
    user.balance += depositData.amount
    user.save()

    DepositLog.objects.create(
        user=user, 
        gateway="Paystack",
        amount=depositData.amount,
        status="successful"
    )

    Transaction.objects.create(
        user = user, 
        amount= depositData.amount
    )
    messages.success(request, "Deposit Successful")
    return redirect("core:dashboard")


@login_required(login_url="account:login")
def success(request):
    user = User.objects.get(id=request.user.id)
    depositData = DepositPreview.objects.get(user=user)
    user.balance += depositData.amount
    user.save()

    DepositLog.objects.create(
        user=user, 
        gateway="coinbase",
        amount=depositData.amount,
        status="successful"
    )

    Transaction.objects.create(
        user = user, 
        amount= depositData.amount
    )
    messages.success(request, "Deposit Successful")
    return redirect("core:dashboard")


@login_required(login_url="account:login")
def cancel(request):
    messages.warning(request, "Deposit failed")
    return redirect("core:dashboard")


@login_required(login_url="account:login")
def courierService(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        print(request.POST)
        print(request.POST)
        user = User.objects.get(id=request.user.id)
        userBalance = user.balance
        bill = "#1500.00"
        chkBal = checkBalance(bill, userBalance)
        if not chkBal:
            messages.warning(request, "Insufficient funds")
            messages.info(request, "Kinldy fund your account")
            return redirect("core:deposit")
        else:
            debitBalance(request.user.id, bill)

            service = CourierService.objects.create(
                user = user,
                sender_full_name = request.POST["name"],
                sender_package = request.POST["shipper_company_name"],
                sender_address = request.POST["shipper_company_address"],
                sender_country = request.POST["shipper_company_country"],
                sender_city = request.POST["shipper_city"],
                sender_state_province = request.POST["shipper_state"],
                sender_postal_code = request.POST["shipper_postal_code"],
                sender_phone_number = request.POST["shipper_telephone_no"],
                sender_email = request.POST["shipper_email"],
                sender_type = request.POST["shipper_type"],
                receiver_full_name = request.POST["receiver_company_name"],
                receiver_shipping_fee = request.POST["receiver_company_name"],
                receiver_address = request.POST["receiver_company_address"],
                receiver_country = request.POST["receiver_company_country"],
                receiver_city = request.POST["receiver_city"],
                receiver_state_province = request.POST["receiver_state"],
                receiver_postal_code = request.POST["receiver_postal_code"],
                receiver_phone_number = request.POST["receiver_telephone_no"],
                receiver_email = request.POST["receiver_email"]
            )
            
            url = "https://cargoton.live/api/courier-service/"

            payload = json.dumps({
                "tracking_id" : service.tracking_id,
                "sender_full_name" : request.POST["name"],
                "sender_package" : request.POST["shipper_company_name"],
                "sender_address" : request.POST["shipper_company_address"],
                "sender_country" : request.POST["shipper_company_country"],
                "sender_city" : request.POST["shipper_city"],
                "sender_state_province" : request.POST["shipper_state"],
                "sender_postal_code" : request.POST["shipper_postal_code"],
                "sender_phone_number" : request.POST["shipper_telephone_no"],
                "sender_email" : request.POST["shipper_email"],
                "sender_type" : request.POST["shipper_type"],
                "receiver_full_name" : request.POST["receiver_company_name"],
                "receiver_shipping_fee" : request.POST["receiver_company_name"],
                "receiver_address" : request.POST["receiver_company_address"],
                "receiver_country" : request.POST["receiver_company_country"],
                "receiver_city" : request.POST["receiver_city"],
                "receiver_state_province" : request.POST["receiver_state"],
                "receiver_postal_code" : request.POST["receiver_postal_code"],
                "receiver_phone_number" : request.POST["receiver_telephone_no"],
                "receiver_email" : request.POST["receiver_email"]
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            messages.success(request, "Delivery details saved")
            return redirect("core:courierDetailsPreview", pk=service.tracking_id)
   
    return render(request, "courier-services.html")


@login_required(login_url="account:login")
def courierDetailsPreview(request, pk):
    try:
        courierDetails = CourierService.objects.get(tracking_id=pk)
    except CourierService.DoesNotExist:
        return HttpResponse(request, "No data found")

    data = {
        "data": courierDetails
    }
    return render(request, "courier-preview.html", context=data)