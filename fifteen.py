import numpy as np
from random import choice, randint
from graph import Graph
import pdb

class Fifteen:
    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.solution = str(self)

        self.graph = Graph()
        for i in self.tiles:
            self.graph.addVertex(i) # creates a vertex for each element in self.tiles

        self.graph.addEdge(0, 12) # only possible moves at this point
        self.graph.addEdge(0, 15)

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move):
        if self.is_valid_move(move): 
            # find where zero and move are in self.tiles
            index_zero = -1
            index_move = -1
            for i in range(0, 16):
                if self.tiles[i] == 0:
                    index_zero = i
                if self.tiles[i] == move:
                    index_move = i

            #exchange zero with move in self.tiles
            self.transpose(index_zero, index_move)

            # we have moved zero to location index_move, if up, left, right
            # and down indices fall within self.tiles then add all of them
            # as zero's neighbors
            # create new vertex for zero and populate neighbors as we dont
            # have method for removing neighbors
            self.graph.addVertex(0)
            up = index_move - 4
            left = index_move - 1
            right = index_move + 1
            down = index_move + 4

            # in the first colum left is illegal
            # in the first column index is always divisible by 4 so index_move % 4 is not valid
            if index_move % 4 == 0:
                left = -1

            # in the last colum right is illegal
            if (index_move + 1) % 4 == 0:
                right = -1

            indices = [up, left, right, down]
            for index in indices:
                if index >= 0 and index <= 15: # if index is within the grid then it is a valid neighbor of zero
                    self.graph.addEdge(0, self.tiles[index])
                    
    # exchange i-tile with j-tile, tiles are numbered 1-15, the last tile is 0 (empty space)
    def transpose(self, i, j):
        temp = self.tiles[i] 
        self.tiles[i] = self.tiles[j]
        self.tiles[j] = temp

    # shuffle tiles
    def shuffle(self, steps=100):
        for i in range(steps):
            move = randint(1, 16)
            if self.is_valid_move(move):
                self.update(move)

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        zero = self.graph.getVertex(0)
        vertex = self.graph.getVertex(move)
        return vertex in zero.getConnections() # valid move if move is a neighbor of 0
    
    # for debug
    # def print_valid_moves(self):
    #     zero = self.graph.getVertex(0)
    #     moves = list()
    #     for vertex in zero.getConnections():
    #         moves.append(vertex.id)
    #     print(f'valid moves: {moves}')

    # verify if the puzzle is solved
    def is_solved(self):
        return self.solution == str(self) # if current string representation of game == solution, then game is solved

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        tiles = self.tiles.reshape(4, 4) # 4x4 matrix
        print('+---+---+---+---+') # top row of grid
        for row in tiles:
            tostr = ''
            for num in row:
                tostr += '|' # print bar before each number
                if num:
                    tostr += '{:^3}'.format(num) # prints each number centered in three spaces
                else:
                    tostr += '   ' # this is the 0
            tostr += '|' # prints bar after each number
            print(tostr)
            print('+---+---+---+---+') # bottom of of each row
    
    # return a string representation of the vector of tiles as a 2d array  1  2  3  4
    #                                                                      5  6  7  8
    #                                                                      9 10 11 12
    #       
    def __str__(self):
        tostr = ''
        tiles = self.tiles.reshape(4, 4) # converts to 4x4 matrix
        for row in tiles:
            for num in row:
                if num:
                    tostr += '{:^3}'.format(num) # prints each number centered in three spaces
                else:
                    tostr += '   '
            tostr += '\n' # creates new line after row
        return tostr
    

if __name__ == '__main__':
    
    # game = Fifteen()
    # game.draw()
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_valid_move(15) == True
    # assert game.is_valid_move(12) == True
    # assert game.is_valid_move(14) == False
    # assert game.is_valid_move(1) == False
    # game.update(15)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    # game.update(15)
    # assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_solved() == True
    # game.shuffle()
    # assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    # assert game.is_solved() == False
    
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    
        
