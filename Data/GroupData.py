class group_data(object):
    branch = 'yandex.ru'

    GLOBAL = {
        'time_element_Wait': 30,

        'Browser': {
            'Name': 'chrome',
            'headless': False,
            'Remote': False
        },
        'yandex.ru': {
            'Name': 'yandex.ru',
            'main_page': 'https://yandex.ru/',
            'Internal_Link': 'https://yandex.ru/',
            'External_Link': 'https://yandex.ru/',
            'API_Internal_Link': '',
            'API_External_Link': '',
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'Login': "",
                    'password': "",
                }
            },
            'SQL_SERVER': {
                'SERVER': '',
                'DATABASE': '',
                'user': '',
                'password': '',
                'DRIVER': '',
            }

        },
    }

    access_token = "",
    token_type = "",
    expires_in = ""
