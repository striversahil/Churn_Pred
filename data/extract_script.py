import zipfile
import os

def extract_zip(zip_path, extract_path , rename):
    '''
    Extracts a zip file to a given path and rename it to the given name

    Arguments :
        zip_path : path of the zip file
        extract_path : path to extract the zip file to

    Returns :
        None
    '''
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path , 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    print(f"Extracted {zip_path} to {extract_path}")


    '''From Here onwards is the code to rename the extracted folder'''
    if rename:

        file_name = os.listdir(extract_path)[0] 
        os.rename(f"{extract_path}/{file_name}", f"{extract_path}/{rename}")

    return 


if __name__ == "__main__":
    extract_zip("/home/sahildev/Development/Projects/DS_ML/Churn_Pred/data/data.zip",    # Path of the zip file
                 "/home/sahildev/Development/Projects/DS_ML/Churn_Pred/extracted_data",  # Path to extract the zip file
                 "data.csv") # Rename the extracted folder
