# -*- coding: UTF-8 -*-
from twilio.rest import Client

# 下面认证信息的值在你的 twilio 账户里可以找到
account_sid = "AC548709ce4a81028a1c134af773035859"
auth_token = "7453b46af8caecffe4c033ad3ce68a18"

client = Client(account_sid, auth_token)

message = client.messages.create(to="+8618640543236",  # 区号+你的手机号码
                                 from_="+16157898047",  # 你的 twilio 电话号码
                                 body="你好啊~")

# call = client.calls.create(
#     to="+8618640543236",  # 区号+你的手机号码
#     from_="+16157898047",  # 你的 twilio 电话号码
#     url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"
# )
