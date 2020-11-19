# ENG PHYS TEXT  ADVENTURE
# Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
# First written on Mar  21,2019 by Brendan Fallon:
"""
This game_scripts_2017.py file is used to write the story, quests, and events of the game by changing objects based on conditions.
EngPhysStory() is the main Eng Phys storyline  and returns once its finished
Quests generally only happen once and are sidequests unrelated to the storyline that do something special
Events are reoccurring based on the condition for the game.
    This also includes PORTALS which is teliportation using interacts
"""


from GameFunctions import *  # importing the global dictionaries/values
import time
import Opening  # used for the EPTA all the way down quest
import os  # used to put files in the cache folder
import AsciiArt
from Colour import *

global QUESTS

# List of quests and storylines that then get's built into a dictionary
# This dictionary is just flags to keep track of quest completion to advance or end quests
# it's defined here for convience of working but is dealing with a global variable defined in gamefunctions

questlist = [
    # story
    'hooded man',
    # sidequests
    'rules sign',
    'EPTA all the way down'
    # events


    ]

    # PHILpocalypse  # After you give Phil is braces he sobers up and becomes tired Phil.
    # After he asks for a coffee "Man I could really use a coffee but I don't want to spend the money
    # if you give him coffee he gives you a free wish "OH YEAH I AM CAFFINATED. I feel like I can do anyhing!"
    # If you give him a cappuccino the PHILpocalypse storyline begins:
    # You see his eyes dilate "OH YEAH I"M FEELING GREAT", He snaps his fingers and there's a flash.
    # You wake in JHE field "Not again" and everyone on the map is gone. Eventually you meet a Phil clone

# building the quest dictionary because you can't just overwrite the dumb dictionaries for some dumb reason
for quest in questlist:
    QUESTS.update({quest: 1})




def story(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope



    # Talk to hooded man
    # if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
    #     MAPS[4][4][1][0].placeEnemy(ENEMIES["dr. kitai"])
    #     MAPS[2][4][2][0].placeEnemy(ENEMIES["dr. preston"])
    #     MAPS[1][6][2][0].placeEnemy(ENEMIES["dr. lapierre"])
    #     MAPS[5][4][1][0].removeEnemy(ENEMIES["hooded man"])
    #     ENEMIES["hooded man"].location = (None, None, None, None)  # the location should be set to none but for some reason it's fine
    #     ENEMIES['hooded man'].spoke = False
    #     QUESTS["talk to mysterious man"] = 0

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def sidequests(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope


    # --- Side Quests ---
    # -- Secret Spaces --


    # # -- Rules Sign --
    # if INTERACT["rules sign"].quest and QUESTS['rules sign']:  # Once the sign is read
    #     MAPS[2][3][1][0].removeInteract(INTERACT["rules sign"])
    #     INTERACT["rules sign"].location = (None,None,None,None)
    #     printT( "The sign " +indicatecolour+ "disappears" +textcolour+ " in a flash of " +indicatecolour+ "smoke" +textcolour+ ". You look around. Are you still dreaming?")
    #     QUESTS["rules sign"] = 0



    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


# If Events list gets to long can make it its own file
def events(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope



    # Killcount counter in player will trigger the police eventually


    # --- Portals ---
    # TODO Build in this portal fucntionality into INTERACTS or maybe just places with doors

    # # To Green Lake
    # if INTERACT["lake painting"].quest:
    #     PLAYER.location = [0,0,0,2]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
    #     CurrentPlace = MAPS[0][0][0][2]
    #     CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
    #     INTERACT["lake painting"].need = None
    #     printT("(\S)You no longer need the keys to get into this place.")
    #     INTERACT["lake painting"].quest = False
    #
    # # Back to Art Museum
    # if INTERACT["portkey"].quest:
    #     PLAYER.location = [3,0,1,0]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
    #     CurrentPlace = MAPS[3][0][1][0]
    #     CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
    #     INTERACT["portkey"].quest = False

    # -- EBTA All the way Down --
    # when you put the pen in the laptop it opens the thing
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']:
        # TODO as homework see if there's a way to do this with recursion instead of simulating it
        # Would put drums if there was sound effect
        playgame = input('========================================================================\nWould you like to play? \n').lower()
        if playgame == "yes" or playgame == "y":
            printT("You click on the game and it begins in the terminal. The " +red+ "drumming intensifies" +textcolour+ ". You're not sure if you made the right choice.")
            printT("======================================================================== (\S) (\S)")
            import CreativeMode  # this is imported here not at the top to avoid recursive import errors (show up as global names not being defined in the compiler)
            QUESTS['EPTA all the way down'] = 0  # Truns off the quest, has to be before the game saves so the quest is ended when you come back
            save_game(str(GAMEINFO['layersdeep']))  # saving game to be reloaded after death or won the game
            log = GAMEINFO['log']  # keeps the log as a temporary variable to keep a running log in the nested game
            Opening.Opening()
            newplayername = input("First, what is your name?\n")
            layers = GAMEINFO['layersdeep']  # saves layersdeep to a temporary variable for after the load
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game("basegame")  # should display the exact start
            GAMEINFO['layersdeep'] = layers + 1   # increments the global layers deep because you're now in a lower level, using the memory of the local variable

            GAMEINFO['playername'] = PLAYER.name = newplayername  # this is done for the log
            GAMEINFO['gamestart'] = time.time()  # Settign the game and timestart for for this layer
            GAMEINFO['timestart'] = GAMEINFO['gamestart']
            # Passes the log and adds onto it to keep a HUGE running log (TODO Make this more effecient with log appending)
            GAMEINFO['log'] = log + [str(playgame), "--NESTED GAME--", GAMEINFO['layersdeep'], GAMEINFO['versionname'],
                                     GAMEINFO['playername'], time.ctime(GAMEINFO['timestart']),
                                     "--LOG START--"]  # log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
        elif playgame == "no" or playgame == "n":
            printT("You " +indicatecolour+ "decide against it" +textcolour+ ", fearing the worst. You safely edject the pen, drop it on the floor, and " +red+ "smash" +textcolour+ " it to pieces. Better safe than sorry. (\S)" +lightblue+ "The drumming stops" +textcolour+ ".)")
            printT("========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log
        else:
            printT("" +losecolour+ "It was a yes or no question" +textcolour+ ". When you look back the files are " +losecolour+ "gone" +textcolour+ ". (\S)Even the FlexPDE code. Good riddance.")
            printT("========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log




    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS