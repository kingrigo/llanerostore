from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from .models import Item

# Create your views here.
def index(request):
    return render(request,'base.html')

class StoreView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "storeList.html"
    paginate_by = 3 #PROVISORIO PARA TESTEO, CAMBIAR A 10

class StoreDetail(DetailView):
    model = Item
    template_name = "storeDetail.html"

