from ccgets import *
from ccgames import *

# Player: creates object with information on player with username user
class Player:
    def __init__(self, user):
        psoup = getPlayerSoup(user);
        self.idn = psoup.userid.string;
        self.name = user;
        
        [self.games, self.botgames] = getGames(user);
        
        self.kills = self.getKills();
        self.nkills = sum(self.kills.values());
        
        self.killedby = self.getDeaths();
        self.ndeaths = sum(self.killedby.values())
        
        self.nplayed = int(psoup.games_completed.string);
        self.nwon = int(psoup.games_won.string);

    # Make kills dictionary {id : kills}
    def getKills(self):
        kills = {}
        nkills = 0;
        
        for game in self.games:
            if game.eliminations[self.idn]:
                victims = game.eliminations[self.idn];
                for v in victims:
                    if v not in kills.keys():
                        kills[v] = 1;
                    else:
                        kills[v] += 1;

        return kills

    # Make deaths dictionary {id : kills}
    def getDeaths(self):
        killedby = {};
        ndeaths = 0;
        
        for game in self.games:
            for killer in game.eliminations.keys():
                if self.idn in game.eliminations[killer]:
                    if killer in killedby.keys():
                        killedby[killer] += 1;
                    else:
                        killedby[killer] = 1;

        return killedby
