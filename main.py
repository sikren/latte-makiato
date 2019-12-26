from PyQt5.QtWidgets import *
import sys
import sqlite3
from addEditCoffeeForm import Ui_MainWindow as Ui1
from main_ui import Ui_MainWindow as Ui2


class MyWidget(Ui2, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setStyleSheet('font: 75 14pt "Perpetua Titling MT";')
        self.con = sqlite3.connect('data\coffee.sqlite3')
        self.init_UI()
        self.load()

    def init_UI(self):
        self.edit = QPushButton('Edit', self)
        self.edit.move(650, 460)
        self.edit.clicked.connect(self.edit_form)

    def load(self):
        cur = self.con.cursor()

        result = cur.execute("SELECT * FROM sorts").fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(titles)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def edit_form(self):
        self.edit_w = EditWindow(self.con, self)
        self.edit_w.show()


class EditWindow(Ui1, QMainWindow):
    def __init__(self, connection, main):
        super().__init__()
        self.setupUi(self)
        self.con = connection
        self.cur = self.con.cursor()

        self.main = main

        # cell edit
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.modified = {}

        # item
        self.id = None

        # action
        self.action = True  # True -> add

        # buttons connection
        self.Add.clicked.connect(self.add_record)
        self.Start_search.clicked.connect(self.search)
        self.Confirm.clicked.connect(self.save_results)

        result = self.cur.execute(f"""SELECT * FROM sorts
                                              WHERE Name = '321'""").fetchall()

    def add_record(self):
        self.action = True  # Add

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        self.titles = [description[0] for description in self.cur.description][1:]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)

        record = self.titles
        self.tableWidget.blockSignals(True)

        for i, elem in enumerate(record):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(elem)))

        self.tableWidget.blockSignals(False)

    def search(self):
        self.action = False  # Edit

        text = self.Search.text()
        result = self.cur.execute(f"""SELECT * FROM sorts
                                      WHERE Name = '{text}'""").fetchall()
        if len(result) != 0:
            result = min(result, key=lambda x: x[0])

            self.id = result[0]
            result = result[1:]

            self.tableWidget.setColumnCount(len(result))
            self.tableWidget.setRowCount(1)
            self.titles = [description[0] for description in self.cur.description][1:]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            self.tableWidget.blockSignals(True)

            for i, elem in enumerate(result):
                self.tableWidget.setItem(0, i, QTableWidgetItem(str(elem)))

            self.tableWidget.blockSignals(False)

    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.action:
            id = max(self.cur.execute('SELECT id FROM sorts').fetchall())
            record = [id[0] + 1]

            for i in range(6):
                record.append(self.tableWidget.item(0, i).text())
            record = tuple(record)
            self.cur.execute(f"INSERT INTO sorts VALUES{record}")
        else:
            if self.modified:
                que = "UPDATE sorts SET\n"
                for key in self.modified.keys():
                    que += "{}='{}'\n".format(key, self.modified.get(key))
                que += f"WHERE id = {self.id}"
                self.cur.execute(que)
        self.con.commit()
        self.main.load()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
