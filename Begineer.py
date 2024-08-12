#brer " " or '' it's the same
print("Hello world!!")  
print('Hello world!!')
#output Hello world!! doch knea



# assign value to your_name
your_name1="PHOU PHOEURK"
your_name2='phou phoeurk'
print(your_name1)#PHOU PHOEURK
print(your_name2)#phou phoeruk


#Enter value to variable 
a,b,c=1,1.2,'Hello PHOEURK'
print(a)#1
print(b)#1.2
print(c)#Hello PHOEURK

#variable equal variable
site1=site2='I LOVE YOU'
print(site1)
print(site2)


#integer number s
a=1
print(type(a)) #class "int"


#Floating point numbers
b=3.45
print(type(b))#class "Float"

#Complex number
c=1+2j  # a=1,b=2 a,b rbos R
print(type(c))

#Boolean
d=True  #1
e=False #0
print(type(d))
print(type(e))


#integer to float
x=1
y=0.5
n=x+y
print(x)
print(y)
print(n)
print(type(n))


#int or float add str > Error
# f=1
# g='s'
# h=f+g # error

#convert data type on to another
num_int=12
num_str='10'
print("Data type of num_str before Type casting: ",type(num_str))

# Convert string to integer 
num_str=int(num_str)
print("Data type of num_str afther Type casting: ",type(num_str))
num_sum=num_int+num_str
print(num_sum)
print(type(num_sum))

# use(+) connect str & str 
print("PHOU"+"PHOEURK") #unspace
print("PHOU","PHOEURK") #add space between PHOU & PHOEURK

#output data by use (.format)
i=1
j=2
print("Value i={}\nValue j={}".format(i,j))

#Input() && Output DATA
name=input('Enter your name: ')
print(name)
print(type(name))