import os
import random
import requests
import discord
import json
from thefuzz import fuzz

from dotenv import load_dotenv
from discord.ext import commands
from difflib import SequenceMatcher


## baseURL https://api.wiseoldman.net/v2/players/:username

## Stuff with tasks
points = 'points.txt'
task = 'task.txt'
streak = 'streak.txt'
kills = 'kills.txt'

bul_txt = 'bul_log.txt'
myhyll_txt = 'myhyll_log.txt'
elis_txt = 'elisp_log.txt'
petter_txt = 'petter_log.txt'
foose_txt = 'foose_log.txt'
sven_txt = 'sven_log.txt'
jansson_txt = 'jansson_log.txt'



##Kills
bultimer_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}
kylmyhl_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}
elisp_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}
petter_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}
foose_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}
sven_hans_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}
snowman121120_log = {'Barrows': 0, 
            'Giant Mole': 0,
            'Deranged Archaeologist': 0, 
            'Dagannoth Kings': 0, 
            'Sarachnis': 0, 
            'Kalphite Queen': 0,
            'Kree\'arra': 0,
            'Commander Zilyana': 0,
            'General Graardor': 0,
            'K\'ril Tsutsaroth': 0,
            'Corporeal Beast': 0,
            'Nex': 0,
            'Chaos Fanatic': 0,
            'Crazy archaeologist': 0,
            'Scorpia': 0,
            'King Black Dragon': 0,
            'Chaos Elemental': 0,
            'Calvar\'ion & Vet\'ion': 0,
            'Spindel & Venenatis': 0,
            'Artio & Callisto': 0,
            'Zulrah': 0,
            'Vorkath': 0,
            'Phantom Muspah': 0,
            'The Nightmare & Phosani\'s Nightmare': 0,
            'Duke Sucellus': 0,
            'The Leviathan': 0,
            'The Whisperer': 0,
            'Vardorvis': 0,
            'The Gauntlet': 0,
            'The Corrupted Gauntlet': 0,
            'TzTok-Jad': 0,
            'TzKal-Zuk': 0,
            'Tempoross': 0,
            'Wintertodt': 0,
            'Zalcano': 0}



users_and_points = {'bultimer': 0, 
                    'kylmyhl': 0, 
                    'elisp.': 0, 
                    'petter#8901': 0, 
                    'foose': 0, 
                    'sven_hans': 0, 
                    'snowman121120': 0}

users_and_task = {'bultimer': '', 
                    'kylmyhl': '', 
                    'elisp.': '', 
                    'petter#8901': '', 
                    'foose': '', 
                    'sven_hans': '', 
                    'snowman121120': ''}

users_and_streak = {'bultimer': 0, 
                    'kylmyhl': 0, 
                    'elisp.': 0, 
                    'petter#8901': 0, 
                    'foose': 0, 
                    'sven_hans': 0, 
                    'snowman121120': 0}

users_and_kills = {'bultimer': 0, 
                    'kylmyhl': 0, 
                    'elisp.': 0, 
                    'petter#8901': 0, 
                    'foose': 0, 
                    'sven_hans': 0, 
                    'snowman121120': 0}

disc_to_osrs = {'bultimer': 'grindalf', 
                'kylmyhl': 'myhyll', 
                'elisp.': 'elis p', 
                'petter#8901': 'faladorabie', 
                'foose': 'foose', 
                'sven_hans': 'svenhans', 
                'snowman121120': 'jarn-jorgen'}

with open(points, 'r') as f:
    users_and_points = json.load(f)

with open(streak, 'r') as f:
    users_and_streak= json.load(f)

with open(task, 'r') as f:
    users_and_task = json.load(f)

with open(kills, 'r') as f:
    users_and_kills = json.load(f)

with open(bul_txt, 'r') as f:
     bultimer_log = json.load(f)

with open(myhyll_txt, 'r') as f:
     kylmyhl_log = json.load(f)

with open(elis_txt, 'r') as f:
     elisp_log = json.load(f)

with open(petter_txt, 'r') as f:
     petter_log = json.load(f)

with open(foose_txt, 'r') as f:
     foose_log = json.load(f)

with open(sven_txt, 'r') as f:
     sven_hans_log = json.load(f)

with open(jansson_txt, 'r') as f:
     snowman121120_log = json.load(f)



world_bosses = ['Barrows', 
              'Giant Mole',
              'Deranged Archaeologist', 
              'Dagannoth Kings', 'Sarachnis', 
              'Kalphite Queen',
              'Kree\'arra',
              'Commander Zilyana',
              'General Graardor',
              'K\'ril Tsutsaroth',
              'Corporeal Beast',
              'Nex']
    
wilderness_bosses = ['Chaos Fanatic',
                         'Crazy archaeologist',
                         'Scorpia',
                         'King Black Dragon',
                         'Chaos Elemental',
                         'Calvar\'ion & Vet\'ion',
                         'Spindel & Venenatis',
                         'Artio & Callisto']
    
instanced_bosses = ['Zulrah',
                        'Vorkath',
                        'Phantom Muspah',
                        'The Nightmare & Phosani\'s Nightmare',
                        'Duke Sucellus',
                        'The Leviathan',
                        'The Whisperer',
                        'Vardorvis']
    
# slayer_bosses = ['Grotesque Guardians',
#                  'Abyssal Sire',
#                  'Kraken',
#                  'Cerberus',
#                  'Thermonuclear smoke devil',
#                  'Alchemical Hydra']
    
minigame_bosses = ['The Gauntlet',
                       'The Corrupted Gauntlet',
                       'TzTok-Jad',
                       'TzKal-Zuk']
    
skilling_bosses = ['Tempoross',
                       'Wintertodt',
                       'Zalcano']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

save_counter = 0

##Så jävla fult jag dör
def handle_log(name):
    if(name == 'bultimer'):
        return bultimer_log
    if(name == 'kylmyhl'):
        return kylmyhl_log
    if(name == 'elisp.'):
        return elisp_log
    if(name == 'petter#8901'):
        return petter_log
    if(name == 'foose'):
        return foose_log
    if(name == 'sven_hans'):
        return sven_hans_log
    if(name == 'snowman121120'):
        return snowman121120_log
    
# def update_kc(bosses, log):
#     threshhold = 0.8
#     for key in bosses.keys():
#         if(key )

no_boss = ['abyssal_sire', 
           'alchemical_hydra', 
           'bryophyta', 
           'cerberus', 
           'chambers_of_xeric', 
           'chambers_of_xeric_challenge_mode', 
           'grotesque_guardians', 
           'hespori', 
           'kraken', 
           'mimic', 
           'obor', 
           'skotizo', 
           'theatre_of_blood', 
           'theatre_of_blood_hard_mode', 
           'thermonuclear_smoke_devil',
           'tombs_of_amascut', 
           'tombs_of_amascut_expert',
           'dagannoth_prime', 
           'dagannoth_rex', 
           'dagannoth_supreme', 
           'nightmare', 
           'phosanis_nightmare', 
           'artio', 
           'callisto', 
           'calvarion', 
           'vetion', 
           'venenatis', 
           'spindel']
dagannoths = ['dagannoth_prime', 'dagannoth_rex', 'dagannoth_supreme']
nightmare = ['nightmare', 'phosanis_nightmare']
artio_callisto = ['artio', 'callisto']
vetion_calvarion = ['calvarion', 'vetion']
spindel_venenatis = ['venenatis', 'spindel']

@bot.command(name='complete')
async def complete_task(ctx):
    if(users_and_task[ctx.author.name] == ''):
        await ctx.send('You do not have a task to complete. Get a new task with the command **!task**.')
        return
    
    log_to_update = handle_log(ctx.author.name)
    log_to_update[users_and_task[ctx.author.name]] = users_and_kills[ctx.author.name]

    users_and_streak[ctx.author.name] += 1
    users_and_task[ctx.author.name] = ''
    streak = users_and_streak[ctx.author.name]

    points_gained = 1

    if(streak % 5 == 0):
        users_and_points[ctx.author.name] += 5
        points_gained = 5
        await save(ctx)
    else:
        users_and_points[ctx.author.name] += 1
    await ctx.send(f'**{ctx.author.nick}** has completed **{users_and_streak[ctx.author.name]}** tasks in a row and gained **{points_gained}** **DoDDo** point and now has a total of **{users_and_points[ctx.author.name]}** **DoDDo** points!')

async def update_bosses(ctx, arg):
    base_url = 'https://api.wiseoldman.net/v2/players/'
    response = {'username': 'response'}
    user = arg
    json_string = requests.get(f'{base_url}{user}', json=response)
    response = json_string.text
    response_dict = json.loads(response)
    osrs_boss_data = response_dict['latestSnapshot']['data']['bosses']
    log_to_update = handle_log(ctx.author.name)
    
    for boss_name in osrs_boss_data.keys():
        if(boss_name in dagannoths):
            log_to_update['Dagannoth Kings'] += osrs_boss_data.get(boss_name).get('kills')
        if(boss_name in vetion_calvarion):
            log_to_update['Calvar\'ion & Vet\'ion'] += osrs_boss_data.get(boss_name).get('kills')
        if(boss_name in artio_callisto):
            log_to_update['Artio & Callisto'] += osrs_boss_data.get(boss_name).get('kills')
        if(boss_name in spindel_venenatis):
            log_to_update['Spindel & Venenatis'] += osrs_boss_data.get(boss_name).get('kills')
        if(boss_name in nightmare):
            log_to_update['The Nightmare & Phosani\'s Nightmare'] += osrs_boss_data.get(boss_name).get('kills')
        if(boss_name in no_boss):
            continue
        kc = osrs_boss_data.get(boss_name).get('kills')
        if(kc == -1):
            kc = 0
        filtered_boss = max(log_to_update.keys(), key=lambda i:fuzz.partial_ratio(i.lower(), boss_name))
        log_to_update[filtered_boss] = kc

@bot.command(name='log')
async def get_log(ctx):
    monkas_emoji = discord.utils.get(bot.emojis, name='Monkas')
    yaz_emoji = discord.utils.get(bot.emojis, name='yaz')
    await update_bosses(ctx, disc_to_osrs[ctx.author.name])
    log = handle_log(ctx.author.name)
    to_print = f'# Boss Log for {ctx.author.nick} {str(yaz_emoji)}\n'
    for entry in log.items():
        to_print += f'**{entry[0]}  - ** ***Kills***: {entry[1] if entry[1] > 0 else "Unranked  " + str(monkas_emoji)}\n'

    await ctx.send(to_print)

@bot.command(name='skip')
async def skip_task(ctx):
    if(users_and_task[ctx.author.name] == ''):
        await ctx.send('You do not have a task to skip... What are you doing????')
        return
    if(users_and_points[ctx.author.name] < 2):
        await ctx.send(f'You cannot skip your current task. Skipping a task costs **2** **DoDDo** points and you have **{users_and_points[ctx.author.name]}**. Complete your current task before returning.')
        return
    users_and_task[ctx.author.name] = ''
    users_and_points[ctx.author.name] -= 2
    await ctx.send('You successfully cancelled your task. You **n00ba**...')
    
@bot.command(name='points')
async def get_points(ctx):
    await ctx.send(f'**{ctx.author.nick}** has **{users_and_points[ctx.author.name]}** **DoDDo** points!')

@bot.command(name='task')
async def do_boss(ctx):
    current_boss = users_and_task[ctx.author.name]
    if(current_boss != ''):
        await ctx.send(f'You are already assigned **{users_and_kills[ctx.author.name]}** **{current_boss}**. Go DoDDo.')
        return
    boss = random.choice(world_bosses + minigame_bosses + skilling_bosses + instanced_bosses + wilderness_bosses)
    kc = random.randint(1, 50)
    if(boss == 'TzTok-Jad' or boss == 'TzKal-Zuk'):
        kc = 1

    users_and_task[ctx.author.name] = boss
    users_and_kills[ctx.author.name] = kc
    await ctx.send(f'You have been assigned to execute **{kc}** **{boss}**. \n\nRemember to type **!complete** when you have completed your task!')
    
@bot.command(name='raid')
async def do_raid(ctx):
    osrs_raids = ['Chambers of Xeric.', 'Theatre of Blood.', 'Tombs of Amascut.']
    reasons = ['You should go and lose some money at ','Try your luck at ','If you want a bad time, go do ']
    raid_response = random.choice(osrs_raids)
    reason_response = random.choice(reasons)
    await ctx.send(reason_response + raid_response)

@bot.command(name='save')
async def save(ctx):
    ngest_emoji = discord.utils.get(bot.emojis, name='ngest')
    with open(points, 'w') as fi:
            fi.write(json.dumps(users_and_points))
    with open(streak, 'w') as fi:
        fi.write(json.dumps(users_and_streak))     
    with open(task, 'w') as fi:
        fi.write(json.dumps(users_and_task))
    with open(kills, 'w') as fi:
        fi.write(json.dumps(users_and_kills))

    with open(bul_txt, 'w') as fi:
        fi.write(json.dumps(bultimer_log))
    with open(myhyll_txt, 'w') as fi:
        fi.write(json.dumps(kylmyhl_log))
    with open(elis_txt, 'w') as fi:
        fi.write(json.dumps(elisp_log))
    with open(petter_txt, 'w') as fi:
        fi.write(json.dumps(petter_log))
    with open(foose_txt, 'w') as fi:
        fi.write(json.dumps(foose_log))
    with open(sven_txt, 'w') as fi:
        fi.write(json.dumps(sven_hans_log))
    with open(jansson_txt, 'w') as fi:
        fi.write(json.dumps(snowman121120_log))
        
    await ctx.send(f'Saved data in case of crash... {str(ngest_emoji)}')

@bot.command(name='exit')
async def close(ctx):
    if(ctx.author.name == 'bultimer'):
        with open(points, 'w') as fi:
            fi.write(json.dumps(users_and_points))
        with open(streak, 'w') as fi:
            fi.write(json.dumps(users_and_streak))     
        with open(task, 'w') as fi:
            fi.write(json.dumps(users_and_task))
        with open(kills, 'w') as fi:
            fi.write(json.dumps(users_and_kills))

        with open(bul_txt, 'w') as fi:
            fi.write(json.dumps(bultimer_log))
        with open(myhyll_txt, 'w') as fi:
            fi.write(json.dumps(kylmyhl_log))
        with open(elis_txt, 'w') as fi:
            fi.write(json.dumps(elisp_log))
        with open(petter_txt, 'w') as fi:
            fi.write(json.dumps(petter_log))
        with open(foose_txt, 'w') as fi:
            fi.write(json.dumps(foose_log))
        with open(sven_txt, 'w') as fi:
            fi.write(json.dumps(sven_hans_log))
        with open(jansson_txt, 'w') as fi:
            fi.write(json.dumps(snowman121120_log))
        await ctx.send('The DoDDo Master is going on vacation. CyaL8R Suqhas.')
        await bot.close()

bot.run(TOKEN)

# Opening the file and sending it directly to the channel:

# with open('my_image.png', 'rb') as f:
#     picture = discord.File(f)
#     await channel.send(file=picture)
# Passing the file name directly:

# await channel.send(file=discord.File('my_image.png'))