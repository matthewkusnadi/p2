class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_first_name(self):
        return self.name.split(' ')[0]