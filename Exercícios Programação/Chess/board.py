from pieces import Piece


class Board:
    COLUMN_MAP = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    COLUMNS = list(COLUMN_MAP.keys())

    def __init__(self):
        self.grid = [[None] * 8 for _ in range(8)]

    # ── Coordinate helpers ────────────────────────────────────────────────────

    def col_index_to_letter(self, index: int) -> str:
        return self.COLUMNS[index]

    def pos_to_indices(self, position: str) -> tuple[int, int]:
        """Converts 'e4' → (col_index, row_index). Raises ValueError on bad input."""
        col = position[0].lower()
        row = int(position[1]) - 1
        if col not in self.COLUMN_MAP or not (0 <= row <= 7):
            raise ValueError(f"Invalid position: {position}")
        return self.COLUMN_MAP[col], row

    # ── Piece access ──────────────────────────────────────────────────────────

    def get_piece(self, position: str) -> Piece | None:
        try:
            col, row = self.pos_to_indices(position)
            return self.grid[row][col]
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def place_piece(self, piece: Piece, position: str) -> bool:
        try:
            col, row = self.pos_to_indices(position)
            if self.grid[row][col] is not None:
                print(f"Error: {position} is already occupied.")
                return False
            self.grid[row][col] = piece
            piece.column = position[0].lower()
            piece.row = position[1]
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def remove_piece(self, position: str) -> bool:
        try:
            col, row = self.pos_to_indices(position)
            if self.grid[row][col] is None:
                print(f"Error: No piece at {position}.")
                return False
            self.grid[row][col] = None
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def move_piece_raw(self, piece: Piece, from_pos: str, to_pos: str):
        """Directly moves a piece on the grid without validation (used for simulation)."""
        fc, fr = self.pos_to_indices(from_pos)
        tc, tr = self.pos_to_indices(to_pos)
        self.grid[fr][fc] = None
        self.grid[tr][tc] = piece
        piece.column = to_pos[0].lower()
        piece.row = to_pos[1]

    def __repr__(self):
        return "<Board 8x8>"
