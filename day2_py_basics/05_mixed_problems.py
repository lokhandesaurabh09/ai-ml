# Prime number check

num = int(input("Enter a number: "))
if num < 2:
    print("Not prime")
else:
    is_Prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_Prime = False
            break
    print("Prime" if is_Prime else "Not Prime")

#-----------------------------------------------

# FizzBuzz(1 to 20)
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    
