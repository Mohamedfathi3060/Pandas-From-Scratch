from file_handler import read_csv_file, read_dtype, write_file
import stats
import csv

class Dataframe:
    def __init__(self, data:dict, dtype:dict):
        self.data = data
        self.dtype = dtype


    #TODO: define read_csv(data_path, dtype_path)
    @classmethod
    def read_csv(self, data_path='data/titanic.csv', dtype_path='data/titanic_dtype.csv'):
        try:
            dtypes = read_dtype(dtype_path)
            data = read_csv_file(data_path, dtypes)
            return Dataframe(data, dtypes)
        except:
            print("Invalid File Path or Data")
            return None

    #TODO: define count_nulls()
    def count_nulls(self):
        try:
            res = {}
            for key,val in self.dtype.items():
                res[key] = 0
            for key,val in self.data.items():
                for v in val:
                    if v is None:
                            res[key]+=1
            return res
        except:
            print("invalid Data Type")
            return None

    #TODO: define describe()
    def describe(self, path='data/describe.csv'):
        nulls = self.count_nulls()
        methods = [
            'get_col_max',
            'get_col_min',
            'get_col_mean',
            'get_col_median',
            'get_col_mode'
        ]
        headers = ['column', 'nulls', 'max','min','mean','median', 'mode']
        try:
            with open(path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(headers)

                dict ={}
                for col, ncount in nulls.items():
                    dict[col] = [ncount]

                for m in methods:
                    d = stats.get_stat(self.data, self.dtype, m)
                    for col in self.dtype.keys():
                        if col not in d:
                            dict[col].append('')
                        else:
                            dict[col].append(d[col])
                for key, val in dict.items():
                    l = list([key])
                    l.extend(val)
                    writer.writerow(l)
        except:
            print("Cannot Write Describe data")
    #TODO: define fillna()
    def fillna(self, num_strategy, cat_strategy):
        try:
            mods = stats.get_stat(self.data, self.dtype, cat_strategy)
            median = stats.get_stat(self.data, self.dtype, num_strategy)

            for key, val in self.data.items():
                if self.dtype[key] == 'string' :
                    for i in range(len(val)):
                        if val[i] is None:
                            val[i] = mods[key]
                else:
                    for i in range(len(val)):
                        if val[i] is None:
                            val[i] = median[key]
        except:
            print("Invalid Filling Null")

    #TODO: define to_csv()
    def to_csv(self):
        try:
            write_file('data/out.csv',self.data)
        except:
            print("Invalid")
#
# df = Dataframe.read_csv("data/titanic.csv","data/titanic_dtype.csv")
# df.describe()