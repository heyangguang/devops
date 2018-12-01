import requests
import json

# 登录
def get_wuqi_list():
    url = 'http://dtsg-channel.galaxymx.com/phpDaemon/SamDefenceCN/getLoginPage.php'
    data = {
        "pushID": "8ed932133be4a0984d1ab46121e8da8d0ec92d84",
        "appVersion": 137,
        "noKakaoMessage": 0,
        "loginType": 15,
        "open_id": "1c35fd89845b1666439e5b16586f8d60",
        "hanoId": "sst1mobicbd2c9884ed7437f970e6e481b038d00104990",
        "thumbnailPath": "",
        "isQQ": 0,
        "kakaoId": "sst1mobicbd2c9884ed7437f970e6e481b038d00104990",
        "marketType": 0
    }

    login_ret = requests.post(url, data).content
    json_login_ret = json.loads(login_ret)
    # print(json_login_ret)
    tbl_user_item_list = json_login_ret['tbl_user_item']
    uuid = json_login_ret['userBase'][0]['lastLoginUDID']
    user_list = json_login_ret['tbl_user_general']
    tab_user_item_ret = []
    user_item_ret = []
    for i in tbl_user_item_list:
        if i['level'] == "0":
            tab_user_item_ret.append(i['idx'])
    for i in user_list:
        if i['isLock'] == "0":
            user_item_ret.append(i['idx'])
    print(user_item_ret)
    return uuid, tab_user_item_ret, user_item_ret

get_wuqi_list()

