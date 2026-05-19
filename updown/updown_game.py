import random

class UpDownGame:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.target = random.randint(start,end)
        self.tries = 0
    
    def input_number(self):
        while True:
            try:
                number = int(input("숫자를 입력하세요: "))
                return number
            except ValueError:
                print("숫자만 입력해주세요.")
    
    def give_hint(self,guess):
        if guess < self.target:
            print(f"높게 입력하세요! 남은 횟수 {5-self.tries}번")
        elif guess > self.target:
            print(f"낮게 입력하세요! 남은 횟수 {5-self.tries}번")
    
    def give_extra_hint(self,guess):
        difference = abs(self.target - guess)

        if difference <= 5:
            print("HINT: 거의 다 왔습니다!")
        elif difference <= 10:
            print("HINT: 가까워지고 있습니다.")
        else:
            print("HINT: 아직 멀었습니다.")
    
    def play(self):
        print(f"{self.start}부터 {self.end}사이의 숫자를 맞춰보세요.")
        print(self.target) #test용
    
        while self.tries < 5:
            guess = self.input_number()
            self.tries += 1

            if guess == self.target:
                print(f"정답입니다!")
                nickname = input("닉네임을 입력해주세요: ")
                return nickname, self.tries
            
            self.give_hint(guess)
            self.give_extra_hint(guess)
        
        print(f"실패입니다. 정답은 {self.target}였습니다.")
        return None, self.tries