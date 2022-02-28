class Ice_Dragon:
    def __init__(self, name, color, level=1):
        self.name = name
        self.color = color
        self.level = level

    def fight(self):
        self.level += 1

    def frost_breath(self):
        self.mouth = 'open'
        self.breath = 'freezing'
        print(f'{self.name}\'s mouth is {self.mouth}'
              f' and her breath is {self.breath}.')
