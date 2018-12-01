import requests
from get_login import get_wuqi_list

def clear_user(uuid, user_list):
    url = 'http://dtsg-channel.galaxymx.com/phpDaemon/SamDefenceCN/tw_sellGeneralAll.php'
    data = {
        "generalIdxs": "1098505",
        "userIdx": "41343",
        "lastLoginUDID": "cf816adc-a0fe-4c14-abc0-ce5f4aa886db"
    }

    data['lastLoginUDID'] = uuid
    for i in user_list:
        data['generalIdxs'] = i
        ret = requests.post(url, data).content
        print(ret)