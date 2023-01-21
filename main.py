import birddict
import termcolor
import os

class Node:
    def __init__(self, name, sciName, about):
        self.name = name
        self.edges = []
        self.about = about
        self.sciName = sciName

Chicken = Node(birddict.birds["nodes"][0]["commonName"], birddict.birds["nodes"][0]["sciName"], birddict.birds["nodes"][0]["about"])
Chachalacas = Node(birddict.birds["nodes"][1]["commonName"], birddict.birds["nodes"][1]["sciName"], birddict.birds["nodes"][1]["about"])
GoldenPheasant = Node(birddict.birds["nodes"][2]["commonName"], birddict.birds["nodes"][2]["sciName"], birddict.birds["nodes"][2]["about"])
Mallard = Node(birddict.birds["nodes"][3]["commonName"], birddict.birds["nodes"][3]["sciName"], birddict.birds["nodes"][3]["about"])
Galliformes = Node(birddict.birds["nodes"][4]["commonName"], birddict.birds["nodes"][4]["sciName"], birddict.birds["nodes"][4]["about"])
RoufusHummingbird = Node(birddict.birds["nodes"][5]["commonName"], birddict.birds["nodes"][5]["sciName"], birddict.birds["nodes"][5]["about"])
CommonNighthawk = Node(birddict.birds["nodes"][6]["commonName"], birddict.birds["nodes"][6]["sciName"], birddict.birds["nodes"][6]["about"])
ChimneySwift = Node(birddict.birds["nodes"][7]["commonName"], birddict.birds["nodes"][7]["sciName"], birddict.birds["nodes"][7]["about"])
GreatBlueTuraco = Node(birddict.birds["nodes"][8]["commonName"], birddict.birds["nodes"][8]["sciName"], birddict.birds["nodes"][8]["about"])
RockDove = Node(birddict.birds["nodes"][10]["commonName"], birddict.birds["nodes"][10]["sciName"], birddict.birds["nodes"][10]["about"])
BengalFlorican = Node(birddict.birds["nodes"][11]["commonName"], birddict.birds["nodes"][11]["sciName"], birddict.birds["nodes"][11]["about"])
CommonCuckoo = Node(birddict.birds["nodes"][12]["commonName"], birddict.birds["nodes"][12]["sciName"], birddict.birds["nodes"][12]["about"])
GreaterRoadrunner = Node(birddict.birds["nodes"][13]["commonName"], birddict.birds["nodes"][13]["sciName"], birddict.birds["nodes"][13]["about"])
BlackBelliedSandgrouse = Node(birddict.birds["nodes"][14]["commonName"], birddict.birds["nodes"][14]["sciName"], birddict.birds["nodes"][14]["about"])
GreaterFlamingo = Node(birddict.birds["nodes"][16]["commonName"], birddict.birds["nodes"][16]["sciName"], birddict.birds["nodes"][16]["about"])
PiedBilledGrebe = Node(birddict.birds["nodes"][17]["commonName"], birddict.birds["nodes"][17]["sciName"], birddict.birds["nodes"][17]["about"])
PipingPlover = Node(birddict.birds["nodes"][18]["commonName"], birddict.birds["nodes"][18]["sciName"], birddict.birds["nodes"][18]["about"])
SnowyPlover = Node(birddict.birds["nodes"][19]["commonName"], birddict.birds["nodes"][19]["sciName"], birddict.birds["nodes"][19]["about"])
AmericanOystercatcher = Node(birddict.birds["nodes"][20]["commonName"], birddict.birds["nodes"][20]["sciName"], birddict.birds["nodes"][20]["about"])
LeastSandpiper = Node(birddict.birds["nodes"][21]["commonName"], birddict.birds["nodes"][21]["sciName"], birddict.birds["nodes"][21]["about"])
SandwichTern = Node(birddict.birds["nodes"][22]["commonName"], birddict.birds["nodes"][22]["sciName"], birddict.birds["nodes"][22]["about"])
LaughingGull = Node(birddict.birds["nodes"][23]["commonName"], birddict.birds["nodes"][23]["sciName"], birddict.birds["nodes"][23]["about"])
HerringGull = Node(birddict.birds["nodes"][24]["commonName"], birddict.birds["nodes"][24]["sciName"], birddict.birds["nodes"][24]["about"])
ArcticTern = Node(birddict.birds["nodes"][25]["commonName"], birddict.birds["nodes"][25]["sciName"], birddict.birds["nodes"][25]["about"])
BlackSkimmer = Node(birddict.birds["nodes"][26]["commonName"], birddict.birds["nodes"][26]["sciName"], birddict.birds["nodes"][26]["about"])
AtlanticPuffin = Node(birddict.birds["nodes"][27]["commonName"], birddict.birds["nodes"][27]["sciName"], birddict.birds["nodes"][27]["about"])
BeltedKingfisher = Node(birddict.birds["nodes"][29]["commonName"], birddict.birds["nodes"][29]["sciName"], birddict.birds["nodes"][29]["about"])
SpeckledMousebird = Node(birddict.birds["nodes"][30]["commonName"], birddict.birds["nodes"][30]["sciName"], birddict.birds["nodes"][30]["about"])
TocoToucan = Node(birddict.birds["nodes"][31]["commonName"], birddict.birds["nodes"][31]["sciName"], birddict.birds["nodes"][31]["about"])
DownyWoodpecker = Node(birddict.birds["nodes"][32]["commonName"], birddict.birds["nodes"][32]["sciName"], birddict.birds["nodes"][32]["about"])
PileatedWoodpecker = Node(birddict.birds["nodes"][33]["commonName"], birddict.birds["nodes"][33]["sciName"], birddict.birds["nodes"][33]["about"])
Kookaburras = Node(birddict.birds["nodes"][34]["commonName"], birddict.birds["nodes"][34]["sciName"], birddict.birds["nodes"][34]["about"])
AmericanKestrel = Node(birddict.birds["nodes"][36]["commonName"], birddict.birds["nodes"][36]["sciName"], birddict.birds["nodes"][36]["about"])
AfricanGray = Node(birddict.birds["nodes"][37]["commonName"], birddict.birds["nodes"][37]["sciName"], birddict.birds["nodes"][37]["about"])
BlackLeggedSeriema = Node(birddict.birds["nodes"][38]["commonName"], birddict.birds["nodes"][38]["sciName"], birddict.birds["nodes"][38]["about"])
PeregrineFalcon = Node(birddict.birds["nodes"][39]["commonName"], birddict.birds["nodes"][39]["sciName"], birddict.birds["nodes"][39]["about"])
PrarieFalcon = Node(birddict.birds["nodes"][40]["commonName"], birddict.birds["nodes"][40]["sciName"], birddict.birds["nodes"][40]["about"])
BlueJay = Node(birddict.birds["nodes"][43]["commonName"], birddict.birds["nodes"][43]["sciName"], birddict.birds["nodes"][43]["about"])
EurasianJay = Node(birddict.birds["nodes"][44]["commonName"], birddict.birds["nodes"][44]["sciName"], birddict.birds["nodes"][44]["about"])
FloridaScrubJay = Node(birddict.birds["nodes"][45]["commonName"], birddict.birds["nodes"][45]["sciName"], birddict.birds["nodes"][45]["about"])
AmericanCrow = Node(birddict.birds["nodes"][46]["commonName"], birddict.birds["nodes"][46]["sciName"], birddict.birds["nodes"][46]["about"])
CommonRaven = Node(birddict.birds["nodes"][47]["commonName"], birddict.birds["nodes"][47]["sciName"], birddict.birds["nodes"][47]["about"])
RoseBreastedGrosbeak = Node(birddict.birds["nodes"][49]["commonName"], birddict.birds["nodes"][49]["sciName"], birddict.birds["nodes"][49]["about"])
HouseFinch = Node(birddict.birds["nodes"][50]["commonName"], birddict.birds["nodes"][50]["sciName"], birddict.birds["nodes"][50]["about"])
PurpleFinch = Node(birddict.birds["nodes"][51]["commonName"], birddict.birds["nodes"][51]["sciName"], birddict.birds["nodes"][51]["about"])
CommonRedpoll = Node(birddict.birds["nodes"][52]["commonName"], birddict.birds["nodes"][52]["sciName"], birddict.birds["nodes"][52]["about"])
Passeriformes = Node(birddict.birds["nodes"][42]["commonName"], birddict.birds["nodes"][42]["sciName"], birddict.birds["nodes"][42]["about"])
Inopinaves = Node(birddict.birds["nodes"][41]["commonName"], birddict.birds["nodes"][41]["sciName"], birddict.birds["nodes"][41]["about"])
Strisores = Node(birddict.birds["nodes"][9]["commonName"], birddict.birds["nodes"][9]["sciName"], birddict.birds["nodes"][9]["about"])
Columbaves = Node(birddict.birds["nodes"][15]["commonName"], birddict.birds["nodes"][15]["sciName"], birddict.birds["nodes"][15]["about"])
Aequorlitornithes = Node(birddict.birds["nodes"][28]["commonName"], birddict.birds["nodes"][28]["sciName"], birddict.birds["nodes"][28]["about"])
Coraciimorphae = Node(birddict.birds["nodes"][35]["commonName"], birddict.birds["nodes"][35]["sciName"], birddict.birds["nodes"][35]["about"])
Corvides = Node(birddict.birds["nodes"][48]["commonName"], birddict.birds["nodes"][48]["sciName"], birddict.birds["nodes"][48]["about"])
Emberizoidea = Node(birddict.birds["nodes"][53]["commonName"], birddict.birds["nodes"][53]["sciName"], birddict.birds["nodes"][53]["about"])



Chicken.edges += [Galliformes]
Chachalacas.edges += [Galliformes]
GoldenPheasant.edges += [Galliformes]
Mallard.edges += [Galliformes]
RoufusHummingbird.edges += [Strisores]
CommonNighthawk.edges += [Strisores]
ChimneySwift.edges += [Strisores]
GreatBlueTuraco.edges += [Strisores]
RockDove.edges += [Columbaves]
BengalFlorican.edges += [Columbaves]
CommonCuckoo.edges += [Columbaves]
GreaterRoadrunner.edges += [Columbaves]
BlackBelliedSandgrouse.edges += [Columbaves]
GreaterFlamingo.edges += [Aequorlitornithes]
PiedBilledGrebe.edges += [Aequorlitornithes]
PipingPlover.edges += [Aequorlitornithes]
SnowyPlover.edges += [Aequorlitornithes]
AmericanOystercatcher.edges += [Aequorlitornithes]
LeastSandpiper.edges += [Aequorlitornithes]
SandwichTern.edges += [Aequorlitornithes]
LaughingGull.edges += [Aequorlitornithes]
HerringGull.edges += [Aequorlitornithes]
ArcticTern.edges += [Aequorlitornithes]
BlackSkimmer.edges += [Aequorlitornithes]
AtlanticPuffin.edges += [Aequorlitornithes]
BeltedKingfisher.edges += [Coraciimorphae]
SpeckledMousebird.edges += [Coraciimorphae]
TocoToucan.edges += [Coraciimorphae]
DownyWoodpecker.edges += [Coraciimorphae]
PileatedWoodpecker.edges += [Coraciimorphae]
Kookaburras.edges += [Coraciimorphae]
AmericanKestrel.edges += [Inopinaves]
AfricanGray.edges += [Inopinaves]
BlackLeggedSeriema.edges += [Inopinaves]
PeregrineFalcon.edges += [Inopinaves]
PrarieFalcon.edges += [Inopinaves]
BlueJay.edges += [Corvides]
EurasianJay.edges += [Corvides]
FloridaScrubJay.edges += [Corvides]
AmericanCrow.edges += [Corvides]
CommonRaven.edges += [Corvides]
RoseBreastedGrosbeak.edges += [Emberizoidea]
HouseFinch.edges += [Emberizoidea]
PurpleFinch.edges += [Emberizoidea]
CommonRedpoll.edges += [Emberizoidea]

Galliformes.edges += [Chicken, Chachalacas, GoldenPheasant, Mallard, Strisores]
Strisores.edges += [RoufusHummingbird, CommonNighthawk, ChimneySwift, GreatBlueTuraco, Columbaves, Galliformes]
Columbaves.edges += [RockDove, BengalFlorican, CommonCuckoo, GreaterRoadrunner, BlackBelliedSandgrouse, Aequorlitornithes, Strisores]
Aequorlitornithes.edges += [GreaterFlamingo, PiedBilledGrebe, PipingPlover, SnowyPlover, AmericanOystercatcher, LeastSandpiper, SandwichTern, LaughingGull, HerringGull, ArcticTern, BlackSkimmer, AtlanticPuffin, Coraciimorphae, Columbaves]
Coraciimorphae.edges += [BeltedKingfisher, SpeckledMousebird, TocoToucan, DownyWoodpecker, PileatedWoodpecker, Kookaburras, Inopinaves, Aequorlitornithes]
Inopinaves.edges += [AmericanKestrel, AfricanGray, BlackLeggedSeriema, PeregrineFalcon, PrarieFalcon, Corvides, Coraciimorphae]
Corvides.edges += [BlueJay, EurasianJay, FloridaScrubJay, AmericanCrow, CommonRaven, Passeriformes]
Emberizoidea.edges += [RoseBreastedGrosbeak, HouseFinch, PurpleFinch, CommonRedpoll,Passeriformes]
Passeriformes.edges += [Inopinaves]

birds = {"Inopaves":"Galliformes",
         "Emberizoidea":"Galliformes",
         "Corvides":"Galliformes",
         "Coraciimorphae":"Galliformes",
         "Aequorlitornithes":"Emberizoidea",
         "Columbaves":"Corvides",
         "Strisores":"Emberizoidea",
         "Galliformes":"Corvides"}

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def makeUndirected(self):
        for node in self.nodes:
            for node2 in self.nodes:
                if node is node2:
                    continue
                #implied else
                for edge in node.edges:
                    if edge not in node2.edges:
                        node2.edges += [edge]

    def check_edges(self):
        if self.nodes is None:
            return "none"
        else:
            for i in self.nodes:
                print(i.name)


graph = Graph([Chicken,Chachalacas,GoldenPheasant,Mallard,Galliformes,RoufusHummingbird,CommonNighthawk,ChimneySwift,GreatBlueTuraco,RockDove,BengalFlorican,CommonCuckoo,GreaterRoadrunner,BlackBelliedSandgrouse,GreaterFlamingo,PiedBilledGrebe,PipingPlover,SnowyPlover,AmericanOystercatcher,LeastSandpiper,SandwichTern,LaughingGull,HerringGull,ArcticTern,BlackSkimmer,AtlanticPuffin,BeltedKingfisher,SpeckledMousebird,TocoToucan,DownyWoodpecker,PileatedWoodpecker,Kookaburras,AmericanKestrel,AfricanGray,BlackLeggedSeriema,PeregrineFalcon,PrarieFalcon,BlueJay,EurasianJay,FloridaScrubJay,AmericanCrow,CommonRaven,RoseBreastedGrosbeak,HouseFinch,PurpleFinch,CommonRedpoll, Galliformes, Strisores, Columbaves, Aequorlitornithes, Coraciimorphae, Inopinaves, Corvides, Emberizoidea, Passeriformes])
birdList = ["Galliformes", "Strisores", "Columbaves", "Aequorlitornithes", "Coraciimorphae", "Inopinaves", "Corvides", "Emberizoidea", "Passeriformes"]
while True:
    getinput = input("\n>>  What bird would you like to look at?: ")
    os.system("clear")
    flag = False
    print()
    try:
        for node in graph.nodes:
            if node.name == getinput:
                current = node
                flag = True
        if flag:
            # print(">>  You are currently looking at:    ")
            print("******************************************")
            print("|", end='')
            print(f"{' ':^40}", end='')
            print("|")
            print("|", end='')
            print(termcolor.colored(f"{current.name:^40}", "cyan", attrs=["bold"]), end='')
            print("|")
            print("|", end='')
            print(f"{' ':^40}", end='')
            print("|")
            print("******************************************\n")
            print(f">>  Information About the",end=' ')
            print(termcolor.colored(f"{current.name}", 'cyan', attrs=["bold"]), end=":\n")
            count = 0
            about = current.about.split()
            a = ''
            print()
            for word in about:
                if count < 4:
                    count += 1
                    a += ' '+word
                else:
                    count = 0
                    a += ' '+word+'\n'
            x = a.split("\n")
            for i in x:
                print(termcolor.colored(f"{i:^40}", "yellow"))
            # print(termcolor.colored(f"\n{current.about:^100}\n", "yellow"))
            try:
                if i[-1] != "\n":
                    print()
            except:
                print('', end='')
        else:
            x = y
    except:
        print(termcolor.colored(">>  Bird Does Not Exist!\n", "red"))
    else:
        distant = []
        orders = []
        f = False
        for i in current.edges:
            for j in current.edges[0].edges:
                if j.name != current.name and j.name not in birdList:
                    if f == False:
                        print(">>  The", end=' ')
                        print(termcolor.colored(f"{current.name}", 'cyan', attrs=["bold"]), end= ' ')
                        print("is closely related to:")
                        print()
                        f = True
                    else:
                        print(termcolor.colored(f"{j.name:^40}", "yellow"))
                else:
                    orders.append(j)

            distant.append(i)
        print()
        for j in distant:
            print(">>  The", end=' ')
            print(termcolor.colored(f"{current.name}", 'cyan', attrs=["bold"]), end= ' ')
            print("is in the order:\n")
            #print(">>  The", current.name, "is in the order:\n")
            print(termcolor.colored(f"{j.name:^40}", "magenta", attrs=["bold"]))
            print()
        p = True
        for i in orders:
            if i.name in birdList:
                if p:
                    print(">>  ", end='')
                    print(termcolor.colored(f"{j.name}", "magenta", attrs=["bold"]), end =' ')
                    print("are connected to the order(s):\n")
                    p = False
                print(termcolor.colored(f"{i.name:^40}", "blue", attrs=["bold"]))
        print()
        for k,v in birds.items():
            if k == j.name:
                print(">>  The ", end='')
                print(termcolor.colored(f"{current.name}", "cyan", attrs=["bold"]), end =' ')
                print("is least connected to the order:\n")
                print(termcolor.colored(f"{v:^40}", "green", attrs=["bold"]))
        print()

        reprompt = input(">>  Enter another bird?(y/n): ")
        while reprompt != 'y' and reprompt != 'n':
            print(termcolor.colored(">>  INVALID!", 'red'))
            reprompt = input(">>  Enter another bird?(y/n): ")
        if reprompt == "y":
            os.system('clear')
        else:
            break
            #prints other bird names
            # for n in i.edges:
            #     print(">> ", n.name, "is in the order:", i.name)

        # if len(j.edges) > 0:
        #     for k in j.edges:
        #         if k.name != current.name:
        #             print(">> ", current.name,"is distantly related to:   ", k.name)



