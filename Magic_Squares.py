#  File: Magic_Squares.py
#  Description: A program that creates a magic square grid.

#  Date Created: 11 / 13 / 2018
#  Date Last Modified: 01 / 06 / 2019

class MagicSquare:

    def __init__(self, sides):

        self.sideLength = sides
        self.grid = []              #create grid

        for row in range(sides):
            row = []
            for col in range(sides):
                row.append(0)
            self.grid.append(row)

        i = 1
        x = 0               # horizontal
        y = sides // 2      # vertical
        self.grid[x][y] = i
        n = sides

        while (i < n**2):
            if(i%n == 0):
                x = (x + 1)%n
            else:
                x = (x - 1 + n)%n
                y = (y + 1)%n
            i = i + 1
            self.grid[x][y] = i

        # use mod % to ensure that values don't go out of the grid

    def display(self):
        for row in self.grid:
            for col in row:
                print(format(col,">5d"),end="")
            print()

def main():

    odd = [1, 3, 5, 7, 9, 11, 13]

    for i in odd:
        print("Magic Square of Length " + str(i))
        square = MagicSquare(i)
        square.display()
        print()

main()
