import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora PyQt5')
        self.setFixedSize(500,500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display,0,0,1,5)  # 5 LINHAS
        self.display.setDisabled(True)
        self.display.setStyleSheet( # CSS
            '* {background: white; color: #000; font-size: 30px;}'
        )
        
        self.add_btn(QPushButton('7'), 1 ,0, 1 , 1)
        self.add_btn(QPushButton('8'), 1 ,1, 1 , 1)
        self.add_btn(QPushButton('9'), 1 ,2, 1 , 1)
        self.add_btn(QPushButton('+'), 1 ,3, 1 , 1)
        self.add_btn(QPushButton('C'), 1 ,4, 1 , 1 , 
        lambda: self.display.setText(''),
        'background: #F08080; color: #fff ; font-weight: 700;'
        ) # deixando o text vazio
        
        self.add_btn(QPushButton('4'), 2 ,0, 1 , 1)
        self.add_btn(QPushButton('5'), 2 ,1, 1 , 1)
        self.add_btn(QPushButton('6'), 2 ,2, 1 , 1)
        self.add_btn(QPushButton('-'), 2 ,3, 1 , 1)
        self.add_btn(QPushButton('⌫'), 2 ,4, 1 , 1, lambda: self.display.setText(
        self.display.text()[:-1]
        ),
        'background: #0000FF; color: #fff; font-weight: bold;'
        )
        self.add_btn(QPushButton('1'), 3 ,0, 1 , 1)
        self.add_btn(QPushButton('2'), 3 ,1, 1 , 1)
        self.add_btn(QPushButton('3'), 3 ,2, 1 , 1)
        self.add_btn(QPushButton('/'), 3 ,3, 1 , 1)
        self.add_btn(QPushButton('%'), 3 ,4, 1 , 1)
        
        self.add_btn(QPushButton('.'), 4 ,0, 1 , 1)
        self.add_btn(QPushButton('0'), 4 ,1, 1 , 1)
        self.add_btn(QPushButton('⌦'), 4 ,2, 1 , 1, lambda: self.display.setText(
            self.display.text()[1:]
        ),
        'background: #8B4513; color: #fff; font-weight: bold;'
                     )
        self.add_btn(QPushButton('*'), 4 ,3, 1 , 1)
        self.add_btn(QPushButton('='), 4 ,4, 1 , 1,
        self.eval_igual,
        'background: #228B22; color: #fff; font-weight: 700;')
        
        self.setCentralWidget(self.cw)  ## PONTO CENTRAL
        
    def add_btn(self, but, row, col , rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(but, row, col , rowspan, colspan)
        
        if not funcao: 
            but.clicked.connect(
            lambda: self.display.setText(
                self.display.text() + but.text()
            ) 
            )
        else:
            but.clicked.connect(funcao)
        
        if style:
            but.setStyleSheet(style)
            
        but.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        
    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())) # função ''eval'' engloba as contas e verifica se a conta existe
            )
        except Exception as e:
            self.display.setText('Conta inválida')     
    
if __name__ =='__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
    
    
    
    
