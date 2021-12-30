from django.shortcuts import render,redirect
from django.shortcuts import render


# Create your views here.
def test(request):
    context = {}
    if (request.method == 'POST'):
        x1=float(request.POST.get('x1'))
        x2 = float(request.POST.get('x2'))
        y1=float(request.POST.get('y1'))
        y2 = float(request.POST.get('y2'))
        a=(y2-y1)/(x2-x1)
        b=y1-a*x1
        if(b==0):
            equation='('+str(a)+')'+'*x'
        else:
            equation='('+str(a)+')'+'*x + '+'('+str(b)+')'
        context = {
            'myList': equation
        }
    return render(request, 'website/hello.html',context)



#cela fonctionne que si le fichier de base est bien xlsx qui n'a pas été converti à l'aide d'un autre logiciel
