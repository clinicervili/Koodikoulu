

# https://dmoj.ca/problem/wc16c1j1 - A Spooky Season

def spooky_season():
    str = "spky"
    count = int(input())
    if 2 <= count <= 20:
        count = 'o'*count
        str = str[:2]+count+str[2:]
        print(str)
    else:
        print("")


# https://dmoj.ca/problem/wc15c2j1 - A New Hope

def starwars()
input = int(input())
    if input == 1:
        string= "A long time ago in a galaxy far away..."
        print(string)
    elif 2 <= input <= 5:
        string = "A long time ago in a galaxy " + (input-1)*"far, " + "far away..."
        print(string)
    else:
        print("")


# https://dmoj.ca/problem/ccc13j1 - Next in Line

def oldest_child_age()
    input1 = int(input())
    input2 = int(input())

    oldest = 2*input2-input1

    print(oldest)

# https://dmoj.ca/problem/wc17c1j2 - How's the Weather?
def celsius_to_fahrenheit()
    input = int(input())
    fahrenheit = (9/5)*input+32
    print(fahrenheit)

# https://dmoj.ca/problem/wc18c3j1 - An Honest Day's Work
def rahnaa():
    P = int(input())
    B = int(input())
    D = int(input())

    jakojäännös = P % B
    paint_for_buttons = P - jakojäännös

    money = (paint_for_buttons/B)*D + jakojäännös
    money = int(money)
    print(money)

# https://dmoj.ca/problem/ccc06j1 - Canadian Calorie Counting
def kanadakalori():
    burger = [461,431,420,0]
    sides = [100,57,70,0]
    drink = [130,160,118,0]
    dessert = [167,266,75,0]

    input1 = int(input())
    input2 = int(input())
    input3 = int(input())
    input4 = int(input())

    calories = burger[input1-1] + sides[input2-1] + drink[input3-1] + dessert[input4-1]

    print(f"Your total Calorie count is {calories}.")

# https://dmoj.ca/problem/ccc15j1 - Special Day

def date():
    import datetime

    month = int(input())
    day = int(input())
    year = 2015

    date = datetime.date(year=year,month=month,day=day)

    to_test_date = datetime.date(year=year,month=2,day=18)

    if date < to_test_date:
        print("Before")
    elif date == to_test_date:
        print("Special")
    else:
        print("After")

# https://dmoj.ca/problem/ccc15j2 - Happy or Sad

def happy_or_sad():
    string = input()
    happy = ":-)"
    sad = ":-("
    happy_count = string.count(happy)
    sad_count = string.count(sad)

    if happy_count == 0 and sad_count==0:
        print("none")
    elif happy_count > sad_count:
        print("happy")
    elif happy_count == sad_count:
        print("unsure")
    else:
        print("sad")

# https://dmoj.ca/problem/dmopc16c1p0 - C.C. and Cheese-kun

def pizza():
    width = int(input())
    cheesy = int(input())

    if width ==3 and cheesy >=95:
        print("C.C. is absolutely satisfied with her pizza.")
    elif width ==1 and cheesy <=50:
        print("C.C. is fairly satisfied with her pizza.")
    else:
        print("C.C. is very satisfied with her pizza.")

# https://dmoj.ca/problem/ccc07j1 - Who is in the Middle

def mid():
    input1 = int(input())
    input2 = int(input())
    input3 = int(input())

    mama = sorted([input1,input2,input3])[1]

    print(mama)

# https://dmoj.ca/problem/wc17c3j3 - Uncrackable

def password():
    string = input()

    lowercase_count = sum(1 for i in string if i.islower())
    uppercase_count = sum(1 for i in string if i.isupper())
    digit_count = sum(1 for i in string if i.isdigit())

    len = lowercase_count+uppercase_count+digit_count

    if lowercase_count >=3 and uppercase_count >=2 and digit_count >=1 and 8 <= len <=12:
        print("Valid")
    else:
        print("Invalid")

# https://dmoj.ca/problem/coci18c3p1 - Magnus

def find_honi():
    string = input()

    count=0
    characters = ['H','O','N','I']
    where = 0
    for c in string:
        if c == characters[where]:
            where +=1
            if where == 4:
                count +=1
                where=0

    print(count)


# https://dmoj.ca/problem/ccc11s1 - English or French

count = int(input())
text=""
t_count=0
s_count=0
for i in range(count):
    text += input()


for i in text:
    t_count += i.count("t") + i.count("T")
    s_count += i.count("s") + i.count("S")

if t_count > s_count:
    print("English")
else:
    print("French")

# https://dmoj.ca/problem/ccc11s2 - Multiple Choice

n = int(input())
count=0
student_a = []
right_a = []
i=0
for i in range(2*n):
    ans = input()
    if i <= n-1:
        student_a.append(ans)
    else:
        right_a.append(ans)
j=0
for j in range(n):
    if student_a[j-1] == right_a[j-1]:
        count +=1

print(count)

# https://dmoj.ca/problem/coci12c5p1 - Ljestvica


string_full = "AEB|CD"
string = string_full.split("|")
C = ["C","F","G"]
A = ["A","D","E"]
A_mol = []
C_dur = []
for i in string:
    if i[0] in A:
        A_mol.append(i)
    elif i[0] in C:
        C_dur.append(i)

if len(C_dur) > len(A_mol):
    print("C-dur")
elif len(A_mol) > len(C_dur):
    print("A-mol")
elif len(C_dur) == len(A_mol):
    if string_full[-1]=="C":
        print("C-dur")
    elif string_full[-1]=="A":
        print("A-mol")



# https://dmoj.ca/problem/coci13c3p1 - Rijeci

start = "A"
k = int(input())
text = ""
for i in range(k):
    text = ""
    for c in start:
        if c == "A":
            text += "B"
        else:
            text +="BA"
    start=text
A_count = start.count("A")
B_count = start.count("B")
print(f"{A_count} {B_count}")

"""
Tuli runtime erroreita niin pyysin chatgpt:tä tekemään mulle vauhdikkaan version tästä 

"k = int(input())
A_count = 1
B_count = 0

for _ in range(k):
    new_B_count = A_count
    new_A_count = B_count
    new_B_count += B_count
    A_count = new_A_count
    B_count = new_B_count

print(f"{A_count} {B_count}")"

#Vähä erilainen lähestymistapa mut pirun sliikki kyl

"""

# https://dmoj.ca/problem/coci18c4p1 - Elder

first_wiz = input()
owner = first_wiz
n = int(input())
winners = []
winners.append(owner)
for i in range(n):
    fight = input()
    fight = fight.split(" ")
    if fight[0] == owner:
        owner = fight[0]
        winners.append(owner)
    elif fight[1] == owner:
        owner = fight[0]
        winners.append(owner)
    else:
        pass

wand_holders = len(list(set(winners)))
print(owner)
print(wand_holders)

# https://dmoj.ca/problem/ccc20j2 - Epidemiology

P = int(input())
N = int(input())
R = int(input())

i=0
sum=0
while sum <= P:
    sum += N*R**i
    i+=1

print(i-1)

# https://dmoj.ca/problem/coci08c1p2 - Ptice

N = int(input())
answers = input()

boys = {"Adrian":"ABC","Bruno":"BABC","Goran":"CCAABB"}
for boy in boys:
    jj= N // len(boys[boy])
    ja = N % len(boys[boy])
    boys[boy] = jj*boys[boy][:N] + boys[boy][:ja]
    
results = []
dict= {"Name":[],"Points":[]}
for boy in boys:
    for c in range(len(answers)):
        if boys[boy][c] == answers[c]:
            results.append(boy)

    dict["Name"].append(boy)
    dict["Points"].append(results.count(boy))

print(dict["Points"][dict["Points"].index(max(dict["Points"]))])

for i, x in enumerate(dict["Points"]):
        if x == max(dict["Points"]):
            print(dict["Name"][i])




# https://dmoj.ca/problem/ccc02j2 - AmeriCanadian

str = ""
vowels = "aeiouy"
while str != "quit!":
    str = input()
    if len(str) > 4 and str[-2:] =="or" and str[-3] not in vowels:
        canadian = str.replace(str[-2:],"our")
        print(canadian)
    elif str == "quit!":
        pass
    else:
        print(str)
        


# https://dmoj.ca/problem/ecoo13r1p1 - Take a Number

num = int(input())
count_serve = 0
count_take = 0

while True:
    str = input()
    if str == "EOF":
        break
    
    if str == "TAKE":
        count_take += 1
        num += 1
        if num > 999:
            num = 1
    elif str == "SERVE":
        count_serve += 1
    else:
        print(f"{count_take} {count_take - count_serve} {num}")
        count_take = 0
        count_serve = 0


# https://dmoj.ca/problem/ecoo15r1p1 - When You Eat Your Smarties


for i in range(10):
    smarties = []
    while True:
        smartie = input()
        if smartie == "end of box":
            break
        smarties.append(smartie)
    
    d = dict.fromkeys(smarties,0)
    for val in smarties:
        d[val] += 1

    total_time = 0

    for candy in d:
        if candy == "red":
            red_time = d[candy]*16
            total_time += red_time
        else:
            if d[candy] % 7 == 0:
                other_time = (d[candy]//7)*13
                total_time += other_time
            else:
                other_time = (d[candy]//7+1)*13
                total_time += other_time

    print(total_time)

# https://dmoj.ca/problem/ccc19j3 - Cold Compress



# https://dmoj.ca/problem/ccc07j3 - Deal or No Deal Calculator
# https://dmoj.ca/problem/coci17c1p1 - Cezar
# https://dmoj.ca/problem/coci18c2p1 - Preokret
# https://dmoj.ca/problem/ccc00s2 - Babbling Brooks
# https://dmoj.ca/problem/ecoo18r1p1 - Willow's Wild Ride
# https://dmoj.ca/problem/ecoo19r1p1 - Free Shirts
# https://dmoj.ca/problem/dmopc14c7p2 - Tides
# https://dmoj.ca/problem/wac3p3 - Wesley Plays DDR
# https://dmoj.ca/problem/ecoo18r1p2 - Rue's Rings
# https://dmoj.ca/problem/coci19c5p1 - Emacs
# https://dmoj.ca/problem/coci20c2p1 - Crtanje
# https://dmoj.ca/problem/dmopc19c5p2 - Charlie's Crazy Conquest

# https://dmoj.ca/problem/ccc13s1 - From 1987 to 2013
# https://dmoj.ca/problem/ccc18j3 - Are we there yet?
# https://dmoj.ca/problem/ecoo12r1p2 - Decoding DNA
# https://dmoj.ca/problem/crci07p1 - Platforme
# https://dmoj.ca/problem/coci13c2p2 - Misa

# http://www.usaco.org/index.php?page=viewproblem2&cpid=855 - Mixing Milk
# http://www.usaco.org/index.php?page=viewproblem2&cpid=711 - Why Did the Cow Cross the Road
# http://www.usaco.org/index.php?page=viewproblem2&cpid=735 - The Lost Cow
# http://www.usaco.org/index.php?page=viewproblem2&cpid=963 - Cow Gymnastics
# http://www.usaco.org/index.php?page=viewproblem2&cpid=736 - Bovine Genomics
# http://www.usaco.org/index.php?page=viewproblem2&cpid=831 - Team Tic Tac Toe
# http://www.usaco.org/index.php?page=viewproblem2&cpid=918 - Sleepy Cow Herding

# https://dmoj.ca/problem/crci06p1 - Bard
# https://dmoj.ca/problem/dmopc19c5p1 - Conspicuous Cryptic Checklist
# https://dmoj.ca/problem/coci15c2p1 - Marko
# https://dmoj.ca/problem/ccc06s2 - Attack of the CipherTexts
# https://dmoj.ca/problem/dmopc19c3p1 - Mode Finding
# https://dmoj.ca/problem/coci14c2p2 - Utrka
# https://dmoj.ca/problem/coci17c2p2 - ZigZag

# http://www.usaco.org/index.php?page=viewproblem2&cpid=891 - Shell Game
# http://www.usaco.org/index.php?page=viewproblem2&cpid=639 - Diamond Collector
# https://dmoj.ca/problem/coci20c1p1 - Patkice
# https://dmoj.ca/problem/ccc09j2 - Old Fishin' Hole
# https://dmoj.ca/problem/ecoo16r1p2 - Spindie
# https://dmoj.ca/problem/cco96p2 - SafeBreaker
# http://www.usaco.org/index.php?page=viewproblem2&cpid=964 - Where Am I
# http://www.usaco.org/index.php?page=viewproblem2&cpid=592 - Angry Cows
# http://www.usaco.org/index.php?page=viewproblem2&cpid=666 - Counting Haybales
# https://dmoj.ca/problem/crci06p3 - Firefly