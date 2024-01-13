"""A program that show the best possible way for the knight
to get to the goal position which is (8,8) cell using A* algorithm
NOTE: user can enter block count and blocks position."""


class Node:
    """A class for nodes object"""

    g = None
    h_v = None
    f = None
    moves_made = None
    moves_made_board = None
    knight_position = None

    def __init__(self, old_g, moves_list, moves_board_list, knight_new_position, old_board):
        self.g = old_g + 1
        self.moves_made = moves_list.copy()
        self.moves_made_board = moves_board_list.copy()
        self.knight_position = knight_new_position
        self.knight_position = knight_new_position

        board = old_board
        board[knight_new_position[1]][knight_new_position[0]] = "♞"

        self.moves_made_board.append(board)
        self.moves_made.append(knight_new_position)

        self.h_v = self.h()
        self.f = self.h_v + self.g

    def h(self):
        """calculate value of h"""
        x, y = self.knight_position
        return (14 - x - y) / 3


def print_board(board_):
    """print the board"""
    for i in range(7, -1, -1):
        print(board_[i])


def knight_possible_moves(knight_position_, blocks):
    """return knight possible moves"""
    moves = []
    x, y = knight_position_

    moves.append((x + 2, y + 1))
    moves.append((x + 2, y - 1))
    moves.append((x - 2, y + 1))
    moves.append((x - 2, y - 1))
    moves.append((x + 1, y + 2))
    moves.append((x - 1, y + 2))
    moves.append((x - 1, y - 2))
    moves.append((x + 1, y - 2))

    possible_moves = []
    for i in range(8):
        if 0 <= moves[i][0] <= 7 and 0 <= moves[i][1] <= 7:
            possible_moves.append(moves[i])

    for i in blocks:
        x_b, y_b = i
        for index, element in enumerate(possible_moves):
            x_p, y_p = element
            if x_b == x_p and y_b == y_p:
                possible_moves.pop(index)
                break

    return possible_moves


def board_copy(board):
    """make a copy of board"""
    ls = []
    for i in board:
        row = i.copy()
        ls.append(row)
    return ls


def main():
    """Entry of program"""

    board = [
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', 'G'],
    ]

    blocks = []

    block_count = int(input("How many blocks ?"))

    for _ in range(block_count):
        print(_ + 1, "=>")
        x = int(input("X :"))
        y = int(input("Y :"))

        if (x == 1 and y == 1) or (x == 8 and y == 8):
            raise ValueError("Block position can not be (1, 1) OR (8, 8)")

        board[y - 1][x - 1] = '*'
        blocks.append((x - 1, y - 1))

    start = Node(-1, [], [], (0, 0), board_copy(board))

    frontier = [start]
    explored = []

    while frontier:
        min_f = frontier[0].f
        index = 0
        for i, item in enumerate(frontier):
            if item.f < min_f:
                index = i
                min_f = item.f
        node = frontier.pop(index)

        if node.knight_position[0] == 7 and node.knight_position[1] == 7:
            break

        explored.append(node)

        for move in knight_possible_moves(node.knight_position, blocks):
            frontier.insert(index, Node(node.g,
                                        node.moves_made,
                                        node.moves_made_board,
                                        move,
                                        board_copy(board)))

    for i in node.moves_made_board:
        print_board(i)
        print("*" * 20)

main()
