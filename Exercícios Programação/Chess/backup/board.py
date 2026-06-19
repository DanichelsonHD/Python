from pieces import Piece


class Board:
    COLUMN_MAP = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    
    def __init__(self):
        self.columns = 8
        self.rows = 8
        self.grid = [[None for _ in range(8)] for _ in range(8)]
    
    def convert_position(self, position: str) -> tuple:
        col = position[0].lower()
        row = int(position[1]) - 1
        
        if col not in self.COLUMN_MAP or row < 0 or row > 7:
            raise ValueError(f"Invalid position: {position}")
        
        return (self.COLUMN_MAP[col], row)
    
    def place_piece(self, piece: Piece, position: str) -> bool:
        try:
            col, row = self.convert_position(position)
            
            if self.grid[row][col] is not None:
                print(f"Error: Position {position} is already occupied!")
                return False
            
            self.grid[row][col] = piece
            piece.column = position[0].lower()
            piece.row = position[1]
            #print(f"{piece.get_type()} {piece.color} placed at {position}")
            return True
        
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def remove_piece(self, position: str) -> bool:
        try:
            col, row = self.convert_position(position)
            if self.grid[row][col] is None:
                print(f"Error: No piece at {position}")
                return False
            self.grid[row][col] = None
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def get_piece(self, position: str) -> Piece:
        try:
            col, row = self.convert_position(position)
            return self.grid[row][col]
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    def __repr__(self):
        return f"<Board {self.columns}x{self.rows}>"
