from django import forms


class NumberForm(forms.Form):
    patientPC = forms.CharField()

def ButtonTemplate():
    buttons = {'name': [['2D график по столбцам матрицы T(счета)', 'OpenPC2DS', 1],
                        ['2D график по столбцам матрицы P (нагрузки)', 'OpenPC2DL', 2],
                        ['3D график по столбцам матрицы T (счета)', 'OpenPC3DS', 3],
                        ['Найти средние отношения поглощения', 'RATIOAVERAGE', 4],
                        ['Найти отношения поглощений конкретных ММ', 'RATIOCHOOSE', 5]]}
    return buttons
