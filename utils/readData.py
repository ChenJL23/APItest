import json
import os

current_path = os.path.dirname(__file__)
proj_dir = os.path.dirname(current_path)


def get_data(filepath):
    with open(proj_dir + filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data_list = []
        for itme in data:
            tmp = tuple(itme.values())
            data_list.append(tmp)
    return data_list


if __name__ == '__main__':
    login_data = get_data('/data/ihrm_login.json')
    print(login_data)
