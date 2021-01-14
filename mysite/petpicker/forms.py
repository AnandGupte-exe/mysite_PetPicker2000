from django import forms

class petpicker_Form(forms.Form):
    Init_Price = forms.IntegerField(label='Init_Price')
    Main_Time = forms.IntegerField(label='Main_Time')
    Life_Span = forms.IntegerField(label='Life_Span')
    Trainable = forms.IntegerField(label='Trainable')
    Main_Cost = forms.IntegerField(label='Main_Cost')
    Weight = forms.IntegerField(label='Weight')
    Lenght = forms.IntegerField(label='Lenght')
    Max_Space = forms.IntegerField(label='Max_Space')

form = petpicker_Form()
