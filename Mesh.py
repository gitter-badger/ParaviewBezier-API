# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:58 2020

@author: User
"""
import numpy as np
def Connectvity(ndm,conn,wghts,tnel,nel,mel,lel,n,m,l,p,q,r):
    
    
    nen = (p+1)*(q+1)*(r+1)
    IX=[[0 for i in range(nen)] for j in range(tnel)]
    w =[[0 for i in range(nen)] for j in range(tnel)]
    
    """ 
    IX[0][]=conn[0:m*l][0:p+1]
    IX[1][]=conn[0:m*l][p:2*p+1]
    IX[2][]=conn[0:m*l][2*p:3*p+1]
    .
    .
    .
    IX[nel-1][]=conn[0:m*l][(nel-1)*p:nel*p] 
    """
    Elem=0
    e=2
    f=1
    g=2
    'There could be some relation between n-p and nel'
    # temp1=open("temp1.k", "w")
    
    if ndm==1:
    
        e=1
        for k in range(nel):
            count=0                
            for kloc in range(0,p+1):
                
                npr=(k*e)+kloc #local function location
                
                IX[Elem][count]=conn[npr]
                w[Elem][count]=wghts[npr]
                #temp1.write(' %8d'%(IX[Elem][count]))
                count+=1
            #temp1.write('\n')
            Elem=Elem+1
            
    if ndm==2:
        
        f=1
        e=1
        for k in range(nel):
            for i in range(mel):
                count=0                
                for iloc in range(0,q+1):
                    for kloc in range(0,p+1):
                        
                        npr=(k*e)+kloc
                        nps=i*f+iloc

                        IX[Elem][count]=conn[nps][npr]
                        w[Elem][count]=wghts[nps][npr]
                        
                        #temp1.write(' %8d'%(IX[Elem][count]))
                        count+=1
                #temp1.write('\n')
                Elem=Elem+1
        
    if ndm==3:
        
        for k in range(nel):
            for i in range(mel):
                for j in range(lel):
                    count=0
                
                    for jloc in range(0,((r+1)*(q+1))):
                        for kloc in range(0,p+1):
                    
                            npr=(k*e)+kloc
                            nps=i*f+j*(q+1)+jloc
                    
                            IX[Elem][count]=conn[nps][npr]
                            w[Elem][count]=wghts[nps][npr]
                            #temp1.write(' %8d'%(IX[Elem][count]))
                            count+=1
                    #temp1.write('\n')
                    Elem=Elem+1
                    
        # temp1.write('\n')
    #print(nel,lel,mel,tnel)
    
    return IX,w

def Bezier_IX(nenloc,tnel,ixbezloc,temp_ixbez,temp_order,p,q,r):
    
    tnelloc=len(ixbezloc)
    temp,c=(0,0)
    for x in temp_ixbez:
        temp=len(x)
        if temp>c:
            c=temp
    row=tnel-tnelloc
    if nenloc >= c:
        nen=nenloc
    else:
        nen=c
    #print(row,tnelloc,tnel,nen,c,nenloc)
    global_ixbez = ([[0 for i in range(nen)] for j in range(tnel)])
    
    for i in range(row):
        for j in range(nen):
           
            if j >= c:
                global_ixbez[i][j]=0
            else:
                global_ixbez[i][j]=temp_ixbez[i][j] 
    print('l',row,tnelloc,tnel,nen,c,nenloc)
    for i in range(row,tnel,1):
        for j in range(nen):
           
            if j<nenloc:
                global_ixbez[i][j]=ixbezloc[i-row][j]
            else:
                global_ixbez[i][j]=0
    
    for i in range(tnelloc):
        temp_order = np.row_stack((temp_order, [p,q,r]))
    
    
    
    return global_ixbez,temp_order,nen
    
    