#1 global variables
x="awesome"  
def myfunc():
    x="fantastic"  #x is a local variable
    print("Python is "+x)

myfunc()

print("Python is " +x)

#2
def myfunc():
    global x
    x="fantastic"
    
myfunc()

print("python is "+x)

#3
x="awesome"
def myfunc():
    global x
    x="fantastic"
    
myfunc()

print("python is "+x)

#4 Complex datatype
x=1j
print(x)
print(type(x))

#5 List datatype
x=["banana","apple","cherry"]
print(x)
print(type(x))

#6 Tuple datatype
x=("Banana","apple","cherry")
print(x)
print(type(x))

#7 Set datatype
x={"Banana","apple","cherry"}
print(x)
print(type(x))

#8 Dictionary datatype
x={'name':'John','age':36}
print(x)
print(type(x))

#9 frozen set - is immutable and it is not assured that the order of elements will be retained.
x= frozenset({"apple","banana","cherry"})
print(x)
print(type(x))

#10 Boolean datatype
x=True
print(x)
print(type(x))

#11 NoneType datatype
x= None
print(x)
print(type(x))

#12 bytes datatype
x=b"hello" #the b keyword instructs the interpreter to read the string content as sequence of bytes rather than character. The byte literals are used for representing binary datalike images, audio, encoded texts etc.
print(x)
print(type(x))

#13 bytearray datatype
x=bytearray(5)
print(x)# this method returns a bytearray object i.e array of bytes which is mutable sequence of integer in range 0<=x<256.
print(type(x))

#14 Range datatype
x=range(6)
print(x)
print(type(x))

