# Print multiplication table from 1 to 10

# pseudo code

# use nested for loop to make the multiplication table
for outer in range (1, 11):
    print("Multiples of", outer,":")
    for inner in range (1 , 11):
        inner *= outer
        print(inner, end = " ")
    print()