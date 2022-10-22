import pandas as pd
from lat_util import *

def readf(file):
    
    df = pd.read_fwf(file)
    arr = df.to_numpy()
    return arr

def df(idx, name, key, s, l, x, y, z, theta, phi, psi, sx, sy, sz):
    pb=pd.DataFrame({'index':idx, 'name':name, 'key':key, 's (m)':s,\
                     'l (m)':l, 'floor.x':x,'floor.y':y,'floor.z':z,\
                     'floor.theta':theta,'floor.phi':phi,'floor.psi':psi,\
                     'spin.x':sx,'spin.y':sy,'spin.z':sz})
    #pd.set_option('display.max_rows', None)
    display(pb)
    
def DF(file,t):
    arr = readf(file)
    idx, name, key, s, l, x, y, z, theta, phi, psi, sx, sy, sz = search_engine(arr,t)
    df(idx, name, key, s, l, x, y, z, theta, phi, psi, sx, sy, sz)