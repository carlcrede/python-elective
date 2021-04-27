class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    # make
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, make):
        self.__make = make

    # model
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    # bhp
    @property
    def bhp(self):
        return self.__bhp

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    # mph
    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, mph):
        self.__mph = mph

    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, bhp: {self.bhp}, mph: {self.mph}'

    def __repr__(self):
        return f'{self.__dict__}'