"""
    双色球问题：
    红球：6个 ，1--33之间的
"""
# import random
#
# list_ticket = []
#
# while len(list_ticket) < 6:
#     random_number = random.randrange(1, 33)
#     if random_number not in list_ticket:
#         list_ticket.append(random_number)
#
# list_ticket.append(random.randrange(1,16))
# print(list_ticket)

list_ticket = []

while len(list_ticket) < 6:
    red_number = int(input("请输入第%d红球号码:" % (len(list_ticket) + 1)))
    if red_number > 33 or red_number < 1:
        print("号码不在范围内")
    elif red_number in list_ticket:
        print("号码已经重复")
    else:
        list_ticket.append(red_number)
