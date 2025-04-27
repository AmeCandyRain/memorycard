#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский','Японский', 'Русский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Какой фигуры нет в шахматах', 'Пёс', 'Слон', 'Конь', 'Ладья'))
questions_list.append(Question('Какого предмета нет в 7-х классах', 'Астрономия', 'Алгебра', 'Химия', 'Физика'))
questions_list.append(Question('Сколько уроков мы писали MemoryCard', '4', '3', '2', '5'))
questions_list.append(Question('Дата инагурации Трампа', '20.01.25', '30.02.25', '23.11.24', '11.09.02'))
questions_list.append(Question('Когда приедет мой заказ с OZON', 'завтра', 'никогда', 'никогда', 'никогда'))
questions_list.append(Question('Ваш уровень знания python', 'Впервые слышу', 'Немного разбираюсь', 'Средний', 'Высокий'))
questions_list.append(Question('Дата инагурации Путина', '07.05.24', '11.09.02', '20.01.25', 'а?'))
questions_list.append(Question('самая популярная игра в мире', 'RAID: shadow legends', 'minecraft', 'league of legends', 'Dota2'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('memory card')
main_win.resize(600, 300)
main_win.show()
btn_ok = QPushButton('Ответить')
ib_question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулынцы')
rbtn4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
ib_result = QLabel('Правильно/Неправильно')
ib_Correct = QLabel('правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(ib_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(ib_Correct, alignment =Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(ib_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    ib_question.setText(q.question)
    ib_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    ib_result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно uwu')
        main_win.score += 1
        print('статистика\n - Всего вопросов:', main_win.total, "\n - Правильных ответов", main_win.score)
        print('Рейтинг:', main_win.score / main_win.total * 100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3]. isChecked:
            show_correct("Не правильно >_<")
            print('Рейтинг:', main_win.score / main_win.total * 100, '%')
def next_question():
    main_win.total += 1
    print('статистика\n - Всего вопросов:', main_win.total, "\n - Правильных ответов", main_win.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == "Ответить":
        check_answer()
    else:
        next_question()

btn_ok.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0
next_question()
main_win.show()
app.exec_()