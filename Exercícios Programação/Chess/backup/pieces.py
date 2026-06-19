from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color: str, position: str):
        self.color = color
        self.column = position[0].lower()
        self.row = position[1]

    @abstractmethod
    def get_type(self) -> str:
        pass
    
    @abstractmethod
    def get_move_offsets(self) -> list:
        pass
    
    def moves(self, board) -> list:
        valid = []
        offsets = self.get_move_offsets()
        
        for col_offset, row_offset in offsets:
            new_col_idx = board.COLUMN_MAP.get(self.column, -1) + col_offset
            new_row_idx = int(self.row) - 1 + row_offset
            
            if 0 <= new_col_idx < 8 and 0 <= new_row_idx < 8:
                target_piece = board.grid[new_row_idx][new_col_idx]
                if target_piece is None or target_piece.color != self.color:
                    col_letter = list(board.COLUMN_MAP.keys())[new_col_idx]
                    valid.append((col_letter, new_row_idx + 1))
        
        return valid
    
    def valid_moves(self, board) -> list:
        return self.moves(board)

    def __repr__(self):
        return f"<{self.get_type()}; {self.color}; {self.column}{self.row}>"


class Queen(Piece):
    def get_type(self):
        return "Q"
    
    def get_move_offsets(self):
        offsets = []
        for i in range(1, 8):
            offsets.extend([(i, 0), (-i, 0), (0, i), (0, -i)])
            offsets.extend([(i, i), (i, -i), (-i, i), (-i, -i)])
        return offsets


class King(Piece):
    def __init__(self, color: str, position: str):
        super().__init__(color, position)
        self.has_moved = False  # Booleano para rastrear se o rei já se moveu (para castling)
    
    def get_type(self):
        return "K"
    
    def get_move_offsets(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1), 
                (1, 1), (1, -1), (-1, 1), (-1, -1)]


class Rook(Piece):
    def __init__(self, color: str, position: str):
        super().__init__(color, position)
        self.has_moved = False  # Booleano para rastrear se a torre já se moveu (para castling)
    
    def get_type(self):
        return "R"
    
    def get_move_offsets(self):
        offsets = []
        for i in range(1, 8):
            offsets.extend([(i, 0), (-i, 0), (0, i), (0, -i)])
        return offsets


class Pawn(Piece):
    def __init__(self, color: str, position: str):
        super().__init__(color, position)
        self.first_move = True  # Booleano para rastrear primeiro movimento
        self.last_double_move = False  # Booleano para rastrear pulo duplo
    
    def get_type(self):
        return "P"
    
    def get_move_offsets(self):
        if self.color == 'white':
            return [(0, 1), (0, 2)]
        else:
            return [(0, -1), (0, -2)]
    
    def valid_moves(self, board, last_move=None) -> list:
        """
        Calcula movimentos válidos do peão incluindo capturas e en passant.
        last_move: tupla (piece, old_pos, new_pos) do último movimento
        """
        valid = []
        current_col_idx = board.COLUMN_MAP[self.column]
        current_row_idx = int(self.row) - 1
        
        if self.color == 'white':
            # Movimento para frente (uma casa)
            new_row = current_row_idx + 1
            if new_row < 8:
                target = board.grid[new_row][current_col_idx]
                if target is None:
                    col_letter = list(board.COLUMN_MAP.keys())[current_col_idx]
                    valid.append((col_letter, new_row + 1))
                    
                    # Movimento duplo no primeiro movimento
                    if self.first_move:
                        new_row_2 = current_row_idx + 2
                        target_2 = board.grid[new_row_2][current_col_idx]
                        if target_2 is None:
                            col_letter = list(board.COLUMN_MAP.keys())[current_col_idx]
                            valid.append((col_letter, new_row_2 + 1))
            
            # Capturas na diagonal
            for col_offset in [-1, 1]:
                new_col = current_col_idx + col_offset
                new_row = current_row_idx + 1
                if 0 <= new_col < 8 and new_row < 8:
                    target = board.grid[new_row][new_col]
                    # Captura normal
                    if target and target.color != self.color:
                        col_letter = list(board.COLUMN_MAP.keys())[new_col]
                        valid.append((col_letter, new_row + 1))
                    
                    # En passant: peão inimigo fez pulo duplo e está na fileira 5 (row_idx 4)
                    elif last_move and current_row_idx == 4:  # Peão branco na fileira 5
                        last_piece, last_old, last_new = last_move
                        if (last_piece.get_type() == 'P' and 
                            last_piece.color == 'black' and
                            last_piece.last_double_move and
                            last_new[0] == new_col and
                            last_new[1] == 4):  # Peão preto na fileira 5 (row_idx 4)
                            col_letter = list(board.COLUMN_MAP.keys())[new_col]
                            valid.append((col_letter, new_row + 1))
        
        else:  # black
            # Movimento para frente (uma casa)
            new_row = current_row_idx - 1
            if new_row >= 0:
                target = board.grid[new_row][current_col_idx]
                if target is None:
                    col_letter = list(board.COLUMN_MAP.keys())[current_col_idx]
                    valid.append((col_letter, new_row + 1))
                    
                    # Movimento duplo no primeiro movimento
                    if self.first_move:
                        new_row_2 = current_row_idx - 2
                        target_2 = board.grid[new_row_2][current_col_idx]
                        if target_2 is None:
                            col_letter = list(board.COLUMN_MAP.keys())[current_col_idx]
                            valid.append((col_letter, new_row_2 + 1))
            
            # Capturas na diagonal
            for col_offset in [-1, 1]:
                new_col = current_col_idx + col_offset
                new_row = current_row_idx - 1
                if 0 <= new_col < 8 and new_row >= 0:
                    target = board.grid[new_row][new_col]
                    # Captura normal
                    if target and target.color != self.color:
                        col_letter = list(board.COLUMN_MAP.keys())[new_col]
                        valid.append((col_letter, new_row + 1))
                    
                    # En passant: peão inimigo fez pulo duplo e está na fileira 4 (row_idx 3)
                    elif last_move and current_row_idx == 3:  # Peão preto na fileira 4
                        last_piece, last_old, last_new = last_move
                        if (last_piece.get_type() == 'P' and 
                            last_piece.color == 'white' and
                            last_piece.last_double_move and
                            last_new[0] == new_col and
                            last_new[1] == 3):  # Peão branco na fileira 4 (row_idx 3)
                            col_letter = list(board.COLUMN_MAP.keys())[new_col]
                            valid.append((col_letter, new_row + 1))
        
        return valid


class Bishop(Piece):
    def get_type(self):
        return "B"
    
    def get_move_offsets(self):
        offsets = []
        for i in range(1, 8):
            offsets.extend([(i, i), (i, -i), (-i, i), (-i, -i)])
        return offsets
    

class Knight(Piece):
    def get_type(self):
        return "N"
    
    def get_move_offsets(self):
        return [(1, 2), (1, -2), (-1, 2), (-1, -2), 
                (2, 1), (2, -1), (-2, 1), (-2, -1)]
