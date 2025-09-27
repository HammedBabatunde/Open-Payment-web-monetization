from django.shortcuts import render

# Create your views here.
def creator_home(request):
    # This is the wallet address for your creator user
    payment_pointer = "https://ilp-sandbox.chimoney.com/thisguy"
    
    context = {
        'payment_pointer': payment_pointer
    }
    return render(request, 'webpage/index.html', context)