#Merge Sort
from random import randint
import numpy as np
from time import time
import matplotlib.pyplot as plt
from math import log
times = []

#####################################
def merge(a,b):
    if type(a)==int and type(b)==int:
        c = [min(a,b),max(a,b)]
    else:
        if (type(a) == list and type(b) == int): 
            b = [b]
        elif (type(b) == list and type(a) == int):
            a = [a]
        c = [];i=0
        j,k = 0,0
        while i < len(a)+len(b):
            if j < len(a):
                if k < len(b):
                    if a[j] <= b[k]:
                        c.append(a[j])
                        j += 1
                    else:
                        c.append(b[k])
                        k += 1
                else:
                    c.extend(a[j:])
                    break
            else: 
                c.extend(b[k:])
                break
            i += 1
    return c

def merge_list(a):
    l=[]
    for i in range(int(len(a)/2)+1):
        if 2*i+1 < len(a):
            #print([a[2*i]],[a[2*i+1]])
            l.append(merge(a[2*i],a[2*i+1]))
        elif 2*i+1 == len(a):
            l.append(a[-1])
        else:
            break
    return l

def merge_sort_rec(a):
    if len(a) == 1:
        return a[0]
    else:
        a = merge_list(a)
        #print(a)
        return merge_sort_rec(a)
       

lengths = [10000*(ll+1) for ll in range(40)]
for length in lengths:
    #print(length)
    t0 = time()
    a = [randint(1,3000000) for i in range(length)]
    #a.sort(reverse=True)
    b = list(a)
    t1 = time()
    a = merge_sort_rec(a) 
    t2 = time()
    times.append(t2-t1)
print('done')
times_avg = []
for i in range(100):
    a = [randint(1,3000000) for i in range(lengths[0])]
    t3 = time()
    a = merge_sort_rec(a)
    times_avg.append(time()-t3)

time_avg = sum(times_avg)/len(times_avg)    
n = [(i/lengths[0])*time_avg for i in lengths]
n_log = [(log(i/lengths[0])+1)*(i/lengths[0])*time_avg for i in lengths]

    ##################

print('Time to make random array of size',str(length)+':',str(int(10000*(t1-t0))/10000)+'s')
print('Time to sort:',str(int(10000*(t2-t1))/10000)+'s')
b.sort()
b = np.array(b)
a = np.array(a)
#print("Correctness:",sum(a == b)==length, str(int(10000*(time()-t2))/10000)+'s')
print('---------------------')
plt.plot(lengths,times,label='Merge Sort')
plt.plot(lengths[:35],n_log[:35],'-r',label='n log(n)')
plt.plot(lengths,n,'-g',label='n')
plt.xlabel('Size of Array')
plt.ylabel('Time (s)')
plt.legend(loc='upper left')
plt.savefig('Merge Sort.png',dpi=500)
plt.show()
