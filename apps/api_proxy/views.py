import json, requests
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from apps.login_reg.models import User, Bill


def index(request):
    return render(request, 'api_proxy/index.html')

def data(request):
    if request.method == 'POST':
        try:
            return JsonResponse(requests.get(request.POST['url']).text, safe=False)
        except:
            return JsonResponse({'error': 'Request failed'})

    return JsonResponse({'error': 'GET request not allowed'})

def demo(request):

    return render(request, 'api_proxy/demo.html')

def bill(request):
    if 'user_id' not in request.session:
        return redirect('login_reg:login')

    return render(request, 'api_proxy/bill.html')

def authenticate_bill(request):
    if request.method == "POST":
        success = False
        bill = None
        success, bill = create_bill(request)

        if success:
            return JsonResponse({
                "desc": bill.desc,
                "amount": bill.amount,
                })

        errors= [str(message) for message in messages.get_messages(request)]

        return JsonResponse({'errors': errors}, status=400)

    return JsonResponse({'message': 'method not allow'})


def delete_bill(request):
    bill_id = request.POST['bill_id']
    
    try:
        bill = Bill.objects.get(id = bill_id)
        bill.delete()
        return JsonResponse({"message": "deleted"})

    except:
        pass

    return JsonResponse({"message": "cannot be deleted"})

def update_bill(request):
    desc = request.POST['new_desc']
    amount = request.POST['new_amount']
    user_id = request.session['user_id']
    bill_id = request.session['bill_id']


    return JsonResponse({"desc": desc, "amount": amount})

def create_bill(request):
    desc = request.POST['html_desc']
    amount = request.POST['html_amount']
    user_id = request.session['user_id']
    
    is_valid = len(desc) > 0

    try:
        int_amount = float(amount)
        is_valid = is_valid and len(amount)>0
        print("in good try")
    except:
        is_valid = False
        messages.error(request, 'Amount need to be a number')
        return False, None

    if is_valid:
        try:
            bill = Bill.objects.create(desc = desc, amount = amount, user_id = user_id)
            return True, bill

        except:
            messages.error(request, "Bad Bill")

    return False, None