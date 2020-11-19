#The Great Engineering Text Adventure
#Authors: Mitchell Lemieux, Tyler Kashak
#Music: Brian, Erik What music do we have lol?
#Start Date: April 14th, 2018
#Library of Items and Locations
#Latest Edit 22/2/2019
"""
Rules for Writing Objects in the Eng Phys Text Adventure
0. ALWAYS check the paramaters of the object. If unsure check GameClasses.py for the constructor
1. Use " (\S)" instead of "\n" for newline characters
2. If using ANY quotes (" or ') ONLY use ' inside strings.
The " quote is used to define the string boundry and any in the sentence will break the string.
ex) "You think to yourself 'Gee, do I like quotes'! 'Lets go somewhere!' "
not) "You think to yourself "Gee, do I like quotes"! "Lets go somewhere"! "
3. When an attribute is "None" it needs to be capitalized as such: "None"
4. When Naming a MAP

Obsolete: 5. When puting a needed or dropped object.name in an interact it MUST be lowercase.
All object keys in the game are stored lowercase and used to throw a key error but are now changed in the constructor
"""


from GameClasses import *
import csv
from Colour import *

# these define bounds of the list constructor MAPS1, they control this main loop
# TODO Get rid of these ranges and make them dimension specific with dimension dictionary
XRANGE = 10  # when changing these also change the values in the CreativeMode.load() function
YRANGE = 10
ZRANGE = 4
DRANGE = 6  # Dimensional range of the map, i.e. number of different buildings/dimensions with interiors + overworld
# TODO IF game starts to slow down due to size of MAPS1 empty spaces in this definition:
#  we'll have to define some funky magic to define different map dictionaries
#  OR Redefine how the constructor works so don't have to loop through huge empty space to define an new map location

def Reset():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    global INTERACT1

    # Using List comprehensions to define the null map space of the game for objects to be put into
    # Ineffecient due to number of empty spaces and each dimension being 10x10x5 but whatever for now
    MAPS1 = [ [ [ [None for dim in range(DRANGE)] for z in range(ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE) ]


    LOCATIONS1=[
    # --- OVERWORLD: Dimension 0 ---

    # --- CAPSTONE ROOM: Dimension 1 ---
    Map("THE ECLIPSE", (0, 0, 0, 1), "THE ECLIPSE~:\n","AW DANG The Eclipse! But yeah this windshield is a bit much", ('l','b','d', 'u'), True),
    Map("ZebraShark", (0, 1, 0, 1), "ZebraShark~:\n", "Where are they? O.m.g. is that a pool downstairs?",('l','d', 'u'), True),
    Map("T.A. Area", (0, 2, 0, 1), "T.A. Area~:\n","Is this where the PSRs get lost? Also just storage space for STARS", ('f','l','d', 'u'), True),

    Map("S.T.A.R.S.", (1, 0, 0, 1), "S.T.A.R.S.~:\n",
            "S.T.A.R.S. PLEASE WORK.\nYou see a man wearing a pink shirt and a giant robot point a cannon where ever he goes.\nIs this how the world ends?",
            ('b','d', 'u'), True),  # S.T.A.R.S. System T69
    Map("FRAS", (1, 1, 0, 1), "FRAS~:\n", "Yeah that's a tank. This is a 3D printed Tank.", ('d', 'u'), True),
    Map("Capstone Doorway", (1, 2, 0, 1), "Capstone Doorway~:\n", "This beeping door is the bane of your existance on late nights", ('f','d','u'), True),

    Map("NANOrims", (2, 0, 0, 1), "NANOrims~:\n", "NANNNOOORYMMSS.", ('r','d','u'), True),
    Map("Milli", (2, 1, 0, 1), "Milli~:\n", "Great Job Mili!", ('r','d','u'), True),
    Map("Circuit Smart", (2, 2, 0, 1), "Circuit Smart~:\n",
            "(Print text of spagetti)\nIf you unplugged one wire of this these people would go insane.", ('f', 'r','u','d'),
            True),

    #Map("Electronics Lab", (0, 1, 0, 1), "Peter's Lab~:\n", "I'm just glad to not have to be in here anymore.",( 'l','f','u','d'), True),
    #Map("Peter Jonasson's Office", (0, 1, 0, 1), "Peter Johnason's Office~:\n", "The grand sorcerer's mystic place",('b', 'l','r','u','d'), True),

    # --- GREEN LAKE: Dimension 2 ---
    Map("Green Lake",(0,0,0,2),"~~","You wake up in a peaceful place. The water is rushing by down on a nearby like. The leaves are blowing in the wind casting shadows in the green clearing. You feel the warm sun kissing your skin. (\S)Standing just in front of log house you see an old black lab. Sitting patiently waiting for you to throw his ball. He sits beside a sign that reads: Freds' Place.",('f','b','l','r','u','d'),True)

    ]


    # TODO Sort items back into "Head", "Body", "Hand", "Off-hand", "Special" (quest items). Via CSVs is the easiest way
    ITEMS1 = [
    Equipment("Polaroid Photograph", (None), "PolaroidPhoto.jpg",
                  "What? Do people still make these? Next thing you know you'll find an 8-inch floppy disk laying around. (\S)The photo shows you smashed out of your mind at the " + mapcolour + "Phoenix" + textcolour + ". Looks like a good time.",
                  "off-hand", (0, 0, 0), -2),
    Equipment("Tyler's Visor Glasses", (None), "FastGlasses.jpg","Damn, you are now travelling waaaay to fast. Slow down dude!", "head", (1, 5, 35), ""),
    Equipment("Tyler's Big Hits Shirt", (None), "BigHits.jpg", "The Shirt of the Hero of Kyvach!", "body",(10, 5, 5), ""),
    Equipment("Tyler's Hulk Hands", (None), "HulkHands.jpg", "These pack a serious punch...", "hand", (15, 5, 20),""),
    Equipment("Tyler's Green Bang Bong", (None), "GBB.jpg","The sacred glass flute providing righteous tokes since '69.", "off-hand", (69, 69, 69), ""),
    Equipment("Tony Hawk Shirt", (None), "TonyHAwkShirt.jpg", "A shirt personally made by tony hawk!", "body", (5,5,5),""),
    Equipment("Big Hits Shirt", (None), "BigHits.jpg", "The Shirt of the Hero of Kyvach!", "body", (10,5,5),""),
    Equipment("Helm of Orin Bearclaw", (None), "SkullHelmet.jpg", "A note left beside the helmet says 'A leftover relic from a purple hero'", "head", (35,30,10),""),


        # Green Lake Items
    Equipment("Tennis Ball", (0, 0, 0, 2), "TennisBall.jpg","The slobery wet ball that belongs to Fred. He's probably looking for it.", "hand", (1, 1, 1), ""),
    Equipment("Dog biscuit", (0, 0, 0, 2), "DogBiscuit.jpg", "Probably better known as a cookie. One of Fred's favourite snacks.", "off-hand", (1, 1, 1), 3),
    Equipment("Softwood 2x4 Stud", (0, 0, 0, 2), "Soft2x3Stud.jpg", "A prime peice of Douglas Fir. Useful to be made into whatever you can imagine", "off-hand", (1, 1, 1), ""),

    ]  # DON"T FORGET TO REMOVE THE LAST COMA!


    ENEMIES1 = [
    Enemy("Brendan Fallon","What's up dude? I'm here to bless up your shit.\nDo you have my lunch box?",None,(9999,9999,9999),999,"green bang bong","Brendan Fallon's lunchbox","THANKS! TOKE UP MY DUDES!","",False),


        # --- Green Lake People ---
    Animal("Fred the Good Boy", "You talk to Fred. His wise eyes stare at you. It's almost as if he understands what you're saying but he'd rather have have you play with the ball.", (0,0,0,2),(9999,9999,9999),9999,"tennis ball","tennis ball","Fred barks happily. He chews on it for a second and then kicks it back happily to you.","","He smiles at you happily! His tail wags but you can tell he just wants to play with the ball.",True)

    ]

    #Stationary Objects to interact with
    #Interact(name,location,info,Sinfo,need,drop)
    INTERACT1 = [
    Interact("Rules Sign", (None), "It reads: (\S)THERE ARE NO RULES", "", "", "", False),
    Interact("Lenovo Laptop", (None), "This heap of computing majesty could block bullets... I think...",
                 "You plug in the Eng Phs USB Pen.\nYou find all of 2P04 files, who uses FlexPDE anymore? You also find a \nweird exe called the Eng Phys Text Adventure! That sounds like fun.\nYou hear a drumming in your ears, is that coming from the pen?",
                 "eng phys usb pen", "", False),
    # Green Lake Interactables
    #Interact("Lake Painting", (3, 0, 1, 0), "A painting of a beautiful lake. It brings you peace.", "You feel a pull. All of a sudden you're being pulled into the painting and all around you it's getting bright. (\S)You wake up to the sound of birds chirping and a soft breeze.", "old car keys", None,True),
    Interact("Portkey", (0, 0, 0, 2), "This portkey looks like the way back. Whatever magic brought you here must be related to this lake.", "Your world compresses as you're pulled violently into something. (\S)You're back in the Art Museum. Were you ever gone?", None, None,True),
    Interact("Rick's Crafting Bench", (0, 0, 0, 2), "This bench can create anything made of wood or diamond.","You spend hours crafting the device to the precision you need. It's perfect.","softwood 2x4 stud", "sharpxchange",True),
    ]

Reset()

# TODO If Rebuild: Make this into a dictionary with an adjacency list (Graph/path). Not sure if in object or not
def WorldMap():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    for i in LOCATIONS1:
        position = i.location
        x = position[0]
        y = position[1]
        z = position[2]
        dim = position[3]
        MAPS1[x][y][z][dim] = i
    for i in ENEMIES1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].placeEnemy(i)
        else:
            i.location = (None,None,None,None)
        if i.need:
            i.need = i.need.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
        if i.drop:
            i.drop = i.drop.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
    for i in ITEMS1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].placeItem(i)
        else:
            i.location = (None,None,None,None)
    for i in INTERACT1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].placeItem(i)
        else:
            i.location = (None,None,None,None)
        if i.need:
            i.need = i.need.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
        if i.drop:
            i.drop = i.drop.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
    return tuple(MAPS1)

def ItemDictionary():
    global ITEMS1
    ItemDictionary = {}
    for item in ITEMS1:
        name = item.name.lower()
        ItemDictionary.update({name:item})
    return ItemDictionary

def EnemyDictionary():
    global ENEMIES1
    EnemyDictionary = {}
    for enemy in ENEMIES1:
        name = enemy.name.lower()
        EnemyDictionary.update({name:enemy})
    return EnemyDictionary

def InteractDictionary():
    global INTERACT1
    InteractDictionary = {}
    for interact in INTERACT1:
        name = interact.name.lower()
        InteractDictionary.update({name:interact})
    return InteractDictionary

