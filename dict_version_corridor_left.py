stop = False
print('Идя по коридору, слева вы видите уборную комнату')
while stop != True:
    print('\nВаши действия?')
    actions = {1: "Попробовать открыть дверь", 2: "Идти дальше", 3: "Вернуться в холл"}
    for i in actions.keys():
        print(f"[{i}]{actions[i]}")
    PlayerChoice = int(input("Ввод: "))
    if PlayerChoice == 1:
        print('Вы осмотрели дверь, после чего попытались ее открыть, но понимаете что дверь закрыта')
        stop = True
    elif PlayerChoice == 2:
        print("Пройдя дальше, вы попадаете в комнату со аварийную комнату, тут вы наблюдаете 4 спасательных шатла \
и какой-то шкаф")
        stop = True
    elif PlayerChoice == 3:
        print('Пройдя по коридору обратно, вы вернулись в холл.\nНа стене только доска почета, а прямо напротив вас \
большой иллюминатор.\nСлева от иллюминатора лестница на второй этаж.\nНа разных концах холла - коридоры.')
        stop = True
    else:
        print("Неправильный выбор")