from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def restaurant_page(request):
    return render(request, 'restaurant.html', context)