def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()





# my practice 👇 

# def main():

#     dvident: int = int (input('enter no dvident:'))
#     dvissor: int = int (input('enter no dvissor:'))

#     qusent: int = dvident // dvissor
#     remdr: int = dvident % dvissor

#     print('your divide ans is:'+ str(qusent) + ' and reminder is :' + str(remdr) )


# if __name__ == '__main__':
#     main()    