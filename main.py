from dataframe import Dataframe
def main():
    pass
    # TODO: Read data
    df = Dataframe.read_csv()
    print(df.count_nulls())
    df.describe('data/Before_Fill_Desc.csv')
    # # TODO: Fill missing values
    # # Numeric columns → mean
    # # Categorical columns → mode
    df.fillna('get_col_mean','get_col_mode')
    # # TODO:Generate statistics file
    df.describe('data/After_Fill_Desc.csv')
    
    # TODO:Write cleaned data to CSV
    df.to_csv()


if __name__ == "__main__":
    main()
