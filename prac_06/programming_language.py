class ProgrammingLanguage:
    def __int__(self):
        self.field = ""
        self.typing = ""
        self.reflection = False
        self.year = 0

    def is_dynamic(self):
        if self.typing == "Dynamic":
            self.typing = True

        else:
            self.typing = False

    def __str__(self):
        print("{}, {} Typing, Reflection={}, First appeared in {}".format())