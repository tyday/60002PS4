import ps4

#create 100 non-resistant bacteria
baclist = []
count = 0
for i in range(0,100):
    a = ps4.ResistantBacteria(.5,.5,False,.5)
    baclist.append(a)
print(a.birth_prob, a.death_prob,a.resistant, a.mut_prob)
while len(baclist) > 0:
    for bacteria in baclist:
        if a.is_killed():
            baclist.remove(bacteria)
        else:
            count += 1
print(count, count/100)

#create 100 resistant bacteria
baclist = []
count = 0
for i in range(0,100):
    a = ps4.ResistantBacteria(.5,.5,True,.5)
    baclist.append(a)
print(a.birth_prob, a.death_prob,a.resistant, a.mut_prob)
while len(baclist) > 0:
    for bacteria in baclist:
        if a.is_killed():
            baclist.remove(bacteria)
        else:
            count += 1
print(count, count/100)