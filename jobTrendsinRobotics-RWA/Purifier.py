import numpy as np
import pandas as pd
import csv

class Purifier:

    def __init__(self, config):
        self.convert()
        self.drop_columns(config.relevant_columns)
        self.drop_duplicate_rows()
        self.dataset_to_lowercase()
    
    #Converts the archive excel sheet to a csv file
    def convert(self):
        print("Converts the archive excel sheet to a csv file")
        df = pd.read_excel(r"robotics-worldwide_jobs.xlsx")
        df.to_csv(r"robotics-worldwide_jobs.csv", sep=";")
    
    #Removes columns from the csv file that aren't required for the program
    def drop_columns(self, column_titles):
        print("Removes columns from the csv file that aren't required for the program")
        f = pd.read_csv(r"robotics-worldwide_jobs.csv", sep=";", low_memory=False)
        new_f = pd.DataFrame(f[column_titles])
        new_f.to_csv(r"robotics-worldwide_jobs_purified.csv", index=False)

    #Removes repeated rows to reduce redundant data
    def drop_duplicate_rows(self):
        print("Removes repeated rows to reduce redundant data")
        f = pd.read_csv(r"robotics-worldwide_jobs_purified.csv", low_memory=False)
        f.drop_duplicates(subset=['year', 'content'], keep='last')

    #Converts file to lowercase
    def dataset_to_lowercase(self):
        print("Converts file to lowercase")
        f = pd.read_csv(r"robotics-worldwide_jobs_purified.csv", low_memory=False)
        for label, content in f.items():
            f[label] = f[label].astype('str')
            f[label] = f[label].str.lower()
        f.to_csv(r"robotics-worldwide_jobs_purified_lower.csv", index=False)


