from django import forms

class petpicker_Form(forms.Form):
    Init_Price = forms.FloatField(label='Init_Price')
    Main_Time = forms.FloatField(label='Main_Time')
    Life_Span = forms.FloatField(label='Life_Span')
    Trainable = forms.FloatField(label='Trainable')
    Main_Cost = forms.FloatField(label='Main_Cost')
    Weight = forms.FloatField(label='Weight')
    Lenght = forms.FloatField(label='Lenght')
    Max_Space = forms.FloatField(label='Max_Space')

form = petpicker_Form()
