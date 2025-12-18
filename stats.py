from functools import reduce
import file_handler
def get_col_max(col:list):
    """
    Compute the maximum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The maximum value in the column (numeric type).
    """
    try:
        return reduce(lambda x, y: y if (x is None) or ((y is not None) and x < y) else x, col)
    except:
        print("Invalid Data Type")

def get_col_min(col:list):
    """
    Compute the minimum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The minimum value in the column (numeric type).
    """
    try:
        return reduce(lambda x, y: y if (x is None) or ((y is not None) and x > y) else x, col)
    except:
        print("Invalid Data Type")

def get_col_mean(col:list):
    """
    Compute the mean (average) value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The mean value of the column (float).
    """
    try:
        count = 0
        sum = 0.0
        for el in col:
            if el is not None:
                sum += el
                count += 1
        return  (sum / count).__round__(2)
    except:
        print("Non Numerical Column")
        return 0

def get_col_median(col:list):
    """
    Compute the median value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The median value of the column (numeric type).
    """
    try:
        newcol = custom_sort(col.copy())
        if len(newcol) % 2 == 1:
            return newcol[len(newcol) // 2]
        else:
            return ((newcol[(len(newcol) // 2)] + newcol[(len(newcol) // 2) -1] ) / 2).__round__(2)
    except:
        print("Invalid Data Type")

def get_col_mode(col:list):
    """
    Compute the mode (most frequent value) of a column.

    Args:
        col (list): A list of values. `None` values are ignored.

    Returns:
        The mode value of the column. If multiple values have the same
        frequency, the first encountered is returned.
    """
    try:
        dict = {}
        for el in col:
            if el is not None:
                try:
                    dict[el] += 1
                except:
                    dict[el] = 1
        max_col = ""
        max_count = 0
        for key, val in dict.items():
            if val > max_count:
                max_col = key
                max_count = val
        return max_col
    except:
        print("Invalid Data Type")
        return None
        
def get_stat(data:dict, dtypes:dict, function):
    """
    Apply a statistical function to all numerical columns in a dataset.

    Args:
        data (dict): Dictionary where keys are column names and values are lists of column values.
        dtypes (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        function (function): A function to apply to each numerical column (e.g., get_col_max, get_col_mean).

    Returns:
        dict: A dictionary where keys are column names and values are the result
        of applying the function to that column. Only numerical columns are processed.
    """
    try:
        stringToFunction = {
            'get_col_max' : get_col_max,
            'get_col_min': get_col_min,
            'get_col_mean':get_col_mean,
            'get_col_median':get_col_median,
            'get_col_mode':get_col_mode
        }
        if function not in [get_col_max,get_col_min, get_col_mean, get_col_median, get_col_mode]:
            function = stringToFunction[function]
        res = {}
        for key, val in data.items():
            if dtypes[key] == "string" and function != get_col_mode:
                continue
            res[key] = function(val)
        return res
    except:
        print("Invalid Method")
        return None

def custom_sort(arr:list):
    try:
        arr = [ x for x in arr if x is not None]
        change = True
        while change:
            change = False
            for i  in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    tmp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = tmp
                    change = True
        return arr
    except:
        print("invalid Data Type")
        return None

# print(get_stat({'A':[-10,None,10],
#           'B':[10,None, -10],
#           'C':['A','B','A','E','E','E','A','E','E']
#           }, {'A':'int','B':'float','C':'string'}, 'get_col_max'))


# dtypes = file_handler.read_dtype()
# data = file_handler.read_csv_file(dtypes=dtypes)
#
# print(get_stat(data, dtypes, 'get_col_mode'))
