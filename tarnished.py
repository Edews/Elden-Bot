import os
import random
import discord
import re
from dotenv import load_dotenv

load_dotenv()
token = os.environ["DISCORD_TOKEN"]
my_guild = os.environ["DISCORD_GUILD"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)

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

def stringGen(word = ""):
    #Select a random word from a random wordlist
    if(word == ""):
        wordList = wordPools[random.randint(0, len(wordPools)-1)]
        word = wordList[random.randint(0, len(wordList)-1)]

    #attach the random word to the templates
    string = [word+" ahead", "No "+word+" ahead",word+" required ahead","Be wary of "+word,"Try "+word,
        "Likely "+word,"First off, "+word,"Seek "+word,"Still no "+word+"...","Why is it always "+word+"?",
        "If only I had a "+word+"...","Didn't expect a "+word+"...","Visions of "+word+"...",
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

@client.event
async def on_ready():
    print(f"{client.user} is connected to the following guild:\n")
    for guild in client.guilds:
        if guild.name == my_guild:
            break
        print(f"{guild.name} (id: {guild.id})")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_content = message.content.lower()
    if "!message" in message_content or "!msg" in message_content:
        
        #50-50 whether or not a conjunction should be used
        isConjunction = random.randint(0,1)
        #If conjunction should be used then it will add a conjunction and another string generator
        if isConjunction == 1:
            messageString = stringGen()+conGen()+stringGen()
        #If no conjunction, only one string generator function call is made
        else:
            messageString = stringGen()
        await message.channel.send(messageString)
        print(message.author.name+" from \""+message.guild.name+"\" got the message \""+messageString+"\"\n")

    if "!cmessage" in message_content or "!cmsg" in message_content:
        splitMessage = re.split(' !cmessage | !cmsg ',message_content)
        customWord = splitMessage[-1]

        isConjunction = random.randint(0,1)
        if isConjunction == 1:
            conOrder = random.randint(0,1)
            if conOrder == 0:
                messageString = stringGen(customWord)+conGen()+stringGen()
            else:
                messageString = stringGen()+conGen()+stringGen(customWord)
        else:
            messageString = stringGen(customWord)
        await message.channel.send(messageString)
        # print(message.author.name+" from \""+message.guild.name+"\" got the message \""+messageString+"\"\n")
        print(message.author.name+" from \""+message.guild.name+"\" generated a custom message\n")

client.run(token)