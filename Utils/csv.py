class File:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as file:
            return file.readlines()

    def write(self, data):
        with open(self.path, 'w') as file:
            file.writelines(data)

    def append(self, data):
        with open(self.path, 'a') as file:
            file.writelines(data)

    def clear(self):
        open(self.path, 'w').close()
