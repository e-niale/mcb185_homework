# saving throws!!
import random

def savingthrow(trials, dc):
    success_normal = 0
    success_advantage = 0
    success_disadvantage = 0

    # normally
    for i in range(trials):
        if random.randint(1, 20) >= dc:
            success_normal += 1

    # advantage
    for i in range(trials):
        advroll = 0
        advroll1 = random.randint(1, 20)
        advroll2 = random.randint(1, 20)
        if advroll1 > advroll2:
            advroll = advroll1
        else:
            advroll = advroll2
        if advroll >= dc:
            success_advantage += 1
    
    # disadvantage
    for i in range(trials):
        disroll = 0
        disroll1 = random.randint(1, 20)
        disroll2 = random.randint(1, 20)
        if disroll1 < disroll2:
            disroll = disroll1
        else:
            disroll = disroll2
        if disroll >= dc:
            success_disadvantage += 1
            
    print(dc, success_normal / trials, success_advantage / trials, success_disadvantage / trials)

print('DC', 'Normal', 'Advantage', 'Disadvantage')
savingthrow(1000, 5)
savingthrow(1000,10)
savingthrow(1000,15)


