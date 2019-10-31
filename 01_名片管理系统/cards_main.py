#!/usr/bin/env python3
import cards_tools

while True:

    cards_tools.show_card()

    action_str = input("请选则操作功能：")

    if action_str in ( "1", "2", "3"):
        if action_str == "1":
            cards_tools.new_card()

        elif action_str == "2":
            cards_tools.show_all()

        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")

        break

    else:
        print("你输入的不正确，请重新选择！")
