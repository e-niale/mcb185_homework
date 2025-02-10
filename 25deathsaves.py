# death saves, dc < 10 fail, dc >= 10 success, 3 fails you die, 3 success you win, roll 20 you revive, roll 1 you fail twice
import random

def deathsaves(trials):
    stable = 0
    dead = 0
    revived = 0
    for i in range(trials):
        success = 0
        fail = 0
        roll = random.randint(1, 20)
        while True:
            if roll == 20:
                revived += 1
                break
            elif roll == 1:
                fail += 2
            elif roll >= 10:
                success += 1
            else:
                fail += 1
            if success == 3:
                stable += 1
                break
            elif fail >= 3:
                dead += 1
                break
    print(stable / trials, dead / trials, revived / trials)

print("%Stabilized", "%Dead", "%Revived")
deathsaves(100)
        