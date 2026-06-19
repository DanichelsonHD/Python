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

    def valid_moves(self, board, last_move=None) -> list:
        valid = []
        for col_offset, row_offset in self.get_move_offsets():
            new_col = board.COLUMN_MAP.get(self.column, -1) + col_offset
            new_row = int(self.row) - 1 + row_offset
            if 0 <= new_col < 8 and 0 <= new_row < 8:
                target = board.grid[new_row][new_col]
                if target is None or target.color != self.color:
                    valid.append((board.col_index_to_letter(new_col), new_row + 1))
        return valid

    def pos(self) -> str:
        """Returns the piece's current position as a string like 'e4'."""
        return f"{self.column}{self.row}"

    def __repr__(self):
        return f"<{self.get_type()} {self.color} {self.pos()}>"


# ── Sliding pieces ────────────────────────────────────────────────────────────

class Queen(Piece):
    def get_type(self): return "Q"

    def get_move_offsets(self):
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        return [(i * dc, i * dr) for i in range(1, 8) for dc, dr in directions]


class Rook(Piece):
    def __init__(self, color: str, position: str):
        super().__init__(color, position)
        self.has_moved = False

    def get_type(self): return "R"

    def get_move_offsets(self):
        return [(i * dc, i * dr) for i in range(1, 8) for dc, dr in [(1,0),(-1,0),(0,1),(0,-1)]]


class Bishop(Piece):
    def get_type(self): return "B"

    def get_move_offsets(self):
        return [(i * dc, i * dr) for i in range(1, 8) for dc, dr in [(1,1),(1,-1),(-1,1),(-1,-1)]]


# ── Jumping pieces ────────────────────────────────────────────────────────────

class Knight(Piece):
    def get_type(self): return "N"

    def get_move_offsets(self):
        return [(dc, dr) for dc in [-2,-1,1,2] for dr in [-2,-1,1,2] if abs(dc) != abs(dr)]


class King(Piece):
    def __init__(self, color: str, position: str):
        super().__init__(color, position)
        self.has_moved = False

    def get_type(self): return "K"

    def get_move_offsets(self):
        return [(dc, dr) for dc in [-1,0,1] for dr in [-1,0,1] if (dc, dr) != (0, 0)]


# ── Pawn ──────────────────────────────────────────────────────────────────────

class Pawn(Piece):
    def __init__(self, color: str, position: str):
        super().__init__(color, position)
        self.first_move = True
        self.last_double_move = False

    def get_type(self): return "P"

    def get_move_offsets(self):
        # Unused — valid_moves overrides fully for pawns
        d = 1 if self.color == 'white' else -1
        return [(0, d), (0, d * 2)]

    def valid_moves(self, board, last_move=None) -> list:
        valid = []
        col = board.COLUMN_MAP[self.column]
        row = int(self.row) - 1
        d = 1 if self.color == 'white' else -1  # direction

        # Forward one square
        if 0 <= row + d < 8 and board.grid[row + d][col] is None:
            valid.append((board.col_index_to_letter(col), row + d + 1))
            # Forward two squares on first move
            if self.first_move and board.grid[row + d * 2][col] is None:
                valid.append((board.col_index_to_letter(col), row + d * 2 + 1))

        # Diagonal captures and en passant
        for dc in [-1, 1]:
            tcol, trow = col + dc, row + d
            if not (0 <= tcol < 8 and 0 <= trow < 8):
                continue
            target = board.grid[trow][tcol]
            if target and target.color != self.color:
                valid.append((board.col_index_to_letter(tcol), trow + 1))
            elif self._can_en_passant(last_move, row, tcol):
                valid.append((board.col_index_to_letter(tcol), trow + 1))

        return valid

    def _can_en_passant(self, last_move, current_row: int, target_col: int) -> bool:
        if not last_move:
            return False
        last_piece, _, last_new_idx = last_move
        ep_row = 4 if self.color == 'white' else 3  # row index where en passant applies
        return (
            last_piece.get_type() == 'P'
            and last_piece.color != self.color
            and last_piece.last_double_move
            and current_row == ep_row
            and last_new_idx[0] == target_col
            and last_new_idx[1] == ep_row
        )
