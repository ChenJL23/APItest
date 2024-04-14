import json
import os

current_path = os.path.dirname(__file__)
data_dir = os.path.dirname(current_path) + '\\data\\'


def get_inrm_login_data():
    with open(data_dir + 'ihrm_login.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        data_list = []
        for itme in data:
            data_list.append((itme['unname'], itme['pwd'], itme['code'], itme['message']))
    return data_list


if __name__ == '__main__':
    login_data = get_inrm_login_data()
    print(login_data)
