from django.shortcuts import render
from Graph_App.forms import NumberForm
from PCA_app.MathApp.read_data import ReadingFromFiles
from PCA_app.MathApp.max_min import MaxMinSearch
from PCA_app.MathApp.sort_data import SortAndCalcRatio
from PCA_app.MathApp.pca_analyzation import PcaAnalyzation
from PCA_app.MathApp.derivative import Derivative
from Graph_App.forms import ButtonTemplate
import re


def Graph(request):
    context = {'buttons': ButtonTemplate}
    t_matrix, p_matrix, filenames, first_deriv, second_deriv, calculated_average, calculated_samples = ProcessData(request)
    for i in range(len(t_matrix)):
        t_matrix[i] = list(t_matrix[i])
    for i in range(len(p_matrix)):
        p_matrix[i] = list(p_matrix[i])
    t_matrix = list(t_matrix)
    p_matrix = list(p_matrix)
    request.session['t_matrix'] = t_matrix
    request.session['p_matrix'] = p_matrix
    request.session['filenames'] = filenames
    request.session['first_deriv'] = first_deriv
    request.session['second_deriv'] = second_deriv
    request.session['calculated_average'] = calculated_average
    request.session['calculated_samples'] = calculated_samples
    print('1---------------------------------')
    print(request.session['t_matrix'])
    print('2---------------------------------')
    print(request.session['p_matrix'])
    print('3---------------------------------')
    print(request.session['first_deriv'])
    print('4---------------------------------')
    print(request.session['second_deriv'])
    print('5---------------------------------')
    print(request.session['calculated_average'])
    print('6---------------------------------')
    print(request.session['calculated_samples'])
    return render(request, 'Graph_App/GraphWindow.html', context)


def testview(request, param):
    if param == 1:
        header = "Введите номера главных компонент для 2D:"
        condition = 1
        return test(request, header, condition, param)
    elif param == 2:
        header = "Введите номера главных компонент для 3D:"
        condition = 1
        print(param, type(param))
        return test(request, header, condition, param)
    elif param == 3:
        header = "Введите номер главной компоненты для графика нагрузок:"
        condition = 1
        print(param, type(param))
        return test(request, header, condition, param)
    elif param == 4:
        header = ''
        condition = 0
        print(param, type(param))
        return test(request, header, condition, param)
    elif param == 5:
        header = "Введите номера пациентов для сравнения с донорами:"
        condition = 1
        print(param, type(param))
        return test(request, header, condition, param)
    else:
        context = {'buttons': ButtonTemplate, 'condition': 1}
        print(param, type(param))
        return render(request, 'Graph_App/GraphWindow.html', context)


def test(request, header, condition, param):
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            print(form.data)
            cd = form.cleaned_data
            try:
                selected_numbers = re.findall(r'(\d+)', cd['patientPC'])
                if selected_numbers == []:
                    selected_numbers = 'Вы ввели что-то не так, проверьте, есть ли в вашем запросе номера объектов, которые вы хотите вывести на график'
                else:
                    for ind in range(len(selected_numbers)):
                        selected_numbers[ind] = int(selected_numbers[ind])
                    print('ya tut')
                    x_y_data = ChooseTypeOfGraph(request, param, selected_numbers)
                    print('ya uje tut')
                    print(x_y_data, type(x_y_data))
            except:
                selected_numbers = 'Ошибка'
            context = {'form': form, 'buttons': ButtonTemplate, 'data': selected_numbers, 'condition': condition, 'header': header}
            return render(request, 'Graph_App/GraphWindow.html', context)
        else:
            selected_numbers = 'Вы ничего не ввели или ввели с данные ошибкой'
            context = {'form': form, 'buttons': ButtonTemplate, 'data': selected_numbers, 'condition': condition, 'header': header}
            return render(request, 'Graph_App/GraphWindow.html', context)
    else:
        form = NumberForm()
        context = {'form': form, 'buttons': ButtonTemplate, 'condition': condition, 'header': header}
    return render(request, 'Graph_App/GraphWindow.html', context)


def ProcessData(request):
    from PCA_app.models import PatientFiles
    first = request.session['first']
    second = request.session['second']
    data_about_patients = PatientFiles.objects.all()
    path_type_list = list(data_about_patients.values("patient_path", "patient_type", "patient_number"))
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
    "Считаются средние отношения поглощений в найденных контрольных точках"
    calculated_average = test_3.calculate_average()
    "Считаются для каждого образца отношения поглощений в найденных контрольных точках"
    calculated_samples = test_3.calculate_samples()
    "Обработка для простого сравнения завершена"
    "Начинается обработка матриц при помощи метода главных компонент"
    test_4 = PcaAnalyzation(input_matrix)
    test_4.eigenvalues_and_vectors()
    "Получаем Т и Р матрицы, они нужны для постройки графиков"
    t_matrix, p_matrix = test_4.t_and_p_matrix()
    t_matrix = list(t_matrix)
    p_matrix = list(p_matrix)
    "Посчитаем производную от входной матрицы"
    test_5 = Derivative(input_matrix)
    first_deriv = test_5.calc_derivative()
    "Посчитаем вторую производную от входной матрицы"
    test_5 = Derivative(first_deriv)
    second_deriv = test_5.calc_derivative()
    return t_matrix, p_matrix, filenames, first_deriv, second_deriv, calculated_average, calculated_samples


def ChooseTypeOfGraph(request, param, selected_numbers):
    donor_col = [[], []]
    mm_col = [[], []]
    non_mm_col = [[], []]
    unknown = [[], []]
    x_y_data = {}
    filenames = request.session['filenames']
    if param == (1 or 2 or 3):
        if param == (1 or 3):
            selected_matrix = request.session['t_matrix']
        elif param == 2:
            selected_matrix = request.session['p_matrix']
        for ind in range(len(selected_matrix)):
            if filenames[ind][0] == ('D' or 'H'):
                donor_col[0].append(selected_matrix[ind][selected_numbers[0]-1])
                donor_col[1].append(selected_matrix[ind][selected_numbers[1] - 1])
                if param == 3:
                    donor_col[2].append(selected_matrix[ind][selected_numbers[2] - 1])
                else:
                    pass
            elif filenames[ind][0] == ('M' or 'P'):
                mm_col[0].append(selected_matrix[ind][selected_numbers[0]-1])
                mm_col[1].append(selected_matrix[ind][selected_numbers[1] - 1])
                if param == 3:
                    mm_col[2].append(selected_matrix[ind][selected_numbers[2] - 1])
                else:
                    pass
            elif (filenames[ind][0] == 'N') or (filenames[ind][0:3] == 'Non'):
                non_mm_col[0].append(selected_matrix[ind][selected_numbers[0] - 1])
                non_mm_col[1].append(selected_matrix[ind][selected_numbers[1] - 1])
                if param == 3:
                    non_mm_col[2].append(selected_matrix[ind][selected_numbers[2] - 1])
                else:
                    pass
            else:
                unknown[0].append(selected_matrix[ind][selected_numbers[0] - 1])
                unknown[1].append(selected_matrix[ind][selected_numbers[1] - 1])
                if param == 3:
                    unknown[2].append(selected_matrix[ind][selected_numbers[2] - 1])
                else:
                    pass
            x_y_data = {"donor": donor_col, "myeloma": mm_col, "non_myeloma": non_mm_col, "unknown": unknown}
    elif param == 4:
        selected_matrix = request.session['calculated_average']
        donor_col[0], donor_col[1] = selected_matrix['donor'], selected_matrix['donor_waves']
        mm_col[0], mm_col[1] = selected_matrix['patient'], selected_matrix['patient_waves']
        non_mm_col[0], non_mm_col[1] = selected_matrix['non_secreting'], selected_matrix['non_secreting']
        x_y_data = {"donor": donor_col, "myeloma": mm_col, "non_myeloma": non_mm_col, "unknown": unknown}
    elif param == 5:
        selected_matrix = request.session['calculated_samples']
        mm_name = []
        non_name = []
        for name in range(len(filenames)):
            if filenames[name][0] == ("D" or "H"):
                pass
            elif filenames[name][0] == ("M" or "P"):
                mm_name.append(filenames[name])
            elif (filenames[name][0] == "N") or (filenames[name][0:3] == "Non"):
                non_name.append(filenames[name])
        for i in range(len(mm_name)):
            for num in selected_numbers:
                try:
                    if mm_name[i][1:] == num:
                        mm_col[0].append(selected_matrix['patient'][i])
                        mm_col[1].append(selected_matrix['patient_waves'][i])
                    elif non_name[i][1:] == num:
                        non_mm_col[0].append(selected_matrix['non_secreting'][i])
                        non_mm_col[1].append(selected_matrix['non_secreting_waves'][i])
                    else:
                        pass
                except:
                    pass
        x_y_data = {"donor": donor_col, "myeloma": mm_col, "non_myeloma": non_mm_col, "unknown": unknown}
    return x_y_data
