class Ice_Dragon:
    """A class used to build Ice Dragons."""

    def __init__(self, name, color, level=1, drg_hp=15):
        """Creates an Ice Dragon at level 1."""
        self.name = name
        self.color = color
        self.level = level
        self.drg_hp = drg_hp

    def fight(self):
        """Increases the dragon's level by 1 after fighting."""
        self.level += 1

    def frost_breath(self):
        """Ice dragon attacks with freezing breath."""
        self.mouth = 'open'
        self.breath = 'freezing'
        print(f'{self.name}\'s mouth is {self.mouth}'
              f' and her breath is {self.breath}.')
