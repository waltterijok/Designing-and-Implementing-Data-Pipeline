# main.py

from config import APP_NAME, VERSION
from database.connection import init_db
from ui.app import *

def main():
    init_db()
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()