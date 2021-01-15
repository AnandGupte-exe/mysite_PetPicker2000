from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import petpicker_Form
from .models import petpicker_Model
from .Pet_Calculator import PetCal
import matplotlib.pyplot as plt
import urllib, base64
import io

# Create your views here.
def About_Page(request):
    if request.method == "GET":
        return render(request, 'main/Info_Page.html')

def get_PetData(request):
    global PetData
    if request.method == 'POST':
        form = petpicker_Form(request.POST)
        if form.is_valid():
            obj = petpicker_Model()
            obj.Init_Price = form.cleaned_data['Init_Price']
            obj.Main_Time = form.cleaned_data['Main_Time']
            obj.Life_Span = form.cleaned_data['Life_Span']
            obj.Trainable = form.cleaned_data['Trainable']
            obj.Main_Cost = form.cleaned_data['Main_Cost']
            obj.Weight = form.cleaned_data['Weight']
            obj.Lenght = form.cleaned_data['Lenght']
            obj.Max_Space = form.cleaned_data['Max_Space']
            obj.save()
            PetData = PetCal(obj.Init_Price,
                             obj.Main_Time,
                             obj.Life_Span,
                             obj.Trainable,
                             obj.Main_Cost,
                             obj.Weight,
                             obj.Lenght,
                             obj.Max_Space)

            plt.plot(range(10))
            fig = plt.gcf()
            #convert graph into dtring buffer and then we convert 64 bit code into image
            buf = io.BytesIO()
            fig.savefig(buf,format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

            return render(request, 'main/Data_view.html', {'Data': PetData})
    else:

        form = petpicker_Form()
    return render(request, 'main/home.html', {'form': form})
