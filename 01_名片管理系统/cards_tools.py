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

def show_all():
    print("功能：显示全部")
    print("=" * 50)

    print("姓名\t\t电话\t\tQQ\t\t邮箱")
    print("-" * 60)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    print("-" * 60)

def search_card():
    print("功能：查询名片")
    print("-" * 50)

    action_str = input("姓名：")
    for find_dict in card_list:
        if find_dict["name"] == action_str:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 60)
            print("{}\t\t{}\t\t{}\t\t{}".format(find_dict["name"],
                find_dict["phone"], find_dict["qq"], find_dict["email"]))
            print("-" * 60)

            deal_card(find_dict)

            break
    else:
        print("提示：未找到%s的名片！" % action_str)

def deal_card(find_dict):
    action_str = input("请选择操作 【1】修改  【2】删除  【0】返回上层菜单：")
    if action_str == "1":
        find_dict["name"] = card_input_info(find_dict["name"], "姓名,[回车不修改]:")
        find_dict["phone"] = card_input_info(find_dict["phone"], "电话,[回车不修改]:")
        find_dict["qq"] = card_input_info(find_dict["qq"], "QQ号码,[回车不修改]:")
        find_dict["email"] = card_input_info(find_dict["email"], "邮箱,[回车不修改]:")
        print("名片修改成功！")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("名片删除成功")

def card_input_info(dict_value, tip_message):
    find_name = input(tip_message)

    if len(find_name) > 0:
        return find_name
    else:
        return dict_value

