class Game:
    def __init__(self, n, territory):
        self.__n = n
        self.__territory = territory
        self.__snake_pos = self.search_matrix(self.__territory, 'S')
        self.game_over = False
        self.food_quantity = 0
        self.ops = {
            'up': lambda: self.move(-1, 0),
            'down': lambda: self.move(1, 0),
            'left': lambda: self.move(0, -1),
            'right': lambda: self.move(0, 1),
        }

    def move(self, dy, dx):
        y, x = self.__snake_pos
        self.__territory[y][x] = '.'
        new_y = y + dy
        new_x = x + dx
        if new_y > (self.__n - 1) or new_y < 0 or new_x > (self.__n - 1) or new_x < 0:
            self.game_over = True
            return
        at_pos = self.__territory[new_y][new_x]
        if at_pos == 'B':
            self.__territory[new_y][new_x] = '.'
            new_y, new_x = self.search_matrix(self.__territory, 'B')
        elif at_pos == '*':
            self.food_quantity += 1
            if self.food_quantity == 10:
                self.game_over = True
        self.__territory[new_y][new_x] = 'S'
        self.__snake_pos = (new_y, new_x)

    def print_territory(self):
        print('\n'.join([''.join(row) for row in self.__territory]))

    def play(self):
        while not self.game_over:
            command = input()
            move_fn = self.ops[command]
            move_fn()

    def print_stats(self):
        if self.game_over and self.food_quantity < 10:
            print("Game over!")
        else:
            print("You won! You fed the snake.")
        print(f'Food eaten: {self.food_quantity}')
        self.print_territory()

    @staticmethod
    def search_matrix(matrix, search):
        for y, row in enumerate(matrix):
            for x, char in enumerate(row):
                if char == search:
                    return y, x


n = int(input())
territory = [list(input()) for _ in range(n)]

game = Game(n, territory)
game.play()
game.print_stats()