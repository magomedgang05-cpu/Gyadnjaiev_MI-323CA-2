import random

class TicTacToe:
    def __init__(self, vs_computer=False):

        self.field = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.vs_computer = vs_computer
        self.moves_count = 0

        print("    0   1   2")
        print("  ┌───┬───┬───┐")
        
        for i, row in enumerate(self.field):
            print(f"{i} │", end="")
            for j, cell in enumerate(row):
                print(f" {cell} ", end="")
                if j < 2:
                    print("│", end="")
                else:
                    print("│")

            if i < 2:
                print("  ├───┼───┼───┤")
            else:
                print("  └───┴───┴───┘")
    
    def is_valid_move(self, row, col):

        if row < 0 or row > 2 or col < 0 or col > 2:
            return False

        if self.field[row][col] != ' ':
            return False
        
        return True
    
    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        
        self.field[row][col] = self.current_player
        self.moves_count += 1
        return True
    
    def check_winner(self):
        for row in self.field:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.field[0][col] == self.field[1][col] == self.field[2][col] != ' ':
                return self.field[0][col]

        if self.field[0][0] == self.field[1][1] == self.field[2][2] != ' ':
            return self.field[0][0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] != ' ':
            return self.field[0][2]
        
        return None
    
    def check_draw(self):
        return self.moves_count == 9 and self.winner is None
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def computer_move(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == ' ':
                    self.field[i][j] = 'O'
                    if self.check_winner() == 'O':
                        self.field[i][j] = ' '
                        return i, j
                    self.field[i][j] = ' '
        
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == ' ':
                    self.field[i][j] = 'X'
                    if self.check_winner() == 'X':
                        self.field[i][j] = ' '
                        return i, j
                    self.field[i][j] = ' '
        
        if self.field[1][1] == ' ':
            return 1, 1
        
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        empty_corners = [c for c in corners if self.field[c[0]][c[1]] == ' ']
        if empty_corners:
            return random.choice(empty_corners)

        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == ' ':
                    empty_cells.append((i, j))
        
        return random.choice(empty_cells) if empty_cells else None
    
    def get_human_move(self):
        while True:
            try:
                move = input(f"\nИгрок {self.current_player}, введите координаты (строка столбец): ")
                coords = move.split()
                
                if len(coords) != 2:
                    print("Введите два числа через пробел!")
                    continue
                
                row, col = int(coords[0]), int(coords[1])
                
                if self.is_valid_move(row, col):
                    return row, col
                else:
                    print("Недопустимый ход! Попробуйте снова.")
            
            except ValueError:
                print("Введите числа от 0 до 2!")
            except Exception as e:
                print(f"Ошибка: {e}")
    
    def play_turn(self):
        self.print_field()
        
        if self.vs_computer and self.current_player == 'O':
            print("\nХод компьютера (O)...")
            row, col = self.computer_move()
            self.make_move(row, col)
            print(f"Компьютер пошел: {row}, {col}")
        else:
            row, col = self.get_human_move()
            self.make_move(row, col)
        
        self.winner = self.check_winner()
        
        if self.winner:
            self.game_over = True
            self.print_field()
            if self.vs_computer and self.winner == 'O':
                print(f"\n{'='*40}")
                print("Компьютер победил! Попробуйте еще раз!")
                print(f"{'='*40}")
            else:
                print(f"\n{'='*40}")
                print(f"Игрок {self.winner} победил! Поздравляем!")
                print(f"{'='*40}")
        elif self.check_draw():
            self.game_over = True
            self.print_field()
            print(f"\n{'='*40}")
            print("НИЧЬЯ! Игра окончена.")
            print(f"{'='*40}")
        else:
            self.switch_player()
    
    def play_game(self):

        print("\n" + "="*50)
        print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'КРЕСТИКИ-НОЛИКИ'!")
        print("="*50)
        print("Правила:")
        print("- Игроки ходят по очереди")
        print("- Вводите координаты в формате: строка столбец")
        print("- Координаты от 0 до 2")
        print("- Первый игрок: X")
        print("="*50)
        
        if self.vs_computer:
            print("\nРежим: Игра против компьютера")
            print("Вы играете за X, компьютер за O")
        
        while not self.game_over:
            self.play_turn()

def main():
    while True:
        print("\n" + "="*50)
        print("КРЕСТИКИ-НОЛИКИ")
        print("="*50)
        print("1. Играть против другого игрока")
        print("2. Играть против компьютера")
        print("3. Правила игры")
        print("4. Выйти")
        print("="*50)
        
        try:
            choice = int(input("Выберите вариант: "))
            
            if choice == 1:
                game = TicTacToe(vs_computer=False)
                game.play_game()
            elif choice == 2:
                game = TicTacToe(vs_computer=True)
                game.play_game()
            elif choice == 3:
                print("\n" + "="*50)
                print("ПРАВИЛА ИГРЫ:")
                print("="*50)
                print("1. Игровое поле 3x3 клетки")
                print("2. Игроки ходят по очереди")
                print("3. Первый игрок ставит 'X', второй - 'O'")
                print("4. Для хода введите два числа (строка и столбец)")
                print("5. Победит тот, кто первым выстроит 3 своих символа")
                print("   в ряд по горизонтали, вертикали или диагонали")
                print("6. Если все клетки заполнены, но нет победителя - ничья")
                print("="*50)
                
                print("\nПример координат:")
                example = TicTacToe()
                example.print_field()
                print("\nДля хода в центр введите: 1 1")
                print("Для хода в левый верхний угол: 0 0")
                
                input("\nНажмите Enter чтобы вернуться в меню...")
            elif choice == 4:
                print("Спасибо за игру! До свидания!")
                break
            else:
                print("Неверный выбор! Введите число от 1 до 4.")
        
        except ValueError:
            print("Ошибка! Введите число.")

def simple_tic_tac_toe():

    print("\n" + "="*40)
    print("ПРОСТЫЕ КРЕСТИКИ-НОЛИКИ")
    print("="*40)
    
    field = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    moves = 0
    
    def print_simple_field():
        print("\n  0 1 2")
        for i, row in enumerate(field):
            print(f"{i} {' '.join(row)}")
    
    def check_simple_winner():
        for row in field:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if field[0][col] == field[1][col] == field[2][col] != ' ':
                return field[0][col]

        if field[0][0] == field[1][1] == field[2][2] != ' ':
            return field[0][0]
        if field[0][2] == field[1][1] == field[2][0] != ' ':
            return field[0][2]
        
        return None

    while True:
        print_simple_field()

        try:
            move = input(f"\nИгрок {current_player}, введите координаты (строка столбец): ")
            row, col = map(int, move.split())

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Координаты должны быть от 0 до 2!")
                continue
            
            if field[row][col] != ' ':
                print("Клетка уже занята!")
                continue

            field[row][col] = current_player
            moves += 1

            winner = check_simple_winner()
            if winner:
                print_simple_field()
                print(f"Игрок {winner} победил!")
                break
            
            if moves == 9:
                print_simple_field()
                print("Ничья!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        except ValueError:
            print("Ошибка ввода! Введите два числа через пробел.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    print("╔" + "═" * 50 + "╗")
    print("║" + "КРЕСТИКИ-НОЛИКИ".center(50) + "║")
    print("╚" + "═" * 50 + "╝")

    print("Выберите версию игры:")
    print("1.Меню с игой против ПК и юзера")
    print("2.Только два игрока")
    
    try:
        version = int(input("Ваш выбор (1 или 2): "))
        
        if version == 1:
            main()
        elif version == 2:
            simple_tic_tac_toe()
        else:
            print("Неверный выбор! Запускаю полную версию...")
            main()
    
    except ValueError:
        print("Ошибка! Запускаю полную версию...")
        main()