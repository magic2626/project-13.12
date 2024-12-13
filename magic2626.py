import random
def play():
    possible_actions = ["камень", "бумага" , "ножницы"]

    while True:
        user_action = input("Сделайте выбор - камень, ножницы или бумага: ").lower()

        if user_action not in possible_actions:
            print("Пожалуйста, введите правильный вариант: камень, ножницы или бумага.")
            continue

        computer_action = random.choice(possible_actions)
        print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")

        if user_action == computer_action:
            print(f"Оба пользователя выбрали {user_action}. Ничья!")
        elif (user_action == "Камень" and computer_action == "ножницы") or \
                (user_action == "бумага" and computer_action == "камень") or \
                (user_action == "ножницы" and computer_action == "бумага"):
            print("Вы победили!")
        else:
            print("Вы проиграли")

if __name__ == "__main__":
    play()




