#action 1: matchstick or flashlight
light = input ("You are running through a dark jungle and find two items: a MATCHSTICK and a FLASHLIGHT. which one do you want to pick up?")
if light.lower() == "matchstick":
    print("you pick up the matchstick and strike it and for an instance the forest around you is illuminated. you see a lion  and then the match burns out. Do you want to FIGHT, RUN, HIDE behind the tree?")
    action = input()
    if action.lower() == "run":
      print("head north to a safety camp")
    if action.lower() == "fight":
      print("pick upa rock and throw aim it at it's head")
    if action.lower() == "hide":
        print("climb a tree and wait for it to leave the area")
    else :print("not applicable.")
    
    

if light.lower() == "flashlight":   
  print ("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
  action = input()
  if action.lower() =="follow":
    print("would you want to follow the path SLOWLY to maintain silence or jOGGING, until you get to the nearest cabin house")
    action = input()
    if action.lower() == "slowly":
      print("you need to follow the path slowly to avoid any noise")
    if action.lower() == "jogging":
      print("you need to jog to the nearest safety cabin quickly") 
  if action.lower() == "look":
    print("Look in the trees and you see a lion staring at you, would you FIGHT or RUN for safety")
    actiion = input()
    if action.lower() == "fight":
      print("pick up a rock and throw at its's head") 
    if action.lower() =="run":
      print("head north to a safety camp")
  else :print ("not applicable")
    


