from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import petpicker_Form
from .models import petpicker_Model
from .utils import PetCal, get_plot_animal_Data, get_plot_Full_animal_Data, get_plot_Full_animal_Data_Heat
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

            PetData, Graph_data, Total_Data = PetCal(obj.Init_Price,
                                                     obj.Main_Time,
                                                     obj.Life_Span,
                                                     obj.Trainable,
                                                     obj.Main_Cost,
                                                     obj.Weight,
                                                     obj.Lenght,
                                                     obj.Max_Space)

            chart1 = get_plot_animal_Data(PetData, Graph_data, 6)
            chart2 = get_plot_animal_Data(PetData, Graph_data, 7)
            chart3 = get_plot_animal_Data(PetData, Graph_data, 8)

            Full_Chart = get_plot_Full_animal_Data(Total_Data)
            Full_Heat = get_plot_Full_animal_Data_Heat(Graph_data)

            return render(request, 'main/Data_view.html', {'Data' : PetData,
                                                            'chart1' : chart1,
                                                            'chart2' : chart2,
                                                            'chart3' : chart3,
                                                            'Full_Chart' : Full_Chart,
                                                            'Full_Heat' : Full_Heat})

    else:

        form = petpicker_Form()

    return render(request, 'main/home.html', {'form': form})
