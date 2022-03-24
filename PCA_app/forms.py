from django import forms


class DiapasonForm(forms.Form):
    first_number = forms.IntegerField()
    second_number = forms.IntegerField()
