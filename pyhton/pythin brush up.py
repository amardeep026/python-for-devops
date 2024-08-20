# # #add two nu.

# # def add_two(a,b):
# #     result = a+b
# #     return result
# #     print(result)

# # a=2
# # b=5
# # x=  add_two(a,b)
# # print(x)


# # #multiply 2 mos. 

# # def mult(a,b):
# #     return(a*b)

# # x= mult(5,7)
# # print(x)

# #get input from user and print their name and age
# # If you want to pass name and age as arguments to the function, 
# # you should not take input inside the function but rather use the parameters directly:
# # def name_age():
# #     name= input("enter your name : ")
# #     age= input("enter your age : ")
# #     print(f"Hello your name is {name} and you age is {age} ")
# # # name_age()

# # def name_age(n,a):
# #     print(f"Hello {n} you age is {a} enjoy")
# # n= 'wery'
# # a= 45
# # name_age(n,a)

# #Write defination to add number upto 10
# # x= 10
# # s= 0
# # for i in range(x):
# #     s= s+i
# # print(s)
# #using def      
# # def sum_upto(x):
# #     s=0
# #     for i in range(x):
# #         s=s+i
# #     return(s)
# # j=sum_upto(20)
# # print(j)

# #function to write even number 
# # def even_noupto(x,y):
    
# #     even_no=[]
# #     for i in range(x,y):
# #         if i%2 ==0 and i>0:
# #             even_no.append(i)
# #         else:
# #             i=i+1
# #     return(even_no)

# # f=even_noupto(0,10)
# # print(f)
            
# #better way 
# #function to write even number 
# # def even_noupto(x,y):
# #     if x>=y:
# #         raise ValueError("start no must be less than end")
# #     even_no= [i for i in range(x,y) if i%2 ==0 and i>0]
# #     return even_no
# # f=even_noupto(0,10)
# # print(f)   


# #odd num    
# def odd_no_between(n1,n2):
#     odd_no =[i for i in range(n1,n2) if i%2!=0 and n2>n1]
#     return odd_no
    
# j=odd_no_between(1,10)
# print(j)
