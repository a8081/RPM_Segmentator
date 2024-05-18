#%%
import os
import csv

def process_csv_files(directory):
    # Recorre cada archivo en el directorio
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, "processed_" + filename)
            
            with open(file_path, 'r', newline='') as infile, open(new_file_path, 'w', newline='') as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
                
                for row in reader:
                    writer.writerow(row)

# Llama a la función con el directorio donde se encuentran los archivos .csv
directory = 'tom/'
process_csv_files(directory)



#%%
import os
import pandas as pd
import csv

# Diccionario para sustituir nombres de columnas
column_mapping = {
    "case:concept:name": "caseID",
    "category": "target.class",
    "application": "targetApp",
    "time:timestamp": "timeStamp",
    "org:resource": "userID",
    "concept:name": "eventType",
    "browser_url": "url",
    "clipboard_content": "content",
    "workbook": "target.workbookName",
    "tag_name": "target.tagName",
    "tag_type": "target.type",
    "tag_value": "target.value",
    "tag_innerText": "target.innerText",
    "tag_checked": "target.checked",
    "tag_href": "target.href",
    "tag_option": "target.option",
    "tag_title": "target.title",
    "id": "target.id",
    "case:concept:name": "target.name",
    "current_worksheet": "target.sheetName",
    "tag_html": "target.innerHTML"
}

def process_csv(file_path, results_path):
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    # Renombrar columnas según el diccionario
    df.rename(columns=column_mapping, inplace=True)
    
    # Convertir todos los valores a strings con quotes
    # df = df.map(lambda x: f'{x}' if pd.notnull(x) else '')
    
    # Guardar el archivo CSV procesado
    output_file = f"processed_{os.path.basename(file_path)}"
    output_file = os.path.join(results_path, output_file)
    df.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL, escapechar='\\', na_rep='')
    
    # with open(file_path, 'r', newline='') as infile, open(new_file_path, 'w', newline='') as outfile:
    #     reader = csv.reader(infile)
    #     writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    #     for row in reader:
    #         writer.writerow(row)

def process_directory(directory):
    # Comprobar si en "directory" existe el directorio "processed", sino crearlo
    processed_directory = os.path.join(directory, "processed")
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)
    
    for file_name in os.listdir(directory):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory, file_name)
            process_csv(file_path, processed_directory)

# Especifica la carpeta que deseas procesar
directory_path = "tom/"

process_directory(directory_path)
