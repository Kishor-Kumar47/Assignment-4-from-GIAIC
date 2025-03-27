# def main():
#     lst = []  # Make an empty list to store things in

#     val = input("Enter a value: ")  # Get an initial value
#     while val:  # While the user input isn't an empty value
#         lst.append(val) # Add val to list
#         val = input("Enter a value: ")  # Get the next value to add

#     print("Here's the list:", lst)


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()



def  main():
    holder = []

    val = input('Enter value to add in list: ')

    while val:
        holder.append(val)

        val = input('Enter value to add in list: ')

    
    print('Here is the list' ,holder)

if __name__ == '__main__':
    main()    