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
    )
    lowest = cereals.groupby('mfr').median().get('calories').sort_values(ascending=True).index[0]
    m1 = abbr[abbr.get('names') == cereals.groupby('mfr').median().get('calories').sort_values(ascending=True).index[0]]
    print(m1)

query_3_9()
print('\n\n')
groupby_3_10()

