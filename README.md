# Watcher of Friends Online

The script displays a list of online friends from the most popular social network in Russia [VK.com](https://vk.com)

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

```bash
# Run without arguments for input from keyboard mode
$ python vk_friends_online.py
Введите логин Вконтакте: ***
Введите пароль Вконтакте:: ***
# or from comandline with arguments
$ python vk_friends_online.py --login *** --password ***
# in this mode script create auth.txt JSON file with auth data
# or load auth data from JSON data
$ python vk_friends_online.py --config filepath
```

### Output:
```bash
В данный момент N ваших друзей online..

1   Name     Surname            https://vk.com/id******          Mobile
2   Name2    Surname2           https://vk.com/id******          Mobile
3   Name3    Surname3           https://vk.com/id******          Mobile
N   NameN    SurnameN           https://vk.com/id******          Desktop
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
