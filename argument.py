def year_of_birth (name,age):
    year=2023-age
    print(f"Hello{name},you were born in {year}")

def my_country (country="Kenya"):
    print(f"Hello you are from{country}")

def hello(*names):
    for name in names:
       print(f"Hello{name}")

# def sum(*nums):
#     answer=0
#     for num in nums:
#         answer +=num


#      return answer
if you do not specify to the name of the argument you refer to is as positional

def multiply_many(**kwargs):
    answer=1
    for num in kwargs.values():
        answer*=num   
    return answer

def concatenate_arrgs(*names):
    for name in names:
        print(f"country{name}")

def concatenate_kwargs(**numbs):
    answer=0
    for numb in numbs.values():
        answer+=numb
    return answer    



       

     
    
    
   
