from mimetypes import init
import fastf1 as ff1
import random as rnd
import matplotlib.pyplot as plt
import pandas
import string
from uiFiles.ui_mainWindow import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QScrollBar,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QDialog,
    QInputDialog,
    # QAlignCenter,
)

from multiprocessing.sharedctypes import Value


class fastf1(Ui_MainWindow):
    def __init__(self, year:int, number:int, type:str):
        self.type = type
        self.year = year
        self.race = number
        self.sessions = ["Practice 1", "Practice 2", "Practice 3", "Qualifying", "Race"]
        self.session_type = type
        self.current_event = None
        self.current_session = None
        self.current_session.load()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.year = 2005
        self.race = 9
        self.sessions = ["Practice 1", "Practice 2", "Practice 3", "Qualifying", "Race"]
        self.type = self.sessions[4]
        self.session_type = type
        self.ln_pod.setText("0")
        self.sb_session.valueChanged.connect(lambda: self.update_session_type())
        self.btn_search_for_name_on_position.clicked.connect(lambda: self.research())
        self.data_set_1 = []
        self.data_set_2 = []
        self.data_set_equal = []
        self.btn_graph1.clicked.connect(lambda: self.graph_1())
        self.btn_graph2.clicked.connect(lambda: self.graph_2())
        # self.set_current_session()
        self.btn_graph3.clicked.connect(lambda: self.telemetry())
        
    def telemetry(self):
        self.set_current_session()
        self.current_session.load()
        self.current_session.laps.load()
        best_bottas = self.session.laps.pick_driver('BOT').pick_fastest()

        print(best_bottas['LapTime'])

    def graph_1(self):
        pass

    def graph_2(self):
        self.data_set_equal = [1,2,3,4,5,6]
        self.data_set_1 = []
        for i in self.data_set_equal:
            val = self.sb_session.value()
            self.data_set_1.append(rnd.randint(0, 100))
        self.data_set_2 = [6,5,4,3,2,1]
        self.redraw()
        
    def redraw(self):
        plot = plt.bar(self.data_set_equal, self.data_set_1)
        plot2 = plt.bar(self.data_set_equal, self.data_set_2)
        plot3 = plt.plot(self.data_set_equal, self.data_set_1)
        plt.xlabel(None)
        plt.ylabel(None)
        plt.grid(True)
        plt.setp(plot, 'color', 'r', 'linewidth', 1)
        plt.setp(plot2, 'color', 'g', 'linewidth', 1)
        plt.show()
        """wenn man die datei ausführt, dann muss man auf den 2. Button in der Rechten Spalte klicken um das Problem zu reproduzieren
        """


    def research(self):
        self.year = int(self.ln_input_year.text())
        self.race = int(self.ln_race_number.text())
        self.set_current_session()
        position = int(self.ln_pod.text())
        self.set_current_session()
        text = self.current_session.results.iloc[position - 1, 7]
        print(text)
        self.lb_output_name_position.setText(str(text) + " hat " + self.session_name() + " in Platz " + str(position) + " beendet")   

    def set_current_session(self):
        self.current_session = ff1.get_session(self.year, self.race, self.type)
        self.current_session.load()

    def set_current_event(self):
        self.current_event = ff1.get_event(self.year, self.race)
        self.current_event.load()

    def update_session_type(self):
        self.sessions = ["Practice 1", "Practice 2", "Practice 3", "Qualifying", "Race"]
        self.type = self.sessions[self.sb_session.value()-1]

    def list_columns_results(self): print(self.current_race.results.columns)

    def session_name(self): return self.current_session.name

    def weekend_name(self): return self.event.name

    def output_position(self, position): print(self.current_session.results.iloc[position-1, 7], "hat", self.session_name(), "in Platz", position, "beendet")

class something():
    def something():
        fastf1.Cache.enable_cache("F:\cache")
        year = 2020
        race_number = 1
        qualy_session = fastf1.get_session(year, race_number, "Qualifying")
        race_session = fastf1.get_session(year, race_number, "Race")
        qualy_session.load()
        race_session.load()
        schedule = fastf1.get_event_schedule(2022)

        # driver_number = []
        # position = []
        # for i in session.results.Q3:
        #     driver_number.append[]
        a = []
        b =  []
        number = 0
        for index in race_session.results.FullName:
            a.append(number)
            number +=1
        number = 0
        for index in qualy_session.results.FullName:
            b.append(number)
            number += 1
            
        plot = plt.plot(race_session.results.Abbreviation, a, "or")
        plot2 = plt.plot(qualy_session.results.Abbreviation, b, "or")
        plot2
        plot
        plt.xlabel(None)
        plt.ylabel(None)
        plt.tight_layout()
        plt.xscale = 1
        plt.grid(True)
        plt.colormaps()
        plt.setp(plot, 'color', 'r', 'linewidth', 2)
        plt.setp(plot2, 'color', 'g', 'linewidth', 0.1)
        plt.show()

def year():
    try:
        return int(input("In what year took the race place?\n>"))
    except ValueError:
        year()

def race_number():
    try:
        return int(input("Wich race was it?\n"))
    except ValueError:
        race_number()

def position():
    try:
        return int(input("Aus welcher position sollen die Infos kommen ?\n"))
    except ValueError:
        position()
def load():
    pass

if __name__ == '__main__':
    ff1.Cache.enable_cache("A:\cache")
    # year = 2020
    # number = 3
    # f = fastf1(year=year, number=number, type="R")
    # position = position()
    # f.output_position(position)
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    load()
    app.exec()