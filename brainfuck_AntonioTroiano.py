from aifc import Error


class BrainfuckMachine():

    HeadOverflow = Error
    BracketMismatch = Error

    def __init__(self, value):
        self.code = ""
        self.value = value
        self.tape = [0]*self.value
        self.head = 0
        self.HeadOverflow = Error
        self.BracketMismatch = Error

    def run(self):
        self.tape = [self.tape[i]*0 for i in self.tape]
        self.head = 0
        codelenght = 0
        BracketOpenlist = []
        BracketCloselist = []
        
        while codelenght < len(self.code):

            if (self.code[codelenght] == '+'):
                self.tape[self.head] += 1
                if (self.tape[self.head] > 255):
                    self.tape[self.head] = 0

            elif (self.code[codelenght] == '-'):
                self.tape[self.head] -= 1
                if (self.tape[self.head] < 0):
                    self.tape[self.head] = 255

            elif (self.code[codelenght] == '>'):
                self.head += 1
                if (self.head > self.value):
                    raise self.HeadOverflow

            elif (self.code[codelenght] == '<'):
                self.head -= 1
                if (self.head < 0):
                    raise self.HeadOverflow

            elif (self.code[codelenght] == '['):
                if (self.tape[self.head] > 0):
                    BracketOpenlist.append(codelenght)
                else:
                    BracketCloselist.reverse()
                    if (len(BracketCloselist) > 0):
                        codelenght = BracketCloselist.pop()
                    else:
                        raise self.BracketMismatch

            elif (self.code[codelenght] == ']'):
                if (len(BracketOpenlist) > 0):
                    BracketCloselist.append(codelenght)
                    codelenght = BracketOpenlist.pop()-1
                else:
                    raise self.BracketMismatch

            codelenght += 1
