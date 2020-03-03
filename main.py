import requests


class VK:
    # APP_ID = '7344387'
    # OAUTH_URL = 'https://oauth.vk.com/authorize'
    # OAUTH_PARAMS = {
    #     'client_id': APP_ID,
    #     'display': 'page',
    #     'scope': 'status',
    #     'response_type': 'token',
    #     'v': '5.52',
    # }


    @staticmethod
    def get_token():
        ACCESS_TOKEN = 'e1eb099b0fae3c4391a190b1363ac157172acf0358a7051f4f1eb3790a45547fc78c20686f8c0a9db4264'
        return ACCESS_TOKEN


class User(VK):
    __FRIENDS =[]

    def __init__(self, user_id):
        self.user_id = user_id
        self.__FRIENDS = self.update_friends_list()


    def update_friends_list(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'user_id': self.user_id,
                'access_token': VK.get_token(),
                'v': '5.52',
            }
        )
        list = response.json()['response']['items']
        return list


    def get_friends(self):
        return self.__FRIENDS


    def __and__(self, other):
        return set(self.__FRIENDS) & set(other.get_friends())


    def __str__(self):
        return f'https://vk.com/id{self.user_id}'

user1 = User(220914059)
user2 = User(46743995)


print(f'Common friends for user1({user1.user_id}) and user2({user2.user_id}) are: {user1 & user2}')

print(user1)
print(user2)

