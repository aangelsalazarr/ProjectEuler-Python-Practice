import numpy as np

# purpose is to convert txt file into a readable file in our program
with open('1000-digit-number.txt') as f:
    lines = f.readlines()

lines_stripped = []

# purpose is to show our new list of strings
print(lines)

# checking to see if all elements are the same length
for i in lines:
    print(len(i)) # value is 51 except for last line which is 50

# all string elements, except for [-1], have a '\n' and it needs to be removed
for i in lines:
    lines_stripped.append(i.replace("\n", ""))

# checking to see if we successfully removed new line portion
print(lines_stripped)

# initializing substring
k = 1

# empty list where split string will go into
res = []

# purpose is to now split all digits into their own element
for i in lines_stripped:
    for idx in range(0, len(i), k):
        # converting to int, after slicing
        res.append(int(i[idx : idx + k]))

# checking to see if we successfully split all digits in to their own element
print(res)

# check the length of res - we are good to go!
print(len(res))

# we will be using zip method to print out consecutive elements pairing in a list
# res is our test list in this case

# printing the original list
print("\n")
print("The original list : " + str(res))

# using zip()
# consecutive element pairing; 13 adjacent elements in the 100 digit list
result = list(map(list, zip(res,
                            res[1:],
                            res[2:],
                            res[3:],
                            res[4:],
                            res[5:],
                            res[6:],
                            res[7:],
                            res[8:],
                            res[9:],
                            res[10:],
                            res[11:],
                            res[12:])))

# print result - good to go!
print("The Consecutive Element Paired List is:" + str(result))

# creating empty list to add products
products = []

# now we want to take the product of each element and return the highest element
for element in result:
    products.append(np.prod(element))

# check to see our new list of products
print(products)

# lastly, we want to find max number and its position!
max_value = max(products) # return the max value of the list

# find the index of the max value
max_index = products.index(max_value)

# print max index and max value
print(max_index)
print(max_value)

# print element of 13 adjacent numbers that is supposed to be the highest product
print(result[503])

# creating a new empty list
product_list = []

## we will solve without numpy as it is showing errors
def multiplylist(mylist):
    """Purpose is to take the product of elements in a list"""
    # mutliplying elements one by one
    product = 1
    for x in (mylist):
        product = product * x
    product_list.append(product)

# applying our function to each element in a list
for element in result:
    multiplylist(element)

# finding max value of element in list
max_value_2 = max(product_list)
print(max_value_2) # yay we got it!!!
