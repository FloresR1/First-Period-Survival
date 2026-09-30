# First Period Survival Game

def ask(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print("Choose one of:", ", ".join(options))


state = "home"       # home | street | school | class | late
time = 3             # how much time you have
passes = 0           # remembers whether you got a hall pass

print("You wake up late! You have to make it to first period.")

while state not in ("class", "late"):
    print(f"\n[STATE: {state.upper()} | Time: {time} | Passes: {passes}]")

    if state == "home":
        choice = ask(
            "Do you (r)un out the door or (e)at breakfast? ",
            ["r", "e"]
        )

        if choice == "r":
            print("You grab your backpack and run outside!")
            time -= 1
            state = "street"
        else:
            print("You eat breakfast, but you lose some time.")
            time -= 2
            state = "street"

    elif state == "street":
        choice = ask(
            "You see the bus! Do you (b)oard it or (w)alk to school? ",
            ["b", "w"]
        )

        if choice == "b":
            print("You catch the bus just in time!")
            passes += 1
            time -= 1
        else:
            print("You walk quickly toward school.")
            time -= 1

        if time <= 0:
            state = "late"
        else:
            state = "school"

    elif state == "school":
        if passes > 0:
            print("You have a pass, so you can quickly get through the hallway.")
            time += 1
        else:
            print("The hallway is crowded and you get slowed down.")
            time -= 1

        if time <= 0:
            state = "late"
        else:
            state = "class"

print(f"\n[STATE: {state.upper()} | Time: {time} | Passes: {passes}]")

if state == "class":
    print("You made it to first period on time! 🎉")
else:
    print("You arrived late to class. Better luck tomorrow!")
