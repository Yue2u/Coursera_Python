class FileReader:

    def __init__(self, way_to_file=None):
        self.way = way_to_file or ""

    def read(self):
        try:
            with open(self.way, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ""


if __name__ == "__main__":
    print("FileReader installed...")
