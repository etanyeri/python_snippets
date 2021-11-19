# Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    
    #0 and 1 is not prime
    
    for i in range(2,num+1):
        prime=True
        
    for i in range(2,num+1):
            if(num%i == 0):
                prime=False
                break
        if prime:
            counter += 1
            print(num)
            
    return counter