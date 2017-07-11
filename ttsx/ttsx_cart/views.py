from django.shortcuts import render

# Create your views here.

def index(request):
    uname = request.session.get('uname')
    context = {'uname':uname, }
    return render(request, 'cart/cart.html', context)

