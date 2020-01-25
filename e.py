import csv
import os
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

from tabulate import tabulate


class DataFrame:
    def __init__(self, headers, rows):
        self._headers = headers
        self._rows = rows

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, new_headers):
        print(self._headers)
        assert len(self._headers) == len(new_headers)
        pass

    @property
    def rows(self):
        return self._rows

    def group_by(self, by):
        groups = {}
        for line in self._rows:
            print(self._headers)
            if line[self._headers.index(by)] not in groups.keys():
                groups[self._headers.index(by)] = [line]
            else:
                groups[self._headers.index(by)].append(line)
        return GrouppedDataFrame(by=by, headers=self._headers, groups=groups)

    def merge(self, df, by):
        pass

    def __getitem__(self, name):
        pass

    def __setitem__(self, name):
        pass

    def __str__(self):
        return tabulate(self.rows, headers=self.headers)

    @staticmethod
    def from_file(path):
        with open(path, "r", encoding='utf=8') as f_obj:
            reader = csv.reader(f_obj)
        return reader


    def to_csv(self, path):
        with open(path, 'w') as file:
            for row in self._rows:
                file.write(f'{row}\n')


class GrouppedDataFrame:

    def __init__(self, by, headers, groups):
        self._by = by
        self._headers = headers
        self._groups = groups

    def sum_by(self, by):
        rows = []
        for group in self._groups:
            print(self._headers,by)
            index = self._headers.index(by)
            new_val = 0
            new_row = self._groups[group][0]
            for line in self._groups[group]:
                new_val += int(line[index])
            rows.append(new_row)
        return DataFrame(headers=self._headers, rows=rows)


# BASE_PATH = '/home/olya/Downloads'
# PATH = os.path.join(BASE_PATH, 'spb_cameras.csv')
# POPULATION_PATH = os.path.join(BASE_PATH, 'spb_population_per_district.csv')
# CAMERAS_PATH = os.path.join(BASE_PATH, 'cameras_per_district.csv')
PATH = 'spb_cameras.csv'
POPULATION_PATH = 'spb_population_per_district.csv'
CAMERAS_PATH = 'cameras_per_district.csv'
# ===================================================
df = DataFrame.from_file(PATH)
amount_df = df.group_by('district').sum_by('amount')
amount_df.headers = ['Район', 'Число Камер']
amount_df.to_csv('cameras_per_district.csv')
print(amount_df)

# ===================================================
amount_df = DataFrame.from_file(CAMERAS_PATH)
pop_df = DataFrame.from_file(POPULATION_PATH)
full_df = amount_df.merge(pop_df, by='Район')
print(full_df)


# full_df['Плотность'] = # ...
# full_df.to_csv('exam_done.csv')
# print(full_df)
