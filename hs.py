# Works

class Game:
    def __init__(self, name):
        self.name = name
        self.scores = []
        
    def add_score(self, score):
        self.scores.append(score)

    def highscore(self):
        listSorted = sorted(self.scores)
        HighScore = listSorted[-1]
        return f"The current highscore is {HighScore}"
    
    def topthree(self):
        listSorted = sorted(self.scores)
        TopScores = listSorted[-3:]
        return f"The three highest scores are: {TopScores}"
    
    def recentscore(self):
        RecentScore = self.scores[-1]
        return f"The recent score is {RecentScore}"