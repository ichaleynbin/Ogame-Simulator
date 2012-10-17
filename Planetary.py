#! /usr/bin/env python
import math

unispeed = 4

BBCD =  {"SolarPlant":[75,30,0],"MetalMine":[60,15,0],"CrystalMine":[48,24,0]
        ,"DeuteriumMine":[225,75,0],"ResearchLab":[200,400,200],"FusionPlant":[900,360,180]
        ,"Shipyard":[400,200,100],"Robots":[400,120,200],"Nanites":[1000000,500000,100000]
        ,"MetalStorage":[1000,0,0],"CrystalStorage":[1000,500,0],"DeutStorage":[1000,1000,0]
        ,"Terraformer":[0,50000,100000],"AllianceDepot":[20000,40000,0],"MissileSilo":[20000,20000,1000]}

BSCD =  {"RocketLauncher":[2000,0,0],"LightLaser":[1500,500],"HeavyLaser":[6000,2000,0]
        ,"GaussCannon":[20000,15000,2000],"IonCannon":[2000,6000,0]
        ,"PlasmaTurret":[50000,50000,30000],"LSD":[50000,50000,0],"SSD":[10000,10000,0]
        ,"ABM":[8000,0,2000],"IPM":[12500,2500,10000],"LightFighter":[3000,1000,0]
        ,"HeavyFighter":[6000,4000,0],"Cruiser":[20000,7000,2000],"Battleship":[45000,15000,0]
        ,"BattleCruiser":[30000,40000,15000],"Bomber":[50000,25000,15000]
        ,"Destroyer":[60000,50000,15000],"DeathStar":[5000000,4000000,1000000]
        ,"SmallCargo":[2000,2000,0],"LargeCargo":[6000,6000,0],"ColonyShip":[10000,20000,10000]
        ,"EspionageProbe":[0,1000,0],"Recycler":[10000,7000,2000],"SolarSat":[0,2000,500]}

BTCD =  {}

Tree =  {"FusionPlant":{"DeuteriumMine":5,"Energy":3},"Shipyard":{"Robots":2}
        ,"Nanites":{"Robots":10,"ComputerTech":10},"Terraformer":{"Nanites":1,"Computer":12}
        ,"RocketLauncher":{"Shipyard":1},"LightLaser":{"Laser":3,"Shipyard":2}
        ,"HeavyLaser":{"Laser":5,"Shipyard":4},"GaussCannon":{"Weapons":3,"Shielding":1
        ,"Energy":6,"Shipyard":6},"IonCannon":{"Ion":4,"Shipyard":4}
        ,"PlasmaTurret":{"Plasma":7,"Shipyard":8},"SSD":{"Shielding":2,"Shipyard":2}
        ,"LSD":{"Shielding":6,"Shipyard":6},"ABM":{"MissileSilo":2}
        ,"IPM":{"MissileSilo":4,"Impulse":1,"Shipyard":1},"LightFighter":{"Shipyard":1
        ,"CombustionDrive":1},"HeavyFighter":{"ImpulseDrive":2,"Armor":2,"Shipyard":3}
        ,"Cruiser":{"ImpulseDrive":4,"Ion":2,"Shipyard":5},"BattleShip":{"HyperDrive":4
        ,"Shipyard":7},"SmallCarco":{"Shipyard":2,"CombustionDrive":2},"ColonyShip"
        :{"Imuplse":3,"Shipyard":4},"EspionageProbe":{"CombustionDrive":3,"Espionage":3}
        ,"Recycler":{"Shielding":2,"CombustionDrive":6,"Shipyard":4},"SolarSat":{"Shipyard":1}
        ,"BattleCruiser":{"HyperDrive":5,"Laser":12,"Hyperspace":5,"Shipyard":8}
        ,"Bomber":{"Plasma":5,"ImpulseDrive":6,"Shipyard":8},"Destroyer":{"HyperDrive":6
        ,"Hyperspace":5,"Shipyard":9},"DeathStar":{"Grav":1,"HyperDrive":7
        ,"Hyperspace":6,"Shipyard":12},"MissileSilo":{"Shipyard":1}}

class Technologies():

    Techs = {'Energy':0,'Laser':0,'Ion':0,'Hyperspace':0,'Plasma':0,'CombustionDrive':0
            ,'ImpulseDrive':0,'HyperDrive':0,'Espionage':0,'Computer':0,'Astrophysics':0
            ,'IGRN':0,'Grav':0,'Weapons':0,'Shielding':0,'Armor':0}

    def __init__(self):
        setattr(self,"Techs",Techs)

    def __call__(self,key):
        try: print self.Techs[key]; 
        except KeyError:
            print "error!"


class Planet():

    def __init__(self,Metalbonus,Crystalbonus,Deutbonus):
        Stats = {'Temperature':37,'BuildingQueue':0,'ShipyardQueue':0,'MetalMine':0
                ,'CrystalMine':0,'DeuteriumMine':0,'EnergyProd':0,'EnergyUsed':0
                ,'ProductionFactor':1,'Resource':[500+Metalbonus,500+Crystalbonus,Deutbonus]
                ,'Prod':[unispeed*30,unispeed*15,0],'MetalStorage':0,'CrystalStorage':0,'DeuteriumStorage':0
                ,'MetalCap':10000,'CrystalCap':10000,'DeuteriumCap':10000,'SolarPlant':0
                ,'FusionPlant':0,'Satellites':0,'Robots':0,'Shipyard':0,'ResearchLab':0
                ,'AllianceDepot':0,'MissileSilo':0,'Nanites':0,'Terraformer':0
                ,'RocketLauncher':0,'LightLaser':0,'HeavyLaser':0,'GaussCannon':0
                ,'IonCannon':0,'PlasmaTurret':0,'SmallShieldDome':0,'LargeShieldDome':0
                ,'ABM':0,'IPM':0,'LightFighter':0,'HeavyFighter':0,'Cruiser':0
                ,'Battleship':0,'SmallCargo':0,'LargeCargo':0,'ColonyShip':0
                ,'Battlecruiser':0,'Bomber':0,'Destroyer':0,'Deathstar':0,'Recycler':0
                ,'Probe':0,'WaitingFlag':0,'WaitingMetal':0,'WaitingCrystal':0,'WaitingDeut':0
                ,'ResScaleFactor':1}
        setattr(self,"Stats",Stats)

    def __call__(self, key):
        try: print self.Stats[key]
        except KeyError:
            print "error!"

    def TechsMet(self,BuildingName,TechList):
        boot = True
        for key, value in Tree[BuildingName]:
            if self.Stats[key]: 
                if self.Stats[key] < value:
                    boot = False
            else:
                if TechList[key] < value:
                    boot = False
        return boot;

    def SR(self,ResCostList):
        if min([self.Stats["Resource"][x] >= ResCostList[x] for x in range(3)]):
            for x in range(3):
                self.Stats["Resource"][x] -= ResCostList[x]
            return sum(ResCostList[0:2]);
        else: 
            return 0;

    def BUSC(self,BuildingName,level):
        if BuildingName == "MetalMine" or BuildingName == "DeuteriumMine":
            return [BBCD[BuildingName][x]*1.5**level for x in range(3)];
        if BuildingName == "CrystalMine":
            return [BBCD[BuildingName][x]*1.6**level for x in range(3)];
        if BuildingName == "FusionPlant":
            return [BBCD[BuildingName][x]*1.8**level for x in range(3)];
        else:
            return [BBCD[BuildingName][x]*2**level for x in range(3)];

    def BUC(self,BuildingName,total = 0):
        if total == 1:
            Cost = 0
            for x in range(self.Stats(BuildingName)):
                Cost += BUSC(BuildingName,x)
        else: 
            Cost = BUSC(BuildingName,self.Stats(BuildingName))
        return Cost;

    def SYC(self,PieceName,NumberPieces):
        return [(BSCD[PieceName][x]*NumberPieces) for x in range(NumberPieces + 1)];

    def BT(self,Cost):
        return ((3600.0 * Cost) / (unispeed * 2500 * (1 + self.Stats["Robots"]) * 2 ** self.Stats["Nanites"]));

    def SYT(self,Cost):
        return ((3600.0 * Cost) / (unispeed * 2500 * (1 + self.Stats["Shipyard"]) * 2 ** self.Stats["Nanites"]));

    def BU(self,BuildingName,TechList):
        if self.Stats["BuildingQueue"] == 0 and self.TechsMet(BuildingName,TechList):
            self.Stats["BuildingQueue"] += self.BT(self.SR(self.BUC(BuildingName)))
            if self.Stats["BuildingQueue"] >= 1:
                self.Stats[BuildingName] += 1
        return;

    def DU(self,PieceName,TechList,NumberPieces):
        if self.TechsMet(PieceName,TechList):
            x = self.SYT(self.SR(self.SYC(DefenseName,NumberPieces)))
            self.Stats["ShipyardQueue"] += x
            if x > 0:
                self.Stats[DefenseName] += NumberPieces
        return;
    
    def RU(self,TechName,TechList):
        if self.TechsMet(TechName,TechList):
            x = self.RT(self.SR(self.RUC(TechName,TechList)))


class Fleet():
    pass

class Account():
    def __init__(self):
        Goals = {"Technology":Technologies(),"Planet":Planet()}
        Actual = {"Technology":Technologies(),"PlanetOne":Planet()}
        Fleets = {}
        setattr(self,"Goals",Goals)
        setattr(self,"Actual",Actual)
        setattr(self,"Fleets",Fleets)
    
    def RC(self,TechName,level):
        if TechName == "Astrophysics":
            return [100*round(BBCD[TechName][x]*1.75**level) for x in range(3)]
        else:
            return [BBCD[TechName][x]*2**level for x in range(3)]

    def RUC(self,TechList,TechName,total=0):
        if total == 1:
            Cost = 0
            for x in range(TechList[TechName]):
                Cost += RC(TechList,TechName)
        else:
            Cost = RC(TechList,TechName)

    def __call__(self):
        total = 0
        for Key,Cat in self.Actual:
            if Key == "Technology":
                for key in Cat.Stats:
                    total += self.RUC(Self.Actual["Technology"],key,1)
            else:
                for key, value in Cat.Stats:
                    if BBCD(key):
                        total += Cat.BUC(key,1)
                    else:
                        total += Cat.SYC(key,value)
