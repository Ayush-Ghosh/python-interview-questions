# Enter your code here. Read input from STDIN. Print output to STDOUT
class wordseek:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1,0],[1,0],[1,1],
                    [1,-1],[-1,-1],[-1,1],
                    [0,1],[0,-1]]
                    
    def search(self, grid,row,col,word):
        if grid[row][col]!=word[0]:
            return False
        for x,y in self.dir:
            rd,cd = row + x, col + y
            flag = True
            
            for k in range(1, len(word)):
                if (0<=rd <self.R and 0<=cd < self.C and word[k] == grid[rd][cd]):
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
            if flag:
                return True
        return False
    
    def patternsearch(self,grid,word):
        self.R = len(grid)
        self.C = len(grid[0])
        
        for row in range(self.R):
            for col in range(self.C):
                if self.search(grid,row,col,word):
                    print(word,str(row),str(col))

if __name__=='__main__':
    grid = []
    words = []
    # for i in range(14):
    #     m = str(input().strip())
    #     grid.append(m)

    # for i in range(9):
    #     n = str(input().strip())
    #     if n !='':
    #         words.append(n)
    
    # for x in words:
    #     ws = wordseek()
    #     ws.patternsearch(grid,x)
    while True:
        m = str(input().strip())
        if not m:
            break
        grid.append(m)
        
    while True:
        try:
            n = str(input().strip())
            if not n:
                break
            words.append(n)
        except:
            break

    for x in words:
        ws = wordseek()
        ws.patternsearch(grid,x)
        
    
    
STFHESPENTEOPB
UULNTLEALNSTWA
DYOTACNOEETINU
DSWNSTARELSSUT
EMEVITANNEDSAK
NTRCGMIRERRDEE
LFAINTOAEDEGAV
YYLOACUPRWSGEP
URGMLDAORAOEAD
AMSCRIVBCOHMWE
DSPADEMEBSGTIC
RIDEUCEUEAISDI
CIRYLATORWGATW
OKEGURPBYROEHT
ANTIC
BRAG
CABBAGE
DEGREE
DEUCE
DIAPER
DROVE
EAGER
ENACT
FAINT
FIRE
FLOWER
GLARE
GRID
HOSE
LYRIC
MATINEE
MOWER
NATIVE
NOSE
OMINOUS
PADDLE
PLANET
POET
RACE
RADIO
RELENT
SCOUT
SIGNAL
SPADE
SPENT
STARE
SUDDENLY
TANNED
THEORY
TIARA
TUSSLE
TWICE
UNITE
VESSEL
WIDTH