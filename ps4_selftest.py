import ps4
import random

#create 100 non-resistant bacteria
baclist = []
count = 0
roundlist = []
for i in range(0,1000):
    a = ps4.ResistantBacteria(.5,.5,False,.5)
    baclist.append(a)

while len(baclist) > 0:
    killlist = []
    roundcount = 0
    roundcount_lived = 0
    startcount = len(baclist)
    for bacteria in baclist:
        if bacteria.is_killed():
            roundcount +=1
            killlist.append(bacteria)
        else:
            count += 1
            roundcount_lived += 1
    for bact in killlist:
        baclist.remove(bact)
    roundlist.append(100*(roundcount/startcount))
print('non-resistant bacteria death test')
print(a.birth_prob, a.death_prob,a.resistant, a.mut_prob)
print(count, 'Rounds. Average deaths per round: ' + str(sum(roundlist)/len(roundlist)))

#create 100 resistant bacteria
baclist = []
count = 0
roundlist = []
for i in range(0,1000):
    a = ps4.ResistantBacteria(.5,.5,True,.5)
    baclist.append(a)

while len(baclist) > 0:
    killlist = []
    roundcount = 0
    startcount = len(baclist)
    for bacteria in baclist:
        if bacteria.is_killed():
            baclist.remove(bacteria)
            roundcount += 1
        else:
            count += 1
    for bact in killlist:
        baclist.remove(bact)
    roundlist.append(100*(roundcount/startcount))
print("resistant bacteria death test")
print(a.birth_prob, a.death_prob,a.resistant, a.mut_prob)
print(count, 'Rounds. Average deaths per round: ' + str(sum(roundlist)/len(roundlist)))


#test birth chance on 100
baclist = []
countofbabies = 0
countofmutants = 0
for i in range(0,1000):
    a = ps4.ResistantBacteria(.5,.5,False,.5)
    baclist.append(a)

for bact in baclist:
    newbaby = bact.reproduce(0)
    if newbaby == 0:
        pass
    else:
        countofbabies += 1
        if newbaby.resistant == True:
            countofmutants += 1
print("\nbirth chance & mutation chance")
print(countofbabies, countofmutants)

