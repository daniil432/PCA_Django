import numpy as np


class MaxMinSearch(object):
    def __init__(self, input_df_list):
        self.input_df_list = input_df_list

    def min_max_search(self):
        "В данных промежутках находятся минимумы и максимумы на спектрах"
        diapason = [[1600, 1650], [1580, 1600], [1550, 1580], [1500, 1510], [1440, 1470]]
        baseline = [1720, 2000]
        ratio = []
        waves = []
        for input_df in self.input_df_list:
            "Создание диапазона для построения графиков сравнений"
            intensities = []
            waves_in_diapason = []
            "из всего диапазона волновых чисел вырезаются нужные фрагменты с макс. и мин."
            for i in diapason:
                temp = input_df.drop(input_df[input_df[0] <= i[0]].index)
                temp = temp.drop(temp[temp[0] >= i[1]].index)
                intensities.append(temp[1].values.astype('float').tolist())
                waves_in_diapason.append(temp[0].values.astype('float').tolist())
            "базовая линия 2000-1700 см-1 и её среднее, которое будет вычитаться из остального спектра"
            base = input_df.drop(input_df[input_df[0] <= baseline[0]].index)
            base = base.drop(base[base[0] >= baseline[1]].index)
            base = base[1].values.astype('float')
            coefficient = np.mean(base)
            "находим макс. и мин., вычитаем из них среднее по базовой линии"
            waves_temp = []
            max_min_temp = []
            for ind in range(5):
                waves.append(waves_temp)
                max_min_temp.append(max(intensities[ind]) - coefficient)
                waves_temp.append(waves_in_diapason[ind][intensities[ind].index(max(intensities[ind]))])
            "находим отношения максимумов и минимумов попарно"
            ratio_temp = []
            for i in range(len(max_min_temp)):
                for j in range(i + 1, len(max_min_temp)):
                    ratio_temp.append(max_min_temp[i] / max_min_temp[j])
            ratio.append(ratio_temp)
        return ratio, waves
