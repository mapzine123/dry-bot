import json
import requests
import datetime

# URL 상수 정의
SIGN_UP_URL = 'http://localhost:8080/api/admins/sign-up'
LOGIN_URL = 'http://localhost:8080/api/admins/login'


# Request Header
HEADERS = {
    'Content-Type': 'application/json'
}

sign_up_data = {
    'id': 'bot1',
    'password': '12341234**',
    'nickname': 'bot1',
    'email': 'bot1@naver.com'
}

def admin_sign_up(data):
    json_data = json.dumps(data)
    response = requests.post(SIGN_UP_URL, data=json_data, headers=HEADERS)
    if response.status_code == 200:
        print(response.status_code)

def admin_login(idInput, passwordInput, statusLabel, statusScrollArea):
    data = {
        'id': idInput.text(),
        'password': passwordInput.text()
    }
    text = statusLabel.text()
    time = getTime()
    try:
        json_data = json.dumps(data)
        response = requests.post(LOGIN_URL, data=json_data, headers=HEADERS)
        text += "\n[" + time + "] [" + idInput.text() + "]" + " login : " + str(response.status_code)
        statusLabel.setText(text)
    except:
        text += "\n[" + time + "] [" + idInput.text() + "]" + " login : error"
        statusLabel.setText(text)

    statusScrollArea.verticalScrollBar().setValue(statusScrollArea.verticalScrollBar().maximum())

def admin_signup(idInput, passwordInput, nicknameInput, emailInput, statusLabel, statusScrollArea):
    data = {
        'id': idInput.text(),
        'password': passwordInput.text(),
        'nickname': nicknameInput.text(),
        'email': emailInput.text()
    }
    text = statusLabel.text()
    time = getTime()

    try:
        json_data = json.dumps(data)
        response = requests.post(SIGN_UP_URL, data=json_data, headers=HEADERS)
        text += "\n[" + time + "] [" + idInput.text() + "]" + " sign-up : " + str(response.status_code)
        statusLabel.setText(text)

    except:
        text += "\n[" + time + "] [" + idInput.text() + "]" + " sign-up : error"
        statusLabel.setText(text)

def getTime():
    current_time = datetime.datetime.now()

    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time