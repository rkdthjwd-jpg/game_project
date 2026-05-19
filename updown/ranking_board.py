class RankingBoard:
    def __init__(self):
        self.record = {
            "updown": [],
            "hangman": []
        }
    
    def add_record(self, game_name, nickname, tries):
        record ={"name": nickname, "tries": tries}
        self.record[game_name].append(record)
    
    def show_ranking(self, game_name):
        if len(self.record[game_name]) == 0:
            print("등록된 기록이 없음")
            return
        
        self.record[game_name].sort(key=lambda x: (x["tries"], x["name"]))

        print("----명예의 전당----")
        
        rank = 1

        for i in range(len(self.record[game_name])):
            if i > 0:
                if self.record[game_name][i]["tries"] > self.record[game_name][i-1]["tries"]:
                    rank = i + 1

            if i < 3:
                print(f"{rank}위 {self.record[game_name][i]['name']} {self.record[game_name][i]['tries']}회")