import os
import time

class Cheess:

    positionABC={'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    position123 = {0: 'A', 1: 'B', 2: 'C', 3: 'D',  4: 'E',  5: 'F', 6: 'G', 7 :'H'}
    turn = ["Blacks", "Whites"]
    num_turn = 1
    moves_of_blacks = 0
    moves_of_whites = 0
    
    def __init__(self):
        # '#' is black square and '@' is a white square
        self.table = [['@','#','@','#','@','#','@','#'],
                      ['#','@','#','@','#','@','#','@'],
                      ['@','#','@','#','@','#','@','#'],
                      ['#','@','#','@','#','@','#','@'],
                      ['@','#','@','#','@','#','@','#'],
                      ['#','@','#','@','#','@','#','@'],
                      ['@','#','@','#','@','#','@','#'],
                      ['#','@','#','@','#','@','#','@']]

        self.table_reference = [['@', '#', '@', '#', '@', '#', '@', '#'],
                                ['#', '@', '#', '@', '#', '@', '#', '@'],
                                ['@', '#', '@', '#', '@', '#', '@', '#'],
                                ['#', '@', '#', '@', '#', '@', '#', '@'],
                                ['@', '#', '@', '#', '@', '#', '@', '#'],
                                ['#', '@', '#', '@', '#', '@', '#', '@'],
                                ['@', '#', '@', '#', '@', '#', '@', '#'],
                                ['#', '@', '#', '@', '#', '@', '#', '@']]
        # Minusculas negras, Mayusculas blancas
        self.blacks = ['p','t','c','a','q','r']
        self.whites = ['P','T','C','A','Q','R']

    def table_costrution(self):
        os.system("cls")

        tablero = " | A B C D E F G H |\n-+-----------------+-\n"
        number_row = 1

        for row in self.table:
            tablero += str(number_row) + "| "

            for col in row:
                
                tablero += col + " "

            tablero +="|" + str(number_row) + "\n"
            number_row += 1

        tablero += "-+-----------------+-\n | A B C D E F G H |"
        print tablero

    def distribution_of_pieces(self):
        
        self.table[0][0] = self.blacks[1]
        self.table[0][-1] = self.blacks[1]
        self.table[0][1] = self.blacks[2]
        self.table[0][-2] = self.blacks[2]
        self.table[0][2] = self.blacks[3]
        self.table[0][-3] = self.blacks[3]
        self.table[0][3] = self.blacks[4]
        self.table[0][4] = self.blacks[5]

        for peon in range(0,8):
            self.table[1][peon] = self.blacks[0]

        self.table[-1][0] = self.whites[1]
        self.table[-1][-1] = self.whites[1]
        self.table[-1][1] = self.whites[2]
        self.table[-1][-2] = self.whites[2]
        self.table[-1][2] = self.whites[3]
        self.table[-1][-3] = self.whites[3]
        self.table[-1][3] = self.whites[4]
        self.table[-1][4] = self.whites[5]

        for peon in range(0, 8):
            self.table[-2][peon] = self.whites[0]

    def move_piece(self, actual_position, next_position):
        actual_Y = actual_position[0].upper()
        actual_Y = self.positionABC[actual_Y]
        
        actual_X = int(actual_position[-1])-1
        
        next_Y = next_position[0].upper()
        next_Y = self.positionABC[next_Y]

        next_X = int(next_position[-1])-1

        turn, num_turn = self.is_a_turn(self.turn[self.num_turn], self.table[actual_X][actual_Y])

        if turn:

            if self.move_approve(actual_X, actual_Y, next_X, next_Y):
                
                if self.is_piece(actual_X, actual_Y):
                    self.table[next_X][next_Y] = self.table[actual_X][actual_Y]
                    self.table[actual_X][actual_Y] = self.table_reference[actual_X][actual_Y]
                else:
                    print ("This not a piece...")
                    time.sleep(3)
            else:
                print ("Can't move")
                time.sleep(100)
        else:
            print ("Is not are your turn...")
            time.sleep(3)

    def is_black(self, piece):
        return piece == piece.lower()

    def is_piece(self, actual_X, actual_Y):
        piece = self.table[actual_X][actual_Y].lower()
        if self.is_black(piece):
            return piece in self.blacks

    def is_a_turn(self, turn_of, piece):
        if turn_of == self.turn[0] and self.is_black(piece):
            return True, 1
        if turn_of == self.turn[1] and not self.is_black(piece):
            return True, 0
        return False, self.num_turn

    def restrictions(self, piece, posX, posY):
        if piece.lower() == 'p':
            if self.num_turn == 1:
                if self.moves_of_whites == 0:
                    posibles_moves = [
                        self.position123[posY] + str(posX + 1), self.position123[posY] + str(posX + 2)]
                else:
                    posibles_moves = [self.position123[posY] + str(posX + 1)]
            else:
                if self.moves_of_blacks == 0:
                    posibles_moves = [self.position123[posY] + str(posX + 1) , self.position123[posY] + str(posX + 2)]
                else:
                    posibles_moves = [self.position123[posY] + str(posX + 1)]
        return posibles_moves

    def move_approve(self, actual_X, actual_Y, next_X, next_Y):
        # for moves in self.restrictions(self.table[actual_X][actual_Y], actual_X, actual_Y):
        #     print "Done"
        #     print self.positionABC[moves[0]] , next_Y , (next_X , int(moves[1]) - 2 , next_X , int(moves[1])-1)

        #     if self.positionABC[moves[0]] == next_Y and (next_X == int(moves[1]) - 2 or next_X == int(moves[1])-1):
        #         return True
        # return False
        piece = self.table[actual_X][actual_Y].lower()
        if piece == "p":
            if self.table[next_X][next_Y].lower() == "#" or self.table[next_X][next_Y].lower() == "@":
                if actual_Y == 7 or actual_Y == 1: move_n = 2
                else: move_n = 1
                if next_X == actual_X - move_n or next_X == actual_X  - 1:
                    return True
        elif piece == "r":
            if self.table[next_X][next_Y].lower() == "#" or self.table[next_X][next_Y].lower() == "@":
                if next_X == actual_X and next_Y == actual_Y:
                    return False
                else:
                    pass
        return False

game = Cheess()

game.distribution_of_pieces()

game.move_piece('b7', 'b5')
game.table_costrution()