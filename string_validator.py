a = False
def string_validator(s, a):

    print(max([i.isalnum() for i in s]))
    print(max([i.isalpha() for i in s]))
    print(max([i.isdigit() for i in s]))
    print(max([i.islower() for i in s]))
    print(max([i.isupper() for i in s]))  
           
s = 'qA2'

print(string_validator(s, a))