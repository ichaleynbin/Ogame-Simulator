#! /usr/bin/env python
import math
from TechTree import teching
from movingres import TotalRes, CheckToMove
from Buildings import *
unispeed = 5
metalwt = 3
cryzwt = 2
deutwt = 1
colonyweight = 1
miningtype = 2

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
	setattr(TechList[i],'Shielding',0)
	setattr(TechList[i],'Armor',0)
	setattr(TechList[i],'MetalMax',0)
	setattr(TechList[i],'CrystalMax',0)
	setattr(TechList[i],'DeuteriumMax',0)
	return TechList;
	
def FleetSpeeds(PlanetList,FleetList,TechList,i,ShipList):
	newfleet = Fleet()
	FleetList.append(newfleet)
	setattr(FleetList[0],'LightFighter',12500)
	setattr(FleetList[0],'HeavyFighter',10000)
	setattr(FleetList[0],'Cruiser',15000)
	setattr(FleetList[0],'Battleship',10000)
	setattr(FleetList[0],'SmallCargo',5000)
	setattr(FleetList[0],'LargeCargo',7500)
	setattr(FleetList[0],'Colony',2500)
	setattr(FleetList[0],'Battlecruiser',10000)
	setattr(FleetList[0],'Bomber',4000)
	setattr(FleetList[0],'Destroyer',5000)
	setattr(FleetList[0],'Deathstar',100)
	setattr(FleetList[0],'Recycler',2000)
	setattr(FleetList[0],'Probe',100000)
	FleetList.append(newfleet)


def NewFleet(PlanetList,FleetList,TechList,i,ShipList):
	if len(FleetList) <= (TechList[0].Computer + 2):
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
	
def NewPlanet(PlanetList,TechList,FleetList,IdealPlanet,Metalbonus,Crystalbonus,Deutbonus):
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
	return PlanetList;



def EffectiveMining(PlanetList,TechList,IdealPlanet):
	newcolmetalcost = 100*round(40*1.75**TechList[0].Astrophysics) + 100*round(40*1.75**(TechList[0].Astrophysics+1)) / IdealPlanet[0].ResScaleFactor / IdealPlanet[0].ResScaleFactor
	newcolcrystalcost = 100*round(80*1.75**TechList[0].Astrophysics) + 100*round(80*1.75**(TechList[0].Astrophysics+1)) / IdealPlanet[0].ResScaleFactor
	newcoldeutcost = 100*round(40*1.75**TechList[0].Astrophysics) + 100*round(40*1.75**(TechList[0].Astrophysics+1)) / IdealPlanet[0].ResScaleFactor
	for x in range(IdealPlanet[0].MetalMine):
		newcolmetalcost += 60*1.5**x / IdealPlanet[0].ResScaleFactor
		newcolcrystalcost += 15*1.5**x / IdealPlanet[0].ResScaleFactor
	for x in range(IdealPlanet[0].CrystalMine):
		newcolmetalcost += 48*1.6**x / IdealPlanet[0].ResScaleFactor
		newcolcrystalcost += 24*1.6**x / IdealPlanet[0].ResScaleFactor
	for x in range(IdealPlanet[0].DeuteriumMine):
		newcolmetalcost += 225*1.5**x / IdealPlanet[0].ResScaleFactor
		newcolcrystalcost += 75*1.5**x / IdealPlanet[0].ResScaleFactor
	metalproductivity = unispeed*(30*IdealPlanet[0].MetalMine*1.1**IdealPlanet[0].MetalMine+30) / IdealPlanet[0].ResScaleFactor
	crystalproductivity = unispeed*(20*IdealPlanet[0].CrystalMine*1.1**IdealPlanet[0].CrystalMine+15) / IdealPlanet[0].ResScaleFactor
	deutproductivity = unispeed*(20*IdealPlanet[0].DeuteriumMine*1.1**IdealPlanet[0].DeuteriumMine)*(0.68-0.002*IdealPlanet[0].Temperature) / IdealPlanet[0].ResScaleFactor
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
	if IdealPlanet[0].Shipyard < 4:
		IdealPlanet[0].Shipyard = 4
	for i in range(len(PlanetList)):
		if len(PlanetList) < ((TechList[0].Astrophysics + 1)/2 + 1):
			if PlanetList[i].ColonyShip > 0:
				if PlanetList[i].Resource[0] > 4656 and PlanetList[i].Resource[1] > 1367 and PlanetList[i].Resource[2] > 700:
					print "Colony Founded!"
					PlanetList[i].Resource[0] -= 4656 / IdealPlanet[0].ResScaleFactor
					PlanetList[i].Resource[1] -= 1367 / IdealPlanet[0].ResScaleFactor
					PlanetList[i].Resource[2] -= 700 / IdealPlanet[0].ResScaleFactor
					PlanetList[i].ColonyShip -= 1
					IdealPlanet[0].WaitingFlag = 0
					NewPlanet(PlanetList,TechList,FleetList,IdealPlanet,4656 / IdealPlanet[0].ResScaleFactor,1367 / IdealPlanet[0].ResScaleFactor,700 / IdealPlanet[0].ResScaleFactor)
					PlanetList[-1].Satellites = PlanetList[0].Satellites
				else:
					if IdealPlanet[0].WaitingFlag == 0:
						IdealPlanet[0].WaitingFlag = 1
						IdealPlanet[0].WaitingMetal = 4656
						IdealPlanet[0].WaitingCrystal = 1367
						IdealPlanet[0].WaitingDeut = 700
	if len(PlanetList) < ((TechList[0].Astrophysics + 1)/2 + 1):
		built = 0
		for i in range(len(PlanetList)):
			if PlanetList[i].ColonyShip > 0:
				built = 1
		for i in range(len(PlanetList)):
			if PlanetList[i].Resource[0] >= 10000 / IdealPlanet[0].ResScaleFactor and PlanetList[i].Resource[1] >= 20000 / IdealPlanet[0].ResScaleFactor and PlanetList[i].Resource[2] >= 10000 / IdealPlanet[0].ResScaleFactor and PlanetList[i].Shipyard >= 4 and built == 0:
				print "Produced Colony Ship on Planet " + str(i) + "!"
				PlanetList[i].Resource[0] -= 10000  / IdealPlanet[0].ResScaleFactor
				PlanetList[i].Resource[1] -= 20000 / IdealPlanet[0].ResScaleFactor
				PlanetList[i].Resource[2] -= 10000 / IdealPlanet[0].ResScaleFactor
				PlanetList[i].ColonyShip += 1 
				IdealPlanet[0].WaitingFlag = 0
				built = 1
			elif PlanetList[i].Shipyard >=4:
				if IdealPlanet[0].WaitingFlag == 0:
					IdealPlanet[0].WaitingFlag = 1
					IdealPlanet[0].WaitingMetal = 10000
					IdealPlanet[0].WaitingCrystal = 20000
					IdealPlanet[0].WaitingDeut = 10000
			elif PlanetList[i].Shipyard < 4:
				if IdealPlanet[0].Shipyard <4:
					IdealPlanet[0].Shipyard = 4
				checkupshipyard(PlanetList,TechList,FleetList,IdealPlanet,i)

def CheckRocketLaunchers(PlanetList,TechList,FleetList,IdealPlanet,i):
	if PlanetList[i].Shipyard == 0:
		checkupshipyard(PlanetList,TechList,FleetList,IdealPlanet,i)
	else:
		TMetal,TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
		if PlanetList[i].RocketLauncher < IdealPlanet[0].RocketLauncher:
			Rockets = IdealPlanet[0].RocketLauncher - PlanetList[i].RocketLauncher 
			RocketCost = Rockets * 2000 / IdealPlanet[0].ResScaleFactor
			if RocketCost > PlanetList[i].Resource[0]:
				CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,RocketCost,0,0,i)
			if RocketCost < PlanetList[i].Resource[0]:
				PlanetList[i].RocketLauncher += Rockets
				PlanetList[i].Resource[0] -= RocketCost
				print "Built " + str(Rockets) + " Rocket Launchers on Planet " + str(i) + "!"
				IdealPlanet[0].WaitingFlag = 0
			else: 
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = RocketCost
				IdealPlanet[0].WaitingCrystal = 0
				IdealPlanet[0].WaitingDeut = 0
		elif (PlanetList[i].Resource[0] > (0.6 * PlanetList[i].MetalCap) and (PlanetList[i].Resource[1] < (0.3 * PlanetList[i].CrystalCap) and PlanetList[i].Resource[2] < (0.3 * PlanetList[i].DeuteriumCap))) or PlanetList[i].Resource[0] > (0.80 * PlanetList[i].MetalCap) and IdealPlanet[0].WaitingFlag == 0:
			Rockets = int(PlanetList[i].Resource[0]/(4000 / IdealPlanet[0].ResScaleFactor))
			PlanetList[i].RocketLauncher += Rockets
			PlanetList[i].Resource[0] -= Rockets * 2000 / IdealPlanet[0].ResScaleFactor
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

		if PlanetList[i].RocketLauncher < IdealPlanet[0].RocketLauncher:
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
	if len(PlanetList) == 1:
		if PlanetList[0].MetalMine <= (PlanetList[0].CrystalMine + 1) and PlanetList[0].MetalMine <= (PlanetList[0].DeuteriumMine + 8) and PlanetList[0].MetalMine < 13 and PlanetList[0].MetalMine == IdealPlanet[0].MetalMine:
			IdealPlanet[0].MetalMine += 1
		elif PlanetList[0].MetalMine > (PlanetList[0].CrystalMine + 1) and PlanetList[0].CrystalMine == IdealPlanet[0].CrystalMine and PlanetList[0].MetalMine >=3:
			IdealPlanet[0].CrystalMine += 1
		elif PlanetList[0].DeuteriumMine + 6 < PlanetList[0].MetalMine and PlanetList[0].DeuteriumMine == IdealPlanet[0].DeuteriumMine:
			IdealPlanet[0].DeuteriumMine += 1
		elif PlanetList[0].MetalMine >= 13 and PlanetList[0].CrystalMine >= 12 and PlanetList[0].DeuteriumMine >= 5:
			TechList[1].Astrophysics = 1
		if PlanetList[0].MetalMine >= 8:
			if PlanetList[0].RocketLauncher == IdealPlanet[0].RocketLauncher != 2**(PlanetList[0].MetalMine - 7):
				IdealPlanet[0].RocketLauncher = 2**(PlanetList[0].MetalMine - 7)
				print "flagged RLs"
			elif PlanetList[0].RocketLauncher < IdealPlanet[0].RocketLauncher:
				CheckRocketLaunchers(PlanetList,TechList,FleetList,IdealPlanet,0)
	if 2 <= len(PlanetList) <= 100:
		metalmax = metalmax2 = 1
		crystalmax = crystalmax2 = 1
		deutmax = deutmax2 = 1
		TMetal, TCrystal, TDeut = TotalRes(PlanetList,IdealPlanet)
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
		if metalmax2 == 1 and crystalmax2 == 1 and deutmax2 == 1 and len(PlanetList) == ((TechList[1].Astrophysics + 1)/2 + 1) and IdealPlanet[0].WaitingFlag == 0 and miningtype == 1:
			metale,crystale,deute,newcole = EffectiveMining(PlanetList,TechList,IdealPlanet)
			if metale >= crystale and metale >= deute:
				IdealPlanet[0].MetalMine +=1
			if crystale >= metale and crystale >= deute:
				IdealPlanet[0].CrystalMine +=1
			if deute >= metale and deute >= crystale:
				IdealPlanet[0].DeuteriumMine +=1
			if newcole > metale and newcole > crystale and newcole > deute:
				if TechList[1].Astrophysics == 0:
					IdealPlanet[0].WaitingFlag = 1
					IdealPlanet[0].WaitingMetal = 4000 / IdealPlanet[0].ResScaleFactor
					IdealPlanet[0].WaitingCrystal = 8000 / IdealPlanet[0].ResScaleFactor
					IdealPlanet[0].WaitingDeut = 4000 / IdealPlanet[0].ResScaleFactor
					TechList[1].Astrophysics = 1
					if IdealPlanet[0].Shipyard < 4:
						IdealPlanet[0].Shipyard = 4
				else:
					if TechList[0].Astrophysics == TechList[1].Astrophysics:
						IdealPlanet[0].WaitingFlag = 1
						IdealPlanet[0].WaitingMetal = 100*round(40*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
						IdealPlanet[0].WaitingCrystal = 100*round(80*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
						IdealPlanet[0].WaitingDeut = 100*round(40*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
						TechList[1].Astrophysics +=2
		elif metalmax2 == 1 and crystalmax2 == 1 and deutmax2 == 1 and len(PlanetList) == ((TechList[1].Astrophysics + 1)/2 + 1) and IdealPlanet[0].WaitingFlag == 0 and miningtype == 2:
			metale,crystale,deute,newcole = EffectiveMining(PlanetList,TechList,IdealPlanet)
			MetalProd, CrystalProd, DeutProd = TotalProd(PlanetList,TechList,FleetList,IdealPlanet)
			MetalMetalTime = 60*1.5**IdealPlanet[0].MetalMine / MetalProd
			MetalCrystalTime = 15*1.5**IdealPlanet[0].MetalMine / CrystalProd
			MetalTime = MetalCrystalTime + MetalMetalTime - IdealPlanet[0].MetalMine/2
			CrystalMetalTime = 48*1.6**IdealPlanet[0].CrystalMine / MetalProd
			CrystalCrystalTime = 24*1.6**IdealPlanet[0].CrystalMine / CrystalProd
			CrystalTime = CrystalCrystalTime + CrystalMetalTime
			DeutMetalTime = 225*1.5**IdealPlanet[0].DeuteriumMine / MetalProd
			DeutCrystalTime = 75*1.5**IdealPlanet[0].DeuteriumMine / CrystalProd
			DeutTime = 2*DeutCrystalTime + 2*DeutMetalTime
			newcolmetalcost = 100*round(40*1.75**TechList[0].Astrophysics) + 100*round(40*1.75**(TechList[0].Astrophysics+1)) / IdealPlanet[0].ResScaleFactor / IdealPlanet[0].ResScaleFactor
			newcolcrystalcost = 100*round(80*1.75**TechList[0].Astrophysics) + 100*round(80*1.75**(TechList[0].Astrophysics+1)) / IdealPlanet[0].ResScaleFactor
			newcoldeutcost = 100*round(40*1.75**TechList[0].Astrophysics) + 100*round(40*1.75**(TechList[0].Astrophysics+1)) / IdealPlanet[0].ResScaleFactor
			for x in range(IdealPlanet[0].MetalMine):
				newcolmetalcost += 60*1.5**x / IdealPlanet[0].ResScaleFactor
				newcolcrystalcost += 15*1.5**x / IdealPlanet[0].ResScaleFactor
			for x in range(IdealPlanet[0].CrystalMine):
				newcolmetalcost += 48*1.6**x / IdealPlanet[0].ResScaleFactor
				newcolcrystalcost += 24*1.6**x / IdealPlanet[0].ResScaleFactor
			for x in range(IdealPlanet[0].DeuteriumMine):
				newcolmetalcost += 225*1.5**x / IdealPlanet[0].ResScaleFactor
				newcolcrystalcost += 75*1.5**x / IdealPlanet[0].ResScaleFactor
			newcolcrystaltime = newcolcrystalcost / CrystalProd
			newcolmetaltime = newcolmetalcost / MetalProd
			if newcolmetaltime < newcolcrystaltime:
				newcoltime = 0.15*newcolcrystaltime
			else:
				newcoltime = 0.15*newcolmetaltime
			if MetalTime <=CrystalTime and MetalTime <= DeutTime and MetalTime <= newcoltime:
				IdealPlanet[0].MetalMine +=1
			if CrystalTime <= MetalTime and CrystalTime <= DeutTime and CrystalTime <= newcoltime:
				IdealPlanet[0].CrystalMine +=1
			if DeutTime <= MetalTime and DeutTime <= CrystalTime and DeutTime <= newcoltime:
				IdealPlanet[0].DeuteriumMine +=1
			if newcoltime <= MetalTime and newcoltime <= CrystalTime and newcoltime <= DeutTime:
				if TechList[1].Astrophysics == 0:
					IdealPlanet[0].WaitingFlag = 1
					IdealPlanet[0].WaitingMetal = 4000 / IdealPlanet[0].ResScaleFactor
					IdealPlanet[0].WaitingCrystal = 8000 / IdealPlanet[0].ResScaleFactor
					IdealPlanet[0].WaitingDeut = 4000 / IdealPlanet[0].ResScaleFactor
					TechList[1].Astrophysics = 1
					if IdealPlanet[0].Shipyard < 4:
						IdealPlanet[0].Shipyard = 4
				else:
					if TechList[0].Astrophysics == TechList[1].Astrophysics:
						IdealPlanet[0].WaitingFlag = 1
						IdealPlanet[0].WaitingMetal = 100*round(40*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
						IdealPlanet[0].WaitingCrystal = 100*round(80*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
						IdealPlanet[0].WaitingDeut = 100*round(40*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
						TechList[1].Astrophysics +=2
		if TDeut > TMetal+TCrystal:
		 	TechList[1].CombustionDrive = TechList[0].CombustionDrive + 1
#	if TechList[0].Energy < IdealPlanet[0].FusionPlant+5:
#		TechList[1].Energy = TechList[0].Energy + 1


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
FleetList = []
TechList = StartTechs(TechList)
TechList = StartTechs(TechList)
for x in range(3):
	IdealPlanet = NewPlanet(IdealPlanet,TechList,FleetList,IdealPlanet,0,0,0)
	setattr(IdealPlanet[x],'WaitingFlag',0)
	setattr(IdealPlanet[x],'WaitingMetal',0)
	setattr(IdealPlanet[x],'WaitingCrystal',0)
	setattr(IdealPlanet[x],'WaitingDeut',0)
	setattr(IdealPlanet[0],'ResScaleFactor',1)
setattr(IdealPlanet[0],'Year',1)
setattr(IdealPlanet[0],'Month',1)
setattr(IdealPlanet[0],'Day',1)
setattr(IdealPlanet[0],'Hour',1)
setattr(IdealPlanet[0],'Minute',1)
PlanetList = NewPlanet(PlanetList,TechList,FleetList,IdealPlanet,0,0,0)
IdealPlanet[0].MetalMine = 3
upgradechecker = 0
for IdealPlanet[0].Year in range(0):
	for IdealPlanet[0].Month in range(12):
		for IdealPlanet[0].Day in range(30):
			print "day: " + str(IdealPlanet[0].Year) + ":" + str(IdealPlanet[0].Month) + ":" + str(IdealPlanet[0].Day)
			for IdealPlanet[0].Hour in range(23):
				for IdealPlanet[0].Minute in range(60):
					if len(PlanetList) < 100:
						minuteprod(PlanetList)
						TMetal, TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
#						if TMetal >= 100000000 or TCrystal >= 100000000 or TDeut >= 100000000:
#							IdealPlanet[0].ResScaleFactor *= 10
#							for i in range(len(PlanetList)):
#								PlanetList[i].Resource[:] = [x/10 for x in PlanetList[i].Resource]
						if IdealPlanet[0].WaitingFlag == 0 or (IdealPlanet[0].WaitingFlag == 1 and TMetal > IdealPlanet[0].WaitingMetal and TCrystal > IdealPlanet[0].WaitingCrystal and TDeut > IdealPlanet[0].WaitingDeut):
							print "Checking Upgrades!"
							evenmaintenance(PlanetList,TechList,FleetList,IdealPlanet)
							ColonyChecker(PlanetList,TechList,FleetList,IdealPlanet)
							teching(PlanetList,TechList,FleetList,IdealPlanet)
							mining(PlanetList,TechList,FleetList,IdealPlanet)
						if len(PlanetList) == 2 and upgradechecker == 0:
							print "colony founded at " + str(IdealPlanet[0].Hour) + ":" + str(IdealPlanet[0].Minute)
							upgradechecker = 1
#							upgradechecker = 0
#						if IdealPlanet[0].WaitingFlag == 1 and upgradechecker == 0:
#							upgradechecker = 1
#							metalmax = 1
#							cry	stalmax = 1
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
#for i in range(len(PlanetList)):
#	print "Planet", i, "; Satts: ", PlanetList[i].Satellites,", M:C:D Mines: ", PlanetList[i].MetalMine,":",PlanetList[i].CrystalMine,":",PlanetList[i].DeuteriumMine,"; Metals: ",PlanetList[i].Resource[0],"/", PlanetList[i].MetalCap,", Crystals: ", PlanetList[i].Resource[1],"/",PlanetList[i].CrystalCap,", Deuteriums:",PlanetList[i].Resource[2],"/",PlanetList[i].DeuteriumCap,", Rocket Launchers: ", PlanetList[i].RocketLauncher, "LC: " , PlanetList[i].LargeCargo , " SC: " , PlanetList[i].SmallCargo, PlanetList[i].EnergyProd-PlanetList[i].EnergyUsed, PlanetList[i].FusionPlant , "Research Lab", PlanetList[i].ResearchLab , PlanetList[i].Shipyard, "\n"
#print "Astrophysics = " + str(TechList[0].Astrophysics) + ":" + str(TechList[1].Astrophysics) + " Combustion = " + str(TechList[0].CombustionDrive) ,":", TechList[1].CombustionDrive , "Ideal Mines", IdealPlanet[0].MetalMine , IdealPlanet[0].CrystalMine, IdealPlanet[0].DeuteriumMine, "Ideal RL" ,IdealPlanet[0].ResearchLab,"energy Tech",TechList[0].Energy,TechList[1].Energy, "Ideal Fusion", IdealPlanet[0].FusionPlant, "Ideal Solar", IdealPlanet[0].SolarPlant, "Impulse", TechList[0].ImpulseDrive, "Espionage", TechList[0].Espionage, "Shipyard", IdealPlanet[0].Shipyard
#print IdealPlanet[0].WaitingMetal, IdealPlanet[0].WaitingCrystal, IdealPlanet[0].WaitingDeut, IdealPlanet[0].WaitingFlag, TMetal, TCrystal, TDeut, "ResScaleFactor" , IdealPlanet[0].ResScaleFactor
