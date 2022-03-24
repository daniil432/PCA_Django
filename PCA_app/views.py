from django.shortcuts import render, HttpResponse
from .models import PatientFiles
from .forms import DiapasonForm
from .MathApp.read_data import ReadingFromFiles
from .MathApp.max_min import MaxMinSearch
from .MathApp.sort_data import SortAndCalcRatio
from .MathApp.pca_analyzation import PcaAnalyzation
from .MathApp.derivative import Derivative
# Create your views here.


def InputPage(request):
    if request.method == 'POST':
        form = DiapasonForm(request.POST)
        print('----------------')
        print(form.data)
        if (form.data.dict()['first_number'] == '') or (form.data.dict()['second_number'] == '') or \
                (form.data.dict()['first_number'] == '' and form.data.dict()['second_number'] == ''):
            return HttpResponse('<h1>Enter data into fields</h1>')
        if form.is_valid():
            cd = form.cleaned_data
            first = cd['first_number']
            second = cd['second_number']
            data_about_patients = PatientFiles.objects.all()
            path_type_list = list(data_about_patients.values("patient_path", "patient_type"))
            "Тут начинается считывание спектров и обработка при помощи метода главных компонент"
            test = ReadingFromFiles(first, second, path_type_list)
            "Считывание спектров из файлов"
            input_df_list, filenames = test.read_files()
            "Обрезка файлов и создание матриц для обработки данных"
            input_matrix, all_samples_for_derivative = test.cut_files()
            "Нормализация матрицы для МГК"
            input_matrix = test.normalization(input_matrix)
            "Начинается обработка данных для простого сравнения"
            test_2 = MaxMinSearch(input_df_list)
            "Из спектров вырезаются нужные фрагменты, внутри них ищутся минимумы и максимумы поглощения"
            ratio, waves = test_2.min_max_search()
            test_3 = SortAndCalcRatio(ratio, waves, filenames)
            test_3.sort_ratio_and_waves()
            "Считаются отношения поглощений в найденных контрольных точках"
            calculated_patients = test_3.calculate_ratio()
            "Обработка для простого сравнения завершена"
            "Начинается обработка матриц при помощи метода главных компонент"
            test_4 = PcaAnalyzation(input_matrix)
            test_4.eigenvalues_and_vectors()
            "Получаем Т и Р матрицы, они нужны для постройки графиков"
            t_matrix, p_matrix = test_4.t_and_p_matrix()
            "Посчитаем производную от входной матрицы"
            test_5 = Derivative(input_matrix)
            first_deriv = test_5.calc_derivative()
            "Посчитаем вторую производную от входной матрицы"
            test_5 = Derivative(first_deriv)
            second_deriv = test_5.calc_derivative()
            return HttpResponse(f'<p>Success</p>')
    else:
        form = DiapasonForm()
    return render(request, 'InputPage.html', {'form': form})
