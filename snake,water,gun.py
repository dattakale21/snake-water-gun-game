import random            # in built module ahi
# it is moodle which choose the random words/digits which i have given.


def gameWin(comp, you):          # parameterized function
    if comp == you:              # if two values are equal then returns tie(none)
        return None

    elif comp == 's':            # checking all the possibilities when computer choose snanke(s)
        if you == 'w':           # if comp=s,if you=w ---->false.(lose)
            return False
        elif you == 'g':         # if comp=s,if you=g---->True.(win)
            return True

    elif comp == 'w':            # checking all the possibilities when computer choose water(w)
        if you == 'g':           # if comp=w,if you=g ---->false.(lose)
            return False
        elif you == 's':         # if comp=w,if you=s---->True.(win)
            return True

    elif comp == 'g':            # checking all the possibilities when computer choose gun(g)
        if you == 's':           # if comp=g,if you=s ---->false.(lose)
            return False
        elif you == 'w':         # if comp=g,if you=w---->True.(win)
            return True

print("Computer turn: snake(s),water(w),gun(g)")

ran = random.randint(1, 3)           # randint is one keyword which displays the random digits in between 1-3,means---->(1,3)--->randomly the digits will print 1,2 or 3. syntax:- to access the module or use the moodle is :- moodule_name.variable_name
if ran == 1:                  # i says:- if computer=1 then snake
    comp = 's'        
elif ran == 2:                # i says:- if computer=2 then water
    comp = 'w'        
else:                         # i says:- if computer=1 then gun
    comp = 'g'



you = input(("Your turn: snake(s),water(w),gun(g): "))          # user turn to write s,w,g
a = gameWin(comp, you)         # me function la comp and mazi value dali.
print("\r")
print("\r")

print("computer choose: ", comp)        # displaying that what computer choose in random.
print("you choose: ", you)              # displaying that what user choose.
print("\r")
print("\r")

if a == None:
    print("The game is tie.")
elif a :
    print("************* You Win! ****************")
else:
    print("************* You lose! ***************")

