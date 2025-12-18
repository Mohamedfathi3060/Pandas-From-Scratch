import csv

def read_csv_file(file_path="data/titanic.csv", dtypes:dict=None):
    """
    Read a CSV file and convert each column to the specified data type.

    Args:
        file_path (str): Path to the CSV data file.
        dtypes (dict): Dictionary mapping column names to data types ('int', 'float', 'string').

    Returns:
        dict: A dictionary where keys are column names and values are lists of column values.
              Missing values (empty strings) are replaced with None.
    
    """
    res = {}
    cols = []
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    cols = row
                    for col in row:
                        res[col] = []
                else:
                    for j, cell in enumerate(row):
                        newCell = 0
                        if cell == '':
                            newCell = None
                        elif dtypes[cols[j]] == 'string':
                            newCell = cell
                        elif dtypes[cols[j]] == 'int':
                            newCell = int(cell)
                        elif dtypes[cols[j]] == 'float':
                            newCell = float(cell)
                        res[cols[j]].append(newCell)

        # for key, val in res.items():
        #     print(key, val)
        #     print("\n\n\n\n\n\n\n\n")
        return res
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError:
        print("Incorrect data type")
        return None

def read_dtype(file_path="data/titanic_dtype.csv"):
    """
    Read a CSV file containing column names and their data types.

    Args:
        file_path (str): Path to the CSV file containing column names and types.

    Returns:
        dict: A dictionary where keys are column names and values are data types ('int', 'float', 'string').
    """
    res = {}
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i != 0:
                    res[row[0]] = row[1]
    except FileNotFoundError:
        print("File not found")
    return res

def write_file(file_path="data/out.csv", data:dict=None):
    """
    Write a data dictionary to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (dict): Dictionary where keys are column names and values are lists of column values.

    Returns:
        None
    """
    try:
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(list(data.keys()))
            for i in range(len(list(data.values())[0])):
                row = []
                for val in data.values():
                    row.append(val[i])
                writer.writerow(row)
    except:
        print("Invalid Data")

# dict = read_dtype("data/titanic_dtype.csv")
# data = read_csv_file("data/titanic.csv",dict)
# write_file('data/out.csv', data)
