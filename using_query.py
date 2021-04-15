import babypandas as bpd
import numpy as np

def query_01():
    # use Query to create tables needed
    cereals = bpd.read_csv('cereal.csv').set_index('name')
    t1 = cereals[(cereals.get('sugars') >= 13) & (cereals.get('fiber') <= 2)]
    print(t1)

query_01()

