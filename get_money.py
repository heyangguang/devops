import requests
from get_login import get_wuqi_list
from clear_user import clear_user

def get_money(wuqi_list):
    url = 'http://dtsg-channel.galaxymx.com/phpDaemon/SamDefenceCN/endPlayPage.php'
    data = {
        "getCandy": 12,
        "kingIdx": 0,
        "stageIdx": 125,
        "userIdx": 41343,
        "lastLoginUDID": "cf816adc-a0fe-4c14-abc0-ce5f4aa886db",
        "playPoint": 13923
    }

    data['lastLoginUDID'], test1, user_list = wuqi_list
    clear_user(data['lastLoginUDID'], user_list)
    for i in range(60):
        ret = requests.post(url, data)
        print(ret.content)

while True:
    get_money(get_wuqi_list())