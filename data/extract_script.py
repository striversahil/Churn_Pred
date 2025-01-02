import zipfile
import os
import time

def extract_zip(zip_path, extract_path , rename):
    '''
    Extracts a zip file to a given path and rename it to the given name

    Arguments :
        zip_path : path of the zip file
        extract_path : path to extract the zip file to

    Returns :
        None
    '''
    # Create the directory
    print(f'Making Directory : {extract_path.split("/")[-1]}')
    
    os.makedirs(extract_path, exist_ok=True)


    # Extracting the Zip File to the given path
    with zipfile.ZipFile(zip_path , 'r') as zip_ref:
        print(f"Extracting {zip_path.split('/')[-1]} to {extract_path.split('/')[-1]} ...")
        zip_ref.extractall(extract_path)

    print(f"Extracting {zip_path.split('/')[-1]} to {extract_path.split('/')[-1]}")


    # Renaming the extracted folder
    if rename:

        file_name = os.listdir(extract_path)[0] 
        os.rename(f"{extract_path}/{file_name}", f"{extract_path}/{rename}")

        print(f"Renamed {file_name} to {rename}")

    return 


if __name__ == "__main__":
    extract_zip("/home/sahildev/Development/Projects/DS_ML/Churn_Pred/data/data.zip",    # Path of the zip file
                 "/home/sahildev/Development/Projects/DS_ML/Churn_Pred/generated_extracted_data",  # Path to extract the zip file
                 "data.csv") # Rename the extracted folder
