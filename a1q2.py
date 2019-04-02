from asgn1 import RSATool
import math

# Put your testing code here
# This function will be executed when you run your program on VPL
# This function will not be graded
def main():
    p = 17
    q = 29
    n=genKeyN(p,q)
    e=genKeyE(p,q)
    d=genKeyD(p,q,e)
    print(p)
    print(q)
    print(n)
    print(e)
    print(d)
    

#Task 2.1
def nextPrime(n):
    g = (int)(n)
    if(RSATool.isPrime(g)==True):
        g=g+1
    while(RSATool.isPrime(g)==False):
        g+=1
    return(g)
    

#This is given
def genKeyN(p, q):
    return p * q

#Task 2.2
def genKeyE(p, q):
    eulphi = genKeyN(p-1, q-1)
    tempe = (math.sqrt(eulphi))
    e = nextPrime(tempe)
    while(eulphi%e == 0):
        e= nextPrime(e)
        if(eulphi%e != 0):
            break
        
    return(e)

#Task 2.3
def genKeyD(p, q, e):
    phi = (p-1) * (q-1)
    d= RSATool.mInverse(e,phi)
    return d
    