print('Вы проснулись в капсуле. Вам тяжело дышать, перед вашим лицом запотевшее стекло и \
сенсорный дисплей для ввода код-пароля.')
stop = False
playerName = 8
while stop != True:
    actions_for_first = {1: "Попробовать открыть дверь", 2: "Попробовать ввести код", 3: "Осмотреть себя"}
    print("\nВаши действия?")
    for i in actions_for_first.keys():
        print(f"[{i}]{actions_for_first[i]}")
    PlayerChoice = int(input("Ввод: "))
    if PlayerChoice in actions_for_first:
        if PlayerChoice == 1:
            print('Потратив множество сил, у вас так и не вышло открыть крышку.')
        elif PlayerChoice == 2:
            code = int(input('Введите код: '))
            if code == playerName:
                print('Крышка открылась. Вы вылезли из капсулы.')
                print("Вы попали в комнату, где стоят 5 анабиозных капсул. Перед вами коридор.")
                stop = True
            else:
                print('Неверный код')
        elif PlayerChoice == 3:
            print('Осмотрев себя вы обнаружили на себе бейджик с числом', playerName)
