from django import forms

class Form(forms.Form):
    img_path = forms.CharField(label='img_path', required=True, \
        widget=forms.TextInput(attrs={'class':'form-control'}))