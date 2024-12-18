import string
charset =string.ascii_lowercase+string.ascii_uppercase+ string.digits+"~!`@#$%^&*()_-+=',./"

def possible_combinations(length,chars):
    if length ==1:
        for char in chars:
            yield  char
    else:
        for previous in possible_combinations(length-1,chars):
            for char in chars:
                yield previous + char
def brute_force(target):
    max_length=8
    for length in range(1,max_length+1):
        for guess in possible_combinations(length,charset):
            print(f"\rTrying: {guess}",end="")
            if guess ==target:
                print(f"\nPassword cracked! The password is: {guess}")
                return                
password=input("Enter Password:")
brute_force(password)