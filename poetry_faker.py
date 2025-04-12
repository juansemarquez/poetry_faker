class PoetryFaker:

    def __init__(self, text, breakline = "\n", prepend = "_", language = "es"):
        self.breakline = breakline
        self.prepend = prepend
        self.language = language
        with open(text, 'r') as content_file:
            self.text = content_file.read()

    def verse_maker(self):
        print(self.eliminate_punctuation())

    def eliminate_punctuation(self):
        letters_and_space=" abcdefghijklmnopqrstuvwxyz"
        if self.language == "es":
            letters_and_space += "áéíóúüñ¡¿"
        total = len(self.text)
        i = 0
        output = ""
        while i < total:
            if self.text[i] == self.prepend:
                output += self.text[i+1] + "\n"
                i+=2
                continue
            if self.text[i] in letters_and_space or self.text[i] in letters_and_space.upper():
                output += self.text[i]
            else:
                if self.text[i] in ("?", "!"):
                    output+=self.text[i]
                output += "\n"
            i+=1
        return output.replace("\n ", "\n")
