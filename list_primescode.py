#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#find primes
def count_prime(upperlimit):
    
    primes_upto_upperlimit=[]
    for x in range(2,upperlimit):

        for y in range (2,x):
            if x%y==0:
                y=y+2
                break


            elif y>=x-1:
                primes_upto_upperlimit.append(x)
                break
            else:
                y=y+2

    
    print(f'there are {len(primes_upto_upperlimit)} prime numbers less than {upperlimit}')
    return(primes_upto_upperlimit)


# %%
#find primes
def count_prime(upperlimit):
    
    primes_upto_upperlimit=[]
    for x in range(2,upperlimit):

        for y in range (2,x):
            if x%y==0:
                y=y+2
                break


            elif y>=x-1:
                primes_upto_upperlimit.append(x)
                break
            else:
                y=y+2

    
    print(f'there are {len(primes_upto_upperlimit)} prime numbers less than {upperlimit}')
    return(primes_upto_upperlimit)



# %%

# %%
