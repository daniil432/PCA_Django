import copy


class Derivative(object):
    def __init__(self, data_deriv):
        self.data_deriv = data_deriv
        
    def calc_derivative(self):
        all_derivatives = []
        "Создаем копию списка волновых чисел и помещаем перед списком всех производных, которые далее будут рассчитаны"
        all_derivatives.append(copy.deepcopy(list(self.data_deriv[0])))
        for sample in range(len(self.data_deriv)):
            sample_derivative = []
            if sample == 0:
                pass
            else:
                "Рассчитываем производную от нашего набора точек"
                "Мы не рассчитываем производную в крайних точках, т.к. в них она не может быть корректно посчитана"
                for point in range(len(self.data_deriv[1])):
                    if point == 0:
                        pass
                        "Можно рассчитать значения для крайних точек диапазона, но эти точки не несут смысла"
                        """deriv = 0.5 * ((self.data_deriv[sample][point+1] - self.data_deriv[sample][point]) /
                                       (self.data_deriv[0][point+1] - self.data_deriv[0][point]))
                        sample_derivative.append(deriv)"""
                    elif point == len(self.data_deriv[1]) - 1:
                        pass
                        "Можно рассчитать значения для крайних точек диапазона, но эти точки не несут смысла"
                        """deriv = 0.5 * ((self.data_deriv[sample][point] - self.data_deriv[sample][point-1]) /
                                       (self.data_deriv[0][point] - self.data_deriv[0][point-1]))
                        sample_derivative.append(deriv)"""
                    elif (point != 0) and (point != len(self.data_deriv[1]) - 1):
                        "Рассчёт производной вне крайних точек, т.е. на всём остальном диапазоне внутри"
                        deriv = 0.5 * (((self.data_deriv[sample][point + 1] - self.data_deriv[sample][point]) /
                                        (self.data_deriv[0][point + 1] - self.data_deriv[0][point])) +
                                       ((self.data_deriv[sample][point] - self.data_deriv[sample][point - 1]) /
                                        (self.data_deriv[0][point] - self.data_deriv[0][point - 1])))
                        "Получили производную для одного набора точек"
                        sample_derivative.append(deriv)
                "Присоединяем одну производную к списку всех производных"
                all_derivatives.append(sample_derivative)
        "Вырезаем из списка волновых чисел крайние точки, чтобы длина совпадала с длиной производной"
        all_derivatives[0].pop(0)
        all_derivatives[0].pop(len(all_derivatives[0]) - 1)
        "Получили список волновых чисел на 0-й позиции и производные от искомого набора данных на остальных позициях"
        return all_derivatives
