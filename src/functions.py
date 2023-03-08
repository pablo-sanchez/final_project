import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re



def pattern_lister(row, pattern):
    list_fulfill_pattern=[]
    list_not_fulfill=[]
    empty=[]
    for x in row:
        match=re.findall(pattern, x)
        if match != empty and match not in list_fulfill_pattern:
            list_fulfill_pattern.append(match)
        elif match == empty:
            list_not_fulfill.append(x)
    return list_fulfill_pattern, list_not_fulfill

def num_cat_splitter(df):
    df1 = df.copy()
    numerical_df = df1.select_dtypes(np.number)
    categorical_df = df1.select_dtypes(object)
    return numerical_df, categorical_df

def size_cleaner(x):
    small_company = ['1 to 50 Employees']
    medium_company = ['51 to 200 Employees','201 to 500 Employees']
    big_company = ['501 to 1000 Employees', '1001 to 5000 Employees', '5001 to 10000 Employees']
    huge_company = ['10000+ Employees']
    unknown_size = ['Unknown'] 
    #we could assume that these companies are more likely to belong to small or medium companies

    if x in small_company:
        return 'Small company'
    elif x in medium_company:
        return 'Medium-sized company'
    elif x in big_company:
        return 'Large company'
    elif x in huge_company:
        return 'Huge company'
    else:
        return 'Unknown size'
    

def type_cleaner(x):
    other = ['Hospital', 'Subsidiary or Business Segment', 'Unknown', 'Government', 'Private Practice / Firm', 'College / University',
             'Nonprofit Organization', 'Franchise', 'Contract', 'Self-employed']

    if x in other:
        return 'Other institutions'
    else:
        return x    
 

def sector_cleaner(x):
    technology = ['Information Technology', 'Telecommunications']
    business_services = ['Management & Consulting', 'Human Resources & Staffing']
    financial_services_and_housing =['Financial Services', 'Real Estate', 'Insurance']
    media_and_entertaiment = ['Media & Communication', 'Arts, Entertainment & Recreation']
    industry = ['Manufacturing', 'Energy, Mining & Utilities', 'Construction, Repair & Maintenance Services']
    health = ['Healthcare', 'Pharmaceutical & Biotechnology']
    other = ['Education', 'Retail & Wholesale','Government & Public Administration', 'Transportation & Logistics',
             'Aerospace & Defense','Restaurants & Food Service', 'Nonprofit & NGO','Hotels & Travel Accommodation','Agriculture', 'Legal'] 

    if x in technology:
        return 'IT and Telecommunications'
    elif x in business_services:
        return 'Business services'
    elif x in financial_services_and_housing:
        return 'Financial and housing services'
    elif x in media_and_entertaiment:
        return 'Media and Entertaiment'
    elif x in industry:
        return 'Industry'
    elif x in health:
        return 'Healthcare'
    elif x in other:
        return 'Other sectors'
    else:
        return x    
    
    
def revenue_cleaner(x):
    less_than_5 = ['Less than $1 million (USD)', '$1 to $5 million (USD)']
    two_figure_millionare = ['$5 to $25 million (USD)','$25 to $100 million (USD)']
    three_figure_millionare = ['$100 to $500 million (USD)', '$500 million to $1 billion (USD)']
    billionare = ['$1 to $5 billion (USD)', '$5 to $10 billion (USD)']
    two_figure_billionare = ['$10+ billion (USD)']

    if x in less_than_5:
        return 'Less than $5 million (USD)'
    elif x in two_figure_millionare:
        return '$5 to $100 million (USD)'
    elif x in three_figure_millionare:
        return '$100 million to $1 billion (USD)'
    elif x in billionare:
        return '$1 to $10 billion (USD)'
    else:
        return x    
    
    
def state_cleaner(x):
    northeastern = ['CT','ME','MA','NH','NJ','NY','PA','RI','VT']
    midwestern = ['IL','IN','IA','KS','MI','MN','MO','NE','ND','OH','SD','WI']
    southern = ['AL','AR','DE','FL','GA','KY','LA','MD','MS','NC','OK','SC','TN','TX','VA','WV','DC','AF','PR']
    western = ['AK','AZ','CA','CO','HI','ID','MT','NV','NM','OR','UT','WA','WY']

    if x in northeastern:
        return 'Northeastern'
    elif x in midwestern:
        return 'Midwestern'
    elif x in southern:
        return 'Southern'
    elif x in western:
        return 'Western'
    else:
        return x
    
    
def countplot_generator(df):
    df2 = df.copy()
    plt_size = len(df2.columns)
    fig, ax = plt.subplots(plt_size, figsize=(12,30))
    n=0

    for col in df2.columns:
        if (len(df2[col].value_counts().index)) >= 6:
            sns.countplot(data = df2, y = col, order = df2[col].value_counts().index, ax = ax[n])
        else:
            sns.countplot(data = df2, x = col, order = df2[col].value_counts().index, ax = ax[n])
        n +=1
    plt.show()
    
