#This is the Bugs/To-do/Done list
* appearently labeling TODO is the convention to mark things in code
* [Markdown Cheat Sheet: https](//github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Markdown Style Guide](https://guides.github.com/features/mastering-markdown/)
* [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/)
# **Bugs**
- [ ] If crashes then gave saves may break the game due to giving the object then brekaing on quest
- [ ] When game is loaded with mismatched items it will break in the middle of the loading loop causing many of the
    things to not be loaded even if they're fine. It needs a save reconsiler that removes the wrong object.
- [ ] still a problem with layers, saving and loading, hope it works for 0.27 release
- [ ] Save files in the wrong location? Where is Doug?
- [ ] Can't play as tyler Kashak after you stop
- [ ] When you exit from the start screen or otherwise the error catcher catches you
- [ ] Check to make sure nest game, correct times, and everything add up
- [ ] Die after winning the game you still get the credits and win dialog, AND THEN CONTINUE. Okay that's bad. - 0.30 Nov. 22, 2020
- [ ] 0.30_dev_neut_complete.txt doesn't "REALLY" do everything in the game. Don't care for 2017 but future games.
A true scripted playthrough should do an actual 100% of the game (test all major functions, all scripted events, go everywhere, kill everyone etc)


        

# 0.31 Anniversary update
- [x] Attempt to see if you can get different modules to import conditionally - Nov. 19, 2020
- [x] Seperate all hard-coded objects to completly seperate the game engine and game
- [ ] Properly rewrite gamefunctions into gameclasses player methods, year them, and maybe even remove script interfaces. 
        Rename gamefunctions to enginefucntions
    - [x] Refactor **Equip** into method and test
    - [X] Refactor **Drop** into method and test
    - [ ] Refactor **Move** into method and test
    - [ ] Refactor **Combat** into method and test
    - [ ] Refactor **Attack** into the combat method and test
    - [ ] Refactor **Talk** into method and test
    - [ ] Refactor **stats** into method and test
    - [ ] Refactor **Inspect examine** into method and test
    - [ ] Refactor **Inspect use** into method and test
    - [ ] Refactor **Inventory** into method and test
    - [ ] Refactor **Eat** into method and test
         
        
- [ ] Get rid of total imports (* brining everything into namespace) 
        so can clearly see and define how to do import dependencies

- [ ] Create selector to select year and import properly
- [ ] Make so you can pause, exit to the start screen
- [ ] Make a build and playtest origional version of the game
- [ ] See if there's a way to refresh the game? If not no worries

- [ ] Attempt to run EPTA in future versions of the game

- 2017 = 2017-2018 Eng Phys Text Adventure (Origional Game)
- 2018 = 2018-2019 Eng Phys Text Adventure (Capstone Room)
- 2019 = 2019-2020
- 2020 = 2020-2021 COVID Text Adventure  (Hollywood)

# 0.32 Nevada Engine Refactor
- [ ] Packaging 8 variables into a game-state which you pass along
- [ ] Text parser becomes controlls or interpreter
- [ ] Everything should be in the main loop
- [ ] All objects/save files shouldn't be script based. Should be file based.
- [ ] Redo Map into adjacency lists
- [ ] Objects for interfaces
- [ ] Maybe do component game objects for all game_objects.




# Done so Far
- Slowly coverting almost everything to PP8 variable naming (something_something for everything except MyClasses)
- Seperated game objects and gamescripts from old version
- Adding scriptting functions to further encapsulate the game engine and game code
- Added killing BF acheivement
- Added not being able to attack an animal. BH punches you.

# **Fixed Bugs**
**Includes version, date, bug, and bug fix**
- 0.30 Nov 22, 2020: If you kill BF his dead course follows you around. This is actually hilarious so I left it in. No fix
- If you die after beating the game you can keep replaying so you're pretty much invincible. 
LOL I don't care 2017, it was finished so not fixing. If you beat the game you get to be invincible XD
- In Python3 input can't take ANSII escape characters so had to fix all those

# Advice from Dr. Carette/G-Scale
- Break things down into tasks that with a resolution of taking you 1 hour to complete. 
    If you don't know how to break that task down then your only task is to figure out how to break that down.
- Sometimes can start with something that's good enough and then begin refactoring the most important bits at a time.
    (That's what I'm doing here with the NEVADA game engine)

# Things to Read
* https://dzone.com/articles/python-thread-part-1
* https://www.python-course.eu/python3_inheritance.php

