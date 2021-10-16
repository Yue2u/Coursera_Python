import requests


ACCESS_TOKEN = 'b997830cb997830cb997830c34b9e1df23bb997b997830cd9b4f3a95596518c6e5bd79a'


def calc_age(uid):
    get_usr_id_url = f'https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}'
    user_id = requests.get(get_usr_id_url).json()["response"][0]["id"]

    get_friends_list_url = \
        f'https://api.vk.com/method/friends.get?v=5.71&access_token={ACCESS_TOKEN}&user_id={user_id}&fields=bdate'
    user_friends_list = requests.get(get_friends_list_url).json()["response"]["items"]

    friends_ages_dict = {}

    for friend in user_friends_list:
        if ("bdate" not in friend) or (friend["bdate"].count('.') != 2):
            continue
        age = 2021 - int(friend["bdate"].split('.')[-1])
        if age not in friends_ages_dict:
            friends_ages_dict[age] = 0
        friends_ages_dict[age] += 1

    result_ages_list = [(age_, count_) for age_, count_ in friends_ages_dict.items()]
    result_ages_list.sort(key=lambda x: x[0])
    result_ages_list.sort(key=lambda x: x[-1], reverse=True)
    
    return result_ages_list


if __name__ == '__main__':
    res = calc_age('224935503')
    print(res)
