# --encoding: utf-8--
# load wechat API
from wxpy import *
import datetime
# Download and scan QR code
bot = Bot()
# Search friend based on "Name" and "Location"
# my_friend = bot.friends().search('邹涛', sex=MALE, city="芜湖")[0]
# friend = bot.friends.search('被单')[0]
my_friend = bot.friends().search('ShengJian')[0]
"""
i = 0
for sb in my_friend:
    print(sb, "\n")
    i = i + 1
    print(i)
"""

# Get all chat group
"""
j = 0
groups = bot.groups()
for group in groups:
    print(group, "\n")
    j = j + 1
    print(j)
"""
""""""
groups = bot.groups()
my_group = groups.search("“剪头”群😜时间5-25-18")[0]
# group.send("hello world!")
#  Tiling key
tuling = Tuling(api_key='6fa0cdae99234d13aaad64c4fa95e57e')

# Automatic chat

"""
@bot.register(my_friend)
# only works for friend, not works for group
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)
"""

"""
@bot.register(my_group)
# only works for group text, not works for group other types
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)
"""


@bot.register(my_group)
# only works for friend, not works for group
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)


# Send message
# my_friend.send('Hello WeChat!')
# Send image
# my_friend.send_image('my_picture.jpg')
# Print others, group,

# """"""
# @bot.register()
# def print_others(msg):
#     print(datetime.datetime.now(), msg)
# """"""
# reply my_friend

"""
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)
"""
# Automatically receive friend request


# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     # accept request
#     new_friend = msg.card.accept()
#     # send to new friend
#     new_friend.send('哈哈，我自动接受了你的好友请求')

# 进入 Python 命令行、让程序保持运行


embed()

# 或者仅仅堵塞线程
# bot.join()