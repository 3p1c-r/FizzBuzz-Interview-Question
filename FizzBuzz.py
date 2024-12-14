def fizz_buzzV1(num):
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 15 == 0:
        print("FizzBuzz")
    else:
        print(str(num))
        
fizz_buzzV1(6)
fizz_buzzV1(10)
fizz_buzzV1(30)

def fizz_buzzV2(num):
    for i in range(0,num + 1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else: 
            print(i)
fizz_buzzV2(10)
