class SortAndCalcRatio(object):
    def __init__(self, ratio, waves, filenames):
        self.ratio = ratio
        self.waves = waves
        self.filenames = filenames


    def sort_ratio_and_waves(self):
        "Сортируем все интенсивности из фаилов по донорам, секретирующим и несекретирующим пациентам"
        self.sorted_patients = {
            'donor': [],
            'donor_waves': [],
            'patient': [],
            'patient_waves': [],
            'non_secreting': [],
            'non_secreting_waves': []
        }
        for i in range(len(self.filenames)):
            if (self.filenames[i][0] == 'D') or (self.filenames[i][0] == 'O') or (self.filenames[i][0] == 'B') or \
                    (self.filenames[i][0] == 'H'):
                self.sorted_patients['donor'].append(self.ratio[i])
                self.sorted_patients['donor_waves'].append(self.waves[i])
            elif (self.filenames[i][0] == 'P') or (self.filenames[i][0] == 'M'):
                self.sorted_patients['patient'].append(self.ratio[i])
                self.sorted_patients['patient_waves'].append(self.waves[i])
            elif self.filenames[i][0] == 'N':
                self.sorted_patients['non_secreting'].append(self.ratio[i])
                self.sorted_patients['non_secreting_waves'].append(self.waves[i])
            else:
                pass

    def calculate_ratio(self):
        calculated_patients = {
            'donor': [0],
            'donor_waves': [0],
            'patient': [0],
            'patient_waves': [0],
            'non_secreting': [0],
            'non_secreting_waves': [0]
        }
        normalization = []
        for key in calculated_patients:
            calculated_patients[key] = calculated_patients[key] * len(self.sorted_patients[key][0])
        for key in self.sorted_patients:
            for i in self.sorted_patients[key]:
                calculated_patients[key] = [x + y for x, y in zip(calculated_patients[key], i)]
        for key in self.sorted_patients:
            for i in range(len(calculated_patients[key])):
                if len(self.sorted_patients[key]) != 0:
                    calculated_patients[key][i] = calculated_patients[key][i] / len(self.sorted_patients[key])
                    if key == 'donor':
                        normalization.append(1/calculated_patients[key][i])
                    if (key == 'donor') or (key == 'patient') or (key == 'non_secreting'):
                        calculated_patients[key][i] = calculated_patients[key][i] * normalization[i]
        return calculated_patients
