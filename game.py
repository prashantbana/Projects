def dark_room(a):
    print "You have enterd a %s." % a
    print "1. Look for a match box"
    print "2. Try to find your way out of the dark  secret room."
# start here . Make 2 cases for match box. In case 1 users hand is caught in a bear trap and user is bleeding. In case 2 he finds the match box . For 2nd option the user is crawling blind and enters a cave/ dungeon blindly probably falls of the staircase OR for input 2 he falls into a pit full of snakes / spikes.
    
# Defining more functions will help us in inteconnecting two or more levels at some point in the game.Plan out more stages , import some of the scenes from movies to make it more interesting. Introduce in the game.

#PROGRAM STARTS HERE
print "You enter a dark room with two doors. Do go through door #1 or door #2?"

door = raw_input(">")

if door == "1": # loop for door 1 
    print "There's a giant bear here eating near the main entrance of the castle. What do you do?"
    print "1. Shout and try to scare the bear."
    print "2. Pick up the sword."
    print "3. Sneak into the secret room."  # condition for bear = 3 is not done. 
    bear = raw_input(">")
     
    if bear == "1": # BEAR 1 
        print "The bear eats your face off. Good job!"
    elif bear == "2": # BEAR 2
        print "The bear is startled.What do you do?"
        print "1. You charge and stab the bear."
        print "2. You make a run towards the main gate." # left to program.
        
        action = raw_input("> ")
        
        if action == "1": # action 1
            print "The bear is wounded and moving slow.You too are hurt.What do you do?" # new stage starting . Bear fight. 
            print "1. Douse the lights to sneak up on the bear."
            print "2. You charge with all the strength you're left with."
            
            
            final = raw_input("> ") 
            
            if final == "1": # FINAL 1
                print "He sniffed you first and tore you to pieces."
            elif final == "2": # FINAL 2 
                print "The bear has seen you.Type attack to kill the bear."
                kill = []
                for i in range(0 , 5):# NEW ADDITION TO THE GAME. ASKING USER FOR INPUT .KILLING THE BEAR.
                    
                    if i == 0:
                        i = raw_input("> ")
                        print "You just made it angry.Attack the bear again."
                    if i == 1:
                        i = raw_input("> ")
                        print "Good he's scared now, keep attacking him."
                    if i == 2:
                        i = raw_input("> ")
                        print "You just stabbed him in the eye.Now you can take him down easily"
                    if i == 3:
                        i = raw_input("> ")
                        print "He's tired and spent.Do not stop."
                    if i == 4:
                        print "Give him a final blow."
                        i = raw_input("> ")
                        print "His head rolls over to your side.\n"
 
                  
                print "You have finally killed the bear.But you're too weak.What do you do?" # new stage starting . Old witch.
                print "1. Ask help from the old witch."
                print "2. Patch yourself up and try to reach some help before you bleed out ?"
                print "3. You see a bottle of rum and cozy up with it."
                
                
                last = raw_input("> ") 
            
                if last == "1": # LAST 1
                    print "Old witch agrees to help you." 
                    print "You enter witches dodgy hut and pass out as she starts reading some enchantments"
                    print "You open your eyes to find that you're tied to the bed.To be continued ..." # expand this even more. Continue from here.
                elif last == "2": # LAST 2
                    print "You have entered the castle only to find that everyone is dead."
                    print "You are bleeding fast . What do you do ?" # continue from here.
                elif last == "3": # LAST 3
                    print "You are the true embodiment of Jack Sparrow. You die drunk and happy alongside the bear."
                else: # LAST else 
                    print "You are now a part of the limbo and will wander in the empty streets looking for redemption. "
            
            else: # else for FINAL
                print "You have somehow managed to escape into the forbidden forest.There are three things infront of you . What do you do?"
                print "1. There's some mushrooms."
                print "2. There's a plank."
                print "3. There's a key." # start from here . Build some story . The user goes ahead and theres a river full of crocodiles . Use the key to unlock the door at the end of this stage . After opening the gate the user can be introduced into any stage earlier described. Use river , Zombies and whitewalkers to reach the castle where the user has to fight a three headed monster to enter the gate. For suspense use signs like WARNINGS and WISE OLD MAN.
                
        elif action == "2": # ACTION 2 . when user chooses to make a run towards the main gate. 
            print "The bear attacked you!"
            dark_room("dark room")
            
        else:
            print "You panicked, there was no where to go, but atleast you helped the bear with his dinner." # getting printed in many options . look for error .
    
    elif bear == "3": # BEAR = 3 
        print "You have entered the secret room, its dark " 
        dark_room("secret room")
        
    else:
        print "Turns out you're his dinner for tonight." 
        
elif door == "2":  # loop for door 2
    print "Yoy stare into the endless abyss at cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revlovers yelling melodies."
        
    insanity = raw_input("> ")
        
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!."
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!."
      
else:
    print "You stumble around and fall on a knife and die. Good job!."
