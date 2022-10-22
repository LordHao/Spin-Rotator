from numpy import *
import sys
import pandas as pd
from float_test import isfloat

def ks(arr,t):
    
    if len(t) == 0:
        sys.exit('Please input a keyword')
    else:
        pass
    
    num = len(arr[:,0])
    ta = []
    for i in range(len(t)):
        ta.append(t[i])
    ta = array(ta)
    ix = arr[:,0]
    nme = arr[:,1]
    ky = arr[:,2]
    sv = arr[:,3]
    
    if len(where(ta == ':')[0])==1:
        if t == ':':
            b = arange(0,num,1)
            
        else:
            c = where(ta == ':')[0][0]
            
            if len(t[0:c])>0:
                A = int(t[0:c])
            else:
                lidx = 0
            
            if len(t[c+1:])>0:
                B = int(t[c+1:])
            else:
                ridx = num 
                   
            if c ==0:
                if len(where(ix == B)[0])==1:
                    ridx = where(ix == B)[0][0]+1
                else:
                    sys.exit('list out of range')
                
            elif c == len(t)-1:
                if len(where(ix == A)[0])==1: 
                    lidx = where(ix == A)[0][0]
                else:
                    sys.exit('list out of range')
                
            else:
                if len(where(arr[:,0] == A)[0])==1 and len(where(arr[:,0] == B)[0])==1:
                    if A<B:
                        lidx = where(ix == A)[0][0]
                        ridx = where(ix == B)[0][0]+1
                    else:
                        sys.exit('the second index must be greater than the first one')
                else:
                    sys.exit('list out of range')
                    
                    
            b = arange(lidx,ridx,1)
                
    else:
        if t.isnumeric() == True:
            if len(where(arr[:,0] == int(t))[0])>0: 
                b  = where(arr[:,0] == int(t))[0]
            else:
                sys.exit('can not find the target element')
                    
        else:
            if len(t)>=2:
                
                if len(where(ta == '*')[0])==1:
                    tse = where(ta == '*')[0][0]
                    keyword = []
                    for i in range(len(nme)):
                            keyword.append(nme[i][0:tse])
                    keyword = array(keyword)
                    
                    if len(where(keyword == t[:-1])[0])>0:
                        b  = where(keyword == t[:-1])[0]
                        
                    else:
                        sys.exit('can not find the target element')
   
                elif 's ' in t and len(where(ta == ' ')[0])==2:
                    n1s = t.find('s ')+2
                    n1e = where(ta == ' ')[0][1]
                    n2s = where(ta == ' ')[0][1]+1
                    n1 = t[n1s:n1e] 
                    n2 = t[n2s:]
                    
                    if len(n1)>0 and len(n2)>0 and isfloat(n1) == True and isfloat(n2) == True:
                        
                        n1 = float(n1)
                        n2 = float(n2) 
                        
                        if n1>=0 and n2>0:
                            if n2 > n1:
                                if n2 <= max(sv)+5:
                                    if len(where(sv >= n1)[0])>0:
                                        A = where(sv >= n1)[0][0]
                                        if len(where(sv <= n2)[0])>0:
                                            B = where(sv <= n2)[0][-1]
                                            if A <= B: 
                                                b = arange(A,B+1,1)
                                            else:
                                                sys.exit('can not find any element in the given s range')
                                        else:
                                            sys.exit('upper boundry too small')
                                    else:
                                        sys.exit('lower boundry too big')
                                else:
                                    sys.exit('upper boundry too big (might exceed the circumference of the ring)')
                                    
                            else:
                                sys.exit('the second number must be greater than the first one')
                            
                        else:
                            sys.exit('s can not be a negative number')
                                
                    else:
                        sys.exit('requires two numbers to scale s')
                    
                    
                else:
                    if len(where(nme == t )[0])>0: 
                        b  = where(nme == t )[0]
                        
                    elif len(where(ky == t)[0])>0: 
                        b  = where(ky == t)[0]
            
                    else:
                        sys.exit('can not find the target element')
            else:
                sys.exit('Keyword too short')
                
    return b

def search_engine_(file,t):
    Data =pd.read_fwf(file)
    arr = Data.values
    b = ks(arr,t)
    data = pd.DataFrame(arr[b,:],columns =Data.columns.tolist())
    return data

def search_engine(arr,t):
    b = ks(arr,t)
    arr = arr[b,:]
    idx = arr[:,0]
    name = arr[:,1]
    key = arr[:,2]
    s  = arr[:,3]
    l = arr[:,4]
    x = arr[:,5]
    y = arr[:,6]
    z = arr[:,7]
    theta = arr[:,8]
    phi = arr[:,9]
    psi = arr[:,10]
    sx = arr[:,11]
    sy = arr[:,12]
    sz = arr[:,13]
    
    return idx, name, key, s, l, x, y, z, theta, phi, psi, sx, sy, sz

def score(inv, num, x, y, z, theta, phi, psi, sx, sy, sz, X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz):
        
    if len(inv)>0:
        gap = int(len(inv)/num)
        if len(inv)>=2*num:
            pass
        else:
            gap += 1
        
        X = append(X,x[inv][::gap])
        Y = append(Y,y[inv][::gap])
        Z = append(Z,z[inv][::gap])
        Theta = append(Theta,theta[inv][::gap])
        Phi = append(Phi,phi[inv][::gap])
        Psi = append(Psi,psi[inv][::gap])
        Sx = append(Sx,sx[inv][::gap])
        Sy = append(Sy,sy[inv][::gap])
        Sz = append(Sz,sz[inv][::gap])
    
    else:
        pass
        
    return X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz


def selector(idx, x, y, z, theta, phi, psi, sx, sy, sz, m, r, n):
    
    X = array([])
    Y = array([])
    Z = array([])
    Theta = array([])
    Phi = array([])
    Psi = array([])
    Sx = array([])
    Sy = array([])
    Sz = array([])
    
    
    a = where(logical_and(idx>=1452, idx<=1654))[0]
    
    b = where(logical_and(idx>=1655, idx<1847))[0]
    
    c = where(logical_and(idx>=1847, idx<=1865))[0]
    
    d = where(logical_and(idx>=1866, idx<2058))[0]
    
    e = where(logical_and(idx>=2058, idx<=5320))[0]
    
    f = where(logical_and(idx>=5321, idx<5513))[0]
    
    g = where(logical_and(idx>=5513, idx<=5517))[0]
    
    h = where(logical_and(idx>=5518, idx<5710))[0]
    
    i = where(logical_and(idx>=5710, idx<=5936))[0]
    
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(a, n, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(b, r, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(c, 1, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(d, r, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(e, m, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(f, r, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(g, 1, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(h, r, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz = score(i, n, \
                                                    x, y, z,theta, phi, psi, sx, sy, sz,\
                                                    X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz)
    
    return X, Y, Z, Theta, Phi, Psi, Sx, Sy, Sz

def ct(theta,sz,sx,sy): #coordinate transformation: from co-moving to lab frame
    Sz = -cos(theta)*sz+sin(theta)*sx
    Sx = -sin(theta)*sz-cos(theta)*sx
    Sy = sy
    return Sz, Sx, Sy

def dc(x, y, z, theta, phi, psi, sx, sy, sz, lsc):
    
    x = x.astype(float)/lsc
    y = y.astype(float)
    z = z.astype(float)/lsc
    theta = theta.astype(float)
    phi = theta.astype(float)
    psi = theta.astype(float)
    sx = sx.astype(float)
    sy = sy.astype(float)
    sz = sz.astype(float)
    
    return  x, y, z, theta, phi, psi, sx, sy, sz


