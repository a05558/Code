#!/usr/bin/env python3

card_list = []

def show_card():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("*" * 50)

def new_card():
    print("功能：新增名片")
    print("-" * 50)

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入邮箱：")

    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}
    card_list.append(card_dict)
    print("%s的名片添加成功" % name_str)
    print("-" * 50)


