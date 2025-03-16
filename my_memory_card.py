#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
#создание окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(400,300)

main_win.total = 0
main_win.score = 0

#сщздание винджетов
lbl_question = QLabel("Ворос")
RadioGrop = QGroupBox('Вариант ответа')
rtb_1 = QRadioButton('Ответ 1')
rtb_2 = QRadioButton('Ответ 2')
rtb_3 = QRadioButton('Ответ 3')
rtb_4 = QRadioButton('Ответ 4')
btn_ok = QPushButton('Ответить')

AnswerGrop = QGroupBox('Результат')
lbl_result = QLabel('Верно/неверно')
lbl_correct = QLabel('Правильный ответ')

lbl_stat=QLabel('Статистика')

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rtb_1)
ButtonGroup.addButton(rtb_2)
ButtonGroup.addButton(rtb_3)
ButtonGroup.addButton(rtb_4)

answ = [rtb_1, rtb_2, rtb_3, rtb_4]

row1 = QHBoxLayout()
row1.addWidget(rtb_1)
row1.addWidget(rtb_2)
row2 = QHBoxLayout()
row2.addWidget(rtb_3)
row2.addWidget(rtb_4)

col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)

RadioGrop.setLayout(col)

col1 = QVBoxLayout()
col1.addWidget(lbl_result, alignment=Qt.AlignLeft)
col1.addWidget(lbl_result, alignment=Qt.AlignCenter)

AnswerGrop.setLayout(col1)
AnswerGrop.hide()
main_layout = QVBoxLayout()
main_layout.addWidget(lbl_question)
main_layout.addWidget(RadioGrop)
main_layout.addWidget(AnswerGrop)
main_layout.addWidget(btn_ok)
main_layout.addWidget(lbl_stat)

main_win.setLayout(main_layout)

class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.r_awswer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = []
q = Question('В каком году вышел превый майнкрафт?', '2009.', '1967', '2021', '2000')
question_list.append(q)
q = Question('В коком году создан windows?', '1985.', '1967', '2000',' 2010')
question_list.append(q)
q = Question('В каком году вышел роблокс?', '2006.', '2000', '2003', '1807')
question_list.append(q)
q = Question('В каком году появился певый сенсерынй телефон', '1992.', '1999', '1989', '1997')
question_list.append(q)


    
def ShowResult():
    RadioGrop.hide()
    AnswerGrop.show()
    btn_ok.setText("Следующий вопрос")

def ShowQuestion():
    num = randint(0, len(question_list)-1)
    ask(question_list[num])
    RadioGrop.show()
    AnswerGrop.hide()
    btn_ok.setText('Ответить')
    ButtonGroup.setExclusive(False)
    rtb_1.setChecked(False)
    rtb_2.setChecked(False)
    rtb_3.setChecked(False)
    rtb_4.setChecked(False)
    ButtonGroup.setExclusive(True)

def StartText():
    if btn_ok.text() =='Ответить':
        if answ[0].isChecked:
            lbl_result.setText('Совершенно верно!')
        ShowResult()
    else:
        ShowQuestion()

def ask(q):
    shuffle(answ)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.r_awswer)
    answ[0].setText(q.r_awswer)
    answ[1].setText(q.wrong1)
    answ[2].setText(q.wrong2)
    answ[3].setText(q.wrong3)
    main_win.total +=1

def checkAnswer():
    if btn_ok.text() =='Ответить':
        if answ[0].isChecked():
            lbl_result.setText('Совершеннов верно')
            main_win.score +=1
        else:
            lbl_result.setText('Не верно!')
        ShowResult()

    
        lbl_stat.setText('Статистика: \nВсего вопросов:'+str(main_win.total)+'\nПравильных ответов:'+str(main_win.score))
    else:
        ShowQuestion() 
    # print('Статистика: \nВсего вопросов:'+str(main_win.total)+'Правильных ответов:'+str(main_win.score)) 


    
num = randint(0, len(question_list)-1)
ask(question_list[num])


btn_ok.clicked.connect(checkAnswer)




main_win.show()
app.exec_()
