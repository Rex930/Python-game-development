# Creating a 2d list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(len(matrix)) #No. of rows
print(len(matrix[0])) #No. of columns
print(matrix[1][2]) #Output should be 6

#Show all the items inside the 2dlist

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = " ")
    print("\n")    

#Take input for empty matrix
rows =  int(input("Enter the number of rows: "))
columns =  int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    temp = []
    for j in range (columns):
        x =  int(input("Enter your element: "))
        temp.append(x)
    matrix.append(temp)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print("\n")

    #Sqaure Matrix and diagonal elements
    matrix= []
    n= int(input("Enter the number of element:"))

    for i in range(n):
        temp = []
        for j in range(n):
            x= int(input("Enter the number of elements: "))
            temp.append(x)
        matrix.append(temp)

print("Diagonal Elements: ")
for i in range(n):
    print(matrix[i][i])