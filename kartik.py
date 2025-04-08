'''
def oddnumber(a):
    if a%2!=0:
        return f"{a} is odd number"
    else:
        return f"{a} is even number"
x= int(input("Enter any number: "))    
result = oddnumber(x)
print(result)
'''

#Sum of all numbers
'''
def sum(a,b,c):
    result = a+b+c
    return result

x=int(input("1st number: "))
y=int(input("2nd number: "))
z=int(input("3rd number: "))
res=sum(x,y,z)
print(res)
'''

#args
'''
def output(*args):
    sum=0
    for number in args:
        sum=sum+number
    return sum 
x=output(3,4,5,0,4,5,6)
print(x)
'''


#multiply 
'''
def multiply(*args):
    multi=1
    for number in args:
        multi=multi*number
    return multi
x=multiply(3,5,4,6,7,9,8)
print(x)
'''

#reverse
'''
reverse ="hello"
print(reverse[::-1])
'''

mayank = [2,3,5,6,8,8]
for gandu in mayank:
    if  gandu%2==0:
            print(gandu)
    else:
        print("is not gandu") 
        
        
        