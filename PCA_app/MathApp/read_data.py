import pandas as pd
import numpy as np
import copy


class ReadingFromFiles(object):
    def __init__(self, number1, number2, path_type_list):
        "Данные передются со страницы с вводом диапазона волновых чисел. Путь к файлам для исследования берется из БД"
        self.number1 = int(number1)
        self.number2 = int(number2)
        self.path_type_list = path_type_list

    def read_files(self):
        filenames = []
        input_df_list = []
        "Диапазон волновых чисел, в котором мы будем проодить исследование"
        self.input_waves = [[self.number1, self.number2]]
        if self.input_waves[0][0] > self.input_waves[0][1]:
            self.input_waves[0][0], self.input_waves[0][1] = self.input_waves[0][1], self.input_waves[0][0]
        "Считываем файлы из БД"
        for j in range(len(self.path_type_list)):
            file_path = self.path_type_list[j]['patient_path']
            filename = self.path_type_list[j]['patient_type'] + str(self.path_type_list[j]['patient_number'])
            input_df = pd.read_csv(file_path, header=None)
            input_df_list.append(input_df)
            "Важная для обработки информация - список пациентов. В дальнешем нужен для корректного отображения графиков"
            filenames.append(filename)
        print('[PCA]: files was read')
        return input_df_list, filenames

    def cut_files(self):
        input_matrix = []
        input_df_list = self.read_files()[0]
        for j in range(len(self.path_type_list)):
            input_df = input_df_list[j]
            "Собираем матрицу из данных, содержащихся внутри считываемых файлов"
            one_pat = []
            for i in range(len(self.input_waves)):
                input_df_temp = input_df.drop(input_df[input_df[0] < self.input_waves[i][0]].index)
                input_df_temp = input_df_temp.drop(input_df_temp[input_df_temp[0] > self.input_waves[i][1]].index)
                one_pat = np.concatenate((one_pat, input_df_temp[1].values.astype('float')))
            "Та матрица, с которой дальше работаем при помощи метода главных компонент"
            input_matrix.append(one_pat)
        "Диапазон волновых чисел, с которыми работаем. Нужен при расчете производной от спектров"
        one_wave = []
        for i in range(len(self.input_waves)):
            input_df = pd.read_csv(self.path_type_list[1]['patient_path'], header=None)
            input_df_temp = input_df.drop(input_df[input_df[0] < self.input_waves[i][0]].index)
            input_df_temp = input_df_temp.drop(input_df_temp[input_df_temp[0] > self.input_waves[i][1]].index)
            one_wave = np.concatenate((one_wave, input_df_temp[0].values.astype('float')))
        "Копия исследуемой матрицы, от копии будет браться производная. Диапазон волновых чисел для нужен этих целей"
        all_samples_for_derivative = copy.deepcopy(input_matrix)
        all_samples_for_derivative.insert(0, one_wave)
        print('[PCA]: файлы прочитаны')
        return input_matrix, all_samples_for_derivative

    def normalization(self, input_matrix):
        "Нормализация матрицы нужна, чтобы метод главных компонент отработал лучше"
        for index in range(len(input_matrix[0])):
            column = [row[index] for row in input_matrix]
            m = np.mean(column)
            s = np.std(column)
            normalization_function = lambda x: (x - m) / s
            normalized_column = normalization_function(column)
            for str_index in range(len(input_matrix)):
                input_matrix[str_index][index] = normalized_column[str_index]
        print('[PCA]: нормализация произведена')
        return input_matrix
