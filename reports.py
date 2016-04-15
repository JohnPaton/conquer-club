#Different types of reports and helper functions

from player import Player
from ccgames import Game
from ccgets import *
from reports import *


# topN: Returns a list of [key, value] for the top N values in the
# dictionary. Prioritizes display of keys in priority in event of a tie.
def topN(d,n,priority=[]):
    tops = [];

    for i in range(0,n):
        tops.append(['',0]);
        
    for k in d.keys():
        placed = False;
        for i in range(0,n):
            if d[k] > tops[i][1] and not placed:
                tops.insert(i, [k, d[k]]);
                tops.pop()
                placed = True;

        if (k in priority) and (d[k] == tops[-1][1]):
                tops[-1] = [k, d[k]];

    return tops;
            

# killsReport: Reports on kills and deaths of user
def killsReport(user,priority=[]):
    p = Player(user);

    print('Elimination report for '+user+':\n')
    print('Top 3 killed:')
    tops = topN(p.kills, 3, priority);
    for t in tops:
        print(getName(t[0])+': '+str(t[1]))
    
    print('\nTop 3 killed by:')
    tops = topN(p.killedby, 3, priority);
    for t in tops:
        print(getName(t[0])+': '+str(t[1]))

    kd = p.nkills/p.ndeaths;
    print('\nTotal Kills: '+str(p.nkills))
    print('Total Deaths: '+str(p.ndeaths))
    print('K/D: %.2f' % kd)


# shensReport: Kills report on Shenanigans members
def shensReport():
    shens = ['BigMoney!','ChefBoyRDave','GenghisConnor','tfroe','HeavenlyHalo',
             'PCStalder','natehildy','Fenzik']

    # Get Player IDs
    shenids = []
    for u in shens:
        shenids.append(getID(u))

    for user in shens:
        killsReport(user,shenids)
        print('-----------------')
