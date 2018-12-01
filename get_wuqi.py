import requests
import json
from get_login import get_wuqi_list

# 获取武器
def get_wuqi(get_wuqi_list):
    url = 'http://dtsg-channel.galaxymx.com/phpDaemon/SamDefenceCN/getItemGamblePage.php'
    data = {
        "gamble_idx": 2,
        "userIdx": 41343,
        "lastLoginUDID": "b314946c-d44b-4c02-9b37-80368e46f2e9"
    }
    data['lastLoginUDID'], idx_list, user_list = get_wuqi_list
    for i in range(40):
        ret = requests.post(url, data)
        print(ret.content)

# 升级武器
def set_wuqi_level(get_wuqi_list):
    url = 'http://dtsg-channel.galaxymx.com/phpDaemon/SamDefenceCN/itemUpgradePage.php'
    data = {
        "currentLevel": "0",
        "cashType": "0",
        "userIdx": "41343",
        "idx": "41388",
        "lastLoginUDID": "bb3fcf83-e21b-4ab5-80b1-dfa9000f722c",
        "useItemPosion": "0",
    }


    data['lastLoginUDID'], idx_list, user_list = get_wuqi_list


    for index in idx_list:
        print(index)
        data['idx'] = index
        status = True
        level = 0
        data['currentLevel'] = level
        while status:
            ret = requests.post(url, data).content
            json_ret = json.loads(ret)
            try:
                level = json_ret['item_upgrade'][0]['items'][0]['level']
            except Exception as e:
                status = False
            data['currentLevel'] = level
            print(json_ret)

get_wuqi(get_wuqi_list())
set_wuqi_level(get_wuqi_list())