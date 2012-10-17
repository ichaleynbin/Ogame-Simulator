#! /usr/bin/env python
import math
from TechTree import teching
from movingres import TotalRes, CheckToMove
from Buildings import *
unispeed = 10
metalwt = 1
cryzwt = 1
deutwt = 1
colonyweight = 1

class TechTree():
	pass

class Planet():
	pass

class Fleet():
	pass


def StartTechs(TechList):
	newtechs = TechTree()
	TechList.append(newtechs)
	i = len(TechList) - 1
	setattr(TechList[i],'Energy',0)
	setattr(TechList[i],'Laser',0)
	setattr(TechList[i],'Ion',0)
	setattr(TechList[i],'Hyperspace',0)
	setattr(TechList[i],'Plasma',0)
	setattr(TechList[i],'CombustionDrive',0)
	setattr(TechList[i],'ImpulseDrive',0)
	setattr(TechList[i],'HyperDrive',0)
	setattr(TechList[i],'Espionage',0)
	setattr(TechList[i],'Computer',0)
	setattr(TechList[i],'Astrophysics',0)
	setattr(TechList[i],'IGRN',0)
	setattr(TechList[i],'Grav',0)
	setattr(TechList[i],'Weapons',0)
	setattr(TechList[i],'Shield',0)
	setattr(TechList[i],'Armor',0)
	setattr(TechList[i],'MetalMax',0)
	setattr(TechList[i],'CrystalMax',0)
	setattr(TechList[i],'DeuteriumMax',0)
	return TechList;
	

def NewFleet(PlanetList,FleetList,TechList,i,ShipList):
	if len(FleetList) <= (TechList[0].Computer + 1):
		created = 1
		newfleet = Fleet()
		FleetList.append(newfleet)
		setattr(FleetList[-1],'LightFighter',ShipList[1])
		setattr(FleetList[-1],'HeavyFighter',ShipList[2])
		setattr(FleetList[-1],'Cruiser',ShipList[3])
		setattr(FleetList[-1],'Battleship',ShipList[4])
		setattr(FleetList[-1],'SmallCargo',ShipList[5])
		setattr(FleetList[-1],'LargeCargo',ShipList[6])
		setattr(FleetList[-1],'Colony',ShipList[7])
		setattr(FleetList[-1],'Battlecruiser',ShipList[8])
		setattr(FleetList[-1],'Bomber',ShipList[9])
		setattr(FleetList[-1],'Destroyer',ShipList[10])
		setattr(FleetList[-1],'Deathstar',ShipList[11])
		setattr(FleetList[-1],'Recycler',ShipList[12])
		setattr(FleetList[-1],'Probe',ShipList[13])
		PlanetList[i].LightFighter -= ShipList[1]
		PlanetList[i].HeavyFighter -= ShipList[2]
		PlanetList[i].Cruiser -= ShipList[3]
		PlanetList[i].Battleship-= ShipList[4]
		PlanetList[i].SmallCargo-= ShipList[5]
		PlanetList[i].LargeCargo-= ShipList[6]
		PlanetList[i].ColonyShip-= ShipList[7]
		PlanetList[i].Battlecruiser-= ShipList[8]
		PlanetList[i].Bomber-= ShipList[9]
		PlanetList[i].Destroyer-= ShipList[10]
		PlanetList[i].Deathstar-= ShipList[11]
		PlanetList[i].Recycler-= ShipList[12]
		PlanetList[i].Probe-= ShipList[13]
	else:
		created = 0
	return created;
	
def NewPlanet(PlanetList,Metalbonus,Crystalbonus,Deutbonus):
	newplanet = Planet()
	PlanetList.append(newplanet)
	length = len(PlanetList) - 1
	setattr(PlanetList[length],'Temperature',37)
	setattr(PlanetList[length],'MetalMine',0)
	setattr(PlanetList[length],'CrystalMine',0)
	setattr(PlanetList[length],'DeuteriumMine',0)
	setattr(PlanetList[length],'EnergyProd',0)
	setattr(PlanetList[length],'EnergyUsed',0)
	setattr(PlanetList[length],'ProductionFactor',1)
	setattr(PlanetList[length],'Resource',[500+Metalbonus,500+Crystalbonus,Deutbonus])
	setattr(PlanetList[length],'Prod',[30,15,0])
	setattr(PlanetList[length],'MetalStorage',0)
	setattr(PlanetList[length],'CrystalStorage',0)
	setattr(PlanetList[length],'DeuteriumStorage',0)
	setattr(PlanetList[length],'MetalCap',10000)
	setattr(PlanetList[length],'CrystalCap',10000)
	setattr(PlanetList[length],'DeuteriumCap',10000)
	setattr(PlanetList[length],'SolarPlant',0)
	setattr(PlanetList[length],'FusionPlant',0)
	setattr(PlanetList[length],'Satellites',0)
	setattr(PlanetList[length],'Robots',0)
	setattr(PlanetList[length],'Shipyard',0)
	setattr(PlanetList[length],'ResearchLab',0)
	setattr(PlanetList[length],'AllianceDepot',0)
	setattr(PlanetList[length],'MissileSilo',0)
	setattr(PlanetList[length],'Nanites',0)
	setattr(PlanetList[length],'Terraformer',0)
	setattr(PlanetList[length],'RocketLauncher',0)
	setattr(PlanetList[length],'LightLaser',0)
	setattr(PlanetList[length],'HeavyLaser',0) 
	setattr(PlanetList[length],'GaussCannon',0)
	setattr(PlanetList[length],'IonCannon',0)
	setattr(PlanetList[length],'PlasmaTurret',0)
	setattr(PlanetList[length],'SmallShieldDome',0)	
	setattr(PlanetList[length],'LargeShieldDome',0)
	setattr(PlanetList[length],'ABM',0)
	setattr(PlanetList[length],'IPM',0)
	setattr(PlanetList[length],'LightFighter',0)
	setattr(PlanetList[length],'HeavyFighter',0)
	setattr(PlanetList[length],'Cruiser',0)
	setattr(PlanetList[length],'Battleship',0)
	setattr(PlanetList[length],'SmallCargo',0)
	setattr(PlanetList[length],'LargeCargo',0)
	setattr(PlanetList[length],'ColonyShip',0)
	setattr(PlanetList[length],'Battlecruiser',0)
	setattr(PlanetList[length],'Bomber',0)
	setattr(PlanetList[length],'Destroyer',0)
	setattr(PlanetList[length],'Deathstar',0)
	setattr(PlanetList[length],'Recycler',0)
	setattr(PlanetList[length],'Probe',0)
	calcstores(PlanetList,TechList,FleetList,IdealPlanet,)
	return PlanetList;



def EffectiveMining(PlanetList,TechList,IdealPlanet):
	newcolmetalcost = 100*round(40*1.75**TechList[0].Astrophysics) + 100*round(40*1.75**(TechList[0].Astrophysics+1))
	newcolcrystalcost = 100*round(80*1.75**TechList[0].Astrophysics) + 100*round(80*1.75**(TechList[0].Astrophysics+1))
	newcoldeutcost = 100*round(40*1.75**TechList[0].Astrophysics) + 100*round(40*1.75**(TechList[0].Astrophysics+1))
	for x in range(IdealPlanet[0].MetalMine):
		newcolmetalcost += 60*1.5**x
		newcolcrystalcost += 15*1.5**x
	for x in range(IdealPlanet[0].CrystalMine):
		newcolmetalcost += 48*1.6**x
		newcolcrystalcost += 24*1.6**x
	for x in range(IdealPlanet[0].DeuteriumMine):
		newcolmetalcost += 225*1.5**x
		newcolcrystalcost += 75*1.5**x
	metalproductivity = unispeed*(30*IdealPlanet[0].MetalMine*1.1**IdealPlanet[0].MetalMine+30)
	crystalproductivity = unispeed*(20*IdealPlanet[0].CrystalMine*1.1**IdealPlanet[0].CrystalMine+15)
	deutproductivity = unispeed*(20*IdealPlanet[0].DeuteriumMine*1.1**IdealPlanet[0].DeuteriumMine)*(0.68-0.002*IdealPlanet[0].Temperature)
	newcolproductivity = metalproductivity + metalwt*crystalproductivity/cryzwt + metalwt*deutproductivity/deutwt
	newcolcost = newcolmetalcost + metalwt*newcolcrystalcost/cryzwt + metalwt*newcoldeutcost/deutwt
	newcoleffectiveness = newcolproductivity/(newcolcost*colonyweight)
	currentmetalprod = unispeed*(30*IdealPlanet[0].MetalMine*1.1**IdealPlanet[0].MetalMine+30)
	currentcrystalprod = unispeed*(20*IdealPlanet[0].CrystalMine*1.1**IdealPlanet[0].CrystalMine+15)
	currentdeutprod = unispeed*(20*IdealPlanet[0].DeuteriumMine*1.1**IdealPlanet[0].DeuteriumMine)*(0.68-0.002*IdealPlanet[0].Temperature)
	nextmetalprod = unispeed*(30*(IdealPlanet[0].MetalMine+1)*1.1**(IdealPlanet[0].MetalMine+1)+30)
	nextcrystalprod = unispeed*(20*(IdealPlanet[0].CrystalMine+1)*1.1**(IdealPlanet[0].CrystalMine+1)+15)
	nextdeutprod = unispeed*(20*(IdealPlanet[0].DeuteriumMine+1)*1.1**(IdealPlanet[0].DeuteriumMine+1))*(0.68-0.002*IdealPlanet[0].Temperature)
	metaleffectiveness = (nextmetalprod-currentmetalprod)/(60*1.5**(IdealPlanet[0].MetalMine+1)+metalwt*15*1.5**(IdealPlanet[0].MetalMine+1)/cryzwt)
	cryzeffectiveness = (nextcrystalprod-currentcrystalprod)/(cryzwt*48*1.6**(IdealPlanet[0].CrystalMine+1)/metalwt+24*1.6**(IdealPlanet[0].CrystalMine+1))
	deuteffectiveness = (nextdeutprod-currentdeutprod)/(deutwt*225*1.6**(IdealPlanet[0].DeuteriumMine+1)/metalwt+deutwt*75*1.6**(IdealPlanet[0].DeuteriumMine+1)/cryzwt)
	return metaleffectiveness,cryzeffectiveness,deuteffectiveness,newcoleffectiveness;

def ColonyChecker(PlanetList,TechList,FleetList,IdealPlanet):
	for i in range(len(PlanetList)):
		if len(PlanetList) < ((TechList[0].Astrophysics + 1)/2 + 1):
			if PlanetList[i].ColonyShip > 0:
				if PlanetList[i].Resource[0] > 4656 and PlanetList[i].Resource[1] > 1367 and PlanetList[i].Resource[2] > 700:
					print "Colony Founded!"
					PlanetList[i].Resource[0] -= 4656
					PlanetList[i].Resource[1] -= 1367
					PlanetList[i].Resource[2] -= 700
					PlanetList[i].ColonyShip -= 1
					NewPlanet(PlanetList,4656,1367,700)
					PlanetList[-1].Satellites = PlanetList[0].Satellites
	if len(PlanetList) < ((TechList[0].Astrophysics + 1)/2 + 1):
		built = 0
		for i in range(len(PlanetList)):
			if PlanetList[i].ColonyShip > 0:
				built = 1
		for i in range(len(PlanetList)):
			if PlanetList[i].Resource[0] >= 10000 and PlanetList[i].Resource[1] >= 20000 and PlanetList[i].Resource[2] >= 10000 and PlanetList[i].Shipyard >= 4 and built == 0:
				print "Produced Colony Ship on Planet " + str(i) + "!"
				PlanetList[i].Resource[0] -= 10000 
				PlanetList[i].Resource[1] -= 20000
				PlanetList[i].Resource[2] -= 10000
				PlanetList[i].ColonyShip += 1 
				built = 1
			elif PlanetList[i].Shipyard < 4:
				checkupshipyard(PlanetList,TechList,FleetList,IdealPlanet,i)

def CheckUpResearchLab(PlanetList,TechList,FleetList,IdealPlanet,i):
	if IdealPlanet[0].DeuteriumMine ==0:
		IdealPlanet[0].DeuteriumMine = 1
	MetalCost = 200*2**PlanetList[i].ResearchLab 
	CrystalCost = 400*2**PlanetList[i].ResearchLab
	DeutCost = 200*2**PlanetList[i].ResearchLab
	if PlanetList[i].Resource[0] > MetalCost and PlanetList[i].Resource[1] > CrystalCost and PlanetList[i].Resource[2] > DeutCost: 
		print "Built Research Lab Level " + str(PlanetList[i].ResearchLab + 1) + " on Planet " + str(i) +"!"
		PlanetList[i].Resource[0] -= int(200*2**PlanetList[i].ResearchLab)
		PlanetList[i].Resource[1] -= int(400*2**PlanetList[i].ResearchLab)
		PlanetList[i].Resource[2] -= int(200*2**PlanetList[i].ResearchLab)
		PlanetList[i].ResearchLab += 1

def CheckRocketLaunchers(PlanetList,TechList,FleetList,IdealPlanet,i):
	if PlanetList[i].Shipyard == 0:
		checkupshipyard(PlanetList,TechList,FleetList,IdealPlanet,i)
	else:
		TMetal,TCrystal,TDeut = TotalRes(PlanetList)
		if PlanetList[i].RocketLauncher < IdealPlanet[0].RocketLauncher:
			Rockets = IdealPlanet[0].RocketLauncher - PlanetList[i].RocketLauncher 
			RocketCost = Rockets * 2000
			if RocketCost > PlanetList[i].Resource[0]:
				CheckToMove(PlanetList,TechList,FleetList,RocketCost,0,0,i)
			if RocketCost < PlanetList[i].Resource[0]:
				PlanetList[i].RocketLauncher += Rockets
				PlanetList[i].Resource[0] -= 2000 * Rockets
				print "Built " + str(Rockets) + " Rocket Launchers on Planet " + str(i) + "!"
				IdealPlanet[0].WaitingFlag = 0
			else: 
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = RocketCost
				IdealPlanet[0].WaitingCrystal = 0
				IdealPlanet[0].WaitingDeut = 0
		elif (PlanetList[i].Resource[0] > (0.6 * PlanetList[i].MetalCap) and (PlanetList[i].Resource[1] < (0.3 * PlanetList[i].CrystalCap) or PlanetList[i].Resource[2] < (0.3 * PlanetList[i].DeuteriumCap))) or PlanetList[i].Resource[0] > (0.80 * PlanetList[i].MetalCap):
			Rockets = int(PlanetList[i].Resource[0]/4000)
			PlanetList[i].RocketLauncher += Rockets
			PlanetList[i].Resource[0] -= 2000 * Rockets
			print "Built " + str(Rockets) + " Rocket Launchers on Planet " + str(i) + "!"


def evenmaintenance(PlanetList,TechList,FleetList,IdealPlanet):
	for i in range(len(PlanetList)):
		if PlanetList[i].RocketLauncher < IdealPlanet[0].RocketLauncher:
			if PlanetList[i].RocketLauncher < PlanetList[IdealPlanet[1].RocketLauncher].RocketLauncher:
				IdealPlanet[1].RocketLauncher = i
		elif PlanetList[i].RocketLauncher > IdealPlanet[0].RocketLauncher:
			IdealPlanet[0].RocketLauncher = PlanetList[i].RocketLauncher

		if PlanetList[i].MetalMine < IdealPlanet[0].MetalMine:
			if PlanetList[i].MetalMine < PlanetList[IdealPlanet[1].MetalMine].MetalMine:
				IdealPlanet[1].MetalMine = i
		elif PlanetList[i].MetalMine > IdealPlanet[0].MetalMine:
			IdealPlanet[0].MetalMine = PlanetList[i].MetalMine
		if PlanetList[i].CrystalMine < IdealPlanet[0].CrystalMine:
			if PlanetList[i].CrystalMine < PlanetList[IdealPlanet[1].CrystalMine].CrystalMine:
				IdealPlanet[1].CrystalMine = i
		elif PlanetList[i].CrystalMine > IdealPlanet[0].CrystalMine:
			IdealPlanet[0].CrystalMine = PlanetList[i].CrystalMine
		if PlanetList[i].DeuteriumMine < IdealPlanet[0].DeuteriumMine:
			if PlanetList[i].DeuteriumMine < PlanetList[IdealPlanet[1].DeuteriumMine].DeuteriumMine:
				IdealPlanet[1].DeuteriumMine = i
		elif PlanetList[i].DeuteriumMine > IdealPlanet[0].DeuteriumMine:
			IdealPlanet[0].DeuteriumMine = PlanetList[i].DeuteriumMine

		if PlanetList[i].FusionPlant < IdealPlanet[0].FusionPlant:
			if PlanetList[i].FusionPlant < PlanetList[IdealPlanet[1].FusionPlant].FusionPlant:
				IdealPlanet[1].FusionPlant = i
		elif PlanetList[i].FusionPlant > IdealPlanet[0].FusionPlant:
			IdealPlanet[0].FusionPlant = PlanetList[i].FusionPlant
		if PlanetList[i].SolarPlant < IdealPlanet[0].SolarPlant:
			if PlanetList[i].SolarPlant < PlanetList[IdealPlanet[1].SolarPlant].SolarPlant:
				IdealPlanet[1].SolarPlant = i
		elif PlanetList[i].SolarPlant > IdealPlanet[0].SolarPlant:
			IdealPlanet[0].SolarPlant = PlanetList[i].SolarPlant

		if PlanetList[IdealPlanet[1].RocketLauncher].RocketLauncher < IdealPlanet[0].RocketLauncher:
			CheckRocketLaunchers(PlanetList,TechList,FleetList,IdealPlanet,i,)
		
		if PlanetList[IdealPlanet[1].SolarPlant].SolarPlant < IdealPlanet[0].SolarPlant:
			CheckUpSolar(PlanetList,TechList,FleetList,IdealPlanet,IdealPlanet[1].SolarPlant)
		if PlanetList[IdealPlanet[1].FusionPlant].FusionPlant < IdealPlanet[0].FusionPlant:
			CheckUpFusion(PlanetList,TechList,FleetList,IdealPlanet,IdealPlanet[1].FusionPlant)
	
		if PlanetList[IdealPlanet[1].CrystalMine].CrystalMine < IdealPlanet[0].CrystalMine:
			CheckUpCrystal(PlanetList,TechList,FleetList,IdealPlanet,IdealPlanet[1].CrystalMine)
		if PlanetList[IdealPlanet[1].MetalMine].MetalMine < IdealPlanet[0].MetalMine:
			CheckUpMetal(PlanetList,TechList,FleetList,IdealPlanet,IdealPlanet[1].MetalMine)
		if PlanetList[IdealPlanet[1].DeuteriumMine].DeuteriumMine < IdealPlanet[0].DeuteriumMine:
			CheckUpDeut(PlanetList,TechList,FleetList,IdealPlanet,IdealPlanet[1].DeuteriumMine)

		if PlanetList[i].ResearchLab < IdealPlanet[0].ResearchLab:
			CheckUpResearchLab(PlanetList,TechList,FleetList,IdealPlanet,i)
		if PlanetList[i].Shipyard < IdealPlanet[0].Shipyard:
			checkupshipyard(PlanetList,TechList,FleetList,IdealPlanet,i)
		

def mining(PlanetList,TechList,FleetList,IdealPlanet):
	metalmax = metalmax2 = 1
	crystalmax = crystalmax2 = 1
	deutmax = deutmax2 = 1
	TMetal, TCrystal, TDeut = TotalRes(PlanetList)
	for x in range(len(PlanetList)):
		others = PlanetList[x].Resource[1] + PlanetList[x].Resource[2]
		if PlanetList[x].Resource[0] > others:
			CheckRocketLaunchers(PlanetList,TechList,FleetList,IdealPlanet,x,)
		if PlanetList[x].MetalMine < IdealPlanet[0].MetalMine:
			metalmax = 0
			if PlanetList[x].MetalMine < IdealPlanet[0].MetalMine-3:
				metalmax2 = 0
		if PlanetList[x].CrystalMine < IdealPlanet[0].CrystalMine:
			crystalmax = 0
			if PlanetList[x].CrystalMine < IdealPlanet[0].CrystalMine-3:
				crystalmax2 = 0
		if PlanetList[x].DeuteriumMine < IdealPlanet[0].DeuteriumMine:
			deutmax = 0
			if PlanetList[x].DeuteriumMine < IdealPlanet[0].DeuteriumMine-3:
				deutmax2 = 0
	if metalmax2 == 1 and crystalmax2 == 1 and deutmax2 == 1 and len(PlanetList) == ((TechList[1].Astrophysics + 1)/2 + 1) and IdealPlanet[0].WaitingFlag == 0:
		metale,crystale,deute,newcole = EffectiveMining(PlanetList,TechList,IdealPlanet)
		if TMetal < TCrystal + TDeut and metalmax == 1:
			IdealPlanet[0].MetalMine +=1
		if TCrystal < TMetal + TDeut and crystalmax == 1:
			IdealPlanet[0].CrystalMine +=1
		if TDeut < TMetal or TDeut < TCrystal and deutmax == 1:
			IdealPlanet[0].DeuteriumMine +=1
		if newcole > metale and newcole > crystale and newcole*4 > deute:
			if TechList[1].Astrophysics == 0:
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = 4000
				IdealPlanet[0].WaitingCrystal = 8000
				IdealPlanet[0].WaitingDeut = 4000
				TechList[1].Astrophysics = 1
				if IdealPlanet[0].Shipyard < 4:
					IdealPlanet[0].Shipyard = 4
			else:
				if TechList[0].Astrophysics == TechList[1].Astrophysics:
					IdealPlanet[0].WaitingFlag = 1
					IdealPlanet[0].WaitingMetal = 100*round(40*1.75**TechList[0].Astrophysics) 
					IdealPlanet[0].WaitingCrystal = 100*round(80*1.75**TechList[0].Astrophysics)
					IdealPlanet[0].WaitingDeut = 100*round(40*1.75**TechList[0].Astrophysics)
					TechList[1].Astrophysics +=2
	if TDeut > TMetal and TDeut > TCrystal:
	 	TechList[1].CombustionDrive = TechList[0].CombustionDrive + 1
	if TechList[0].Energy < IdealPlanet[0].FusionPlant+5:
		TechList[1].Energy = TechList[0].Energy + 1


def minuteprod(PlanetList):
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0]+int(PlanetList[i].Prod[0]/60) < PlanetList[i].MetalCap:
			PlanetList[i].Resource[0] += int(PlanetList[i].ProductionFactor*PlanetList[i].Prod[0]/60)
		else:
			checkupstores(PlanetList,TechList,IdealPlanet,FleetList,PlanetList[i].Resource[0],0,0,i)
		if PlanetList[i].Resource[1]+int(PlanetList[i].Prod[1]/60) < PlanetList[i].CrystalCap:
			PlanetList[i].Resource[1] += int(PlanetList[i].ProductionFactor*PlanetList[i].Prod[1]/60)
		else:
			checkupstores(PlanetList,TechList,IdealPlanet,FleetList,0,PlanetList[i].Resource[1],0,i)
		if PlanetList[i].Resource[2]+int(PlanetList[i].Prod[2]/60) < PlanetList[i].DeuteriumCap:
			PlanetList[i].Resource[2] += int(PlanetList[i].ProductionFactor*PlanetList[i].Prod[2]/60)
		else:
			checkupstores(PlanetList,TechList,IdealPlanet,FleetList,0,0,PlanetList[i].Resource[2],i)


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#######################################################################################################################Start Program

PlanetList = []
IdealPlanet = []
TechList = []
TechList = StartTechs(TechList)
TechList = StartTechs(TechList)
PlanetList = NewPlanet(PlanetList,0,0,0)
for x in range(3):
	IdealPlanet = NewPlanet(IdealPlanet,0,0,0)
	setattr(IdealPlanet[x],'WaitingFlag',0)
	setattr(IdealPlanet[x],'WaitingMetal',0)
	setattr(IdealPlanet[x],'WaitingCrystal',0)
	setattr(IdealPlanet[x],'WaitingDeut',0)
IdealPlanet[0].MetalMine = IdealPlanet[0].CrystalMine = IdealPlanet[0].Deutmine = 1
FleetList = []
upgradechecker = 0
for y in range(10):
	for m in range(12):
		for d in range(30):
			print "day: " + str(y) + ":" + str(m) + ":" + str(d)
			for h in range(23):
				ColonyChecker(PlanetList,TechList)
				for minute in range(60):
#					if len(PlanetList) < 9:
						minuteprod(PlanetList)
						TMetal, TCrystal,TDeut = TotalRes(PlanetList)
						if IdealPlanet[0].WaitingFlag == 0 or (IdealPlanet[0].WaitingFlag == 1 and TMetal > IdealPlanet[0].WaitingMetal and TCrystal > IdealPlanet[0].WaitingCrystal and TDeut > IdealPlanet[0].WaitingDeut and TechList[0].CombustionDrive >=2):
							print "Checking Upgrades!"
							teching(PlanetList,TechList,FleetList,IdealPlanet)
							evenmaintenance(PlanetList,TechList,FleetList,IdealPlanet)
							mining(PlanetList,TechList,FleetList,IdealPlanet)
#							upgradechecker = 0
#						if IdealPlanet[0].WaitingFlag == 1 and upgradechecker == 0:
#							upgradechecker = 1
#							metalmax = 1
#							crystalmax = 1
#							deutmax = 1
#							for x in range(len(PlanetList)):
#								if PlanetList[x].MetalMine < IdealPlanet[0].MetalMine:
#									metalmax = 0
#								if PlanetList[x].CrystalMine < IdealPlanet[0].CrystalMine:
#									crystalmax = 0
#								if PlanetList[x].DeuteriumMine < IdealPlanet[0].DeuteriumMine:
#									deutmax = 0
#							if metalmax == 1 and crystalmax == 1 and deutmax == 1 and TechList[0].Astrophysics != TechList[1].Astrophysics:
#								MetalShort = IdealPlanet[0].WaitingMetal - TMetal
#								CrystalShort =IdealPlanet[0].WaitingCrystal - TCrystal
#								DeutShort = IdealPlanet[0].WaitingDeut - TDeut
#								if MetalShort > CrystalShort and MetalShort > DeutShort:
#									IdealPlanet[0].MetalMine +=1		
#								if CrystalShort > MetalShort and CrystalShort > DeutShort:
#									IdealPlanet[0].CrystalMine +=1
#								if DeutShort > MetalShort and DeutShort > CrystalShort:
#									IdealPlanet[0].DeuteriumMine +=1
for i in range(len(PlanetList)):
	print "Planet", i, "; Satts: ", PlanetList[i].Satellites,", M:C:D Mines: ", PlanetList[i].MetalMine,":",PlanetList[i].CrystalMine,":",PlanetList[i].DeuteriumMine,"; Metals: ",PlanetList[i].Resource[0],"/", PlanetList[i].MetalCap,", Crystals: ", PlanetList[i].Resource[1],"/",PlanetList[i].CrystalCap,", Deuteriums:",PlanetList[i].Resource[2],"/",PlanetList[i].DeuteriumCap,", Rocket Launchers: ", PlanetList[i].RocketLauncher, "LC: " , PlanetList[i].LargeCargo , " SC: " , PlanetList[i].SmallCargo, PlanetList[i].EnergyProd-PlanetList[i].EnergyUsed, PlanetList[i].FusionPlant , "Research Lab", PlanetList[i].ResearchLab , "\n"
print "Astrophysics = " + str(TechList[0].Astrophysics) + ":" + str(TechList[1].Astrophysics) + " Combustion = " + str(TechList[0].CombustionDrive) ,":", TechList[1].CombustionDrive , "Ideal Mines", IdealPlanet[0].MetalMine , IdealPlanet[0].CrystalMine, IdealPlanet[0].DeuteriumMine, "Ideal RL" ,IdealPlanet[0].ResearchLab,"energy Tech",TechList[0].Energy,TechList[1].Energy, "Ideal Fusion", IdealPlanet[0].FusionPlant, "Ideal Solar", IdealPlanet[0].SolarPlant, "Impulse", TechList[0].ImpulseDrive, "Espionage", TechList[0].Espionage
print IdealPlanet[0].WaitingMetal, IdealPlanet[0].WaitingCrystal, IdealPlanet[0].WaitingDeut, IdealPlanet[0].WaitingFlag, TMetal, TCrystal, TDeut
