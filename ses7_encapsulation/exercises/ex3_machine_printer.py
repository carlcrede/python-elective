class Machine:
    def __init__(self):
        self.__power = False

    @property
    def power(self):
        return self.__power

    def start(self):
        self.__power = True
        print('powered on.')
    
    def stop(self):
        self.__power = False
        print('powered off.')

class Printer(Machine):
    def __init__(self):
        super().__init__()
        print('New printer created.')
        self.__papertray = Papertray()

    @property
    def papertray(self):
        return self.__papertray

    def print(self, content):
        if not self.power:
            print('Printer is not powered on.')
        else:
            print(content)
            self.__papertray.use_paper()

class Papertray:
    def __init__(self):
        self.__papers = 10
        print(f'Papertray contains {self.__papers} papers.')

    @property
    def papers(self):
        return self.__papers

    def use_paper(self):
        self.__papers -= 1
        if self.__papers == 0:
            self.load_paper()

    def load_paper(self, papers=5):
        self.__papers += papers
        print(f'{papers} pieces of paper loaded into papertray.')

    def __repr__(self):
        return f'{self.__dict__}'

    