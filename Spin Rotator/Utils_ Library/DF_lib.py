import pandas as pd
from lat_util import *

def readf(file):
    arr = pd.read_fwf(file).to_numpy()
    return arr
    
def DF(file,t):
    data = search_engine_(file,t)
    display(data)
    