class FileHandler:
    filepath: str
    def __init__(self, filepath):
        self.filepath = filepath
        return None
    
    def read(self):
        rows: list[str] = []

        try:
            filehandle = open(self.filepath, "r", encoding="UTF-8")         # with open (self.file etc etc) as
            row = filehandle.readline()
            while row != '':
                rows.append(row.strip('\n'))
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            print("File not found")
            exit(-1)
        return rows
