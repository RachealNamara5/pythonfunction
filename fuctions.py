#write a python program to print the even numbers from a given list
list=[1,2,3,4,5,6,7,8,9]
for item in list:
    if item % 2 == 0:
        print(item)
        
 # write a python program to multiply all the numbers from list
#list=[8,2,3,-1,7] 
# let 8=a,2=b,3=c,-1=d,7=e
def multiply_list(a,b,c,d,e):
    result=a*b*c*d*e
    print(f"multiplication of items{a},{b},{c},{d}and{e}is{result}")
multiply_list(8,2,3,-1,7)
    
       
 #write a python function to sum all numbers in a list
#list=[8,2,3,0,7]
def sumation(p,q,r,s,t):
    output=p+q+r+s+t
    print(f"sumation of items{p},{q},{r},{s}and{t}is {output}")
sumation(8,2,3,0,7)
        
 #write a python program to reverse a string 
# 1,2,3,4,a,b,c,d
def reverse_a_string(string):
     return string[::-1]
 
input_string="1234abcd"
print(reverse_a_string(input_string))