from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("logikaYear")
main_win.resize(400, 200)





btn_answer1 = QRadioButton('1')
btn_answer2 = QRadioButton('2')
btn_answer3 = QRadioButton('3')
btn_answer4 = QRadioButton('4')
layout_main = QVBoxLayout()
btn_answer1.setChecked(True)

btn_group=QButtonGroup
btn_group.addButton(btn_answer1,id=1)
btn_group.addButton(btn_answer2,id=2)
btn_group.addButton(btn_answer3,id=3)
btn_group.addButton(btn_answer4,id=4)

layoutH1 = QVBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()



layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlingCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH4.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)

main_win.setLayout(layout_main)



btn_quetion = QPushButton(text="Перевірити")
layoutH1.addWidget(btn_quetion,alignment=Qt.AlingCenter)

answer=QMessageBox()

answer.setText("Вибрана кнопка під номером" + str(btn_group.checkedId()))

main_win.show()
app.exec_()