def primes(num):
    for ele in range(2,num+1):
        for i in range(2,ele):
            if(ele%i==0):
                break
        else:
            print(ele)
primes(10)