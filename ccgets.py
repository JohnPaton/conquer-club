# Functions to get various simple info from the conquerclub website

from bs4 import BeautifulSoup
import requests

def getSoup(url):
    response = requests.get(url);
    soup = BeautifulSoup(response.content, "html.parser");
    return soup;
    

def getPlayerSoup(user):
    player = getSoup('http://www.conquerclub.com/api.php?mode=player&un='+user);
    return player

def getName(idn):
    idstr = str(idn);
    player = getSoup('http://www.conquerclub.com/api.php?mode=player&u='+idstr);
    return player.username.contents[0];


def getID(user):
    player = getSoup('http://www.conquerclub.com/api.php?mode=player&un='+user);
    return player.userid.contents[0];


def getGamesSoup(user):
    url = 'http://www.conquerclub.com/api.php?mode=gamelist&events=Y&p1un='+user;
    gamessoup = getSoup(url);
    return gamessoup
