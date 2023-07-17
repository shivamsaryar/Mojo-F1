# importing the csv & bigquery libraries
import csv
import os
from google.cloud import bigquery

def getFieldList(file_name):
	
    # opening the csv file passed to the function with the variable name as csv_file
    with open(file_name) as csv_file:

        # creating an object of csv reader with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter = ',')

        # list to store the names of columns
        list_of_column_names = []

        # loop to iterate through the rows of csv
        for row in csv_reader:

            # adding the first row
            list_of_column_names.append(row)

            # breaking the loop after the first iteration itself
            break

    # printing the result
    #print("List of column names : ", list_of_column_names[0])

    #return list of fields as an array
    return list_of_column_names[0]

def create_schema (file_name):
    
    field_list = getFieldList(file_name)
    type_list = []

    for row in field_list:
        type_list.append("STRING")

    #type_list_original = ["STRING", "INTEGER", "STRING"]
    
    schema_list = []

    for fields, types in zip(field_list, type_list):
        #print(fields, " : ", types)
        schema = bigquery.SchemaField(fields, types)
        schema_list.append(schema)
    
    #print("My Schema ",schema_list)
    return schema_list