from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from datetime import date, timedelta
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


# ---------------- PAGES ----------------
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login_page(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def livecurrency(request):
    return render(request, 'livecurrency.html')

def defaultcurrency(request):
    return render(request, 'defaultcurrency.html')

def coinexchange(request):
    return render(request, 'coinexchange.html')


# ---------------- LOGIN ----------------
def loginAction(request):

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect("/")
        return HttpResponse("Invalid login credentials")

    return redirect("/login/")


# ---------------- SIGNUP ----------------
def signupAction(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            return HttpResponse("Username and password required")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = full_name
        user.save()

        return redirect("/login/")

    return redirect("/signup/")


# ---------------- LIVE CURRENCY ----------------
def livecurrencyAction(request):

    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount"))
            from_currency = request.POST.get("from")
            to_currency = request.POST.get("to")
            decimal_places = int(request.POST.get("decimal"))

            url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
            res = requests.get(url, timeout=5)
            data = res.json()

            rate = data["rates"][to_currency]
            result = amount * rate

            return HttpResponse(str(round(result, decimal_places)))

        except:
            return HttpResponse("0")

    return HttpResponse("Invalid request")


# ---------------- DEFAULT CURRENCY ----------------
def defaultcurrencyAction(request):

    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount"))
            from_currency = request.POST.get("from")
            to_currency = request.POST.get("to")
            decimal_places = int(request.POST.get("decimal"))

            url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
            res = requests.get(url, timeout=5)
            data = res.json()

            rate = data["rates"][to_currency]
            result = amount * rate

            return HttpResponse(str(round(result, decimal_places)))

        except:
            return HttpResponse("0")

    return HttpResponse("Invalid request")


# ---------------- COIN EXCHANGE (REAL API) ----------------
def coinAction(request):

    if request.method == "POST":

        try:
            amount = float(request.POST.get("amount"))
            coin_from = request.POST.get("from")
            coin_to = request.POST.get("to")

            # REAL crypto API (CoinGecko - FREE)
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_from}&vs_currencies={coin_to}"

            res = requests.get(url, timeout=5)
            data = res.json()

            rate = data[coin_from][coin_to]
            result = amount * rate

            return JsonResponse({
                "result": round(result, 6)
            })

        except:
            return JsonResponse({"result": 0})

    return JsonResponse({"error": "Invalid request"})


# ---------------- HISTORY ----------------
def currency_history(request):

    from_currency = request.GET.get("from", "USD")
    to_currency = request.GET.get("to", "INR")
    period = request.GET.get("period", "1w")

    today = date.today()

    if period == "1d":
        start = today - timedelta(days=1)
    elif period == "1w":
        start = today - timedelta(days=7)
    elif period == "1m":
        start = today - timedelta(days=30)
    elif period == "1y":
        start = today - timedelta(days=365)
    else:
        start = today - timedelta(days=7)

    try:
        url = f"https://api.frankfurter.app/{start}..{today}?from={from_currency}&to={to_currency}"
        res = requests.get(url, timeout=5)
        data = res.json()

        rates = data.get("rates", {})

        labels = []
        values = []

        for d in sorted(rates.keys()):
            labels.append(d)
            values.append(rates[d][to_currency])

        return JsonResponse({
            "labels": labels,
            "values": values
        })

    except:
        return JsonResponse({"labels": [], "values": []})