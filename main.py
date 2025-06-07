from PySide6.QtWidgets import (
    QApplication
)

from src.lms import LibrarySystem

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    library = LibrarySystem()
    sys.exit(app.exec())

