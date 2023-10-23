from django.shortcuts import render 

def agendar(request):
    return render(request, 'agendar.html', {
        #context
    })