
"""
Should know its current position, and should know in what direction it is moving. 
It should be able to move forward, turn left, and turn right. 
It should also have an action invoked when it looses the game, and one when it wins.
"""
class Bird:
    def __init__(self, current_pos, direction):
        self.current_pos = current_pos
        self.direction = direction

    def move(self, commands):
        for i in commands:
            if i != 'f':
                self.set_direction(i)
            else:
                if self.direction == 'right':
                    self.current_pos["col"] += 1
                elif self.direction == 'left':
                    self.current_pos["col"] -= 1
                elif self.direction == 'down':
                    self.current_pos["row"] += 1
                else:
                    self.current_pos["row"] -= 1      

    def set_direction(self, direction):
        if direction == 'r':
            if self.direction == 'right':
                self.direction = 'down'
            elif self.direction == 'down':
                self.direction = 'left'
            elif self.direction == 'left':
                self.direction = 'up'
            else:
                self.direction = 'right'
        elif direction == 'l':
            if self.direction == 'right':
                self.direction = 'up'
            elif self.direction == 'up':
                self.direction = 'left'
            elif self.direction == 'left':
                self.direction = 'down'
            else:
                self.direction = 'right'

"""
Should know its position. 
It should also have an action invoked when it looses the game, and one when it wins.
"""
class Pig:
    def __init__(self, pos):
        self.pos = pos


"""
Should initialize a Bird and a Pig object. 
It should display the board with the bird and the pig in starting positions. 
It should have a run method
"""
class Board:
    def __init__(self):
        self.bird = Bird({ "row": 2, "col": 2 }, 'right')
        self.pig = Pig({ "row": 7, "col": 6 })
        self.board = [ (i, j) for i in range(10) for j in range(10) ]

    def display(self):
        for i in range(10):
            for j in range(10):
                if self.bird.current_pos["row"] == i and self.bird.current_pos["col"] == j:
                    print('B', end='  ')
                elif self.pig.pos["row"] == i and self.pig.pos["col"] == j:
                    print('P', end='  ')
                else:
                    print('*', end='  ')
            print()


"""
Should have a display method printing out instructions on what to do. 
It should have a method being responsible of creating a collection of commands from user input.
"""
class Workspace:
    def __init__(self):
        pass

    def display_instructions(self, bird):
        #print(f"Bird's current direction: {bird.direction}")
        print(f'What steps do you want to perform?', 
        '\nOptions: move forward (F), change direction: (L / R).',
        '\nType "Q" when finished')

    def collect_user_commands(self):
        return input('Move: ').split(' ')


"""
This class is responsible of running the application. 
It should create objects of Board and Workspace and call their display methods. 
It should also be responsible for deciding if the bird hit the pig or not.
"""
class Game:
    def __init__(self):
        self.board = Board()
        self.workspace = Workspace()
        self.gameOver = False

    def run(self):
        self.board.display()
        self.workspace.display_instructions(self.board.bird)
        self.gameLoop()

    def gameLoop(self):
        gameOver = False
        while gameOver != True:
            commands = self.workspace.collect_user_commands()
            self.board.bird.move(commands)
            gameOver = self.check_for_win()
            #self.board.display()
            #self.workspace.display_instructions(self.board.bird)

    def check_for_win(self):
        if self.board.bird.current_pos == self.board.pig.pos:
            print('Bird won! Game over.')
            print(f"Bird's position: {game.board.bird.current_pos} Pig's position: {game.board.pig.pos}")
            return True
        else:
            return False


game = Game()
game.run()