from django.shortcuts import render
from django.http import HttpResponse
from .crop_prediction import calc
# Create your views here.

def predict(request):
    return render(request, 'index.html')
def result(request):
    if request.method == 'POST':
        pro = float(request.POST.get('production')) 
        ar = float(request.POST.get('Annual_Rainfall'))
        fer = float(request.POST.get('Fertilizers') )
        pes = float(request.POST.get('Pesticides'))
        print(type(pro))

        final_res=calc(ar,fer,pes,pro)
        print(final_res)
    return render(request, 'index_res.html', {'ans': final_res})
    
