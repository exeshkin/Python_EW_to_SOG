from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from design import Ui_MainWindow
import qthread
import sys
import utils


# Создать GUI приложения
class EW_Message_in_SOG(QMainWindow):
    # Инициализация класса
    def __init__(self, parent=None):
        super(EW_Message_in_SOG, self).__init__(parent)

        # Экземпляр класса Ui_MainWindow из файла 'design.py'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Переменная для отслеживания нажатия кнопки 'Стоп'
        self.stop = False
        # Переменная для отслеживания переключателя QComboBox
        self.combobox = ''

        # Слушатели сигналов
        self.ui.btn_start.clicked.connect(self.start_create_sog)
        self.ui.btn_stop.clicked.connect(self.stop_create_sog)
        self.ui.btn_info.clicked.connect(self.show_info)

        # Экземпляр класса CreateSog из файла 'qthread.py'
        self.create_sog = qthread.CreateSog(mainwindow=self)
        # Слушатели сигналов
        self.create_sog.sig_except_one_line.connect(self.print_except_one_line)
        self.create_sog.sig_except_non_standard.connect(
            self.print_except_non_standard)
        self.create_sog.sig_finish.connect(self.print_finish)
        self.create_sog.sig_stop.connect(self.print_stop)

    # Установка параметров и запуск потока
    def start_create_sog(self):
        # Переменная для отслеживания нажатия кнопки 'Стоп'
        self.stop = False
        # Отобразить сообщение окне приложения
        self.ui.log_field.setPlainText(
            'Создание файла началось, дождитесь окончания процесса ...\n-------')
        # Деактивировать кнопку 'Создать *.sog'
        self.ui.btn_start.setEnabled(False)
        # Деактивировать QComboBox
        self.ui.branham_or_vin.setEnabled(False)

        # Установка значения переменной в соответствии со значением QComboBox
        if self.ui.branham_or_vin.currentText() == "Уилльям Маррион Бранхам":
            self.combobox = 'cb_message'
        if self.ui.branham_or_vin.currentText() == "Вин Даял":
            self.combobox = 'cb_vin'

        # Запуск потока
        self.create_sog.start()

    def stop_create_sog(self):
        # Переменная для отслеживания нажатия кнопки 'Стоп'
        self.stop = True

    def print_except_one_line(self, file):
        # Отобразить сообщение окне приложения
        self.ui.log_field.appendPlainText(
            f'{file[:-5]} — текст всей проповеди в одном абзаце (в одну строку). Необходимо добавить данную проповедь в исключения!\n-------')

    def print_except_non_standard(self, file):
        # Отобразить сообщение окне приложения
        self.ui.log_field.appendPlainText(
            f'{file[:-5]} — нестандартный формат проповеди. Необходимо добавить данную проповедь в исключения!\n-------')

    def print_finish(self):
        # Установить значение прогресс-бара на 0
        self.ui.progress_bar.setValue(0)
        # Отобразить сообщение окне приложения
        self.ui.log_field.appendPlainText(
            f'Файл "{utils.name_file(self.combobox)}" готов!\nОн находтися в папке "finished_sog_file"')
        # Активировать кнопку 'Создать *.sog'
        self.ui.btn_start.setEnabled(True)
        # Активировать QComboBox
        self.ui.branham_or_vin.setEnabled(True)

    def print_stop(self):
        # Установить значение прогресс-бара на 0
        self.ui.progress_bar.setValue(0)
        # Отобразить сообщение окне приложения
        self.ui.log_field.setPlainText('Вы прервали создание файла')
        # Активировать кнопку 'Создать *.sog'
        self.ui.btn_start.setEnabled(True)
        # Активировать QComboBox
        self.ui.branham_or_vin.setEnabled(True)

    def show_info(self):
        # Открыть информационное окно
        QMessageBox().information(self, 'Инфо', utils.info_text)


# Старт приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = EW_Message_in_SOG()
    window.show()

    sys.exit(app.exec())
