# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    collection = "user"
    user_type = Field()                 # 账号类型
    answer_count = Field()              # 回答
    headline = Field()                  # 简介
    url_token = Field()
    id = Field()
    articles_count = Field()            # 文章
    type = Field()
    name = Field()                      # 用户名
    url = Field()                       # 用户主页地址
    gender = Field()                    # 性别
    follower_count = Field()            # 关注者
    avatar_url = Field()                # 头像地址
    badge = Field()                     # 认证信息

    vip_info = Field()                  # VIP
    is_vip = Field()


