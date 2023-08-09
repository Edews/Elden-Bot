import os
import random
from PIL import Image, ImageDraw, ImageFont

enemies = ["enemy","weak foe","strong foe","monster","dragon","boss","sentry","group",
            "pack","decoy","undead","soldier","knight","cavalier","archer","sniper",
            "mage","ordnance","monarch","lord","demi-human","outsider","giant","horse",
            "dog","wolf","rat","beast","bird","raptor","snake","crab","ill-omened creature",
            "prawn","octopus","bug","scarab","slug","wraith","skeleton","monstrosity"]

people = ["tarnished","warrior","swordfighter","knight","samurai","sorcerer","cleric","sage","merchant",
        "teacher","master","friend","lover","old dear","old codger","angel","fat coinpurse","pauper",
        "good sort","wicked sort","plump sort","skinny sort","lovable sort","pathetic sort","strange sort",
        "nimble sort","laggardly sort","invisible sort","unfathomable sort","giant sort","sinner","thief",
        "liar","dastard","traitor","pair","trio","noble","aristocrat","hero","champion","monarch","lord","god"]

things = ["item","necessary item","precious item","something","something incredible","treasure chest","corpse",
        "coffin","trap","armament","shield","bow","projectile weapon","armor","talisman","skill","sorcery",
        "incantation","map","material","flower","grass","tree","fruit","seed","mushroom","tear","crystal",
        "butterfly","bug","dung","grace","door","key","ladder","lever","lift","spiritspring","sending gate",
        "stone astrolabe","birdseye telescope","message","bloodstain","erdtree","Elden Ring"]

battleTactics = ["close-quarters battle","ranged battle","horseback battle","luring out","defeating one-by-one",
                "taking on all at once","rushing in","stealth","mimicry","confusion","pursuit","fleeing",
                "summoning","circling around","jumping off","dashing through","brief respite"]

actions = ["attacking","jump attack","running attack","critical hit","two-handing","blocking","parrying",
            "guard counter","sorcery","incantation","skill","summoning","throwing","healing","running",
            "rolling","backstepping","jumping","crouching","target lock","item crafting","gesturing"]

situations = ["morning","noon","evening","night","clear sky","overcast","rain","storm","mist","snow",
            "patrolling","processions","crowd","surprise attack","ambush","pincer attack","beating to a pulp",
            "battle","reinforcements","ritual","explosion","high spot","defensible spot","climbable spot",
            "bright spot","dark spot","open area","cramped area","hiding place","sniping spot","recon spot",
            "safety","danger","gorgeous view","detour","hidden path","secret passage","shortcut","dead end",
            "looking away","unnoticed","out of stamina"]

places = ["high road","checkpoint","bridge","castle","fort","city","ruins","church","tower","camp site",
        "house","cemetary","underground tomb","tunnel","cave","evergaol","great tree","cellar","surface",
        "underground","forest","river","lake","bog","mountain","valley","cliff","waterside","nest","hole"]

directions = ["east","west","south","north","ahead","behind","left","right","center","up","down","edge"]

bodyParts = ["head","stomach","back","arms","legs","rump","tail","core","fingers"]

affinities = ["physical","standard","striking","slashing","piercing","fire","lightning","magic",
            "holy","poison","toxic","scarlet rot","blood loss","frost","sleep","madness","death"]

concepts = ["life","death","light","dark","stars","fire","order","chaos","joy","wrath","suffering",
            "sadness","comfort","bliss","misfortune","good fortune","bad luck","hope","despair",
            "victory","defeat","research","faith","abundance","rot","loyalty","injustice","secret",
            "opportunity","pickle","clue","friendship","love","bravery","vigor","fortitude","confidence",
            "distracted","unguarded","introspection","regret","resignation","futility","on the brink",
            "betrayal","revenge","destruction","recklessness","calmness","vigilance","tranquility",
            "sound","tears","sleep","depths","dregs","fear","sacrifice","ruin"]

phrases = ["good luck","look carefully","listen carefully","think carefully","well done","I did it!",
        "I've failed...","here!","not here!","don't you dare!","do it!","I can't take this...",
        "don't think","so lonely...","here again...","just getting started","stay calm","keep moving",
        "turn back","give up","don't give up","help me...","I don't believe it...","too high up",
        "I want to go home...","it's like a dream...","seems familiar...","beautiful...",
        "you don't have the right","are you ready?"]

conjunctions = ["and then ","or ","but ","therefore ","in short ",
                "except ","by the way ","so to speak ","all the more ",","]

wordPools = [enemies,people,things,battleTactics,actions,situations,
            places,directions,bodyParts,affinities,concepts,phrases]

def stringGen():
    #Select a random word from a random wordlist
    wordList = wordPools[random.randint(0, len(wordPools)-1)]
    word = wordList[random.randint(0, len(wordList)-1)]
    #attach the random word to the templates
    string = [word+" ahead", "No "+word+" ahead",word+" required ahead","Be wary of "+word,"Try "+word,
        "Likely "+word,"First off, "+word,"Seek "+word,"Still no "+word+"...","Why is it always "+word+"?",
        "If only I had a "+word+"...","Didn't expect "+word+"...","Visions of "+word+"...",
        "Could this be a "+word+"?","Time for "+word,word+", O "+word,"Behold, "+word+"!",
        "Offer "+word,"Praise the "+word,"Let there be "+word, "Ahh, "+word+"...",
        word, word+"!",word+"?",word+"..."]
    return string[random.randint(0, len(string)-1)]

def conGen():
    conj = conjunctions[random.randint(0,len(conjunctions)-1)]
    if conj == ",":
        return conj+"\n"
    else:
        return "\n"+conj


def EldenThings():
    # Open an Image
    img = Image.open('pope.png')
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    fonttype = 'arial.ttf'
    fontsize = 16
    W, H = img.size
    # w, h = I1.textsize(stringGen())
    _, _, w, h = I1.textbbox((0, 0), "#JustEldenThings",font=ImageFont.truetype(fonttype, fontsize))
    # Add Text to an image
    I1.text(((W-w)/2,(H-h)/2), "#JustEldenThings",font=ImageFont.truetype(fonttype, fontsize), fill='white')
    _, _, w, h = I1.textbbox((0, 0), stringGen(),font=ImageFont.truetype(fonttype, fontsize))
    I1.text(((W-w)/2,((H-h)/2)+20), stringGen(),font=ImageFont.truetype(fonttype, fontsize), fill='white')
    # Display edited image
    img.show()
        
# #50-50 whether or not a conjunction should be used
# isConjunction = random.randint(0,1)

# #If conjunction should be used, repeats above procedure
# if isConjunction == 1:
#     message = stringGen()+conGen()+stringGen()
#     print(message)
# else:
#     message = stringGen()
#     print(message)
EldenThings()
