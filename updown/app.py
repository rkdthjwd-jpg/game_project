from .config import ADMIN_ID, ADMIN_PW, MAX_LOGIN_ATTEMPTS
from .login_manager import LoginManager
from .ranking_board import RankingBoard
from .updown_game import UpDownGame
from .hangman_game import HangmanGame

class App:
    def __init__(self):
        self.login_manager = LoginManager(ADMIN_ID, ADMIN_PW, MAX_LOGIN_ATTEMPTS)
        self.ranking_board = RankingBoard()
    
    def print_menu(self):
        print("1.게임시작")
        print("2.랭킹보기")
        print("3.게임종료")
    
    def print_game_menu(self):
        print("1.UpDownGame")
        print("2.HangmanGame")

    def input_menu(self):
        while True:
            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu
            except ValueError:
                print("숫자만 입력해주세요.")
    
    def input_game_menu(self):
        while True:
            try:
                game_menu = int(input("게임을 선택하세요: "))
                return game_menu
            except ValueError:
                print("숫자만 입력해주세요.")

    def start(self):
        if not self.login_manager.login():
            return
        while True:
            self.print_menu()
            menu = self.input_menu()

            if menu == 1:
                while True:
                    self.print_game_menu()
                    game_menu = self.input_game_menu()

                    if game_menu == 1:
                        game = UpDownGame()
                        nickname, tries = game.play()
                        self.ranking_board.add_record(nickname, tries)
                        break

                    elif game_menu == 2:
                        game = HangmanGame()

            elif menu == 2:
                self.ranking_board.show_ranking()
            
            elif menu == 3:
                print("프로그램을 종료합니다.")
            
            else:
                print("잘못된 메뉴입니다.")