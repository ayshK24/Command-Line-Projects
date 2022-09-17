''' inspired by bash terminal
'''


import os
# helps to show the ANSI colors in cmd outside the vscode 
os.system("")

# ANSI Color codes 
green = "\033[1;32m"
red = "\033[1;31m"
magenta = "\033[0;35m"
yellow = "\033[0;33m"
white = "\033[1;37m"



Welcome_art = green + """
             ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
"""


print(Welcome_art)

user = input(red + "$ enter your username: " + green)
print("\n"*2)
print(red+f"{user}@Pc: {white}Welcome To Treasure Island\n")
print(red+f"{user}@Pc: {white}Your mission is to find the treasure\n")



cursor = input(red + f"{user}@Pc: {white}left or right ? " + green)

if cursor.lower() != "left":
    print(red + f"{user}@Pc: {magenta}You fell into the Hole!!" + red)
    print(f"{user}@Pc: {magenta}GAME OVER!!" + white)

else:

    cursor = input(red + f"{user}@Pc: {white}swim or wait ? " + green)
    if cursor.lower() != "wait":
        print(red + f"{user}@Pc: {magenta}Attacked by trout!!"+red)
        print(f"{user}@Pc: {magenta}GAME OVER!!" + white)

    else:

        cursor = input(red + f"{user}@Pc: {white}Which door ?[Red, Yellow, Green] " + green)

        if cursor.lower() == "red":
            print(f"{user}@Pc: {magenta}Burned by fire!!" + red)
            print(f"{user}@Pc: {magenta}GAME OVER!!" + white)

        elif cursor.lower() == "blue":
            print(f"{user}@Pc: {magenta}Eaten by beasts!!" + red)
            print(f"{user}@Pc: GAME OVER!!" + white)

        elif cursor.lower() == "yellow":
            print( red + f"{user}@Pc: {yellow}You Win!!" + white)

        else:
            print(red + f"{user}@Pc: {magenta}GAME OVER!!" + white)




