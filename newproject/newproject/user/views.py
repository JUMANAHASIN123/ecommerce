from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request,'userapp/order.html')