from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton ,QHBoxLayout, QLabel,QVBoxLayout , QRadioButton, QGroupBox, QButtonGroup
from random  import shuffle, randint



class QuestionClass():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Мега-викторина!')

RadioGroupBox = QGroupBox('Варианты ответов')

bLineV1 = QVBoxLayout()
bLineV2 = QVBoxLayout()
bLineH = QHBoxLayout()

b1 = QRadioButton('Алеуты')
b2 = QRadioButton('смурфы')
b3 = QRadioButton('негры')
b4 = QRadioButton('эльфы')

bLineV1.addWidget(b1, alignment=Qt.AlignCenter)
bLineV1.addWidget(b2, alignment=Qt.AlignCenter)
bLineV2.addWidget(b3, alignment=Qt.AlignCenter)
bLineV2.addWidget(b4, alignment=Qt.AlignCenter)

bLineH.addLayout(bLineV1)
bLineH.addLayout(bLineV2)

RadioGroupBox.setLayout(bLineH)

question = QLabel('Какой национальности не бывает?')
ansButton = QPushButton('Ответить!')


mLineV = QVBoxLayout()
mLineH1 = QVBoxLayout()
mLineH2 = QVBoxLayout()
mLineH3 = QVBoxLayout()

mLineH1.addWidget(question,alignment=Qt.AlignCenter)
mLineH2.addWidget(RadioGroupBox,alignment=Qt.AlignCenter)
mLineH3.addWidget(ansButton,alignment=Qt.AlignCenter)

#RadioGroupBox.hide()

ansBox = QGroupBox('Результаты ответов')
aLineV = QVBoxLayout()
YesNoLabel = QLabel('Тут будет верно/неверно')
CorrectAns = QLabel('Тут будет верный ответ')

aLineV.addWidget(YesNoLabel,alignment=Qt.AlignCenter)
aLineV.addWidget(YesNoLabel,alignment=Qt.AlignCenter)


ansBox.setLayout(aLineV)

mLineH2.addWidget(ansBox,alignment=Qt.AlignCenter )



mLineV.addLayout(mLineH1)
mLineV.addLayout(mLineH2)
mLineV.addLayout(mLineH3)

main_win.setLayout(mLineV)


RadioGroup = QButtonGroup()
RadioGroup.addButton(b2)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)


ansBox.hide()

def show_results():
    RadioGroupBox.hide()
    ansBox.show()
    ansButton.setText('го некст!')

def show_question():
    ansBox.hide()
    RadioGroupBox.show()
    ansButton.setText('Ответить!')

    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)


def TEST():
   if 'Ответить!' == ansButton.text():
       show_results()
   else:
      show_question()


answer = [b1, b2, b3, b4]

def ask(q: QuestionClass):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question)
    CorrectAns.setText(q.right_answer)
    show_question()


def show_correct(result):
    YesNoLabel.setText(result)
    show_results()


def check():
    if answer[0].isChecked():
        show_correct('Верно')
        main_win.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('неверно!')
    print('Рейтинг:', main_win.score/main_win.total*100, '%')

question_list = []
question_list.append(QuestionClass('кто гей', 'симеон','точно я','сто процентов я','я'))
question_list.append(QuestionClass('1223+1223','2446', '34923','234','2546'))
question_list.append(QuestionClass('2-2','0','212','123','2312'))
question_list.append(QuestionClass('8652-5478','3174','2894','1233','4452'))
question_list.append(QuestionClass('кто гей','я','я','я','я'))
question_list.append(QuestionClass('Как еще называют периметр круга?','окружность','не как ','округление ','хз'))
question_list.append(QuestionClass('Кто изобрел знак равенства','Роберт рекорд ','роберт полсон','хз','я'))
question_list.append(QuestionClass('кто изобрел математику','скала','Эндрью стехмен','архимед','Альберт Эйнштейн'))
question_list.append(QuestionClass('Речка спятила с ума —по домам пошла сама','водопровод','электричество ','литвин','хз'))
question_list.append(QuestionClass('123123123+14414314','42344213131231','212312313','1232313','231212312313'))
#main_win.cur_question = -1

main_win.total = 0
main_win.score = 0


def next_question():
    main_win.total  += 1
    print('Статка',main_win.total,'-всего вопросов.Верно:',main_win.score)

   # main_win.cur_question +=1
   # if main_win.cur_question >= len(question_list):
   #     main_win.cur_question = 0


    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_Ok():
    if 'Ответить!' == ansButton.text():
        check()
    else:
        next_question()












ansButton.clicked.connect(click_Ok)

next_question()
main_win.show()
app.exec_()





