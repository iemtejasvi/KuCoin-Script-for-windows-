import time
import requests
import random
import urllib.parse
import os
import signal
import itertools
import json
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for color output
init(autoreset=True)

# Global variable to control the main loop
running = True
encoded_data_list = []

# Messages for different times of day (example placeholders)
morning_messages = [
"Wake the fuck up, you're still broke, asshole! 💸", "Get your lazy ass out of bed before your mom beats your ass! 💀",
"Pretending to do shit today, huh? You ain't fooling anyone, asshole 😈", "Still living with mommy? Thought so, loser 🍼",
"Good morning, dipshit! Another day of being broke? 😂", "If you're not rich by noon, you might as well stay a fucking loser 🤡",
"Why even bother getting up? Stay poor and save everyone some time 🖕", "You’ll die broke if you don’t get your ass up 💀",
"Is that the smell of failure? Oh wait, it's just you 🗑️", "You waking up just to fuck up again today? Nice plan, asshole!",
"Still broke? Thought you'd fix that shit overnight? Get a grip 💩", "Damn, you made it through another night? Unfortunately for us, asshole 🌅",
"You ain't no boss, you're just unemployed at this point 💼", "Another day, another failure for you, clown 🤡", 
"Grind harder or just quit, we know you ain't going nowhere 🤮", "Good morning to everyone except your lazy ass 🛌",
"Guess what? No one cares about your 'grind'. You're still broke, dumbass 💰", "How's it feel waking up to nothing? Stay down, asshole 👎",
"You ain't getting any richer sitting there like a fucking potato 🥔", "The only thing you've grown is disappointment 🥲",
"Good morning! Your dreams are still out of your broke-ass reach 💸", "Your 'grind' ain't doing shit but making you tired 💤",
"If waking up was a sport, you'd still be losing, asshole 🏅", "Why wake up when your future is as empty as your wallet? 💀",
"Stay down, loser. The world’s better without your broke ass moving around 💩", "Get out of bed, or is the smell of failure keeping you comfy? 🗑️",
"Grind harder? You couldn’t grind cheese with those weak-ass efforts 🍕", "How do you even wake up with that much failure weighing you down? 🤡",
"Rise and shine, loser! Today’s your big chance to do absolutely fucking nothing 🎉", "You ain’t getting out of bed just to lose again, are you? 🤔",
"You better hope today ain’t as shitty as yesterday, but knowing you, it probably will be 🧻", 
"You're so broke, even your dreams are about unemployment 💭", "Rise and fail, like you always do, clown 🤡", 
"Another day, another L for your ass 💀", "Woke up just to disappoint the world again, huh? 🌍", 
"The sun's up and so is your failure rate, dipshit 🌞", "Your morning grind is as real as Santa Claus, asshole 🎅",
"Broke in the morning, broke in the afternoon, and broke at night. You’re consistent at least 🕒", 
"Get up and grind? Nah, just stay in bed. The world don’t need your failures today 🛌", 
"Even a broken clock gets it right twice a day, but not your dumbass 🕰️", "Every morning you wake up, failure sighs with relief 😮‍💨",
"Stay in bed, save yourself the embarrassment of trying and failing again 💀", "Are you grinding, or just pretending like you always do, dipshit? 🤡",
"Rise and grind? More like rise and fail, asshole 🔨", "The only thing that’s risen is your failure level 🌡️",
"If you work as hard as you sleep, you’d still be broke, asshole 😴", "You ain’t hustling shit but excuses 💩", 
"The early bird catches the worm, but you catch nothing but L’s 🐦", "Why are you even awake? Just go back to being useless 😵‍💫",
"Morning! Another day of you fucking everything up 🎉", "Congrats! You woke up to fuck up some more 🏆", 
"Wake the fuck up, nobody cares about your dreams, asshole 🛏️", "Still dreaming about success? That’s as close as you'll ever get 😆",
"Woke up just to fuck up again today, huh? 👏", "Another day to pretend like you’re doing shit, loser 🥴",
"You’re so broke, even your shadow left you, asshole 🌑", "Your morning routine should be called ‘how to fuck up in 5 minutes or less’ 🕒",
"If failure was an Olympic sport, you’d still lose, dumbass 🏅", "You woke up, now what? More excuses, right? 🗑️",
"Rise and shine, asshole. Your wallet’s still as empty as your brain 💀", "Another day to disappoint everyone, good job 🤡",
"What’s the point of waking up if you’re just gonna stay a broke-ass loser? 💩", "You woke up, but did your brain? Doubt it 🤯",
"Still thinking you’ll get rich today? Fuck outta here 😂", "Morning grind? You ain’t grinding shit but failure 🗑️",
"Get your ass up before your mom kicks it 💥", "If you grind as hard as you sleep, you'd still be broke 💸",
"Good morning, loser! Another day of being a failure 😂", "You're so broke even your dreams charge interest 💸",
"Rise and shine, dipshit! Time to fuck up again ☀️", "Get up, you broke-ass clown 🤡",
"Woke up? Great. Still a fucking loser though 😂", "It's morning and you're already failing? Impressive 💩",
"The only thing you're achieving today is wasting air 💨", "Grind hard or stay the fuck in bed 🛏️", 
"The only thing you'll be stacking today is L's, loser 💀", "Is that the smell of failure or just your broke ass? 🤢",
"Wake up and face your sad, broke-ass reality 💀", "Good morning, you're still poor as fuck 😂", 
"You get out of bed just to keep disappointing us? 🤡", "Congrats on waking up. Too bad you still suck at life 💩", 
"You're awake, but your dreams of success are still dead 💀", "Morning! Time to achieve absolutely fucking nothing, asshole 🎉", 
"If your hustle is as weak as your sleep schedule, you're fucked 💀", "Wake up, grind, fail, repeat. The story of your life 🏆",
"Wake up! No one gives a shit about your goals 🤡", "Still broke, still a clown, still you 🤡", 
"You woke up? Damn, thought we'd get a break from your bullshit 🛌", "Morning! Another day to fail miserably 🎉", 
"How's it feel waking up broke every day, asshole? 💸", "You're broke, and your future's even broker 😂", 
"Morning hustle? More like morning bullshit 💩", "Another day, another dollar you're not making 💀", 
"Wake up and face your pathetic reality, asshole 🗑️", "You're awake, but success ain't on your schedule today 🤡", 
"Good morning! You still ain't shit 😂", "Stay in bed. The world doesn’t need your broke ass today 🛌", 
"Grind hard or just stay the fuck down, you're already losing 🤡", "You're awake, but your bank account is still dead 💀",
"Congrats, you woke up. Now go back to being useless 😴", "Another day, another failure in the making 🗑️", 
"You woke up broke, and you'll go to bed even broker 😂", "The only thing you'll achieve today is wasting time ⏳", 
"Morning! Time to watch you fuck up again 🎉", "Still grinding? For what? To stay broke? 💩",
"Your dreams of success are as dead as your willpower 😵‍💫", "You get up just to prove failure's a lifestyle for you 🤡", 
"If you worked as hard as you sleep, you'd still be broke 😂", "Wake up! Your dreams are still out of your broke-ass reach 💸", 
"Get up, loser. The world needs more clowns today 🤡", "Still broke? Shocker 💩", 
"Wake the fuck up and stop wasting air, dumbass 🛏️", "Morning! You still ain't shit, asshole 😂",
"Another day to pretend you're doing shit, clown 🤡", "You woke up to fail again? Bold move 💩", 
"Wake up and face your broke-ass reality, loser 😂", "Another day, another L for your ass 🤡", 
"Morning, dipshit! Time to fuck up again 💀", "Good morning, asshole! You still suck at life 😂", 
"The only thing you're achieving today is wasting air 💨", "Wake the fuck up, nobody cares about your broke-ass dreams 😂",
"Rise and shine, loser. You're still broke as fuck 💸", "You wake up every day just to fail? Impressive 💩", 
"Another day, another dollar you won't make, dumbass 💀", "The only thing you're stacking today is L's 💩",
"Wake up and grind? Nah, just stay broke, clown 🤡", "Morning! Another chance to fuck everything up again 😂",
"Congrats, you woke up. Now go back to being a failure 🛌", "Another day, another failure for you 🤡",
"You woke up to disappoint the world again, huh? 🌍", "Wake up, clown. Your future's still dead 💀", 
"Another day of being a broke-ass loser? You got this 💩", "Wake up, dipshit! Time to pretend you're grinding 🤡", 
"The only thing you're achieving today is staying broke 😂", "Congrats on waking up. Now go fail some more 🛌", 
"You wake up just to fuck everything up again, don't you? 💩", "Morning! Another day of wasting air 🌬️",
"Still broke? Thought you'd fix that overnight? Fuck outta here 😂", "The sun's up and so is your failure rate, dipshit 🌅", 
"Congrats! Another day of being a fucking loser 💀", "Wake the fuck up, asshole! Time to fail again 💩", 
"You're awake, but success is still asleep 😂", "Morning grind? More like morning bullshit 💩",
"Rise and grind? More like rise and fail, asshole 😆", "Wake up, dipshit! Your bank account's still dead 💀", 
"Morning! Time to fuck up again 🎉", "You're awake, but your wallet's still dead, dumbass 💸", 
"Another day of being broke as fuck? You're consistent at least 💩", "Get up, loser. The world's better without your broke ass moving 🌍",
"Good morning, clown! Time to pretend you're doing shit 🤡", "You ain't grinding shit but failure 😂",
"Rise and grind? More like rise and fail, asshole 💩", "Your dreams of success are as dead as your future, dumbass 💀",
"Wake up and grind? Fuck outta here, you ain't grinding shit 💩", "You woke up just to fuck everything up again 😂", 
"Congrats on waking up. Too bad you're still a fucking loser 💀", "Get up, loser. The world's better without your broke ass moving 💩", 
"Morning! Time to watch you fail some more, clown 🤡", "You ain't getting out of bed just to fail again, right? 😂",
"Wake up! Your dreams are still dead, clown 🤡", "You ain't achieving shit today, just like yesterday 💩",
"Congrats on waking up. Now go fuck up some more, dumbass 💀", "Another day, another failure for your broke ass 💩",
"Morning! Time to fuck everything up again, clown 🤡", "Wake the fuck up, asshole! Time to fail some more 💩",
"You're awake, but your wallet's still dead as fuck 😂", "Morning grind? More like morning bullshit, dipshit 💩", 
"You woke up to disappoint the world again? Good job 😂", "Wake up, loser. Your future's still fucked 💩",
"Another day, another L for your dumb ass 💀", "Wake up and grind? Nah, just stay broke, clown 💩", 
"Congrats, you're still broke, dumbass 💸", "Wake the fuck up and stop wasting air, dipshit 🌬️", 
"Good morning, you're still poor as fuck 😂", "You woke up just to fail again, huh? Bold move 😂",
"Congrats! You woke up to fuck up some more, dumbass 💀", "Wake up and grind? Fuck outta here, clown 😂",
"Morning grind? You ain't grinding shit but failure, dumbass 💩", "The only thing you're achieving today is staying broke 💩",
"Congrats on waking up. Now go fuck up some more 🛌", "You're awake, but success is still asleep, dumbass 😆",
"Rise and shine, loser! Another day to pretend you're doing shit 🤡", "Good morning, clown! Time to fail some more 💩",
]
afternoon_messages = [
"Afternoon already and you’re still broke as fuck? Congrats, dumbass 💸", "Lunchtime’s over, and you’ve achieved absolutely nothing 💩", 
"It’s halfway through the day, and you’re still a loser 🤡", "You’ve spent all morning failing, why stop now? Keep going 💀", 
"Afternoon, dipshit! You’ve wasted half the day already 😂", "Still broke? Thought so, loser 🗑️", 
"You’ve had all morning to succeed and you’re still a failure 🛑", "Afternoon’s here, and you’re still a worthless piece of shit 💩", 
"Half the day’s gone, and you’ve done nothing but fail 😂", "The sun’s up, but your future’s still as dark as ever, dumbass 🌞", 
"It’s the afternoon, and your bank account is still dead as fuck 💸", "Congrats, you’ve made it halfway through the day without doing a damn thing 🛑", 
"Afternoon grind? More like afternoon excuses, dumbass 💩", "The clock’s ticking and your broke-ass still hasn’t moved 🕒", 
"You’ve wasted the whole morning, now it’s time to waste the afternoon too, dumbass 💀", "Lunchtime’s over, but you’re still hungry for success you’ll never have 🍽️", 
"It’s midday, and you’re still a fucking failure 🤡", "Half the day’s gone, and you’ve achieved nothing, clown 🛑", 
"Afternoon already? And you’re still a broke-ass loser? Impressive 💸", "You’ve had all morning to grind, but you’re still broke as fuck, dumbass 💩", 
"The sun’s high, but your life is still low as shit 😂", "Congrats on wasting another half of a day, dipshit! Keep it up 🛑", 
"You’ve been broke all morning, why stop now? Keep going 💩", "Afternoon, loser! You’ve done absolutely nothing today, what a shock 🤡", 
"It’s halfway through the day, and you’re still broke as hell 💸", "Afternoon’s here, and you’re still a fucking joke 🤡", 
"You’ve had all morning to succeed, and you’re still a failure, dumbass 🛑", "Congrats on making it to the afternoon without accomplishing anything 💩", 
"It’s the afternoon, and you’re still broke as fuck 😂", "You’ve done jack shit all morning, and the afternoon’s not gonna be any better 💀", 
"Afternoon grind? You haven’t even started grinding yet, dumbass 💩", "The sun’s up, but your wallet’s still dead as fuck, loser 💸", 
"Afternoon already? And you’re still a broke-ass failure? Shocked? 🛑", "You’ve spent all morning being useless, now it’s time to fail through the afternoon 🤡", 
"You’ve had half the day to do something, and you’ve done nothing 💩", "Lunchtime’s over, but you’re still a fucking loser 🍽️", 
"It’s midday and you’re still broke as hell, dumbass 💸", "The clock’s ticking, and you’ve achieved absolutely nothing 🕒", 
"Afternoon’s here, and you’re still a failure, what a surprise 🛑", "You’ve spent all morning being worthless, now it’s time to waste the afternoon too 💩", 
"Afternoon grind? You’re not grinding shit, dipshit 💀", "The sun’s high, but your future’s still fucking dead 😂", 
"You’ve done absolutely nothing all morning, congrats! Keep it going 💩", "Afternoon, dumbass! You’re still broke as fuck, what a surprise 💸", 
"Half the day’s gone, and you’re still a fucking loser, clown 🤡", "You’ve had all morning to grind, but you’re still a broke-ass failure 🛑", 
"The clock’s ticking, and your life’s still a fucking joke 💩", "Afternoon already? And you’ve achieved absolutely nothing? Shocking 💸", 
"You’ve been a failure all morning, and now it’s time to fail through the afternoon too 🤡", "Lunchtime’s over, but you’re still starving for success you’ll never have 🍽️", 
"It’s midday, and you’re still broke as hell, dumbass 😂", "Afternoon’s here, and you’re still a worthless piece of shit 💩", 
"Congrats on wasting the entire morning, now it’s time to waste the afternoon too 🛑", "You’ve been broke all morning, and the afternoon’s not looking any better 💩", 
"Afternoon grind? More like afternoon bullshit, dumbass 💀", "The sun’s high, but your chances of success are still fucking low 😂", 
"You’ve had all morning to do something, and you’ve done nothing, dipshit 💩", "Afternoon already? And you’re still a broke-ass loser? Impressive 💸", 
"Lunchtime’s over, and you’re still a fucking failure, clown 🍽️", "The clock’s ticking, and your life’s still a fucking disaster 🕒", 
"Afternoon’s here, and you’ve achieved jack shit, what a surprise 🛑", "You’ve spent all morning being worthless, now it’s time to fail through the afternoon too 💩", 
"Afternoon grind? You haven’t done shit all day, dumbass 💀", "The sun’s up, but your wallet’s still dead as fuck, loser 💸", 
"Afternoon already? And you’re still a broke-ass failure? Shocker 🛑", "You’ve been a loser all morning, and now it’s time to waste the afternoon too 🤡", 
"Lunchtime’s over, and you’ve achieved absolutely nothing 🍽️", "It’s midday, and you’re still a broke-ass failure, clown 💩", 
"Afternoon’s here, and you’ve achieved jack shit, what a surprise 🛑", "You’ve spent all morning being worthless, now it’s time to fail through the afternoon too, clown 💩", 
"Afternoon grind? You haven’t done shit all day, dumbass 💀", "The sun’s up, but your future’s still fucking dead, loser 💸", 
"Afternoon already? And you’re still a fucking failure? Impressive 🛑", "You’ve had all morning to do something, and you’ve achieved absolutely nothing, clown 💩", 
"Lunchtime’s over, but you’re still starving for success you’ll never have, dumbass 🍽️", "It’s midday, and you’re still a broke-ass loser, dipshit 💸", 
"Congrats on wasting another half a day, now it’s time to waste the rest 💩", "You’ve been a fucking failure all morning, and now it’s time to fail through the afternoon 🤡", 
"Afternoon grind? You haven’t done shit all day, dumbass 💀", "The clock’s ticking, and your life’s still a fucking joke, dipshit 🕒", 
"Afternoon already? And you’ve achieved absolutely nothing? Impressive 💩", "You’ve been broke all morning, and the afternoon’s not looking any better, clown 💸", 
"Lunchtime’s over, and you’re still a fucking failure, dumbass 🍽️", "It’s midday, and you’re still broke as fuck, dipshit 💩", 
"Afternoon’s here, and you’ve done jack shit, what a surprise 🛑", "You’ve spent all morning being worthless, now it’s time to fail through the afternoon too, clown 💩", 
"Afternoon grind? You haven’t done shit all day, dumbass 💀", "The sun’s up, but your future’s still fucking dead, loser 💸",
]
evening_messages = [
"Evening already? And you’re still broke as fuck? Impressive 💩", "Your whole day’s been a failure, why stop now? Keep it going 💀",
"Another day gone, and you’re still broke as hell, dumbass 😂", "Night’s coming, but success sure isn’t for your sorry ass 💸",
"Evening, loser! You managed to fail all day, congrats 🎉", "Sun’s going down, just like your chances of ever being rich 💀",
"You wasted the whole day again, dumbass! Keep up the good work 💩", "Still broke? Thought so, clown 🤡",
"Day’s almost over, and you’ve achieved absolutely nothing 🛑", "Another evening, another reminder that you’re a fucking loser 💀",
"You spent the whole day being worthless, what’s new? 💩", "Sunset’s coming, just like another L for you tonight 😂",
"Evening, dumbass! Your wallet’s still empty, surprise surprise 💸", "You’ve been broke all day, why change now? Keep it up 🗑️",
"Congrats on being a waste of space all day, dumbass 🎉", "Evening grind? More like evening excuses, dipshit 💩",
"The sun’s setting, but your failures just keep rising 😂", "Another day gone, and you’ve accomplished jack shit 💩",
"Evening, loser! Your whole day’s been a joke, just like your life 🤡", "You’ve spent the entire day being broke, what an achievement 🏆",
"The only thing setting is your chances of ever being successful, dumbass 🌅", "Sunset’s here, and you’re still broke as fuck 💸",
"You’ve had all day to grind, but you’re still a failure, clown 🤡", "Evening’s here, and you’re still broke as shit 💀",
"Another day wasted, just like your life 💩", "Evening, asshole! You’ve done fuck-all today, congrats 🎉",
"You’ve been a loser all day, what’s one more evening? 🤡", "Day’s almost over, and you’re still a broke-ass failure 💸",
"Another day, another failure for your sorry ass 🛑", "Evening grind? You haven’t even started grinding yet, dipshit 💩",
"You’ve had all day to succeed, and you’re still broke as hell 😂", "Sunset’s coming, and so is another L for you 💀",
"Evening, loser! You’ve been useless all day, what a surprise 🤡", "Congrats on wasting an entire day again, dumbass 💩",
"You’ve had all day to do something, but you’re still broke 🛑", "The sun’s setting, just like your chances of ever making it 🌅",
"Evening, dipshit! Your wallet’s still empty, surprise surprise 💸", "Another day wasted, and you’re still broke as fuck 💀",
"You’ve accomplished nothing all day, just like every other day 🛑", "Evening grind? More like evening excuses, clown 🤡",
"You’ve been broke all day, why stop now? Keep it going 💩", "The sun’s going down, and you’re still a fucking loser 💀",
"Evening, dumbass! Your whole day’s been a failure, what’s new? 😂", "Another day gone, and you’ve achieved absolutely nothing 💩",
"You’ve spent the whole day being worthless, congrats 🎉", "Evening’s here, and you’re still broke as hell 💸",
"Another evening, another reminder that you’re a loser, dipshit 💩", "The only thing setting is your potential, clown 🤡",
"Evening already? And you’re still a fucking failure? Impressive 💀", "You’ve wasted the entire day, just like your life 🗑️",
"You’ve had all day to get rich, and you’re still broke as hell 😂", "The sun’s setting, but your failures just keep rising 💩",
"Evening, loser! You’ve done absolutely nothing all day, congrats 🎉", "Another day gone, and you’ve accomplished jack shit, dumbass 💩",
"You’ve been broke all day, why change now? Keep it up 🤡", "Sunset’s coming, and so is another L for your sorry ass 💀",
"Evening, dipshit! You’ve been a failure all day, what an achievement 🏆", "You’ve wasted the whole day again, dumbass! Good job 💩",
"Another evening, another reminder that you’re a broke-ass failure 🛑", "The sun’s going down, just like your chances of ever being successful 💸",
"Evening grind? You haven’t even started grinding yet, dipshit 😂", "You’ve had all day to do something, and you’re still broke 💀",
"Congrats on being useless all day, dumbass! Keep it going 🎉", "Evening’s here, and you’re still a fucking loser 🤡",
"Another day wasted, and you’re still broke as fuck, what a surprise 💩", "You’ve spent the whole day failing, and the night’s not gonna be any better 🛑",
"Evening already? And you’re still broke as fuck? Shocker 💸", "You’ve wasted the entire day, just like your life, clown 🤡",
"Another day, another L for you, dumbass! Keep it up 💀", "Evening grind? More like evening bullshit, dipshit 💩",
"You’ve had all day to succeed, and you’ve achieved absolutely nothing 😂", "The sun’s setting, but your failures just keep piling up 💩",
"Evening, loser! Your wallet’s still empty, just like your future 💸", "Congrats on wasting another entire day, dipshit! Good job 🎉",
"You’ve spent the whole day being broke, what an achievement 🏆", "Another day gone, and you’ve done absolutely nothing, dumbass 💩",
"The only thing setting is your chances of ever making it, clown 🤡", "Evening’s here, and you’re still a fucking failure, what a surprise 💀",
"You’ve been broke all day, and the night’s not looking any better 😂", "Sunset’s coming, and so is another L for you, dumbass 💩",
"Evening already? And you’re still a broke-ass failure? Shocking 💸", "You’ve had all day to grind, but you’re still broke as fuck, clown 🤡",
"Another day wasted, just like your entire life, dipshit 🗑️", "Evening grind? You haven’t done shit all day, dumbass 💩",
"You’ve accomplished absolutely nothing all day, and the night’s not gonna be any different 💀", "The sun’s setting, just like your pathetic dreams, loser 💸",
"Congrats on being a fucking failure all day, dumbass! Keep it going 🎉", "You’ve wasted the whole day, and you’re still broke as fuck 💩",
"Evening, dipshit! Your whole day’s been a fucking failure, just like every other day 😂", "Another day gone, and you’ve achieved absolutely nothing, clown 🤡",
"The sun’s going down, and so are your chances of ever being successful 💸", "Evening grind? More like evening bullshit, dumbass 💩",
"You’ve spent the entire day being worthless, what a surprise 🛑", "You’ve been broke all day, why stop now? Keep it up, dipshit 💩",
"Evening already? And you’re still a fucking loser? Impressive 💀", "Another day wasted, and you’ve done jack shit, dumbass 🎉",
"You’ve had all day to grind, but you’re still broke as hell, clown 🤡", "The sun’s setting, and so are your chances of ever being successful 💸",
"Evening grind? You haven’t done shit all day, dipshit! Keep it up 💩", "You’ve accomplished nothing all day, what’s new? 😂",
"Another evening, another reminder that you’re a broke-ass failure, dumbass 💩", "The sun’s going down, and so are your chances of ever making it, loser 💀",
"Congrats on being a useless piece of shit all day, dipshit! Keep up the good work 🎉", "Evening, loser! You’ve done absolutely nothing today, what a surprise 💩",
"You’ve spent the entire day failing, and the night’s not gonna be any better, clown 🤡", "Another day wasted, just like your entire life, dipshit 🗑️",
"Evening grind? More like evening excuses, dumbass! You’ve done jack shit all day 💩", "You’ve had all day to succeed, and you’re still broke as hell, clown 🤡",
"The sun’s setting, just like your pathetic future, dipshit 💸", "Another evening, another reminder that you’re a fucking loser, dumbass 💀",
"You’ve been broke all day, and the night’s not looking any better, clown 😂", "Congrats on wasting another entire day, dipshit! Good job 💩",
]
night_messages = [
"Goodnight, broke-ass! Dreaming of success won’t make you rich, dumbass 💸", "Another night of being useless? Bet you’re proud of that, loser 💀", 
"Sleep tight, failure. You’ll wake up to the same broke-ass reality 😴", "Why sleep when you’re already dreaming about being a loser? 🛌", 
"Going to bed still broke? Congrats, dumbass! 💩", "Your bank account is as empty as your head, asshole 🗑️", 
"Don’t forget to set your alarm, so you can wake up and fail again 😂", "Another night of dreaming about shit you’ll never achieve 💭", 
"Rest up, loser! Tomorrow’s another day to be broke as fuck 💸", "Why bother sleeping when you’re already a failure? 🛏️", 
"Goodnight, clown. Don’t let your broke-ass dreams keep you up 🤡", "Your future’s as dark as the night, dumbass 🌑", 
"Go ahead, sleep. Your failures will be waiting for you in the morning 💤", "You ain’t grinding, you’re just sleeping your broke ass away 😴", 
"Sweet dreams, dumbass! But reality’s still gonna hit you in the face tomorrow 💥", "Another night, another L waiting for you in the morning 💀", 
"Sleep won’t fix your broke ass, dumbass 🛌", "Why sleep? You’ll just wake up to another day of failure 😆", 
"Close your eyes, loser. Maybe tomorrow you’ll finally fail less 🤡", "No amount of sleep is gonna make you rich, dumbass 💸", 
"Dream big, but remember, you’re still broke as fuck when you wake up 💀", "Goodnight! Tomorrow’s another day for you to waste 🎉", 
"Rest up, you’ll need the energy to keep failing tomorrow 😴", "Another night, another reminder that you’re still a loser 🌙", 
"Sweet dreams, clown! Your reality’s still a nightmare 🤡", "Go to bed, dipshit! The world doesn’t need more of your failures 🌍", 
"You’re broke now, and you’ll be broke when you wake up, clown 🤡", "Goodnight, dumbass. Maybe tomorrow you’ll finally get your shit together 💩", 
"Another night of pretending you’ll be successful tomorrow? Laughable 😂", "Goodnight, clown! You’re still gonna suck at life when you wake up 🌙", 
"Going to bed early just to wake up broke again? Sounds like you 💸", "Your bed’s the only thing supporting your broke-ass dreams, loser 🛌", 
"Rest well, clown. Tomorrow’s another day to disappoint everyone again 🤡", "Sleep won’t save your broke ass from reality, dumbass 💀", 
"Dream big, loser! Reality will crush you again in the morning 🛌", "You’ll never escape your failures, not even in your dreams 💭", 
"Why even sleep when your entire life is a nightmare, dumbass 😆", "Goodnight, broke-ass. Tomorrow’s your next opportunity to fail 💩", 
"Your dreams are as dead as your wallet, loser 💀", "Going to bed broke? Congrats, you’re consistent at least 🎉", 
"Sweet dreams, asshole! Tomorrow you’ll still suck at life 💩", "Go ahead, close your eyes. Maybe your failures will disappear overnight 😂", 
"Goodnight, loser! Bet you’ll dream about shit you’ll never achieve 💭", "No amount of sleep will fix your failure problem, dumbass 🛌", 
"Rest up, dipshit! You’ve got a lot of nothing to do tomorrow 💀", "Dream all you want, your reality’s still trash 🗑️", 
"Another night, another reminder that your future’s just as broke as you 💸", "Sleep tight, asshole! You’ll wake up just as worthless tomorrow 🛏️", 
"Goodnight, clown! Tomorrow you’ll wake up to the same broke-ass life 💀", "Your bed’s the only place you’re winning in life, dumbass 🛌", 
"Sleep won’t save you from being a loser, clown 🤡", "Rest up, you’re gonna need energy to keep failing tomorrow 💥", 
"Goodnight, loser! You’ll wake up tomorrow still broke as fuck 💸", "Dreaming about success won’t make it happen, dumbass 😆", 
"Go to bed, clown. Maybe tomorrow you’ll finally stop failing 🤡", "Your future’s just as empty as your wallet, asshole 🗑️", 
"Sweet dreams, loser! But your reality’s still a joke 🤡", "Why sleep when failure’s your default setting anyway, dumbass 💀", 
"Goodnight, dumbass! Another day of failure awaits you tomorrow 🎉", "Go to bed, dipshit! Your broke-ass future won’t change overnight 💸", 
"Rest well, clown. Tomorrow’s your next big opportunity to fuck up 🤡", "Dream big, dumbass! You’ll still wake up to a broke-ass life 🛌", 
"Another night, another reminder that you’re still worthless, loser 💩", "Goodnight, broke-ass! Hope you dream about not failing for once 😂", 
"Why sleep when your life’s already a nightmare, dumbass 💀", "Your dreams are as broke as you are, dipshit 💸", 
"Rest up, loser! You’ll need the energy for another day of nothing tomorrow 💥", "Goodnight, clown! You’ll still suck when you wake up tomorrow 🤡", 
"Go to bed, dipshit. Maybe your broke-ass life will fix itself while you sleep 😂", "Sweet dreams, loser! Reality’s still gonna hit you hard tomorrow 💭", 
"Goodnight, dumbass! Maybe tomorrow you’ll finally stop sucking at life 💀", "Your bank account is as empty as your dreams, asshole 🗑️", 
"Sleep tight, clown! Tomorrow’s your next chance to be a fucking failure 🤡", "Go to bed, dipshit! Tomorrow’s another day to be broke 💸", 
"Why sleep when you’ll wake up to the same broke-ass reality, dumbass 🛌", "Rest well, loser! You’ll need the energy to keep failing tomorrow 💀", 
"Goodnight, dumbass! You’ll still be worthless in the morning 🛏️", "Dream big, asshole! You’ll wake up broke as fuck anyway 💸", 
"Go ahead, sleep. Your failures aren’t going anywhere 😂", "Rest tight, loser! Tomorrow’s your next big chance to do nothing 💀", 
"Goodnight, dipshit! Another day of failure awaits you in the morning 🎉", "Sweet dreams, clown! Your reality’s still a fucking joke 🤡", 
"Why bother sleeping when you’re gonna wake up broke anyway, dumbass 😆", "Rest well, dumbass! Tomorrow’s another day to fuck up 🛌", 
"Goodnight, loser! Maybe tomorrow you’ll finally get your shit together 💀", "Go to bed, clown! Your broke-ass life won’t change while you sleep 🤡", 
"Dream big, dipshit! But reality’s still gonna fuck you up tomorrow 💥", "Goodnight, clown! You’ll still be a fucking loser when you wake up 💩", 
"Sleep tight, loser! You’re still gonna suck at life tomorrow 💀", "Another night, another reminder that you’re still a broke-ass failure 🎉", 
"Go to bed, dumbass! Maybe your dreams will be better than your reality 😂", "Rest tight, loser! Tomorrow’s another day to waste your life 💀", 
"Goodnight, clown! You’ll still be broke when you wake up tomorrow 💸", "Dream big, dipshit! You’ll still wake up to a broke-ass life 🛌", 
"Why sleep when your life’s already a joke, dumbass 😂", "Go to bed, loser! Your failures aren’t going anywhere 💀", 
"Rest up, dumbass! Tomorrow’s another chance to be a fucking disappointment 🎉", "Goodnight, clown! You’ll still be worthless in the morning 💩", 
"Sweet dreams, loser! Your reality’s still a fucking disaster 🗑️", "Why bother sleeping when you’ll wake up broke anyway, dumbass 💸", 
"Rest well, clown! Tomorrow’s your next chance to disappoint everyone again 🤡", "Goodnight, dumbass! You’ll still suck at life when you wake up 💩", 
"Go to bed, dipshit! Your broke-ass life won’t fix itself while you sleep 😂", "Sleep tight, loser! Tomorrow’s another day to fuck up 🛌", 
"Sweet dreams, clown! Reality’s still gonna crush you tomorrow 💭", "Goodnight, dumbass! You’ll still be a fucking failure in the morning 💀", 
"Why sleep when you’re gonna wake up broke as fuck anyway, dumbass 💸", "Rest well, loser! You’ll need the energy to keep failing tomorrow 🎉", 
"Goodnight, clown! Tomorrow’s your next big chance to be worthless 🤡", "Sleep tight, dipshit! Your bank account’s still gonna be empty tomorrow 🛌", 
"Dream big, dumbass! You’ll still wake up to the same broke-ass life 💥", "Go to bed, loser! Your failures aren’t going anywhere 😂", 
"Goodnight, dipshit! Tomorrow’s another day to suck at life 🛏️", "Rest well, loser! Tomorrow’s your next big chance to fail 💩", 
"Sweet dreams, clown! Your reality’s still a fucking joke 🤡", "Why sleep when you’ll wake up broke as fuck anyway, dumbass 💸", 
"Rest tight, dipshit! Tomorrow’s your next chance to be a fucking failure 🛌", "Goodnight, dumbass! You’ll still suck when you wake up tomorrow 💩",
]

# Function to load time-specific messages
def get_time_specific_message():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        messages = morning_messages
    elif 12 <= current_hour < 17:
        messages = afternoon_messages
    elif 17 <= current_hour < 21:
        messages = evening_messages
    else:
        messages = night_messages
    return random.choice(messages)

# Handling persistent account storage
def save_accounts_to_file():
    with open('accounts.txt', 'w') as file:
        json.dump(encoded_data_list, file)

def load_accounts_from_file():
    global encoded_data_list
    if os.path.exists('accounts.txt'):
        with open('accounts.txt', 'r') as file:
            encoded_data_list = json.load(file)

# Global variable to store user accounts between sessions
load_accounts_from_file()

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to handle loading animations
def loading_animation():
    animations = [
        itertools.cycle(['|', '/', '-', '\\']),
        itertools.cycle(['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈']),
        itertools.cycle(['.', '..', '...', '....']),
        itertools.cycle(['🔃', '🔄', '⏳', '⏱️', '⏲️']),
        itertools.cycle(['◐', '◓', '◑', '◒']),
        itertools.cycle(['⊙', '⦾', '⦿', '⊛']),
        itertools.cycle(['⠋', '⠙', '⠚', '⠞', '⠟', '⠿']),
        itertools.cycle(['🌑', '🌒', '🌓', '🌔', '🌕']),
        itertools.cycle(['⢀⠀', '⢂⠀', '⢄⠀', '⡂⠀', '⡄⠀', '⡆⠀', '⡇⠀']),
        itertools.cycle(['◴', '◷', '◶', '◵']),
        itertools.cycle(['⣀', '⣤', '⣶', '⣷', '⣿']),
        itertools.cycle(['🔄', '🔁', '🔂', '🔀']),
        itertools.cycle(['🚀', '✈️', '🛸', '🚁']),
        itertools.cycle(['🚗', '🚕', '🚙', '🚌']),
        itertools.cycle(['⚡', '🔥', '💥', '🌟']),
        itertools.cycle(['💣', '🎯', '🔫', '💰']),
        itertools.cycle(['☕', '🍔', '🍟', '🍕']),
        itertools.cycle(['🕹️', '🎮', '🎲', '🎯']),
        itertools.cycle(['🎶', '🎵', '🎷', '🎺']),
        itertools.cycle(['💾', '📀', '💻', '⌨️'])
    ]

    unique_animations = [
        car_animation,
        rocket_animation,
        bouncing_ball_animation,
        heartbeat_animation
    ]
    
    # Randomly select between regular and unique animations
    if random.choice([True, False]):
        current_animation = random.choice(animations)
        for _ in range(20):
            print(Fore.LIGHTBLACK_EX + f"\rWorking... {next(current_animation)}", end="")
            time.sleep(0.1)
        print("\r" + " " * 40, end="")  # Clear the line after the animation
    else:
        random.choice(unique_animations)()

# Unique animation 1: Car driving across the screen
def car_animation():
    car = "🚗"
    road = "-" * 30
    for i in range(30):
        print(Fore.YELLOW + f"\r{car + road[i:]}", end="")
        time.sleep(0.1)
    print("\r" + " " * 40, end="")  # Clear the line after the animation

# Unique animation 2: Rocket launch
def rocket_animation():
    rocket = "🚀"
    for i in range(10, 0, -1):
        print(Fore.CYAN + f"\r{rocket} Launching in T-{i} seconds", end="")
        time.sleep(0.5)
    print(Fore.GREEN + "\r🚀 Launch Successful! 🎉")

# Unique animation 3: Bouncing ball
def bouncing_ball_animation():
    ball = "⚽"
    screen_width = 30
    for i in range(screen_width):
        spaces = " " * i
        print(Fore.BLUE + f"\r{spaces}{ball}", end="")
        time.sleep(0.1)
    for i in range(screen_width, 0, -1):
        spaces = " " * i
        print(Fore.BLUE + f"\r{spaces}{ball}", end="")
        time.sleep(0.1)
    print("\r" + " " * 40, end="")

# Unique animation 5: Heartbeat animation
def heartbeat_animation():
    heart = "🐍"
    for _ in range(10):
        print(Fore.RED + f"\r{heart}", end="")
        time.sleep(0.2)
        print(Fore.RED + f"\r{heart}🐍", end="")
        time.sleep(0.2)
    print("\r" + " " * 40, end="")

# Signal handler for clean exit
def signal_handler(signum, frame):
    global running
    running = False
    print(Fore.LIGHTBLACK_EX + f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + 
          Fore.YELLOW + "Whoa! Signal caught. Time to pack up...")

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

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

def random_funny_message():
    message = get_time_specific_message()
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
            save_accounts_to_file()  # Save after adding
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
                        save_accounts_to_file()  # Save after deletion
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
                    save_accounts_to_file()  # Save after clearing
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
            random_funny_message()  # Show random funny message (placeholders)
            
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
