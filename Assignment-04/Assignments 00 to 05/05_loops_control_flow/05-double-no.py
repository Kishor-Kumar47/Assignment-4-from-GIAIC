def main ():

 def double_until_limit():
     num = int(input("Enter a number: "))
     
     while num < 100:
         num *= 2
         print(num, end=" ")
 
 double_until_limit()

if __name__ == '__main__':
    main()
