from board import Board
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
import os


class Game:
    def __init__(self):
        self.board = Board()
        self.move_history = []
        self.notation_history = []  # Novo histórico em notação de xadrez
        self.current_turn = 'white'
        self.last_move = None  # Rastreia último movimento (piece, old_pos, new_pos)
        self.move_stack = []  # Pilha para rastrear movimentos e estado para undo
    
    def new_game(self):
        self._place_pawns()
        self._place_pieces()
    
    def _place_pawns(self):
        for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            white_pawn = Pawn('white', f'{col}2')
            black_pawn = Pawn('black', f'{col}7')
            self.board.place_piece(white_pawn, f'{col}2')
            self.board.place_piece(black_pawn, f'{col}7')
    
    def _place_pieces(self):
        white_pieces = [
            (Rook, 'a1'), (Knight, 'b1'), (Bishop, 'c1'), 
            (Queen, 'd1'), (King, 'e1'), (Bishop, 'f1'), 
            (Knight, 'g1'), (Rook, 'h1')
        ]
        
        black_pieces = [
            (Rook, 'a8'), (Knight, 'b8'), (Bishop, 'c8'), 
            (Queen, 'd8'), (King, 'e8'), (Bishop, 'f8'), 
            (Knight, 'g8'), (Rook, 'h8')
        ]
        
        for piece_class, position in white_pieces:
            piece = piece_class('white', position)
            self.board.place_piece(piece, position)
        
        for piece_class, position in black_pieces:
            piece = piece_class('black', position)
            self.board.place_piece(piece, position)
    
    def display_board(self):
        print("\nChess Game")
        print(f"Current Turn: \033[93m{self.current_turn.upper()}\033[0m" if self.current_turn == 'black' else f"Current Turn: {self.current_turn.upper()}")
        
        # Avisa se o rei está em cheque
        if self._is_king_in_check(self.current_turn):
            print("\033[91m⚠️  CHECK! Your king is under attack!\033[0m")
        
        print("   —————————————————")
        for row in range(7, -1, -1):
            print(f"{row + 1} | ", end="")
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece:
                    if piece.color == 'black':
                        print(f"\033[93m{piece.get_type()}\033[0m ", end="")
                    else:
                        print(f"{piece.get_type()} ", end="")
                else:
                    print(". ", end="")
            print(f"| ")
        print("   —————————————————")
        print("    a b c d e f g h  \n")
    
    def _find_pieces_by_type_and_color(self, piece_type: str, color: str) -> list:
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece and piece.get_type() == piece_type and piece.color == color:
                    pieces.append(piece)
        return pieces
    
    def _find_pieces_that_can_move(self, piece_type: str, destination: str, 
                                   source_col: str = None, color: str = 'white') -> list:
        candidates = self._find_pieces_by_type_and_color(piece_type, color)
        valid_pieces = []
        
        for piece in candidates:
            if source_col and piece.column != source_col:
                continue
            
            # Para peões, passa o último movimento
            if piece_type == 'P':
                valid_destinations = piece.valid_moves(self.board, self.last_move)
            else:
                valid_destinations = piece.valid_moves(self.board)
            
            for dest in valid_destinations:
                dest_str = f"{dest[0]}{dest[1]}"
                if dest_str == destination:
                    valid_pieces.append(piece)
        
        return valid_pieces
    
    def _is_position_attacked(self, position: str, by_color: str) -> bool:
        """
        Verifica se uma posição está sendo atacada por uma peça da cor especificada.
        """
        # Encontra todas as peças da cor especificada
        attacking_pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece and piece.color == by_color:
                    attacking_pieces.append(piece)
        
        # Para cada peça, verifica se pode atacar a posição
        for piece in attacking_pieces:
            if piece.get_type() == 'P':
                # Peões têm lógica especial de ataque
                valid_moves = piece.valid_moves(self.board, self.last_move)
            else:
                valid_moves = piece.valid_moves(self.board)
            
            for move in valid_moves:
                move_str = f"{move[0]}{move[1]}"
                if move_str == position:
                    return True
        
        return False
    
    def _is_king_in_check(self, color: str) -> bool:
        """
        Verifica se o rei da cor especificada está em cheque.
        """
        # Encontra o rei
        king = None
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece and piece.get_type() == 'K' and piece.color == color:
                    king = piece
                    break
            if king:
                break
        
        if not king:
            return False
        
        king_pos = f"{king.column}{king.row}"
        opponent_color = 'black' if color == 'white' else 'white'
        
        # Verifica se a posição do rei está sendo atacada
        return self._is_position_attacked(king_pos, opponent_color)
    
    def undo_move(self):
        """
        Desfaz o último movimento.
        """
        if not self.move_stack:
            print("No moves to undo.")
            return
        
        # Remove o último movimento
        move_data = self.move_stack.pop()
        piece = move_data['piece']
        old_pos = move_data['old_pos']
        new_pos = move_data['new_pos']
        captured_piece = move_data['captured_piece']
        pawn_states = move_data['pawn_states']
        king_rook_states = move_data['king_rook_states']
        
        col_idx, row_idx = new_pos
        old_col_idx, old_row_idx = old_pos
        
        # Move a peça de volta para a posição original
        self.board.grid[row_idx][col_idx] = None
        piece.column = list(self.board.COLUMN_MAP.keys())[old_col_idx]
        piece.row = str(old_row_idx + 1)
        self.board.grid[old_row_idx][old_col_idx] = piece
        
        # Restaura peça capturada, se houver
        if captured_piece:
            self.board.grid[row_idx][col_idx] = captured_piece
        
        # Restaura booleanos de peões
        if pawn_states:
            piece.first_move = pawn_states['first_move']
            piece.last_double_move = pawn_states['last_double_move']
        
        # Restaura booleanos de rei e torres
        if king_rook_states:
            piece.has_moved = king_rook_states['has_moved']
        
        # Remove do histórico de notação
        if self.notation_history:
            if self.notation_history[-1][2] is not None:
                # Último movimento foi de black, remove ele
                self.notation_history[-1][2] = None
            else:
                # Último movimento foi de white, remove toda a entrada
                self.notation_history.pop()
        
        # Remove do histórico detalhado
        if self.move_history:
            self.move_history.pop()
        
        # Volta para o turno anterior
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        
        # Reseta last_move
        if self.move_stack:
            last = self.move_stack[-1]
            self.last_move = (last['piece'], last['old_pos'], last['new_pos'])
        else:
            self.last_move = None
        
        self.clear_screen()
        self.display_board()
        print("Move undone!")
    
    def _is_move_legal(self, piece, destination: str, old_pos: str) -> bool:
        """
        Verifica se um movimento é legal simulando-o e checando se deixa o rei em cheque.
        Retorna True se o movimento é legal (não deixa o rei em cheque).
        """
        # Salva o estado atual
        target_piece = self.board.get_piece(destination)
        
        # Simula o movimento
        self.board.remove_piece(old_pos)
        old_column = piece.column
        old_row = piece.row
        piece.column = destination[0].lower()
        piece.row = destination[1]
        if target_piece:
            self.board.grid[int(destination[1]) - 1][self.board.COLUMN_MAP[destination[0]]] = None
        self.board.grid[int(destination[1]) - 1][self.board.COLUMN_MAP[destination[0]]] = piece
        
        # Verifica se o rei continua em cheque
        king_still_in_check = self._is_king_in_check(self.current_turn)
        
        # Restaura o estado
        piece.column = old_column
        piece.row = old_row
        self.board.grid[int(old_pos[1]) - 1][self.board.COLUMN_MAP[old_pos[0]]] = piece
        self.board.grid[int(destination[1]) - 1][self.board.COLUMN_MAP[destination[0]]] = target_piece
        
        # O movimento é legal se o rei não fica em cheque após o movimento
        return not king_still_in_check
    
    def _is_checkmate(self) -> bool:
        """
        Verifica se é checkmate.
        O rei está em cheque E não há nenhum movimento legal disponível.
        """
        if not self._is_king_in_check(self.current_turn):
            return False
        
        # Tenta encontrar qualquer movimento legal
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece and piece.color == self.current_turn:
                    if piece.get_type() == 'P':
                        valid_moves = piece.valid_moves(self.board, self.last_move)
                    else:
                        valid_moves = piece.valid_moves(self.board)
                    
                    for move in valid_moves:
                        move_str = f"{move[0]}{move[1]}"
                        old_pos = f"{piece.column}{piece.row}"
                        if self._is_move_legal(piece, move_str, old_pos):
                            return False  # Encontrou um movimento legal
        
        return True  # Nenhum movimento legal encontrado
    
    def _can_castle(self, king_direction: str) -> bool:
        """
        Verifica se é possível fazer castling (roque).
        king_direction: 'kingside' (lado do rei) ou 'queenside' (lado da rainha)
        Retorna True se o castling é legal.
        """
        # Encontra o rei
        king = None
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece and piece.get_type() == 'K' and piece.color == self.current_turn:
                    king = piece
                    break
            if king:
                break
        
        if not king or king.has_moved:
            return False
        
        # Rei não pode estar em cheque
        if self._is_king_in_check(self.current_turn):
            return False
        
        king_col_idx = self.board.COLUMN_MAP[king.column]
        king_row_idx = int(king.row) - 1
        
        if king_direction == 'kingside':
            # Castling para o lado do rei (h-file)
            rook_col_idx = 7  # coluna h
            castle_col_idx = 6  # coluna g (onde o rei vai)
            rook_final_col_idx = 5  # coluna f (onde a torre vai)
        else:  # queenside
            # Castling para o lado da rainha (a-file)
            rook_col_idx = 0  # coluna a
            castle_col_idx = 2  # coluna c (onde o rei vai)
            rook_final_col_idx = 3  # coluna d (onde a torre vai)
        
        # Procura a torre
        rook = self.board.grid[king_row_idx][rook_col_idx]
        if not rook or rook.get_type() != 'R' or rook.color != self.current_turn or rook.has_moved:
            return False
        
        # Verifica se o caminho está livre
        start = min(king_col_idx, rook_col_idx)
        end = max(king_col_idx, rook_col_idx)
        for col in range(start + 1, end):
            if self.board.grid[king_row_idx][col] is not None:
                return False
        
        # Verifica se as casas pelas quais o rei passa não estão sob ataque
        opponent_color = 'black' if self.current_turn == 'white' else 'white'
        
        # Verifica a posição atual do rei (já confirmada acima)
        # Verifica a posição intermediária (se houver)
        intermediate_col_letter = list(self.board.COLUMN_MAP.keys())[
            (king_col_idx + castle_col_idx) // 2
        ]
        intermediate_pos = f"{intermediate_col_letter}{king.row}"
        if self._is_position_attacked(intermediate_pos, opponent_color):
            return False
        
        # Verifica a posição final do rei
        final_col_letter = list(self.board.COLUMN_MAP.keys())[castle_col_idx]
        final_pos = f"{final_col_letter}{king.row}"
        if self._is_position_attacked(final_pos, opponent_color):
            return False
        
        return True
    
    def _calculate_distance(self, pos1: tuple, pos2: tuple) -> float:
        """Calcula a distância euclidiana entre duas posições (col_idx, row_idx)"""
        return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5
    
    def _position_to_coords(self, position: str) -> tuple:
        """Converte posição como 'e4' para índices (col_idx, row_idx)"""
        col_idx = self.board.COLUMN_MAP[position[0].lower()]
        row_idx = int(position[1]) - 1
        return (col_idx, row_idx)
    
    def _perform_castling(self, direction: str):
        """
        Executa o castling.
        direction: 'kingside' ou 'queenside'
        """
        # Encontra o rei
        king = None
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece and piece.get_type() == 'K' and piece.color == self.current_turn:
                    king = piece
                    break
            if king:
                break
        
        king_col_idx = self.board.COLUMN_MAP[king.column]
        king_row_idx = int(king.row) - 1
        
        if direction == 'kingside':
            rook_col_idx = 7
            castle_col_idx = 6
            rook_final_col_idx = 5
        else:
            rook_col_idx = 0
            castle_col_idx = 2
            rook_final_col_idx = 3
        
        # Move o rei
        rook = self.board.grid[king_row_idx][rook_col_idx]
        
        king.column = list(self.board.COLUMN_MAP.keys())[castle_col_idx]
        king.row = str(king_row_idx + 1)
        king.has_moved = True
        self.board.grid[king_row_idx][king_col_idx] = None
        self.board.grid[king_row_idx][castle_col_idx] = king
        
        # Move a torre
        rook.column = list(self.board.COLUMN_MAP.keys())[rook_final_col_idx]
        rook.row = str(king_row_idx + 1)
        rook.has_moved = True
        self.board.grid[king_row_idx][rook_col_idx] = None
        self.board.grid[king_row_idx][rook_final_col_idx] = rook
        
        print(f"Castling {direction}!")
        
        # Adiciona ao histórico
        if direction == 'kingside':
            notation = 'O-O'
        else:
            notation = 'O-O-O'
        
        if self.current_turn == 'white':
            completed_pairs = len([m for m in self.notation_history if m[2] is not None])
            move_count = completed_pairs + 1
            self.notation_history.append([move_count, notation, None])
        else:
            if self.notation_history:
                self.notation_history[-1][2] = notation
        
        self.move_history.append(f"K{notation}")
        
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        
        self.clear_screen()
        self.display_board()
        
        # Verifica checkmate
        if self._is_checkmate():
            print(f"\033[91m╔════════════════════════════════════╗\033[0m")
            print(f"\033[91m║     CHECKMATE! {self.current_turn.upper()} LOSES!    ║\033[0m")
            print(f"\033[91m╚════════════════════════════════════╝\033[0m")
    
    def _find_closest_pawn(self, destination: str, color: str) -> 'Pawn':
        """Encontra o peão mais próximo que pode se mover para o destino"""
        pawns = self._find_pieces_by_type_and_color('P', color)
        dest_coords = self._position_to_coords(destination)
        
        valid_pawns = []
        for pawn in pawns:
            valid_destinations = pawn.valid_moves(self.board, self.last_move)
            for dest in valid_destinations:
                dest_str = f"{dest[0]}{dest[1]}"
                if dest_str == destination:
                    pawn_coords = self._position_to_coords(f"{pawn.column}{pawn.row}")
                    distance = self._calculate_distance(pawn_coords, dest_coords)
                    valid_pawns.append((distance, pawn))
        
        if not valid_pawns:
            return None
        
        # Retorna o peão mais próximo
        valid_pawns.sort(key=lambda x: x[0])
        return valid_pawns[0][1]
    
    def _is_coordinate(self, move_input: str) -> bool:
        """Verifica se a entrada é apenas uma coordenada (2-3 caracteres sem maiúsculas)"""
        # Remove espaços e verifica o tamanho
        move_input = move_input.strip()
        if len(move_input) < 2 or len(move_input) > 3:
            return False
        
        # Verifica se não tem letras maiúsculas
        if move_input != move_input.lower():
            return False
        
        # Verifica se é formato válido: letra + número (+ número)
        if move_input[0] not in 'abcdefgh':
            return False
        
        if move_input[1] not in '12345678':
            return False
        
        if len(move_input) == 3 and move_input[2] not in '12345678':
            return False
        
        return True
    
    def _get_move_notation(self, piece: 'Piece', destination: str, is_capture: bool = False, origin_pos: str = None) -> str:
        """Converte um movimento para notação de xadrez padrão"""
        piece_type = piece.get_type()
        
        # Para peões, usa a coluna de ORIGEM se for captura
        if piece_type == 'P':
            if is_capture:
                origin_col = origin_pos[0] if origin_pos else piece.column
                return f"{origin_col}x{destination}"
            else:
                return destination
        
        # Para outras peças, começa com a letra da peça
        notation = piece_type
        
        # Verifica se há múltiplas peças do mesmo tipo que podem se mover para este destino
        same_type_pieces = self._find_pieces_by_type_and_color(piece_type, piece.color)
        
        # Conta quantas peças do mesmo tipo podem se mover para este destino
        pieces_that_can_move = []
        for candidate in same_type_pieces:
            if candidate != piece:
                valid_destinations = candidate.valid_moves(self.board)
                for dest in valid_destinations:
                    dest_str = f"{dest[0]}{dest[1]}"
                    if dest_str == destination:
                        pieces_that_can_move.append(candidate)
        
        # Se há outras peças que podem se mover para o mesmo destino, adiciona a coluna
        if pieces_that_can_move:
            notation += piece.column
        
        if is_capture:
            notation += 'x'
        
        notation += destination
        
        return notation
    
    def play_move(self, move_input: str):
        move_input = move_input.strip().lower()
        
        # Verifica comando de castling
        if move_input == 'o-o':
            # Castling kingside
            if self._can_castle('kingside'):
                self._perform_castling('kingside')
            else:
                print("Castling kingside is not legal.")
            return
        elif move_input == 'o-o-o':
            # Castling queenside
            if self._can_castle('queenside'):
                self._perform_castling('queenside')
            else:
                print("Castling queenside is not legal.")
            return
        
        # Verifica se é apenas uma coordenada (2-3 caracteres, sem maiúsculas)
        if self._is_coordinate(move_input):
            destination = move_input
            closest_pawn = self._find_closest_pawn(destination, self.current_turn)
            
            if not closest_pawn:
                print(f"No pawn can move to {destination}")
                return
            
            piece = closest_pawn
            old_pos = f"{piece.column}{piece.row}"
            
            # Valida se o movimento é legal (não deixa o rei em cheque)
            if not self._is_move_legal(piece, destination, old_pos):
                if self._is_king_in_check(self.current_turn):
                    print(f"Illegal move! Your king is in check and this move doesn't resolve it.")
                else:
                    print(f"Illegal move! This move would put your king in check.")
                return
        else:
            # Processamento normal para notação de peças
            if len(move_input) == 3:
                piece_type, destination = move_input[0].upper(), move_input[1:3]
            elif len(move_input) == 4:
                piece_type, source_col, dest_row = move_input[0].upper(), move_input[1], move_input[2:4]
                destination = move_input[2:4]
            elif len(move_input) == 5:
                piece_type = move_input[0].upper()
                source_col = move_input[1]
                destination = move_input[3:5]
            else:
                print("Invalid format. Use: Pf4 (piece+destination), e4 (coordinate), or Rab1 (piece+column+destination)")
                return
            
            source_col_param = move_input[1] if len(move_input) >= 4 else None
            
            candidates = self._find_pieces_that_can_move(piece_type, destination, source_col_param, self.current_turn)
            
            if not candidates:
                print(f"No {piece_type} can move to {destination}")
                return
            
            if len(candidates) > 1:
                print(f"Ambiguous move! Multiple {piece_type} can move to {destination}")
                print("Specify by column: e.g., Rab1 (Rook from column a to b1)")
                return
            
            piece = candidates[0]
            old_pos = f"{piece.column}{piece.row}"
        
        # Valida se o movimento é legal (não deixa o rei em cheque)
        if not self._is_move_legal(piece, destination, old_pos):
            if self._is_king_in_check(self.current_turn):
                print(f"Illegal move! Your king is in check and this move doesn't resolve it.")
            else:
                print(f"Illegal move! This move would put your king in check.")
            return
        
        # Verifica en passant (remoção de peão na diagonal)
        is_en_passant = False
        if piece.get_type() == 'P':
            old_col_idx = self.board.COLUMN_MAP[piece.column]
            old_row_idx = int(piece.row) - 1
            new_col_idx = self.board.COLUMN_MAP[destination[0]]
            new_row_idx = int(destination[1]) - 1
            
            # Se a coluna mudou mas não há peça no destino, é en passant
            if old_col_idx != new_col_idx and self.board.get_piece(destination) is None:
                is_en_passant = True
                # Remove o peão capturado (está na mesma fileira que o peão que está capturando)
                en_passant_pos = f"{destination[0]}{piece.row}"
                en_passant_piece = self.board.get_piece(en_passant_pos)
                if en_passant_piece:
                    print(f"En passant! Captured {en_passant_piece.color} {en_passant_piece.get_type()} at {en_passant_pos}")
                    self.board.remove_piece(en_passant_pos)
        
        target_piece = self.board.get_piece(destination)
        is_capture = target_piece is not None or is_en_passant
        
        if target_piece:
            print(f"Captured {target_piece.color} {target_piece.get_type()} at {destination}")
            self.board.remove_piece(destination)
        
        self.board.remove_piece(old_pos)
        self.board.place_piece(piece, destination)
        print(f"Moved {self.current_turn} {piece.get_type()} from {old_pos} to {destination}")
        
        # Atualiza booleanos has_moved para rei e torres
        if piece.get_type() == 'K':
            piece.has_moved = True
        elif piece.get_type() == 'R':
            piece.has_moved = True
        
        # Verifica e atualiza booleanos de peões
        if piece.get_type() == 'P':
            # Detecta se foi um pulo duplo
            old_row_idx = int(old_pos[1]) - 1
            new_row_idx = int(destination[1]) - 1
            distance = abs(new_row_idx - old_row_idx)
            
            piece.last_double_move = (distance == 2)
            piece.first_move = False
        
        # Reinicia o last_double_move para outros peões do adversário
        opponent_color = 'black' if self.current_turn == 'white' else 'white'
        opponent_pawns = self._find_pieces_by_type_and_color('P', opponent_color)
        for pawn in opponent_pawns:
            if pawn != piece:  # Não reinicia o peão que acabou de se mover
                pawn.last_double_move = False
        
        # Gera notação de xadrez
        move_notation = self._get_move_notation(piece, destination, is_capture, old_pos)
        
        # Adiciona ao novo histórico
        if self.current_turn == 'white':
            # Calcula o número do movimento (quantos pares completos já existem + 1)
            completed_pairs = len([m for m in self.notation_history if m[2] is not None])
            move_count = completed_pairs + 1
            self.notation_history.append([move_count, move_notation, None])
        else:
            # Adiciona o movimento do black ao último par
            if self.notation_history:
                self.notation_history[-1][2] = move_notation
        
        # Adiciona ao histórico antigo (mantém compatibilidade)
        move_notation_old = f"{piece.get_type()}{old_pos}-{destination}"
        self.move_history.append(move_notation_old)
        
        # Rastreia o último movimento (para undo)
        old_pos_tuple = (self.board.COLUMN_MAP[old_pos[0]], int(old_pos[1]) - 1)
        new_pos_tuple = (self.board.COLUMN_MAP[destination[0]], int(destination[1]) - 1)
        self.last_move = (piece, old_pos_tuple, new_pos_tuple)
        
        # Adiciona ao move_stack para undo
        # Salva informações dos booleanos antes de serem alterados
        pawn_states = {}
        if piece.get_type() == 'P':
            pawn_states['first_move'] = piece.first_move
            pawn_states['last_double_move'] = piece.last_double_move
        king_rook_states = {}
        if piece.get_type() in ['K', 'R']:
            king_rook_states['has_moved'] = piece.has_moved
        
        self.move_stack.append({
            'piece': piece,
            'old_pos': old_pos_tuple,
            'new_pos': new_pos_tuple,
            'captured_piece': target_piece,
            'pawn_states': pawn_states,
            'king_rook_states': king_rook_states
        })
        
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        
        self.clear_screen()
        self.display_board()
        
        # Verifica checkmate
        if self._is_checkmate():
            print(f"\033[91m╔════════════════════════════════════╗\033[0m")
            print(f"\033[91m║     CHECKMATE! {self.current_turn.upper()} LOSES!    ║\033[0m")
            print(f"\033[91m╚════════════════════════════════════╝\033[0m")
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_history(self):
        if not self.move_history and not self.notation_history:
            print("No moves yet.")
            return
        
        print("\n" + "="*50)
        print("MOVE HISTORY (Chess Notation)")
        print("="*50)
        if self.notation_history:
            for move_data in self.notation_history:
                move_num, white_move, black_move = move_data
                if black_move:
                    print(f"{move_num}. {white_move} {black_move}")
                else:
                    print(f"{move_num}. {white_move}")
        else:
            print("No moves yet.")
        
        print("\n" + "="*50)
        print("DETAILED MOVE HISTORY")
        print("="*50)
        if self.move_history:
            for i, move in enumerate(self.move_history, 1):
                print(f"{i}. {move}")
        else:
            print("No moves yet.")
        print()