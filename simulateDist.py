import random
import math



def brnl(p):                                    #bernoulli distribution
    s = []
    final = []
    for i in range(0, NS):
        s.append(random.random())
    
        if (s[i] <= p):
            final.append(1)
        else:
            final.append(0)
    print (s)

    return final

def bnml(n,p):                                      #binomial distribution
    finallist=[]
    for i in range (0, NS):
        s = []
        final = []
        count = 0
        for i in range(0, n):
            s.append(random.random())
            if (s[i] <= p):
                final.append(1)
                count+=1
            else:
                final.append(0)
        print(s)
        finallist.append(count)
        
    return finallist

def geo(p):                                     #geometric distribution
    x=1
    for i in range(0, NS):
        while(1>0):
            if (random.random() >p):
                x+=1
            else:
                final.append(x)
                x=1
                break
    return final

def NegBin(s, p):                            #Negative Binomial Distribution
    x=0
    for i in range(0, NS):
        x=0
        k=s
        while(k>0):
            if (random.random() > p):
                x+=1
                continue
            else:
                k-=1
                x+=1            
        final.append(x)
    return final


def new_list(p):                            #creating cdf 
    final_p=[]
    for i in range(0, len(p)):
        if i==0:
            p[i] = p[i]
            final_p.append(p[i])
        else:
            p[i]= p[i] + p[i-1]
            final_p.append((p[i]))
    return final_p    

def arb_dsc(p):                             #arbitrary discrete distribution
    p1 = new_list(p)
    n1 = NS
    n = len(p1)
    final =[]
    s=[]
    while(n1>0):
        s.append(random.random())
        n1-=1
    n1 = NS
    for i in range(0, len(s)):
        for j in range(0, n-1):
            if (s[i] < p[0]):
                final.append(0)
                break
            elif (p1[j] <= s[i] < p1[j+1]):
                final.append(j+1)
        n1-=1
    return final

def exp(p):                                     #exponential distribution
    final=[]
    for i in range (0, NS):
        final.append(((-1/p)*math.log(1-(random.random()))))
    return final

def gamma(a1, p):                               #gamma distribution
    print("in function")
    for i in range (0, NS):
        a = a1
        sum =0
        while(a>0):
            sum +=(((-1/p)*math.log(1-(random.random()))))
            a-=1
        final.append(sum)
        
    return final

def uni(a,b):                                           #uniform distribution
    for i in range(0, NS):
        final.append(a+((b-a)*random.random()))
    return final

def five_one():                          #Five one question distribution
#    x = (U)**(2/3)                     #equate f(x) or y to U
    final =[]
    for i in range(0, NS):
        final.append((random.random())**(2/3) )            
    
    return final

def five_six():                              #five-six question distribution
    s=[]
    final1=[]
    for i in range (0, NS):
        s.append(random.random())   
    print (s)
    for i in s:
        if (i < 0.8):
            final1.append((-1/20)*math.log(i))
        else:
            final1.append((-1/5)*math.log(i))
    
    return final1

def Normal(p1,p2):                           #normal Distribution
    s=[]
    final=[]
    final1=[]
    n = NS
    for i in range(0,n):
        s.append(random.random())
    for i  in range(0, n, 2):
        z1= ((((-2*math.log(s[i]))**(0.5))*(math.cos(2*math.pi*s[i+1]))))
        z2= ((((-2*math.log(s[i]))**(0.5))*(math.sin(2*math.pi*s[i+1]))))
        final.append(z1)
        final.append(z2)
    for i in range(0, len(final)):
        final1.append((p1 + (p2*final[i])))
    if (NS%2==0):
        return final1
    else:
        return final1[:-2]   

def psn(p):                                       #poisson distribution
    final=[]
    sum =1
    var = math.exp(-p)
    print(var)
    for i in range (0, NS):
        count =0
        while(1>0):
            sum *= (random.random())
            count += 1
            if(sum <= var):
                print ( count)
                final.append((count -1)) 
                sum = 1
                count =0
                break
            else:
                continue
                         
    return final
    
             
    
    


                
    
    

        
    

def Mean_SD(op):             #calculating Mean and standard  deviation
    file = open('result.txt', 'a')
    print ("The samples are as below")
    print(op)
    file.write("\n")
    file.write(  Dis+" Distribution\n\n" )
    file.write("Samples: ")
    file.write(str(op))
    sum = 0
    SM = 0  
    sd = 0
    n = len(op)  
    for i in op:
        sum += i
    print("Sum" , sum    )                                 
    SM = sum / n 
    file.write("\nSample Mean: ")
    file.write(str(SM))
    print ("Sample Mean", SM)
    file.write(str(SM))
    
    if (SM == 0):                                 #standard deviation
        print("Sample Standard Deviation is ", 0)
    else:
        for i in op:
            sd += ((i-SM)**2)
        sdn = ((sd/(n-1))**0.5)
    file.write("\nSample Standard Deviation: ")
    file.write(str(sdn))
    file.write("\n")
    file.close()
        
    print("Sample Standard Deviation", sdn)

random.seed(10)                                  #SEED value input

inp = input ("Enter the distribution types and parameters").lower()  #start f

Lst = inp.split(',')

op=[]
final =[]




NS = int(Lst[0])                                #No. of samples
file = open('result.txt', 'a')

                              

Dis = Lst[1]
Dis = Dis.strip()                               #distribution type
print("\nDistribution", Dis)
Param = [float(i) for i in Lst[2:]]
if ( Dis == "bernoulli"):
    p = Param[0]
    final = brnl(p)
    Mean_SD(final)
elif (Dis == "binomial"):
    n = int(Param[0])
    p = Param[1]
    final = bnml(n, p)
    Mean_SD(final)
elif (Dis == "geometric"):
    p = Param[0]
    final = geo(p)
    Mean_SD(final)
elif(Dis == "neg-binomial"):
    k = Param[0]
    p = Param[1]
    final = NegBin(k, p)
    Mean_SD(final)
elif (Dis == "exponential"):
    p = Param[0]
    final = exp(p)
    Mean_SD(final)
elif(Dis == "five-one"):
    final = five_one()
    Mean_SD(final)
elif (Dis == "five-six"):
    final1 = five_six()
    Mean_SD(final1)
elif(Dis == "normal"):
    p1 = Param[0]
    p2 = Param[1]
    final = Normal(p1, p2)
    Mean_SD(final)
elif(Dis=="poisson"):
    p = Param[0]
    final = psn(p)
    Mean_SD(final)
elif (Dis == "uniform"):
    a = Param[0]
    b = Param[1]
    final = uni(a,b)
    Mean_SD(final)
elif (Dis == "gamma"):
    a = Param[0]
    p = Param[1]
    final = gamma(a,p)
    Mean_SD(final)
elif(Dis == "arb-discrete"):
    p = Param
    final = arb_dsc(p)
    Mean_SD(final)
    
    
    


    















