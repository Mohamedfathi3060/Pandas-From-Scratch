from dataframe import Dataframe
def main():
    pass
    # TODO: Read data
    df = Dataframe.read_csv()
    print(df.count_nulls())
    df.describe()
    # TODO: Fill missing values
    # Numeric columns → mean
    # Categorical columns → mode


    # TODO:Generate statistics file


    # TODO:Write cleaned data to CSV



if __name__ == "__main__":
    main()
