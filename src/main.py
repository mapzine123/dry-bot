import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from bot_actions import admin_login, admin_signup


app = QApplication(sys.argv)
window = QMainWindow()

screenX = window.screen().size().width()
screenY = window.screen().size().height()

centralWidget = QWidget()
windowLayout = QHBoxLayout()

botLayout = QStackedLayout()
actionsLayout = QVBoxLayout()
actionsTopLayout = QGridLayout()
actionsBottomLayout = QGridLayout()
statusLayout = QVBoxLayout()

# Widget으로 구역 나누기
botSection = QWidget()

actionsSection = QWidget()
actionsTopSection = QWidget()
actionsBottomSection = QWidget()
statusSection = QWidget()

StatusSection = QWidget()

# Components

# bot
botLabel = QLabel('bot')

# actions
actionsLabel = QLabel('actions')
loginButton = QPushButton('로그인')
signupButton = QPushButton('회원가입')

# form
idInputLabel = QLabel('ID')
idInput = QLineEdit()

passwordInputLabel = QLabel('PASSWORD')
passwordInput = QLineEdit()

nicknameInputLabel = QLabel('NICKNAME')
nicknameInput = QLineEdit()

emailInputLabel = QLabel('EMAIL')
emailInput = QLineEdit()


# status
statusLabel = QLabel()
statusScrollArea = QScrollArea()
statusScrollArea.setWidgetResizable(True)

# QVBoxLayout() : 수직 레이아웃
# QHBoxLayout() : 수평 레이아웃

# 디스플레이 레이아웃 설정
def setDisplay():
    # Bot Section
    botLayout.addWidget(botLabel)

    # Action Button Section
    actionsTopLayout.addWidget(loginButton)
    actionsTopLayout.addWidget(signupButton
                               )
    # Action Input Section
    actionsBottomLayout.addWidget(QFrame())

    # - InputLabel Grid
    actionsBottomLayout.addWidget(idInputLabel, 0, 0)
    actionsBottomLayout.addWidget(passwordInputLabel, 1, 0)
    actionsBottomLayout.addWidget(nicknameInputLabel, 2, 0)
    actionsBottomLayout.addWidget(emailInputLabel, 3, 0)

    # - InputForm Grid
    actionsBottomLayout.addWidget(idInput, 0, 1)
    actionsBottomLayout.addWidget(passwordInput, 1, 1)
    actionsBottomLayout.addWidget(nicknameInput, 2, 1)
    actionsBottomLayout.addWidget(emailInput, 3, 1)


    # 조립
    actionsTopSection.setLayout(actionsTopLayout)
    actionsBottomSection.setLayout(actionsBottomLayout)

    actionsLayout.addWidget(actionsTopSection)
    actionsLayout.addWidget(actionsBottomSection)

    # Status Section
    statusScrollArea.setWidget(statusLabel)
    statusLayout.addWidget(statusScrollArea)


    botSection.setLayout(botLayout)
    actionsSection.setLayout(actionsLayout)
    statusSection.setLayout(statusLayout)

    windowLayout.addWidget(botSection)
    windowLayout.addWidget(actionsSection)
    windowLayout.addWidget(statusSection)

    centralWidget.setLayout(windowLayout)
    window.setCentralWidget(centralWidget)

# 스타일 적용
def setStyles():
    # bot Style
    botLabel.setMaximumSize(botSection.size().width(), 50)
    botSection.setMaximumSize(200, 800)
    botSection.setStyleSheet("border: 2px solid gray")

    # action Style
    loginButton.setStyleSheet('border: 1px solid black;width:100px;height:50px')
    signupButton.setStyleSheet('border: 1px solid black;width:100px;height:50px')
    actionsSection.setMinimumSize(400, 800)
    actionsSection.setStyleSheet("border: 2px solid gray;")
    actionsTopSection.setStyleSheet("border:none;border-bottom: 1px solid gray")

    # form Style
    actionsBottomSection.setStyleSheet("border: none")
    idInputLabel.setStyleSheet("font-size: 12px)")
    idInputLabel.setAlignment(Qt.AlignCenter)

    # status Style
    statusSection.setStyleSheet("border: 2px solid gray")
    statusLabel.setStyleSheet("font-size: 16px;font-weight:bold")


# Event 추가
def addListeners():
    loginButton.clicked.connect(lambda: admin_login(idInput, passwordInput, statusLabel, statusScrollArea))
    signupButton.clicked.connect(lambda: admin_signup(idInput, passwordInput, nicknameInput, emailInput, statusLabel, statusScrollArea))
# window 설정
def showFrame():
    window.setWindowTitle('dry-web-bot')
    window.setGeometry(100, 100, 1200, 800)
    window.show()
    sys.exit(app.exec_())


def run():
    setDisplay()
    setStyles()
    addListeners()
    showFrame()

run()

