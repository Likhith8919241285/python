def main():
    x = int(input("What is x ??: "))     ## These is just outer part of the car or an interface
    print("The number is ",square(x))              ####### These substitutes the value of x to n

def square(n):
    return n - n   ## These is just like an engine
           ## So the enginer (square function) runs it and gives the output to interface(main function)  and the main function process it out                                       
if __name__ == "__main__":
    main()
 

   
