# Loop

# while Loop

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1


# count= 1
# while count <= 5 :
#     print("hello")
#     count += 1
    
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# i = 1
# while i >= 4 :
#     print("I love India")
#     i += 1

# print number from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# print the number from 5 to 1
# i = 5
# while i >= 1 :
#     print(i)      
#     i -= 1

# Print number from 1 to 100
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1
    
# Print number from 100 to 1
# i = 100
# while i >= 1 : #Stopping condition
#     print(i)
#     i -= 1

# Print the multiplication table of number n.
# n = int(input("enter number: "))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i += 1

# Print the elements of the following list using a loop:

# num = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0 
# while idx < len(num):
#     print (num[idx])
#     idx += 1

# search for a number x in this tuple using loop:


# num = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )

# x = 49

# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found at idx", i)
#     i += 1
# else:
#     print("finding")
# i += 1



# Break loop

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     else:
#         print("finding")
#     i += 1
    
# print("end of loop")



# Continue loop

# i = 0
# while i <= 5:
#     if(i == 5):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     if(i%2 == 0): #print odd number
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     if(i%2 != 0): #print even number
#         i +=1
#         continue
#     print(i)
#     i += 1


#For Loops

# num = [1, 2, 3, 4, 5]

# for val in num:
#     print(val)
    
# city = ["Nagpur, Pune, Mumbai, Satara, Bhandara"]
# for el in city:
#     print(len(el))


    
# str = "apna college"

# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)
    
# print("END")

# tup = (1,2,3,4,5,6,7,8,9)

# for num in tup:
#     print(num)


#for loop with else

# city = ["Nagpur, Pune, Mumbai, Satara, Bhandara"]
# for el in city:
#     print(len(el))
# else:
#     print("end")



#print the elements of the following list using a loop:

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

# for val in list:
#     print(val)




#serarch for a number x in this tuple using loop   -----(linear serach)
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

# x = 49
# i = 0
# for el in num:
#     if(el == x):
#         print("number found at idx:", i)
#     i += 1

# Range

# seq = range(5)

# for el in seq:
#     print(el)
    
#     or
    
# for el in range(5): #range(start)
#     print(el)
    
# for i in range(2, 10): #range(start, stop)
#     print(i)
    
# for i in range(2, 10, 2): #range(start, stop, step)
#     print(i)

# for i in range(1, 101): #print number from 1 to 100
#     print(i)

# for i in range(100, 1, -1): #print number from 100 to 1
#     print(i)

# print the multiplication table of a number n
# n = int(input("enter the number : "))

# for i in range(1, 11):
#     print(n * i)

# for i in range(5):   #pass
#     pass
# print("somne useful work")
    
    
    
# find the sum of first n numbers(using while)
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum =", sum)

# print hello 5 times
# count = 1 
# while count <= 5 :
#     print("hello")
#     count =+ 1
# print(count)

#  num = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue 
#     print(i)
#     i += 1


# num = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
# for el in num:
#     print(el)
    
# num = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49 )
# x = 49
# idx = 0

# for el in num:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx += 1

n = int(input("enter number : "))
for i in range(1, 11):
    print( n * i)
        