class LoginManager:
    def __init__(self, correct_id, correct_pw, max_attempts):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts

    def login(self):
        for count in range(self.max_attempts):
            user_id = input("ID 입력: ")
            user_pw = input("PW 입력: ")

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 완료")
                return True
            else:
                print(f"ID, PW를 다시 입력해주세요. 남은 횟수: {self.max_attempts-count-1}회")

        print("계정이 잠금되었습니다.")
        return False
