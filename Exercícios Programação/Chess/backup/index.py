from game import Game


game = Game()
game.new_game()
game.display_board()

while True:
    move = input("Enter move (e4, Nf3, O-O, 'h' for history, 'u' for undo, 'exit' to quit): \n").strip()
    
    if move.lower() == 'exit':
        break
    elif move.lower() == 'h':
        game.show_history()
    elif move.lower() == 'u':
        game.undo_move()
    else:
        game.play_move(move)