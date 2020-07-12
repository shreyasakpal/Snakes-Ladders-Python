import time
import random

def Roll_dice():
    return random.randint(1,6)

def Move(Player, value, P1N, P2N, P3N, P4N, P5N, P6N):
    global num
    snake_squares = {38: 1 , 21: 6, 70: 34, 88: 50, 53: 16, 65: 14, 94: 42, 82: 63, 98: 54, 76: 37}
    ladder_squares = {3: 39, 12: 51, 20: 41, 28: 57, 45: 74, 60: 85, 69: 92, 77: 83, 84: 96}
    Throw = Roll_dice()
    if Player == 1:
        num = value + Throw
        print(P1N, "Rolled a", Throw, "And is now on", num)
    if Player == 2:
        num = value + Throw
        print(P2N, "Rolled a", Throw, "And is now on", num)
    if Player == 3:
        num = value + Throw
        print(P3N, "Rolled a", Throw, "And is now on", num)
    if Player == 4:
        num = value + Throw
        print(P4N, "Rolled a", Throw, "And is now on", num)
    if Player == 5:
        num = value + Throw
        print(P5N, "Rolled a", Throw, "And is now on", num)
    if Player == 6:
        num = value + Throw
        print(P6N, "Rolled a", Throw, "And is now on", num)
    if num in snake_squares:
        print("Player got bitten by a snake and is now on square", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        questions(value,Throw,ladder_squares)
    else:
        print("",end = "")
    return num

def questions(value,Throw,ladder_squares):
    questions={"who is president of USA?\na.Barrack Obama\nb. Hilory Clinton\nc. George Bush\nd. Donald Trump\n":"d",
               "what is the national sport of india?\n\na.Hockey\nb.Cricket\nc.Tennis\nd.Golf\n":"a",
               "World Health day is observed on?\na. 3rd April\nb. 4th April\nc. 5th April\nd. 7th April": "d",
               "Which among the following bodies estimates the national income of India?\na. Office of the Economic Advisor\nb. Ministry of Statistics\nc. Central Statistical Office\nd. Ministry of Finance": "c",
               "What is the name of India’s first nuclear reactor ?\na. Cirius\nb. Apsara\nc. Dhruva\nd. Kamini": "b",
               "Mahatama Gandhi had launched his first Satyagraha in India from which among the following places?\na. Kheda\nb. Bardoli\nc. Champaran\nd. Sabarmati": "c",
               "Who among the following had written Bangladesh’s national anthem” Amar Sonar Bangla” ?\na. Nazrul Islam\nb. Rabindranath Tagore\nc. Anisur Rahman\nd. Santidev Ghosh": "b",
               "Among the following planets, which is the brightest planet?\na. Mercury \nb. Venus \nc. Mars \nd. Jupiter": "b",
               "Which planet is called the red planet in our solar system?\na. Mercury\nb. Mars\nc. Jupiter\nd.Neptune": "b",
               "In which temperature the density of water maximum?\na. 100c\nb. 0c\nc. 4c\nd. 273c": "c",
               "Asia’s largest tulip garden is located in which state?\na. Jammu & Kashmir\nb. Assam\nc. Sikkim\nd. Uttarakhand": "a",
               "Entomology is the science that studies?\na. Behavior of human beings\nb. Insects\nc. The origin and history of technical and scientific terms\nd. The formation of rocks": "b",
               "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of?\na. Asia\nb. Africa\nc. Europe\nd. Australia": "b",
               "The great Victoria Desert is located in?\na. Canada\nb. West Africa\nc. Australia\nd. North America": "c",
               "The landmass of which of the following continents is the least?\na. Africa\nb. Asia\nc. Australia\nd. Europe": "c",
               "Nuclear sizes are expressed in a unit named?\na. Fermi\nb. angstrom\nc. newton\nd. tesla": "a",
               "Light year is a unit of?\na. time\nb. distance\nc. light\nd. intensity of light": "b",
               "Pa(Pascal) is the unit for?\na. thrust\nb. pressure\nc. frequency\nd. conductivity": "b",
               "Sound waves in air are?\na. transverse\nb. longitudinal\nc. electromagnetic\nd. polarised": "b",
               "Magnetism at the centre of a bar magnet is?\na. minimum\nb. maximum\nc. zero\nd. minimum or maximum": "c",
               "Golf player Vijay Singh belongs to which country?\na. USA\nb. Fiji\nc. India\nd. UK": "b",
               "The ozone layer restricts?\na. Visible light\nb. Infrared radiation\nc. X-rays and gamma rays\nd. Ultraviolet radiation": "d",
               "Headquarters of UNO are situated at?\na. New York\nb. Hague\nc. Geneva\nd. Paris": "a",
               "For galvanizing iron which of the following metals is used?\na. Aluminium\nb. Copper\nc. Lead\nd. Zinc": "d",
               "Which of the following is used in pencils?\na. Graphite\nb. Silicon\nc. Charcoal\nd. Phosphorous": "a",
               "Sodium metal is kept under?\na. petrol\nb. alcohol\nc. water\nd. kerosene": "d",
               "What is laughing gas?\na. Nitrous Oxide\nb. Carbon monoxide\nc. Sulphur dioxide\nd. Hydrogen peroxide": "a",
               "Which one programming language is exclusively used for artificial intelligence?\na. C\nb. Java\nc. J2EE\nd. Prolog\n": "d",
               "Which of the following is not an operating system?\na. DOS\nb. Mac\nc. C\nd. Linux\n": "c",
               "Which of the following is not a database management software?\na. MySql\nb. Oracle\nc. Sybase\nd. COBOL\n": "d",
               "Number of layers in the OSI (Open System Interconnections) Model\na.9 \nb. 3\nc. 7\nd. 11\n": "c",
               ".gif is an extension of which file?\na. Image file\nb. Video file\nc. Audio file\nd. Word file\n": "a",
               "A group of 8 bits is called\na. File\nb. Record\nc. Byte\nd. Document\n": "c",
               "The computer abbreviation OS stands for:\na. Optical Sensor\nb. Operating System\nc. Open Software\nd. Order of Significance\n": "b",
               "Which of the following is a programming language among these?\na. FTP\nb. HTTP \nc. HTML\nd. HPML\n": "c",
               "DNS translates a domain name into:\na. Binary\nb. Hex\nc. IP\nd. URL\n": "c",
               "ALU stands for:\na. All Logic Unit\nb. Arithmetic and Logic Unit\nc. All-Live Unit\nd. All Logic Union\n": "b",
               "Which one among the following is not an object oriented programming language?\na. Java\nb. Python\nc. C\nd. C++\n": "c",
               "Which of the following can be used instead of nested if/else statements\na. for\nb. go\nc. while\nd. switch\n": "d",
               "Which datatype represents TRUE/FALSE value?\na. Boolean\nb. char\nc. integer\nd. float\n": "a",
               "Which of the following data type is immutable?\na. list\nb. string\nc. dictionary\nd. set\n": "b",
               "BFS and DFS are algorithms for:\na. traversal\nb. deletion\nc. insertion\nd. search\n": "a",
               "What is part of a database that holds only one type of information?\na. Report\nb. Field\nc. Record\nd. File": "b",
               "'OS' computer abbreviation usually means?\na. Order of Significance\nb. Open Software\nc. Operating System\nd. Optical Sensor": "c",
               "Your computer has gradually slowed down. What's the most likely cause?\na. Overheating\nb. Your processor chip is just getting old\nc.	Adware/spyware is infecting your PC\nd.	You dropped a sandwich in your computer": "c",
               "How many bits is a byte?\na. 4\nb. 8\nc. 16\nd. 32": "b",
               "The abbreviation URL stands for:\na. User Regulation Law\nb. Unknown RAM Load\nc. Uniform Resource Locator\nd.	Ultimate RAM Locator": "c",
               "Which of the following is not a programming language?\na. Basic\nb. Java\nc. Turing(HTML+CSS)\nd. C#": "c",
               "HTML is used to...\na.	Plot complicated graphs\nb. Author webpages\nc.	Translate one language into another\nd.	Solve equations": "b",
               "Computers calculate numbers in what mode?\na. Decimal\nb. Octal\nc. Binary\nd.	None of the above": "c",
               "The speed of your net access is defined in terms of...\na. RAM\nb. MHz\nc. Kbps\nd. Megabytes": "c",
               "The letters, 'DOS' stand for...\na. Data Out System\nb. Disk Out System\nc. Disk Operating System\nd. Data Operating System": "c",
               "Which is not an internet protocol?\na.	STP\nb. FTP\nc. HTTP\nd. IP": "a"}
    global num
    mcq = random.choice(list(questions))
    print(mcq)
    ans = questions[mcq]
    while True:
        response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
        if response == ans:
            print("Player climed a ladder and is now on", ladder_squares[num])
            num= ladder_squares[num]
            break
        else:
            num = value + Throw
            print ("Incorrect Answer: Cannot climb the ladder")
            print("The correct answer is ", ans)
            print("Player rolled a dice and got ", Throw, " is now on", num)
            break

def Setup_Players():
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 6 or players < 2:
                print("Must be less than 7 and greater than 1")
            else:
                return players
        except:
            print("Must be a number")

def Player_Names(NumP):
    Names = []
    for i in range(1,NumP+1):
        Names.append(input("What is the name of Player"+str(i)+"?"))
    Names.append("")
    return Names

Num_Players=Setup_Players()
P_Names = Player_Names(Num_Players)
P1N = 0
P2N = 0
P3N = 0
P4N = 0
P5N = 0
P6N = 0
for i in P_Names:
    if P1N == 0:
        P1N = i
        if Num_Players == 1:
            P2N, P3N, P4N, P5N, P6N = "", "", "", "", ""
            break
    elif P2N == 0:
        P2N = i
        if Num_Players == 2:
            P3N, P4N, P5N, P6N = "", "", "", ""
            break
    elif P3N == 0:
        P3N = i
        if Num_Players == 3:
            P4N, P5N, P6N = "","",""
            break
    elif P4N == 0:
        P4N = i
        if Num_Players == 4:
            P5N, P6N = "",""
            break
    elif P5N == 0:	
        P5N = i
        if Num_Players == 5:
            P6N = ""
            break
    elif P6N == 0:	
        P6N = i
        if Num_Players == 6:
            break
    else:
        break
print(P1N, P2N, P3N, P4N, P5N, P6N, ", Welcome To Snakes And Ladders")
input("Press Enter")
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
Num5 = 0
Num6 = 0
x = 0
while Num1 < 100 and Num2 < 100 and Num3 < 100 and Num4 < 100 and Num5 < 100 and Num6<100:       
    while x < Num_Players:
        x=x+1
        if x == 1:
            Num1 = Move(1, Num1, P1N, P2N, P3N, P4N, P5N ,P6N)
            input("Press Enter")
            if Num1 > 99:
                print(P1N, "WINS!")
                time.sleep(5)
                exit()
        if x == 2:
            Num2 = Move(2, Num2, P1N, P2N, P3N, P4N, P5N, P6N)
            input("Press Enter")
            if Num2 > 99:
                print(P2N, "WINS!")
                time.sleep(5)
                exit()            
        if x == 3:
            Num3 = Move(3, Num3, P1N, P2N, P3N, P4N, P5N, P6N)
            input("Press Enter")
            if Num3 > 99:
                print(P3N, "WINS!")
                time.sleep(5)
                exit()
        if x == 4:
            Num4 = Move(4, Num4, P1N, P2N, P3N, P4N, P5N, P6N)
            input("Press Enter")
            if Num4 > 99:
                print(P4N, "WINS!")
                time.sleep(5)
                exit()
        if x == 5:
            Num5 = Move(5, Num5, P1N, P2N, P3N, P4N, P5N, P6N)
            input("Press Enter")
            if Num5 > 99:
                print(P5N, "WINS!")
                time.sleep(5)
                exit()
        if x == 6:
            Num6 = Move(6, Num6, P1N, P2N, P3N, P4N, P5N, P6N)
            input("Press Enter")
            if Num6 > 99:
                print(P6N, "WINS!")
                time.sleep(5)
                exit()
    x=0