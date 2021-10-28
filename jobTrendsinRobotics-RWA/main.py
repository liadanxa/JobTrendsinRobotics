import pandas as pd
import matplotlib.pyplot as plt
import glob
import os.path
from itertools import cycle, islice
from Configuration import Configuration
from Purifier import Purifier
from Analyzer import Analyzer

archive = r"robotics-worldwide_jobs_purified_lower.csv"

c = Configuration("robotics-worldwide_jobs")
p = Purifier(c)
a = Analyzer(c)

#Generate posts per year
print("Generate posts per year")
df = pd.DataFrame()
s = a.posts_per_year(archive)
df = s
plt.subplots(figsize=(15, 9), dpi=300)
title = "No. of Job Posts per Year (Aug 2005 - Apr 2021)"
df.plot(kind="bar", color="b")
plt.xlabel('Year', fontsize=17)
plt.ylabel('No. of Job Posts', fontsize=17)
plt.title(title, fontsize=20)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.savefig(r"Graphics\job_posts_per_year.png", bbox_inches='tight')
plt.clf()

#Generate line graphs for the no. of and percentage of jobs posted by field per year and bar graphs for the number of jobs posted for each field per year
print("Generate line graphs for the no. of and percentage of jobs posted by field per year and bar graphs for the number of jobs posted for each field per year")
arrayp = []
arrayn = []
legend = []
fields_total = []
for category in c.fields.columns:
    dfs = pd.DataFrame()
    dfp = pd.DataFrame()
    dfn = pd.DataFrame()
    if not isinstance(category, str):
        break
    s = a.percentage_of_posts_per_year_per_field(archive, category)
    fields_total.append([str(category).title(), s[1].sum(axis=0, skipna=True)])
    print(fields_total)
    s[0].name = category
    s[1].name = category
    arrayp.append(s[0])
    arrayn.append(s[1])
    legend.append(category.title())
    dfp = pd.concat(arrayp, axis=1)
    dfn = pd.concat(arrayn, axis=1)
    dfs = s[1]
    print(s[1])
    plt.subplots(figsize=(15, 9), dpi=300)
    dfs.plot(kind='bar')
    plt.xlabel('Year', fontsize=17)
    plt.ylabel('No. of Job Posts', fontsize=17)
    plt.title("No. of Job Posts per Year in the Field of " + category.title() + " (Aug 2005 - Apr 2021)", fontsize=20)
    plt.savefig(r"Graphics\Fields\job_posts_per_year_in_" + category + ".png", bbox_inches='tight')
    plt.clf()
df = pd.DataFrame(fields_total, columns=['field', 'no. of posts'])
df.to_excel(r"field_totals.xlsx")
my_colors = list(islice(cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'palevioletred']), None, len(dfp)))
plt.subplots(figsize=(15, 9), dpi=300)
dfp.plot(kind='line', color=my_colors)
plt.xlabel('Year')
plt.ylabel('% of Job Posts')
plt.legend(legend, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("% of Job Posts per Year by Field (Aug 2005 - Apr 2021)")
plt.savefig(r"Graphics\Fields\percentage_of_job_posts_per_year_by_field.png", bbox_inches='tight')
plt.clf()
plt.subplots(figsize=(15, 9), dpi=300)
dfn.plot(kind='line', color=my_colors)
plt.xlabel('Year')
plt.ylabel('No. of Job Posts')
plt.legend(legend, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("No. of Job Posts per Year by Field (Aug 2005 - Apr 2021)")
plt.savefig(r"Graphics\Fields\job_posts_per_year_by_field.png", bbox_inches='tight')
plt.clf()

#Generate line graphs for the no. of and percentage of jobs posted by career per year and bar graphs for the number of jobs posted for each career per year
print("Generate line graphs for the no. of and percentage of jobs posted by career per year and bar graphs for the number of jobs posted for each career per year")
arrayp = []
arrayn = []
legend = []
careers_total = []
for category in c.careers.columns:
    dfp = pd.DataFrame()
    dfn = pd.DataFrame()
    df = pd.DataFrame()
    if not isinstance(category, str):
        break
    s = a.percentage_of_posts_per_year_per_career(archive, category)
    careers_total.append([str(category).title(), s[1].sum(axis=0, skipna=True)])
    print(careers_total)
    s[0].name = category
    s[1].name = category
    arrayp.append(s[0])
    arrayn.append(s[1])
    dfp = pd.concat(arrayp, axis=1)
    dfn = pd.concat(arrayn, axis=1)
    legend.append(category.title())
    df = s[1]
    plt.subplots(figsize=(15, 9), dpi=300)
    df.plot(kind='bar')
    plt.xlabel('Year', fontsize=17)
    plt.ylabel('No. of Job Posts', fontsize=17)
    plt.title("No. of Job Posts per Year in the " + category.title() + " Sector (Aug 2005 - Apr 2021)", fontsize=20)
    plt.savefig(r"Graphics\Careers\job_posts_per_year_in_" + category + ".png", bbox_inches='tight')
    plt.clf()
df = pd.DataFrame(careers_total, columns=['career', 'no. of posts'])
df.to_excel(r"careers_totals.xlsx")
my_colors = list(islice(cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'palevioletred']), None, len(dfp)))
plt.subplots(figsize=(15, 9), dpi=300)
dfp.plot(kind='line', color=my_colors)
plt.xlabel('Year')
plt.ylabel('% of Job Posts')
plt.legend(legend, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("% of Job Posts per Year by Job Type (Aug 2005 - Apr 2021)")
plt.savefig(r"Graphics\Careers\percentage_of_job_posts_per_year_by_career.png", bbox_inches='tight')
plt.clf()
plt.subplots(figsize=(15, 9), dpi=300)
dfn.plot(kind='line', color=my_colors)
plt.xlabel('Year')
plt.ylabel('No. of Job Posts')
plt.legend(legend, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("No. of Job Posts per Year by Job Type (Aug 2005 - Apr 2021)")
plt.savefig(r"Graphics\Careers\job_posts_per_year_by_career.png", bbox_inches='tight')
plt.clf()

#Generate line graphs for the no. of job posts from the top 10 countries with the highest no. of job posts for each field and job type then generates the number of jobposts for each country by continent
print("Generate line graphs for the no. of job posts from the top 10 countries with the highest no. of job posts for each field and job type")
a = a.posts_by_country(archive)
g=[]
for file in glob.glob(r"Graphics\Countries\csv_countries\*.csv"): 
    df = pd.DataFrame()
    df = pd.read_csv(file)
    g.append([str(file)[41:-4], len(df)])
g = sorted(g, key=lambda x: x[1], reverse=True)
s = []
for item in g:
    s.append(item[0])
print(s)
for i in range(10):
    df_total = pd.DataFrame()
    total = a.posts_per_year(r"Graphics\Countries\csv_countries\country_" + str(s[i]) + ".csv")
    total.name = s[i]
    df_total = total
    plt.subplots(figsize=(15, 9), dpi=300)
    df_total.plot(kind="bar", fontsize=13.5)
    plt.xlabel('Year', fontsize=15)
    plt.ylabel('No. of Job Posts', fontsize=15)
    plt.title("No. of Job Posts per Year in " + str(s[i]).title() + " (Aug 2005 - Apr 2021)", fontsize=17.5)
    plt.savefig(r"Graphics\Countries\top 10\total_job_posts_per_year_in_" + str(s[i]) + ".png", bbox_inches='tight')
    plt.clf()
    array_career = []
    legend=[]
    print(str(s[i]))
    for career in c.careers.columns:
        total = a.total_careers_by_country(r"Graphics\Countries\csv_countries\country_" + str(s[i]) + ".csv", career)
        array_career.append([career, total])
        df_career = pd.DataFrame()
        if not isinstance(career, str):
            break
        t = a.careers_by_country(r"Graphics\Countries\csv_countries\country_" + str(s[i]) + ".csv", career)
        t.name = career
        legend.append(career.title())
        array_career.append(t)
        df_career = pd.concat(array_career, axis=1)
    my_colors = list(islice(cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'palevioletred']), None, len(df_career)))
    plt.subplots(figsize=(15, 9), dpi=300)
    df_career.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Job Type in " + str(s[i]).title() + " (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\top 10\job_posts_per_year_by_career_in_" + str(s[i]) + ".png", bbox_inches='tight')
    plt.clf()
    array_field = []
    legend=[]
    for field in c.fields.columns:
        total = a.total_fields_by_country(r"Graphics\Countries\csv_countries\country_" + str(s[i]) + ".csv", field)
        array_field.append([field, total])
        df_field = pd.DataFrame()
        if not isinstance(field, str):
            break
        t = a.fields_by_country(r"Graphics\Countries\csv_countries\country_" + str(s[i]) + ".csv", field)
        t.name = field
        legend.append(field.title())
        array_field.append(t)
        df_field = pd.concat(array_field, axis=1)
    my_colors = list(islice(cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'palevioletred']), None, len(df_field)))
    plt.subplots(figsize=(15, 9), dpi=300)
    df_field.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Field in " + str(s[i]).title() + " (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\top 10\job_posts_per_year_by_field_in_" + str(s[i]) + ".png", bbox_inches='tight')
    plt.clf()
array_africa = []
array_antarctica = []
array_asia = []
array_australia_oceania = []
array_europe = []
array_north_america = []
array_south_america = []
legend_africa = []
legend_antarctica = []
legend_asia = []
legend_australia_oceania = []
legend_europe = []
legend_north_america = []
legend_south_america = []
df_africa = pd.DataFrame()
df_antarctica = pd.DataFrame()
df_asia = pd.DataFrame()
df_australia_oceania = pd.DataFrame()
df_europe = pd.DataFrame()
df_north_america = pd.DataFrame()
df_south_america = pd.DataFrame()
for file in glob.glob(r"Graphics\Countries\csv_countries\*.csv"):
    s = a.posts_per_year(file)
    s.name = str(file)[130:-4]
    for continent in c.continents.columns:
        for country in c.continents[continent]:
            if str(file)[130:-4] == str(country):
                if str(continent) == 'africa':
                    legend_africa.append(str(file)[130:-4].title())
                    array_africa.append(s)
                    df_africa = pd.concat(array_africa, axis=1)
                if str(continent) == 'antarctica':
                    legend_antarctica.append(str(file)[130:-4].title())
                    array_antarctica.append(s)
                    df_antarctica = pd.concat(array_antarctica, axis=1)
                if str(continent) == 'asia':
                    legend_asia.append(str(file)[130:-4].title())
                    array_asia.append(s)
                    df_asia = pd.concat(array_asia, axis=1)
                if str(continent) == 'australia/oceania':
                    legend_australia_oceania.append(str(file)[130:-4].title())
                    array_australia_oceania.append(s)
                    df_australia_oceania = pd.concat(array_australia_oceania, axis=1)
                if str(continent) == 'europe':
                    legend_europe.append(str(file)[130:-4].title())
                    array_europe.append(s)
                    df_europe = pd.concat(array_europe, axis=1)
                if str(continent) == 'north america':
                    legend_north_america.append(str(file)[130:-4].title())
                    array_north_america.append(s)
                    df_north_america = pd.concat(array_north_america, axis=1)
                if str(continent) == 'south america':
                    legend_south_america.append(str(file)[130:-4].title())
                    array_south_america.append(s)
                    df_south_america = pd.concat(array_south_america, axis=1)
my_colors = list(islice(cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'palevioletred', 'darkcyan', 'mediumpurple', 'black', 'chartreuse', 'dodgerblue', 'lightsalmon', 'mediumseagreen', 'darkblue', 'darkgreen', 'gold', 'darkgoldenrod', 'indigo', 'lightskyblue', 'darkseagreen', 'orangered', 'orchid', 'plum', 'teal', 'yellow', 'yellowgreen']), None, 32))
if not df_africa.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_africa.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_africa, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in Africa (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_africa.png", bbox_inches='tight')
    plt.close()
if not df_antarctica.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_antarctica.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_antarctica, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in Antarctica (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_antarctica.png", bbox_inches='tight')
    plt.close()
if not df_asia.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_asia.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_asia, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in Asia (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_asia.png", bbox_inches='tight')
    plt.close()
if not df_australia_oceania.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_australia_oceania.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_australia_oceania, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in Australia/Oceania (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_australia_oceania.png", bbox_inches='tight')
    plt.close()
if not df_europe.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_europe.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_europe, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in Europe (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_europe.png", bbox_inches='tight')
    plt.close()
if not df_north_america.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_north_america.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_north_america, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in North America (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_north_america.png", bbox_inches='tight')
    plt.close()
if not df_south_america.empty:
    plt.subplots(figsize=(15, 9), dpi=300)
    df_south_america.plot(kind='line', color=my_colors)
    plt.xlabel('Year')
    plt.ylabel('No. of Job Posts')
    plt.legend(legend_south_america, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("No. of Job Posts per Year by Countries in South America (Aug 2005 - Apr 2021)")
    plt.savefig(r"Graphics\Countries\Continents\job_posts_per_year_south_america.png", bbox_inches='tight')
    plt.close()

#Generate csv files of posts separated by year to calculate yearly totals of each field and career type
df = pd.read_csv(r"robotics-worldwide_jobs_purified_lower.csv")
years = df['year'].unique()
for item in years:
    df = pd.read_csv(r"robotics-worldwide_jobs_purified_lower.csv")
    df = df[df['year'] == item]
    df.to_csv(r"posts_in_" + str(item) + ".csv")
    array_career = []
    for career in c.careers.columns:
        total = a.total_careers_by_country(r"posts_in_" + str(item) + ".csv", career)
        array_career.append([career, total])
    print(item)
    array_field = []
    for field in c.fields.columns:
        total = a.total_fields_by_country(r"posts_in_" + str(item) + ".csv", field)
        array_field.append([field, total])
    print(array_career)
    print(array_field)

