GridInput = int(input("Enter the corresponding index for the column you would like printed (0,1,2): "))

number_grid = [ 
[1,2,3],
[4,5,6],
[7,8,9],
[0]
]

for row in number_grid:
    try:
        print(row[GridInput])
    except:
        print("list index out of range")
        break

   