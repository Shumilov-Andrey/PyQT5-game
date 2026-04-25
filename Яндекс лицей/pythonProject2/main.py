import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow


class Bull_and_cow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Быки и коровы')

        self.rules = QPushButton('Правила', self)
        self.rules.resize(self.rules.sizeHint())
        self.rules.move(370, 100)
        self.rules.clicked.connect(self.open_rules)

        computer_number = random.randint(1000, 9999)
        numbers = list(str(computer_number))
        self.numbers = numbers

        self.btn = QPushButton('Ваш ход', self)
        self.btn.resize(100, 30)
        self.btn.move(30, 100)
        self.btn.clicked.connect(self.transition_process)

        self.result_human_text = QLabel(self)
        self.result_human_text.setText("Ответ компьютера:")
        self.result_human_text.move(185, 5)

        self.result_human = QLineEdit(self)
        self.result_human.resize(220, 100)
        self.result_human.move(135, 30)
        self.result_human.setEnabled(False)

        self.result_computer_text = QLabel(self)
        self.result_computer_text.setText("Ответ человека:")
        self.result_computer_text.move(185, 135)

        self.result_computer = QLineEdit(self)
        self.result_computer.resize(215, 100)
        self.result_computer.move(145, 160)

        self.counter = 0

        self.list_number = []
        for i in range(1000, 10000):
            self.list_number.append(i)

        self.human_number_text = QLabel(self)
        self.human_number_text.setText("Ваш вариант:")
        self.human_number_text.move(30, 5)

        self.human_number = QLineEdit(self)
        self.human_number.resize(80, 30)
        self.human_number.move(30, 30)

        self.text_number = QLabel(self)
        self.text_number.setText("Придумайте число:")
        self.text_number.move(370, 5)

        self.intended_number = QLineEdit(self)
        self.intended_number.resize(80, 30)
        self.intended_number.move(370, 30)

        self.computer_number_text = QLabel(self)
        self.computer_number_text.setText("Вариант компьютера:")
        self.computer_number_text.resize(150, 30)
        self.computer_number_text.move(30, 145)

        self.computer_number = QLineEdit(self)
        self.computer_number.resize(80, 30)
        self.computer_number.move(30, 170)
        self.computer_number.setEnabled(False)
        self.computer_number.setText(str(random.choice(self.list_number)))

        self.result_text = QLabel(self)
        self.result_text.setText("Победитель:")
        self.result_text.move(365, 150)

        self.result = QLineEdit(self)
        self.result.resize(80, 30)
        self.result.move(365, 175)
        self.result.setEnabled(False)

        self.counter_users = 0

    def transition_process(self):
        if self.intended_number.text() != "":
            self.intended_number.setEnabled(False)

        self.list_bull_and_cow = []

        if self.counter % 2 != 0:
            self.btn.setText('Ваш ход')
            if self.result_computer.text() != "":
                brain = ['1', '2', '3', '4']
                six = self.result_computer.text().split()
                for j in range(len(six)):
                    if "," in six[j]:
                        b = six[j]
                        six[j] = b[:-1]
                shesterca = self.computer_number.text()
                for a in range(len(six)):
                    if six[a] == "корова":
                        b = len(self.list_number)
                        index = 0
                        while index < b:
                            qwer = str(self.list_number[index])
                            if (not shesterca[int(six[a - 1]) - 1] in qwer) or shesterca[int(
                                    six[a - 1]) - 1] == qwer[int(six[a - 1]) - 1]:
                                del (self.list_number[index])
                                b -= 1
                                index -= 1
                            index += 1
                        if six[a - 1] in brain:
                            brain.remove(six[a - 1])

                    elif six[a] == "бык":
                        b = len(self.list_number)
                        index = 0
                        while index < b:
                            qwer = str(self.list_number[index])
                            if shesterca[int(six[a - 1]) - 1] != qwer[int(six[a - 1]) - 1]:
                                del (self.list_number[index])
                                b -= 1
                                index -= 1
                            index += 1
                        if six[a - 1] in brain:
                            brain.remove(six[a - 1])

                if brain != []:
                    b = len(self.list_number)
                    index = 0
                    for u in range(len(brain)):
                        while index < b:
                            if shesterca[int(brain[u]) - 1] in str(self.list_number[index]):
                                del (self.list_number[index])
                                b -= 1
                                index -= 1
                            index += 1
                        index = 0

            if self.result_computer.text() != "1 бык, 2 бык, 3 бык, 4 бык" and int(shesterca) in self.list_number:
                self.list_number.remove(int(shesterca))
            elif self.result_computer.text() == "1 бык, 2 бык, 3 бык, 4 бык":
                self.result.setText("компьютер")

            self.computer_number.setText(str(random.choice(self.list_number)))

        else:
            self.btn.setText('Ход компьютера')
            self.counter_users += 1
            numder_human = list(self.human_number.text())
            for k in range(len(numder_human)):
                if numder_human[k] == self.numbers[k]:
                    self.list_bull_and_cow.append(str(k + 1) + ' бык')
                elif numder_human[k] in self.numbers and numder_human[k] != self.numbers[k]:
                    self.list_bull_and_cow.append(str(k + 1) + ' корова')
            self.result_human.setText(', '.join(self.list_bull_and_cow))
            if self.result_human.text() == "1 бык, 2 бык, 3 бык, 4 бык":
                self.result.setText("человек")
        self.counter += 1

    def open_rules(self):
        self.second_form = Rules(self, "Вы играете против компьютера, Ваша задача быстрее него отгадать четырёхзначное число." + "\n"
                                       " Правила игры: Первым делом Вы должны ввести четырёхзначное число в окошко под текстом 'Придумайте число:', " + "\n"
                                       "далее наступает ваша очередь ходить, введите четырёхзначное число(в окошко под текстом 'Ваш вариант'), которое, " + "\n"
                                       "по вашему мнению, является заданным числом компьютера, далее уокомпьютера тоже есть число, которое, " + "\n"
                                       "по его мнению, является вашим загаданным числом(в окошке под надписью 'вариант компьютера'), "+ "\n"
                                       "в окошке под надписью 'Ответ человека:' если в числе, загаданном компьютером, есть такая цифра, " + "\n"
                                       "как в вашем числе и их позиции совпадают, то введите номер этой цифры числа и слово бык, " + "\n"
                                       "если в числе, загаданном компьютером, есть такая цифра, как в вашем числе" + "\n"
                                       "и их позиции  НЕ совпадают, то введите номер этой цифры числа и слово корова. " + "\n"
                                       "Если у загаданного компьютером числом нет ни быков, ни коров с вашим, то введите 'ничего'. " + "\n"
                                       "Далее, ориентируясь на аналагичный текст от компьютера(он будет, если это не самый первый ваш ход " + "\n"
                                       "и если есть быки и коровы с вашим числом) и ажмите кнопку 'Ваш ход', что бы передать ход компьютеру.")
        self.second_form.show()


class Rules(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('Правила')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Bull_and_cow()
    ex.show()
    sys.exit(app.exec())
