from django.shortcuts import render
from django.views import View
from django.urls import path
from templates import *


class HomePageView(View):
    def get(self, request):
        return render(request,'index.html')
class ClubsPageView(View):
    def get(self, request):
        return render(request,'clubs.html')
class TransferPageView(View):
    def get(self, request):
        return render(request,'latest-transfers.html')
class PlayersPageView(View):
    def get(self, request):
        return render(request,'players.html')