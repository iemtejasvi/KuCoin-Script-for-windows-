import time
import requests
import random
import urllib.parse
import os
import signal
import itertools
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for color output
init(autoreset=True)

# Global variable to control the main loop
running = True
encoded_data_list = []

# Extensive collection of funny messages to keep users engaged
funny_messages = [
    "Grabbing coins like a pro! 💸", "Tapping so fast even Kucoin can't keep up! 🚀",
    "Did someone say 'free money'? 🎁", "Hustling harder than your morning coffee ☕",
    "Legend has it, I'm still tapping... 😎", "More taps, more power! 🔥",
    "Hey Kucoin, how about a bonus? 😜", "Why work when I can tap all day? 💼",
    "One tap at a time... greatness is coming! 💪", "Making money, one tap at a time 🤑",
    "This is so satisfying! Tap-tap-tap 🎮", "Someone call Elon, I’m going to the moon! 🌕",
    "A few more taps and we’ll hit the jackpot! 💰", "Is this what rich feels like? 🤩",
    "I could do this all day… oh wait, I am! 🔄", "Just casually tapping my way to wealth 💵",
    "The only exercise I do is tapping 💪", "Kucoin thinks I'm a bot. I’m just too fast! ⚡",
    "I wonder if Kucoin is jealous of my skills 🤔", "Almost there… the treasure chest awaits! 🎉",
    "This is my kind of workout! 🏋️‍♂️", "Tap faster! The coins are waiting! 🏃‍♂️",
    "Another day, another fortune 💎", "Watch out, Jeff Bezos. I’m coming for you 🛩️",
    "Who needs the lottery when you have this? 🎰", "I’m basically printing money at this point 💸",
    "Tapping into success, one click at a time 🖱️", "I could do this with my eyes closed 💤",
    "More taps, more stacks 💸", "Money, meet my bank account 💼",
    "Almost done… Time for that yacht purchase? 🛥️", "With every tap, I’m getting closer to my island 🌴",
    "Tapping isn’t just a skill, it’s an art 🎨", "Am I a genius or just lucky? Who cares! 🎯",
    "Imagine not tapping for coins… couldn’t be me! 😎", "Somewhere out there, Kucoin is shaking in its boots 👢",
    "I’m officially a coin-collecting machine! 🤖", "My fingers might get tired, but not my wallet 💪",
    "Tap tap… I think I’m addicted 😳", "Who needs a job when you have tapping? 💼",
    "Kucoin CEO: ‘Who’s this tapping mastermind?’ 👀", "Feeling like a Kucoin whale right now 🐋",
    "Let’s goooo! More coins for the empire 🏰", "Does this count as passive income? Asking for a friend 🧐",
    "I might break the tap record at this rate 📈", "Tapping is the new yoga… so zen 🧘‍♂️",
    "Wait, is this legal? This much fun for free? 🎉", "One tap closer to financial freedom 💸",
    "Kucoin should just give me the keys to the vault 🔑", "Fortune favors the tapper 🍀",
    "Breaking records and collecting coins 🔥", "Tapping my way through this recession 😎",
    "No one taps like me. No one. 🏆", "I swear I’m not a bot! Just a tapping beast 💻",
    "If you’re reading this, you’re missing out on free coins 🤑", "Making it rain, one tap at a time ☔",
    "Kucoin, prepare to be tapped dry! 😏", "I’ll be the richest tapper alive soon 💸",
    "Does Kucoin even know what’s coming? 😎", "I’d pay to tap, but luckily I don’t have to 🤑",
    "Every tap brings me closer to a Lambo 🚗", "Let’s break some records here, shall we? 🥇",
    "I’m not stopping until my fingers give out 💥", "I’d tap forever if it meant more coins 🌀",
    "I’m basically a coin mining machine at this point ⛏️", "Who needs a job when you have taps? 💼",
    "Somebody better be tracking my tap stats 📊", "Next stop: millionaire status 🏦",
    "My taps are legendary. Just ask Kucoin 👑", "Tapping my way into history books 📚",
    "Feeling like a financial wizard 🧙‍♂️", "I can’t stop, won’t stop 💥", "Kucoin taps = happiness 😊",
    "Can I get paid for tapping this fast? 💼", "What’s the next level after pro tapper? 🏆",
    "Who knew tapping could be so rewarding? 🤑", "I feel like I’m hacking the system… legally! 💻",
    "Tap, earn, repeat. That’s the motto 🔁", "One more tap and I’ll own an island 🏝️",
    "I’ve mastered the art of tapping 💎", "Another tap closer to early retirement ⏳",
    "At this rate, I’ll be unstoppable 🚀", "Tapping like a boss 💼", "I’ll take all the coins, thank you 💰",
    "Do I smell success? Or is that my wallet expanding? 💼", "I'm basically the king/queen of taps 👑",
    "Kucoin better stock up on coins... because I'm not stopping! 💸", "Who's tapping? Oh, it's me—your future millionaire 💵",
    "I tap, therefore I earn 💰", "This is what greatness looks like 🏆",
    "Get ready to call me Mr./Ms. Wealthy 🤑", "I’ll be sipping champagne on my yacht in no time 🥂",
    "They said the dream job didn’t exist. They were wrong 💸", "Is there a medal for fastest tapper? 🏅",
    "I’m basically a millionaire in training 💵", "Coin by coin, I’ll build my empire 👑",
    "The more I tap, the more I win 🏆", "I’m a tap legend in the making 🎮", "More coins, more flex 💪",
    "Tapping feels like unlocking treasure chests all day! 🏴‍☠️", "Every tap brings me closer to the moon 🌕",
    "On my way to being the richest person in my phone contacts 💸", "This is what I call passive income 😎",
    "In the future, they’ll write books about this tap marathon 📚", "Too fast, too furious… for Kucoin 😎",
    "We’re in the final stretch! Keep tapping 🏁", "Almost there! The coins are calling 💰",
    "What if my bank calls? ‘We’ve detected rapid growth…’ 📈", "I should get a badge for this 🏅",
    "No one said it’d be this easy to get rich 😏", "I think I’ll buy that yacht after this 🛥️",
    "I could tap in my sleep at this point 💤", "Tapping my way to the good life ☀️",
    "Who needs luck when you have skills like this? 🎯", "I’m like a money-making machine! 🤖",
    "Let’s tap some more—there’s no limit! 🔥", "Should I slow down, or go faster? Faster it is! 🏎️",
    "Kucoin’s coins won’t know what hit them 💥", "Success is just a few taps away 💸",
    "I wonder what Kucoin would say if they knew 🕵️", "I could tap this all day without even blinking 👀",
    "Tapping into greatness one click at a time 🖱️", "I'm basically unbeatable at this point 💯",
    "Watch out world, this tapper's on fire 🔥", "What’s next, my own island? 🏝️", "Soon I'll need a bigger wallet! 💼",
    "I wonder if my fingers will get tired first, or Kucoin! 💪", "I’m a coin-collecting machine today 💸",
    "I’m in the tap zone—nothing can stop me now 💥", "Why tap for fun when you can tap for fortune? 💰",
    "I’m unstoppable! Kucoin better brace itself 💻", "This is too much fun to be legal 🤑",
    "Just a few more taps and I’ll be on top of the world 🏔️", "Tapping like there's no tomorrow 🌅",
    "Kucoin better not run out of coins… 😜", "When the going gets tough, the taps get faster 🏎️",
    "Kucoin, you’re no match for my skills 🏆", "On my way to making the Forbes list 💰",
    "I'm tapping my way through this like a pro 🎮", "Taps = Coins = Winning 🔥"
]

def signal_handler(signum, frame):
    global running
    running = False
    print(Fore.LIGHTBLACK_EX + f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.YELLOW + "Whoa! Signal caught. Time to pack up...")

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    clear_terminal()
    print(Fore.CYAN + Style.BRIGHT + "🎉 Welcome to Kucoin Tap Master 3000! 🎉")
    print(Fore.GREEN + "A script so cool, even your accounts will feel special.")
    print(Fore.GREEN + "Brought to you by the Virtusoses Team | " + Fore.YELLOW + "Telegram: https://t.me/virtusoses")
    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.LIGHTCYAN_EX + "Initializing... getting ready to take over the world (or at least your Kucoin balance)!\n")

def display_accounts_summary(total_accounts):
    print(Fore.CYAN + "---------------------------------------------------")
    print(Fore.YELLOW + f"Total Legendary Accounts Loaded: {Fore.WHITE}{total_accounts}")
    print(Fore.CYAN + "---------------------------------------------------")
    print(Fore.GREEN + "Login successful! Let's start tapping away those coins 💰")
    print(Fore.GREEN + "Virtusoses Team | " + Fore.YELLOW + "Telegram: https://t.me/virtusoses")
    print(Fore.CYAN + "---------------------------------------------------")

def prompt_encoded_data():
    print(Fore.YELLOW + "\nEnter your encoded magic potion (User Data):")
    print(Fore.LIGHTBLACK_EX + "Format looks something like: " + Fore.WHITE +
          "user=%7B%22id%22%3A6519343180%2C%22first_name%22%3A%22Jack%20Samuel%22%7D&auth_date=...&hash=...")
    data = input(Fore.GREEN + "Type the encoded string: ")
    return data

def loading_animation():
    # Multiple types of animations
    animations = [
        itertools.cycle(['|', '/', '-', '\\']),
        itertools.cycle(['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈']),
        itertools.cycle(['.', '..', '...', '....']),
        itertools.cycle(['🔃', '🔄', '⏳', '⏱️', '⏲️']),
        itertools.cycle(['⢀⠀', '⢂⠀', '⢄⠀', '⡂⠀', '⡄⠀', '⡆⠀', '⡇⠀'])
    ]
    current_animation = random.choice(animations)
    for _ in range(20):
        print(Fore.LIGHTBLACK_EX + f"\rTapping in progress... {next(current_animation)}", end="")
        time.sleep(0.1)
    print("\r" + " " * 40, end="")  # Clear the line after the animation

def random_funny_message():
    message = random.choice(funny_messages)
    print(Fore.LIGHTBLACK_EX + f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " +
          Fore.YELLOW + message)

def manage_accounts():
    while True:
        clear_terminal()
        print(Fore.CYAN + "🏦 Account Management 🏦")
        print(Fore.LIGHTBLACK_EX + "--------------------------------------------")
        print(Fore.GREEN + "[1] 🆕 Add a new account")
        print(Fore.GREEN + "[2] 👀 View all accounts")
        print(Fore.GREEN + "[3] 🗑️ Delete an account")
        print(Fore.GREEN + "[4] 💣 Clear all accounts (it's serious!)")
        print(Fore.CYAN + "[5] 🚀 Start the fun (script)")
        print(Fore.RED + "[0] 🚪 Exit")
        print(Fore.LIGHTBLACK_EX + "--------------------------------------------")

        choice = input(Fore.GREEN + "What’s your choice, commander? ")

        if choice == "1":
            encoded_data = prompt_encoded_data()
            encoded_data_list.append(encoded_data)
            print(Fore.LIGHTBLACK_EX + f"✅ New Account added! Total: {len(encoded_data_list)}")
            time.sleep(1)
        elif choice == "2":
            if encoded_data_list:
                print(Fore.LIGHTCYAN_EX + "💼 Your Special Accounts:")
                for i, data in enumerate(encoded_data_list, 1):
                    print(Fore.LIGHTBLACK_EX + f"[{i}] {data}")
            else:
                print(Fore.RED + "No accounts have graced us with their presence yet.")
            input(Fore.GREEN + "\nPress Enter to return to the magical menu...")
        elif choice == "3":
            if encoded_data_list:
                print(Fore.CYAN + "🔨 Choose an account to delete (RIP):")
                for i, data in enumerate(encoded_data_list, 1):
                    print(Fore.LIGHTBLACK_EX + f"[{i}] {data}")
                to_delete = input(Fore.RED + "Enter the number of the fallen account: ")
                try:
                    index = int(to_delete) - 1
                    if 0 <= index < len(encoded_data_list):
                        deleted = encoded_data_list.pop(index)
                        print(Fore.GREEN + f"💀 Deleted: {deleted}")
                    else:
                        print(Fore.RED + "🤔 That account number doesn't exist.")
                except ValueError:
                    print(Fore.RED + "Enter a number, not a riddle!")
            else:
                print(Fore.RED + "No accounts to delete, try adding one first.")
            time.sleep(1)
        elif choice == "4":
            if encoded_data_list:
                confirmation = input(Fore.RED + "Are you sure you want to wipe them all? (yes/no): ").lower()
                if confirmation == "yes":
                    encoded_data_list.clear()
                    print(Fore.GREEN + "🧹 All accounts cleared. Clean as a whistle!")
                else:
                    print(Fore.YELLOW + "Whew, that was close! Operation cancelled.")
            else:
                print(Fore.RED + "No accounts here. Nothing to clean.")
            time.sleep(1)
        elif choice == "5":
            if encoded_data_list:
                break
            else:
                print(Fore.RED + "No accounts, no fun! Add one first.")
                time.sleep(1)
        elif choice == "0":
            print(Fore.GREEN + "👋 Goodbye, see you next time!")
            exit(0)
        else:
            print(Fore.RED + "I’m not sure that option exists! Try again.")
            time.sleep(1)

def decode_data(encoded_data):
    params = dict(item.split('=') for item in encoded_data.split('&'))
    decoded_user = urllib.parse.unquote(params['user'])
    decoded_start_param = urllib.parse.unquote(params['start_param'])
    return {
        "decoded_user": decoded_user,
        "decoded_start_param": decoded_start_param,
        "hash": params['hash'],
        "auth_date": params['auth_date'],
        "chat_type": params['chat_type'],
        "chat_instance": params['chat_instance']
    }

def login(decoded_data):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/login?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }
    
    body = {
        "inviterUserId": "5496274031",
        "extInfo": {
            "hash": decoded_data['hash'],
            "auth_date": decoded_data['auth_date'],
            "via": "miniApp",
            "user": decoded_data['decoded_user'],
            "chat_type": decoded_data['chat_type'],
            "chat_instance": decoded_data['chat_instance'],
            "start_param": decoded_data['decoded_start_param']
        }
    }

    session = requests.Session()
    response = session.post(url, headers=headers, json=body)
    cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in session.cookies])             
    return cookie

def data(cookie):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "cookie": cookie
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data.get("data", {}).get("availableAmount")
    molecule = data.get("data", {}).get("feedPreview", {}).get("molecule")
    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.GREEN + f"💰 Current Balance: " + Fore.WHITE + f"{balance}")
    return molecule

def tap(cookie, molecule):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/gold/increase?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": cookie
    }

    total_increment = 0

    while total_increment < 3000 and running:
        increment = random.randint(55, 60)
        form_data = {
            'increment': str(increment),
            'molecule': str(molecule)
        }

        try:
            response = requests.post(url, headers=headers, data=form_data)
            total_increment += increment
            
            print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                  Fore.GREEN + f"🖱️ Tapped: " + Fore.WHITE + f"{increment} | " + 
                  Fore.GREEN + f"Total Tapped: " + Fore.WHITE + f"{total_increment}/3000")
            
            loading_animation()  # Animation during tapping
            random_funny_message()  # Show random funny message
            
        except requests.exceptions.RequestException:
            print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                  Fore.RED + "📡 Network issues! Retrying...")
            time.sleep(5)

def new_balance(cookie):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "cookie": cookie
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data.get("data", {}).get("availableAmount")
    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.GREEN + f"New Balance: " + Fore.WHITE + f"{balance}")

def main():
    global running
    welcome_message()
    manage_accounts()
    total_accounts = len(encoded_data_list)
    
    try:
        while running:
            clear_terminal()
            display_accounts_summary(total_accounts)
        
            for index, encoded_data in enumerate(encoded_data_list, start=1):
                if not running:
                    break
                print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                      Fore.GREEN + f"🤖 Processing Account {index}")
                try:
                    decoded_data = decode_data(encoded_data)
                    cookie = login(decoded_data)
                    molecule = data(cookie)
                    tap(cookie, molecule)
                    new_balance(cookie)
                except Exception as e:
                    print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                          Fore.RED + f"❌ Error with Account {index}: {str(e)}")
            
            if running:
                print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
                      Fore.YELLOW + "💤 Taking a 2-minute power nap before the next cycle...")
                for _ in range(120):
                    if not running:
                        break
                    time.sleep(1)
    except Exception as e:
        print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
              Fore.RED + f"😱 Something went wrong: {str(e)}")
    finally:
        print(Fore.LIGHTBLACK_EX + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
              Fore.GREEN + "🎉 Successfully logged out. Time to chill!")

if __name__ == "__main__":
    main()
