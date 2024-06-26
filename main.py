from game import Game

game = Game(title='Ultimate Breakout', size=(800, 600), bg='black')
game.play_game()
game.screen.exitonclick()