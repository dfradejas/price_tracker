from price_tracker_app.functions import addItem
from typing import Text
from django.shortcuts import redirect, render, HttpResponseRedirect
from price_tracker_app.models import Item
from price_tracker_app.forms import AddItemForm
from price_tracker_app.functions import addItem

# Create your views here.

def home(request):
    items = Item.objects.all()

    context = {
        "items": items
    }
    
    return render(request, "home.html", context)



def settings(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            addItem(url)
            return HttpResponseRedirect('/')
    else:
        form = AddItemForm()

    return render(request, 'settings.html', {'form': form})