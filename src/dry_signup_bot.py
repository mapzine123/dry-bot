import schedule
import time
import bot_actions

# schedule 설정 ( bot이 일정 시간마다 할 일 )
schedule.every(20).seconds.do(bot_actions.admin_sign_up)

while True:
    schedule.run_pending()
    time.sleep(1)
#

