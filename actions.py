from dragons import Ice_Dragon


def attack(target, hp):
    print(f"{target} is attacked.")
    hp = hp - 2
    print(f"{target}'s health is now {hp}")
    return hp
