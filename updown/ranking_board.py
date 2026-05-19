class RankingBoard:
    def __init__(self):
        self.record = []
    
    def add_record(self, nickname, tries):
        record ={"name": nickname, "tries": tries}
        self.record.append(record)
    
    def show_ranking(self):
        if len(self.record) == 0:
            print("등록된 기록이 없음")
            return
        
        self.record.sort(key=lambda x: (x["tries"], x["name"]))

        print("----명예의 전당----")

        for i in range(min(3,len(self.record))):
            print(f"{i+1}위 {self.record[i]['name']} {self.record[i]['tries']}회")