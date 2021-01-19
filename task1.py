class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    
    def printer(self):
        print(f"{self.lang} alphabet:")
        for i in self.letters:
            print(i)
        
    def letters_num(self):
        count = len(self.letters)
        print(f"letters in {self.lang} language: {count}")
        
        
alph = Alphabet("unga-bunga", (
"aG",
"cm",
'hP',
"xb",
"By",
"VL",
"Yj",
"Se",
"CK",
"jO",
"Vq",
"dV",
"nF",
"yE",
"LC"))

alph.printer()
alph.letters_num()
        