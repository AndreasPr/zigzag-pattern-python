def convert(inputString, numsRows):
    length = len(inputString)
    arrayWithTheString = ["" for x in range(length)] # ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
    row = 0

    if numsRows == 1:
        return inputString

    for i in range(length):
        arrayWithTheString[row] = arrayWithTheString[row] + inputString[i]

        #If we are at the last row, then don't go down (False), otherwise if we are at the 1st row, go down (True)
        if row == numsRows-1:
            down = False
        elif row == 0:
            down = True

        #If direction is down, increase the row, otherwise decrease it
        if down:
            row = row + 1
        else:
            row = row - 1

    for i in range(numsRows):
        print(arrayWithTheString[i], "\n")

inputString = "ANDREAS"
numRows = 3

convert(inputString, numRows)