import random

class HangmanGame:
    def __init__(self, records):
        self.records = records
        self.words = ["python","apple","banana","school","computer"]
        self.answer = random.choice(self.words)
        self.new_answer = ["_"]*len(self.answer)
        self.life = 5
        self.used = []
        self.count = 0
    
    def show_answer(self):
        for i in range(len(self.new_answer)):
            print(self.new_answer[i], end="")
        print(self.answer) #test용

    def guess(self):
        while True:
            g = input("알파벳을 입력하세요.")
            g = g.lower()
                    
            if len(g) != 1:
                print("한 글자만 입력해주세요.")
            elif g.isalpha() == False:
                print("알파벳만 입력해주세요.")
            elif g in self.used:
                print("이미 입력한 글자입니다.")
            else:
                self.used.append(g)
                return g
    
    def play(self):
        while self.life > 0:
            self.show_answer()

            g = self.guess()
            self.count += 1

            if g in self.answer:
                for i in range(len(self.answer)):
                    if g == self.answer[i]:
                        self.new_answer[i] = g

                print(f"남은 기회: {self.life}")
                print(f"입력한 글자: {g}")
            
                if "_" not in self.new_answer:
                    print("정답입니다!")
                    print(f"시도횟수: {self.count}회")

                    user_id = input("닉네임을 입력해주세요: ")
                    self.records.append([self.count, user_id])
                    self.records.sort()
                    return                
            else:
                self.life -= 1
                print("틀렸습니다.")
                print(f"남은 기회: {self.life}")
                print(f"입력한 글자: {g}")
    
        print("Game over")
        print(f"정답은 {self.answer}였습니다.")