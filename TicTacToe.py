class TicTacToeBoard:

    def __init__(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.count = 1
        self.player = ''

    def get_field(self):
        print('      1    2    3')
        print('1  ', self.board[0])
        print('2  ', self.board[1])
        print('3  ', self.board[2])

    def new_game(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.count = 1
        self.player = ''
        board.get_field()

    def make_move(self, row, col):
        if self.count %2 == 0:
            self.player = 'X'
        else:
            self.player = 'O'
        if self.board[row-1][col-1] == '-':
            self.board[row-1][col-1] = (self.player)
        else:
            print(f'Клетка ({row},{col}) занята')
            self.count -=1
        board.get_field()
        self.count +=1
        
    





board = TicTacToeBoard()
board.new_game()
board.make_move(2,1)
board.make_move(1,2)
board.make_move(3,1)
board.make_move(3,1)
board.make_move(2,3)
board.new_game()
board.make_move(3,1)
board.make_move(2,3)


