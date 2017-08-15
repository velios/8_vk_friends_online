import vk
import argparse
import logging
import getpass


APP_ID = 6146727
DEFAULT_AUTH_FILE_PATH = 'auth.txt'
VERBOSITY_TO_LOGGING_LEVELS = {
    0: logging.WARNING,
    1: logging.INFO,
    2: logging.DEBUG,
}


def get_user_login_and_password_from_cmd():
    user_login = input('Введите логин: ')
    user_password = getpass.getpass('Введите пароль: ')
    return user_login, user_password


def get_online_vk_friends(vk_login, vk_password, scope=None):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=vk_login,
        user_password=vk_password,
        scope=scope
    )
    vk_api = vk.API(session)
    online_friends_ids_list = vk_api.friends.getOnline()
    online_friends_list = vk_api.users.get(user_ids=online_friends_ids_list, fields='online')
    return online_friends_list


def output_friends_to_console(online_friends_list):
    print('В данный момент {} ваших друзей online.\n'.format(len(online_friends_list)))
    for index, friend_data in enumerate(online_friends_list):
        if 'online_mobile' in friend_data:
            friend_from_mobile_text = 'Mobile'
        else:
            friend_from_mobile_text = 'Desktop'
        print('{4:<3} {0:10} {1:20} https://vk.com/id{2:<15} {3}'.format(friend_data['first_name'], friend_data['last_name'],
                                                                         friend_data['uid'], friend_from_mobile_text, index + 1))
    print('\n')


def configurate_cmd_parser():
    parser_description = ("\nСкрипт показывает кто из ваших друзей вконтакте онлайн в данный момент.\n")
    cmd_arguments = argparse.ArgumentParser(description=parser_description)
    cmd_arguments.add_argument('--verbose', '-v', action='count', default=0)
    return cmd_arguments.parse_args()


if __name__ == '__main__':
    cmd_arguments = configurate_cmd_parser()
    logging_level = VERBOSITY_TO_LOGGING_LEVELS[cmd_arguments.verbose]
    logging.basicConfig(level=logging_level)

    vk_login, vk_password = get_user_login_and_password_from_cmd()
    try:
        friends_online = get_online_vk_friends(vk_login, vk_password, scope='friends, users')
        output_friends_to_console(friends_online)
    except Exception:
        print('Ошибка авторизации')
