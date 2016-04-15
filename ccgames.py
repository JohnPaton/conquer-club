# For returning info on cc games

from ccgets import *

# class for single games
class Game:
    def __init__(self, gsoup):
        self.idn = gsoup.game_number.string;
        self.playerids = self.getIDs(gsoup); # List of player ids *in order*
        self.eliminations = self.getElims(gsoup); #{'a' : ['b','c']} = 'a' eliminated 'b' and 'c'
        self.wonby = self.checkWinner(gsoup);
        self.type = self.gameType(); # For filtering out bot games


    def checkWinner(self,gsoup):
        wonby = '';
        if gsoup.game_state.string == 'F':
            wonby = gsoup.players.find('player',state="Won").string;

        return wonby

    # List Player IDs in order
    def getIDs(self,gsoup):
        playerids = [];
        for p in gsoup.players.findAll('player'):
            playerids.append(p.string);
                
        return playerids

    def gameType(self):
        gtype = 'humans'
        
        botids = ['667743','651617','688572','688573','651618','688574','688578',
                  '688577','688576','655218','688575'];
        
        for p in self.playerids:
            if p in botids and gtype != 'bots':
                gtype = 'bots';

        return gtype
    
    # Elimination summary: {'eliminator':[victims]}
    def getElims(self,gsoup):
        eliminations = {};
        
        for p in self.playerids:
            eliminations[p] = [];

        for e in gsoup.events.findAll('event'):
            ev = e.string; # event string
            if 'eliminated' in ev:
                #pns = [int(s) for s in ev.split() if s.isdigit()]; #black magic
                pns = []
                for s in ev.split():
                    if s.isdigit():
                        pns.append(int(s));
                        
                killer = self.playerids[pns[0]-1];
                killed = self.playerids[pns[1]-1];
                eliminations[killer].append(killed);
                
        return eliminations



# getGames: Creates list of game objects for all games (and bot games) of user
def getGames(user):
    url = 'http://www.conquerclub.com/api.php?mode=gamelist&events=Y&p1un='+user;
    gamessoup = getSoup(url);
        
    games = [];
    botgames = [];

    pgs = [int(s) for s in gamessoup.page.string.split() if s.isdigit()]
    
    if pgs[1] > 1: # Deal with multiple pages if neccessary
        for pg in range(1, pgs[1]+1):
            urlpg = url + '&page='+str(pg);
            gamessoup = getSoup(urlpg);
            for gsoup in gamessoup.findAll('game'):
                g = Game(gsoup);
                if g.type == 'bots':
                    botgames.append(g);
                else:
                    games.append(g);

    else:
        for gsoup in gamessoup.findAll('game'):
            g = Game(gsoup);
            if g.type == 'bots':
                botgames.append(g);
            else:
                games.append(g);

    return [games,botgames]
