#Import features
from add import add
from sub import sub
from mul import mul
from div import div

def main():
    a = 10
    b = 5

    print("Addition: (a+b)", add(a,b))
    print("Subtraction (a-b):", sub(a,b))
    print("Multiplication (a*b):", mul(a,b))
    print("Division (a/b):", div(a,b))

if __name__ == "__main__":
    main()
