import pandas as pd

#Initial we have to load the csv file:

def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print('The file has been loaded successfully.')
        return df
    
    except FileNotFoundError:
        print('File not found.')
        return None
    

#Secondly we have to clean the data to make sure that our data has no impurities.

def clean_data(df):
    df.fillna(0, inplace=True)
    print('Missing Valurs have been Handled.')
    return df


#Now we need to analyse the data 

def analyse_data(df):
    print('\n--- Data Summary ---')
    print(df.describe())
    print('\nColumn-wise Null Count:')
    print(df.isnull().sum()) 


#Once the data has been cleaned we would like to save it

def save_clean_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f'Cleaned data saved to {output_file}')


#Now we need to create a main function to combine all the functions we have create(cleaned data)

if __name__ == '__main__':
    file_path = 'Data Processing\laptopData.csv'
    cleaned_file = 'cleaned_data.csv'

    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        analyse_data(df)
        save_clean_data(df, cleaned_file)

