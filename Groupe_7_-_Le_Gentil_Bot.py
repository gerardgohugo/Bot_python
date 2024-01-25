
import random

# Classe du Bot
class Le_Gentil_Bot:

    def __init__(self):
        self.name = "Name of your Bot"

    # BOT FUNCTIONS


    def strat_corners(self, sq):

        square_weights = [
            120, -20, 20, 5, 5, 20, -20, 120,
            -20, -40, -5, -5, -5, -5, -40, -20,
            20, -5, 15, 3, 3, 15, -5, 20,
            5, -5, 3, 3, 3, 3, -5, 5,
            5, -5, 3, 3, 3, 3, -5, 5,
            20, -5, 15, 3, 3, 15, -5, 20,
            -20, -40, -5, -5, -5, -5, -40, -20,
            120, -20, 20, 5, 5, 20, -20, 120,
        ]
    
        return square_weights[sq]


    def check_valid_moves(self, board, game):

        current_move = []
        max_points = -200
        max_points_move = []

        for index_tile in range(len(board.board)):
            x_pos = board.board[index_tile].x_pos
            y_pos = board.board[index_tile].y_pos

            legal_move = board.is_legal_move(x_pos, y_pos, game.active_player)

            if legal_move is not False:
                current_move = [x_pos, y_pos]
                current_points = 0

                for index_legal_move in legal_move:
                    current_points += index_legal_move[0]
            
                current_points += self.strat_corners(index_tile)

                if current_points > max_points:
                    max_points_move = [current_move]
                    max_points = current_points  
                elif current_points == max_points:
                    max_points_move.append(current_move)

        return random.choice(max_points_move)


# Création du Bot
le_gentil_bot = Le_Gentil_Bot()

# Exécution du Bot
move_coordinates = le_gentil_bot.check_valid_moves(othello_board, othello_game)