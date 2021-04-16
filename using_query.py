import babypandas as bpd
import numpy as np

def query_3_9():
    # use Query to create tables needed
    cereals = bpd.read_csv('cereal.csv')
    t1 = cereals[(cereals.get('sugars') >= 13) & (cereals.get('fiber') <= 2)]
    print(t1)

def groupby_3_10():
    cereals = bpd.read_csv('cereal.csv')
    abbr = bpd.DataFrame().assign(
        abbr=['A', 'G', 'K', 'N', 'P', 'Q', 'R'],
        names=['American Home Food Products', 'General Mills', 'Kelloggs', 'Nabisco', 'Post', 'Quaker Oats', 'Ralston Purina']
    ).set_index('names')
    lowest = cereals.groupby('mfr').median().get('calories').sort_values(ascending=True).index[0]
    m1 = abbr.get('abbr').loc[cereals.groupby('mfr').median().get('calories').sort_values(ascending=True).index[0]]
    print(m1)

def groupby_3_10_ver2():
    abbr = bpd.DataFrame().assign(
        abbr=['A', 'G', 'K', 'N', 'P', 'Q', 'R'],
        names=['American Home Food Products', 'General Mills', 'Kelloggs', 'Nabisco', 'Post', 'Quaker Oats', 'Ralston Purina']
    ).set_index('abbr')
    lowest = cereals.groupby('mfr').median().get('calories').sort_values(ascending=True).index[0]
    little_calories = abbr.get('names').loc[cereals.groupby('mfr').median().get('calories').sort_values(ascending=True).index[0]]
    little_calories

# query_3_9()
# print('\n\n')
groupby_3_10()

