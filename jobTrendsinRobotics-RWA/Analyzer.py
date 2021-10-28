import math
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

class Analyzer:
    config = ""

    def __init__(self, config):
        self.config = config

    #Counts the total number of job posts in the file per year
    def posts_per_year(self, filename):
        print("Counts the total number of job posts in the archive per year")
        f = pd.read_csv(filename)
        f = (f['year'].value_counts()).sort_index()
        return f

    #Counts the total number of job posts in the archive per year by field
    def posts_per_year_per_field(self, filename, word):
        print("Counts the total number of job posts in the archive per year by field")
        f = pd.read_csv(filename)
        list = (f['year'].value_counts()).sort_index()
        list.values[:] = 0
        temp = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.fields[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1:
                    temp = list.loc[index] + 1
                    list.at[index] = temp
                    break
        list = list.rename(word)
        return list

    #Calculates the percentage of job posts in the archive by field for each year
    def percentage_of_posts_per_year_per_field(self, filename, word):
        print("Calculates the percentage of job posts in the archive by field for each year")
        word_occurences = self.posts_per_year_per_field(filename, word)
        paper_amounts = self.posts_per_year(filename)
        word_occurences_hundred = word_occurences.multiply(100)
        result = word_occurences_hundred.divide(paper_amounts)
        return result, word_occurences
    
    #Counts the total number of job posts in the archive per year by career
    def posts_per_year_per_career(self, filename, word):
        print("Counts the total number of job posts in the archive per year by career")
        f = pd.read_csv(filename)
        list = (f['year'].value_counts()).sort_index()
        list.values[:] = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.careers[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1:
                    temp = list.loc[index] + 1
                    list.at[index] = temp
                    break
        list = list.rename(word)
        return list

    #Calculates the percentage of job posts in the archive by career for each year
    def percentage_of_posts_per_year_per_career(self, filename, word):
        print("Calculates the percentage of job posts in the archive by career for each year")
        word_occurences = self.posts_per_year_per_career(filename, word)
        paper_amounts = self.posts_per_year(filename)
        word_occurences_hundred = word_occurences.multiply(100)
        result = word_occurences_hundred.divide(paper_amounts)
        return result, word_occurences

    #Counts the total number of job posts in the archive per year by career
    def posts_per_year_per_country(self, filename, word):
        print("Counts the total number of job posts in the archive per year by country")
        f = pd.read_csv(filename)
        list = (f['year'].value_counts()).sort_index()
        list.values[:] = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.countries[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(keyword) != 'nan' and (str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1):
                    temp = list.loc[index] + 1
                    list.at[index] = temp
                    break
        list = list.rename(word)
        return list

    #Counts the total number of job posts in the archive per year by country
    def posts_by_country(self, filename):
        print("Counts the total number of job posts in the archive per year by country")
        countries_counted = [['', 0]]
        for category in self.config.countries.columns:
            df = pd.DataFrame()
            f = pd.read_csv(filename)
            counted = 0
            for index, row in f.iterrows():
                s = pd.Series(row)
                identifiers = [x for x in self.config.countries[category] if str(x) != 'nan']
                for keyword in identifiers:
                    if str(keyword) != 'nan' and (str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1):
                        if counted == 0:
                            df = pd.DataFrame(columns=['year', 'subject', 'content'])
                        df = df.append(s,ignore_index=True)
                        counted = counted + 1
                        break
                if index == f.index[-1] and counted > 0:
                    df.to_csv(r"Graphics\Countries\csv_countries\country_" + str(category) + ".csv")
            if counted > 0:
                countries_counted.append([category, counted])
        countries_counted = sorted(countries_counted, key=lambda x: x[1], reverse=True)
        return countries_counted
    
    #Counts the total number of job posts in the archive per year by career for a given country
    def fields_by_country(self, filename, word):
        print("Counts the total number of job posts in the archive per year by career for a given country")
        f = pd.read_csv(filename)
        list = (f['year'].value_counts()).sort_index()
        list.values[:] = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.fields[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1:
                    temp = list.loc[index] + 1
                    list.at[index] = temp
                    break
        list = list.rename(word)
        return list

    #Counts the total number of job posts in the archive per year by field for a given country
    def careers_by_country(self, filename, word):
        print("Counts the total number of job posts in the archive per year by field for a given country")
        f = pd.read_csv(filename)
        df = pd.read_csv(r"robotics-worldwide_jobs_purified_lower.csv")
        list = (df['year'].value_counts()).sort_index()
        list.values[:] = 0
        temp = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.careers[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1:
                    temp = list.loc[index] + 1
                    list.at[index] = temp
                    break
                if index == f.index[-1] and temp == 0:
                    list.at[index] = 0
        list = list.rename(word)
        return list
    
    def total_fields_by_country(self, filename, word):
        #print("counts the total number of job posts in the archive per year by career for a given country")
        f = pd.read_csv(filename)
        temp = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.fields[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1:
                    temp = temp + 1
                    break
        return temp

    def total_careers_by_country(self, filename, word):
        #print("Counts the total number of job posts in the archive per year by career for a given country")
        f = pd.read_csv(filename)
        temp = 0
        f = f.set_index("year")
        for index, row in f.iterrows():
            s = pd.Series(row)
            identifiers = [x for x in self.config.careers[word] if str(x) != 'nan']
            for keyword in identifiers:
                if str(s['content']).find(str(keyword)) != -1 or str(s['subject']).find(str(keyword)) != -1:
                    temp = temp + 1
                    break
        return temp