class File:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as file:
                return file.readlines()
        except Exception as e:
            print(f"Error reading {self.path}: {e}")
            return []

    def write(self, data):
        try:
            with open(self.path, 'w') as file:
                file.writelines(data)
        except Exception as e:
            print(f"Error writing {self.path}: {e}")

    def append(self, data):
        try:
            with open(self.path, 'a') as file:
                file.writelines(data)
        except Exception as e:
            print(f"Error appending to {self.path}: {e}")

    def clear(self):
        try:
            open(self.path, 'w').close()
        except Exception as e:
            print(f"Error clearing {self.path}: {e}")
