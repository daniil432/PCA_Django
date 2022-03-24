import os
import psycopg2
from psycopg2 import Error
import re
import glob


def write_data():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="pca_database")
        cursor = connection.cursor()
        path = "C:/PCA_proj/PCA_app/dpt_data/"
        os.chdir(path)
        all_pathways = glob.glob("*.dpt")
        i = 0
        for one_file in all_pathways:
            path_for_database = path + one_file
            print(path_for_database)
            patient = re.findall(r'[A-Z]{1,2}', one_file)[0]
            if len(patient) == 2:
                i += 1
                number_of_patient = i
            else:
                number_of_patient = re.search(r'\d{1,2}', one_file).group()
            print(patient, number_of_patient)
            try:
                create_table_query = f'''INSERT INTO public."PCA_app_patientfiles" (patient_type, patient_path, patient_number) VALUES ('{patient}', '{path_for_database}', {int(number_of_patient)})'''
                cursor.execute(create_table_query)
                connection.commit()
            except (Exception, Error) as error2:
                print("Error while writing files in db", error2)
        cursor.close()
        connection.close()
        print("PostgresSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def update_id():
    connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pca_database")
    cursor = connection.cursor()
    for i in range(68):
        if i == 0:
            pass
        else:
            create_table_query = f'''UPDATE public."PCA_app_patientfiles" SET id = {i} WHERE id = 5 + {i};'''
            cursor.execute(create_table_query)
            connection.commit()


def delete_table():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="pca_database")
        cursor = connection.cursor()
        # SQL query to create a new table
        create_table_query = '''DROP TABLE dpt_path'''
        # Execute a command: this creates a new table
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("PostgresSQL connection is closed")
        print("Table created successfully in PostgreSQL ")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
