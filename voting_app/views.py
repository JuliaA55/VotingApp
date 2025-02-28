from django.shortcuts import render
from django.http import JsonResponse
from .web3_service import add_candidate, vote, get_winner, get_balance
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from web3 import Web3

# Create your views here.

def home(request):
    return render(request, 'votings/home.html')
@csrf_exempt 
def add_candidate_view(request):
    if request.method == "POST":
        print(f"POST-дані: {request.POST}")
        name = request.POST.get("name")
        sender = request.POST.get("sender")
        sender = Web3.to_checksum_address(sender)
        print(f"Отримані дані: name={name}, sender={sender}") 
        add_candidate(name, sender)
        return JsonResponse({"message": "Candidate added!"})
    
@csrf_exempt 
def vote_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sender = request.POST.get("sender")
        sender = Web3.to_checksum_address(sender)
        vote(name, sender)
        return JsonResponse({"message": "Vote counted!"})
    
def get_winner_view(request):
  return JsonResponse({"winner": get_winner()})

def get_balance_view(request):
    balance_wei = get_balance()
    balance_eth = Web3.from_wei(balance_wei, 'ether') 
    return JsonResponse({"balance": balance_eth})
