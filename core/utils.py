from core.models import *


def checkBalance(bill, balance):
    if int(bill[1:-3]) > int(balance):
        return False
    else:
        return True


def debitBalance(userid, bill):
    user = User.objects.get(id=userid)
    user.balance -= float(bill[1:-3])
    user.save()