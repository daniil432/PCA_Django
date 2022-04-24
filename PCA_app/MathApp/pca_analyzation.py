import numpy as np
import os
import pandas as pd
from subprocess import run


class PcaAnalyzation(object):
    def __init__(self, input_matrix):
        "Входная матрица. Тут может быть как матрица спектров, так и матрица производных от спектров"
        self.input_matrix = input_matrix

    def eigenvalues_and_vectors(self):
        "вычисляем транспонированную матрицу от входной"
        x_matrix = np.array(self.input_matrix)
        x_matrix_transpose = x_matrix.transpose()

        "перемножаем, x_matrix * x_matrix_transpose = c_matrix"
        "перемножаем, x_matrix_transpose * x_matrix = b_matrix"
        c_matrix = x_matrix @ x_matrix_transpose
        b_matrix = x_matrix_transpose @ x_matrix

        "записать c_matrix и b_matrix в файл"
        c_matrix_dataframe = pd.DataFrame(c_matrix)
        b_matrix_dataframe = pd.DataFrame(b_matrix)
        curpath = os.path.abspath(os.curdir)
        os.chdir('C:\\PCA_proj\\PCA_app')
        c_matrix_dataframe.to_csv('R_script\\input\\c_matrix.csv', index=False, header=None)
        b_matrix_dataframe.to_csv('R_script\\input\\b_matrix.csv', index=False, header=None)

        "запуск скрипта на R для поиска собственных чисел и собственных векторов c_matrix и b_matrix"
        R_BIN_PATH = 'C:\\Program Files\\R\\R-4.0.4\\bin'
        current_directory = os.path.abspath(os.curdir)
        run([R_BIN_PATH + '\\Rscript.exe', current_directory +
             '\\R_script\\eigenvalues_vectors.R', current_directory])

        "прочитать собственне числа и собственные вектора c_matrix и b_matrix"
        temp = {
            "eigenvectors_c": pd.read_csv('R_script\\output\\eigenvectors_c.csv', header=None).values.tolist(),
            "eigenvalues_c": pd.read_csv('R_script\\output\\eigenvalues_c.csv', header=None).values.tolist(),
            "eigenvectors_b": pd.read_csv('R_script\\output\\eigenvectors_b.csv', header=None).values.tolist(),
            "eigenvalues_b": pd.read_csv('R_script\\output\\eigenvalues_b.csv', header=None).values.tolist()
        }

        "удалить временные файлы, использовавшиеся для нахождения собственных чисел и векторов"
        os.remove('R_script\\input\\c_matrix.csv')
        os.remove('R_script\\input\\b_matrix.csv')
        os.remove('R_script\\output\\eigenvalues_c.csv')
        os.remove('R_script\\output\\eigenvalues_b.csv')
        os.remove('R_script\\output\\eigenvectors_c.csv')
        os.remove('R_script\\output\\eigenvectors_b.csv')

        self.eigen = {
            "eigenvectors_c": [],
            "eigenvalues_c": [],
            "eigenvectors_b": [],
            "eigenvalues_b": []
        }

        for key in temp:
            for value in temp[key]:
                self.eigen[key].append(value)
        os.chdir(curpath)

    def t_and_p_matrix(self):
        u_vectors, u_values, v_vectors, v_values = self.eigen["eigenvectors_c"], self.eigen["eigenvalues_c"], \
                                                   self.eigen["eigenvectors_b"], self.eigen["eigenvalues_b"]
        "pandas не совсем удобно сформировал список собственных чисел, поэтому меняем его"
        temp = []
        for value in u_values:
            temp.append(value[0])
        u_values = temp
        temp = []
        for value in v_values:
            temp.append(value[0])
        v_values = temp

        "Трнаспонируем матрицы собвстенных векторов, чтобы вектроа располагались в столбцах"
        u_vectors = np.array(u_vectors).transpose()
        v_vectors = np.array(v_vectors).transpose()

        "строим матрицу S, изначально заполняем нулями"
        s_matrix = np.zeros((len(u_values), len(v_values)))

        "какие-то собственные числа в 2х наборах совпадают, смотрим, где чисел меньше (меньше там, где матрица меньше)"
        if len(u_values) > len(v_values):
            eigenvalues = v_values
        else:
            eigenvalues = u_values

        "на диагональ матрицы S ставим собственные числа"
        for index in range(len(eigenvalues)):
            s_matrix[index][index] = (abs(eigenvalues[index])) ** (1 / 2)

        "находим матрицы T и P"
        t_matrix = u_vectors @ s_matrix
        p_matrix = v_vectors
        for el in range(len(t_matrix)):
            t_matrix[el] = list(t_matrix[el])
        for el in range(len(p_matrix)):
            p_matrix[el] = list(p_matrix[el])
        # g = u_vectors @ s_matrix @ v_vectors
        return list(t_matrix), list(p_matrix)
