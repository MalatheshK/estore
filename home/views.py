from django.shortcuts import render
from .models import products
from .forms import BuyForm

# Create your views here.
def index(request):
    obj = products.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'home_page.html', context)

def buy(request):
    context = {}

    form = BuyForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = BuyForm()

    context['form']=form
    return render(request, 'buy_page.html', context)

def about(request):
    return render(request, 'about_page.html')