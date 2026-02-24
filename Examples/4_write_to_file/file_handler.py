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

    def write(self, rows:list[str]):
        try:
            filehandle = open(self.filepath, "w", encoding="UTF-8")
            for row in rows:
                filehandle.write(f"{row}\n")
            filehandle.close()
        except Exception:
            print(f"Failed to write file '{self.filepath}'")
            exit(-1)
        return None
