#! /usr/bin/env python
from TechTree import *
from movingres import TotalRes, CheckToMove
import math

unispeed = 5
metalwt = 1
cryzwt = 1
deutwt = 1
colonyweight = 1


def TotalProd(PlanetList,TechList,FleetList,IdealPlanet):
	TotalMetal = TotalCrystal = TotalDeut = 0
	for x in range(len(PlanetList)):
		TotalMetal += PlanetList[x].Prod[0]
		TotalCrystal += PlanetList[x].Prod[1]
		TotalDeut += PlanetList[x].Prod[2]
	return TotalMetal, TotalCrystal,TotalDeut;

def calcstores(PlanetList,TechList,FleetList,IdealPlanet):
	for i in range(len(PlanetList)):
		constant = 20.0/33.0
		metalpow = PlanetList[i].MetalStorage * constant
		crystalpow = PlanetList[i].CrystalStorage * constant
		deutpow = PlanetList[i].DeuteriumStorage * constant
		PlanetList[i].MetalCap = 5000 * int(2.5 * math.e ** metalpow) / IdealPlanet[0].ResScaleFactor
		PlanetList[i].CrystalCap = 5000 * int(2.5 * math.e ** crystalpow) / IdealPlanet[0].ResScaleFactor
		PlanetList[i].DeuteriumCap = 5000 * int(2.5 * math.e ** deutpow) / IdealPlanet[0].ResScaleFactor

def calcenergy(PlanetList,TechList,FleetList,IdealPlanet,i):
	PlanetList[i].EnergyProd = 20*PlanetList[i].SolarPlant*1.1**PlanetList[i].SolarPlant + 30*PlanetList[i].FusionPlant*(1.05+0.01*TechList[0].Energy)**PlanetList[i].FusionPlant + PlanetList[i].Satellites*int((PlanetList[i].Temperature+160)/6)
	PlanetList[i].EnergyUsed = 10*PlanetList[i].MetalMine*1.1**PlanetList[i].MetalMine+10*PlanetList[i].CrystalMine*1.1**PlanetList[i].CrystalMine + 20*PlanetList[i].DeuteriumMine*1.1**PlanetList[i].DeuteriumMine
	if PlanetList[i].EnergyProd < PlanetList[i].EnergyUsed:
		PlanetList[i].ProductionFactor = PlanetList[i].EnergyProd/PlanetList[i].EnergyUsed
	else:
		PlanetList[i].ProductionFactor=1

def checkupstores(PlanetList,TechList,IdealPlanet,FleetList,Metal,Crystal,Deut,i):
	calcstores(PlanetList,TechList,FleetList,IdealPlanet)
	if Metal >= PlanetList[i].MetalCap-PlanetList[i].Prod[0]/60:
		TMetal, TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
		MetalCost = 1000*2**PlanetList[i].MetalStorage / IdealPlanet[0].ResScaleFactor
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,0,0,i)
		if PlanetList[i].Resource[0] >= MetalCost:
			print "Built Metal Storage Level " + str(PlanetList[i].MetalStorage + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].MetalStorage += 1
			IdealPlanet[0].WaitingFlag = 0
		else:
			if IdealPlanet[0].WaitingFlag == 0: 
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
	if Crystal >= PlanetList[i].CrystalCap-PlanetList[i].Prod[1]/60:
		TMetal, TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
		MetalCost = 1000*2**PlanetList[i].CrystalStorage / IdealPlanet[0].ResScaleFactor
		CrystalCost = 500*2**PlanetList[i].CrystalStorage / IdealPlanet[0].ResScaleFactor
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost:
			print "Built Crystal Storage Level " + str(PlanetList[i].CrystalStorage + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].CrystalStorage += 1
			IdealPlanet[0].WaitingFlag = 0
		else:
			if IdealPlanet[0].WaitingFlag == 0: 
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
				IdealPlanet[0].WaitingCrystal = CrystalCost
	if Deut >= PlanetList[i].DeuteriumCap-PlanetList[i].Prod[2]/60:
		TMetal,TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
		MetalCost = 1000*2**PlanetList[i].CrystalStorage / IdealPlanet[0].ResScaleFactor
		CrystalCost = 1000*2**PlanetList[i].CrystalStorage / IdealPlanet[0].ResScaleFactor
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost:
			print "Built Deuterium Storage Level " + str(PlanetList[i].DeuteriumStorage + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].DeuteriumStorage += 1
			IdealPlanet[0].WaitingFlag = 0
		else:
			if IdealPlanet[0].WaitingFlag == 0: 
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
				IdealPlanet[0].WaitingCrystal = CrystalCost
	calcstores(PlanetList,TechList,FleetList,IdealPlanet)

def CheckUpFusion(PlanetList,TechList,FleetList,IdealPlanet,i):
	TotalMetal,TotalCrystal,TotalDeut = TotalRes(PlanetList,IdealPlanet)
	if PlanetList[i].DeuteriumMine >= 5 and TechList[0].Energy >= 3:
		MetalCost = 900*1.8**PlanetList[i].FusionPlant / IdealPlanet[0].ResScaleFactor
		CrystalCost = 360*1.8**PlanetList[i].FusionPlant / IdealPlanet[0].ResScaleFactor
		DeutCost = 180*1.8**PlanetList[i].FusionPlant / IdealPlanet[0].ResScaleFactor
		checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,DeutCost,i)
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,DeutCost,i)
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2]>=DeutCost:
			print "Built Fusion Plant Level " + str(PlanetList[i].FusionPlant + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2]-= DeutCost
			PlanetList[i].FusionPlant += 1
			calcenergy(PlanetList,TechList,FleetList,IdealPlanet,i)
			IdealPlanet[0].WaitingFlag = 0
		else: 
			if IdealPlanet[0].WaitingFlag == 0: 
				print "Flagged Fusion"
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
				IdealPlanet[0].WaitingCrystal = CrystalCost
				IdealPlanet[0].WaitingDeut = DeutCost
	else:
		if PlanetList[i].DeuteriumMine < 5 and IdealPlanet[0].DeuteriumMine < 5:
			IdealPlanet[0].DeuteriumMine = 5
		if PlanetList[i].DeuteriumMine < 5 and IdealPlanet[0].DeuteriumMine >=5:
			CheckUpDeut(PlanetList,TechList,FleetList,IdealPlanet,i)
		if TechList[0].Energy < 3:
			TechList[1].Energy = 3
			
def CheckUpSolar(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 75*1.5**PlanetList[i].SolarPlant / IdealPlanet[0].ResScaleFactor
	CrystalCost = 30*1.5**PlanetList[i].SolarPlant / IdealPlanet[0].ResScaleFactor
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,0,i)
	TotalMetal,TotalCrystal,TotalDeut = TotalRes(PlanetList,IdealPlanet)
	CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
	if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost:
		print "Built Solar Plant Level " + str(PlanetList[i].SolarPlant + 1) + " on Planet " + str(i) +"!"
		PlanetList[i].Resource[0] -= MetalCost
		PlanetList[i].Resource[1] -= CrystalCost
		PlanetList[i].SolarPlant += 1
		calcenergy(PlanetList,TechList,FleetList,IdealPlanet,i)
		IdealPlanet[0].WaitingFlag = 0
	else: 
		if IdealPlanet[0].WaitingFlag == 0: 
			print "Flagged Solar"
			IdealPlanet[0].WaitingFlag = 1
			IdealPlanet[0].WaitingMetal = MetalCost
			IdealPlanet[0].WaitingCrystal = CrystalCost
			IdealPlanet[0].WaitingDeut = 0

def BuildSatts(PlanetList,TechList,FleetList,IdealPlanet,i,n):
	CrystalCost = 2000*n / IdealPlanet[0].ResScaleFactor
	DeutCost = 500*n / IdealPlanet[0].ResScaleFactor
	TotalMetal,TotalCrystal,TotalDeut = TotalRes(PlanetList,IdealPlanet)
	if TotalDeut > 0:
		if TotalCrystal >= CrystalCost and TotalDeut >= DeutCost and (PlanetList[i].Resource[1] < CrystalCost or PlanetList[i].Resource[2]< DeutCost) and PlanetList[i].Shipyard >=1:
			CrystalCost -= PlanetList[i].Resource[1]
			DeutCost -= PlanetList[i].Resource[2]
			if CrystalCost < 0:
				CrystalCost = 0
			if DeutCost < 0:
				DeutCost = 0
			if CrystalCost > 0 or DeutCost > 0:
				CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,0,CrystalCost,DeutCost,i)
		if PlanetList[i].Resource[1] > CrystalCost and PlanetList[i].Resource[2]> DeutCost and PlanetList[i].Shipyard >=1:
			print "Built " + str(n) + " Solar Satellites on Planet " + str(i)
			PlanetList[i].Resource[2]-= DeutCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Satellites += n
			calcenergy(PlanetList,TechList,FleetList,IdealPlanet,i)
			IdealPlanet[0].WaitingFlag = 0
		else: 
			if IdealPlanet[0].WaitingFlag == 0 and PlanetList[i].Shipyard >=1: 
				print "Flagged Satts"
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = 0
				IdealPlanet[0].WaitingCrystal = CrystalCost
				IdealPlanet[0].WaitingDeut = DeutCost
		if PlanetList[i].Shipyard < 1:
			IdealPlanet[0].Shipyard = 1
		
def CheckUpPower(PlanetList,TechList,FleetList,IdealPlanet,i,PowerNeeded):
	calcenergy(PlanetList,TechList,FleetList,IdealPlanet,i)
	sattpower = int((PlanetList[i].Temperature+160)/6)
	sattsneeded = int(PowerNeeded/sattpower)
	if PowerNeeded > 0:
		if (float(PowerNeeded)/sattpower) > sattsneeded:
			sattsneeded += 1
		if PlanetList[i].EnergyProd > 0:
			if PlanetList[i].Resource[2]> 0 and TechList[0].Astrophysics >=1:
				if ((PowerNeeded + PlanetList[i].Satellites * sattpower)/(PlanetList[i].EnergyProd+PowerNeeded)) < 0.5 and IdealPlanet[0].CrystalMine > 5:	
					BuildSatts(PlanetList,TechList,FleetList,IdealPlanet,i,sattsneeded)
				else: 
					TotalSolarCost = 75*1.5**PlanetList[i].SolarPlant + 30*1.5**PlanetList[i].SolarPlant * metalwt / cryzwt
					TotalSolarBoost = 20*(PlanetList[i].SolarPlant+1)*1.1**(PlanetList[i].SolarPlant+1) - 20*PlanetList[i].SolarPlant*1.1**PlanetList[i].SolarPlant
					SolarEffect = TotalSolarBoost/TotalSolarCost
					TotalFusionCost = 900*1.8**PlanetList[i].FusionPlant + 360*1.8**PlanetList[i].FusionPlant * metalwt/cryzwt + 180*1.8**PlanetList[i].FusionPlant * metalwt/deutwt
					TotalFusionBoost = 30*(PlanetList[i].FusionPlant+1)*(1.05 + (0.01 * TechList[0].Energy))**(PlanetList[i].FusionPlant+1) - 30*PlanetList[i].FusionPlant*(1.05 + (0.01 * TechList[0].Energy))**PlanetList[i].FusionPlant
					FusionEffect = TotalFusionBoost/TotalFusionCost
					if SolarEffect > FusionEffect:
						if PlanetList[i].SolarPlant < IdealPlanet[0].SolarPlant:
							CheckUpSolar(PlanetList,TechList,FleetList,IdealPlanet,i)
						else: 
							IdealPlanet[0].SolarPlant += 1
					else:
						if PlanetList[i].FusionPlant < IdealPlanet[0].FusionPlant:
							CheckUpFusion(PlanetList,TechList,FleetList,IdealPlanet,i)
						else:
							IdealPlanet[0].FusionPlant += 1
			else:
				if PlanetList[i].SolarPlant < IdealPlanet[0].SolarPlant:
					CheckUpSolar(PlanetList,TechList,FleetList,IdealPlanet,i)
				else:
					IdealPlanet[0].SolarPlant += 1
		else:
			CheckUpSolar(PlanetList,TechList,FleetList,IdealPlanet,i)
	calcenergy(PlanetList,TechList,FleetList,IdealPlanet,i)

def CheckUpMetal(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 60*1.5**PlanetList[i].MetalMine / IdealPlanet[0].ResScaleFactor
	CrystalCost = 15*1.5**PlanetList[i].MetalMine / IdealPlanet[0].ResScaleFactor
	SparePower = PlanetList[i].EnergyProd - PlanetList[i].EnergyUsed + 10
	PowerBoost = 10*(PlanetList[i].MetalMine+1)*1.1**(PlanetList[i].MetalMine+1)-10*PlanetList[i].MetalMine*1.1**PlanetList[i].MetalMine
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,0,i)
	if SparePower > PowerBoost:
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
		if PlanetList[i].Resource[0] > MetalCost and PlanetList[i].Resource[1] > CrystalCost:
			print "Built Metal Mine Level " + str(PlanetList[i].MetalMine + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].EnergyUsed += PowerBoost
			PlanetList[i].MetalMine += 1
			PlanetList[i].Prod[0] = unispeed * (30*PlanetList[i].MetalMine*1.1**PlanetList[i].MetalMine+30)
			IdealPlanet[0].WaitingFlag = 0
		else: 
			if IdealPlanet[0].WaitingFlag == 0: 
				print "Flagged MM"
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
				IdealPlanet[0].WaitingCrystal = CrystalCost
				IdealPlanet[0].WaitingDeut = 0
	else:
		CheckUpPower(PlanetList,TechList,FleetList,IdealPlanet,i,PowerBoost-SparePower)

def CheckUpCrystal(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 48*1.6**PlanetList[i].CrystalMine / IdealPlanet[0].ResScaleFactor
	CrystalCost = 24*1.6**PlanetList[i].CrystalMine / IdealPlanet[0].ResScaleFactor
	SparePower = PlanetList[i].EnergyProd - PlanetList[i].EnergyUsed + 10
	PowerBoost = 10*(PlanetList[i].CrystalMine+1)*1.1**(PlanetList[i].CrystalMine+1)-10*PlanetList[i].CrystalMine*1.1**PlanetList[i].CrystalMine
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,0,i)
	if SparePower > PowerBoost:
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
		if PlanetList[i].Resource[0] > MetalCost and PlanetList[i].Resource[1] > CrystalCost:
			print "Built Crystal Mine Level " + str(PlanetList[i].CrystalMine + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].EnergyUsed += PowerBoost
			PlanetList[i].CrystalMine += 1
			PlanetList[i].Prod[1] = unispeed * (20*PlanetList[i].CrystalMine*1.1**PlanetList[i].CrystalMine+15)
			IdealPlanet[0].WaitingFlag = 0
		else: 
			if IdealPlanet[0].WaitingFlag == 0: 
				print "Flagged CM"
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
				IdealPlanet[0].WaitingCrystal = CrystalCost
				IdealPlanet[0].WaitingDeut = 0
	else:
		CheckUpPower(PlanetList,TechList,FleetList,IdealPlanet,i,PowerBoost-SparePower)

def CheckUpDeut(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 225*1.5**PlanetList[i].DeuteriumMine / IdealPlanet[0].ResScaleFactor
	CrystalCost = 75*1.5**PlanetList[i].DeuteriumMine / IdealPlanet[0].ResScaleFactor
	SparePower = PlanetList[i].EnergyProd - PlanetList[i].EnergyUsed + 10
	PowerBoost = 10*(PlanetList[i].DeuteriumMine+1)*1.1**(PlanetList[i].DeuteriumMine+1)-10*PlanetList[i].DeuteriumMine*1.1**PlanetList[i].DeuteriumMine
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,0,i)
	if SparePower > PowerBoost:
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
		if PlanetList[i].Resource[0] > MetalCost and PlanetList[i].Resource[1] > CrystalCost:
			print "Built Deuterium Mine Level " + str(PlanetList[i].DeuteriumMine + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].EnergyUsed += PowerBoost
			PlanetList[i].DeuteriumMine += 2
			PlanetList[i].Prod[2] = unispeed * (20*PlanetList[i].DeuteriumMine*1.1**PlanetList[i].DeuteriumMine)
			IdealPlanet[0].WaitingFlag = 0
		else: 
			if IdealPlanet[0].WaitingFlag == 0: 
				print "Flagged DM"
				IdealPlanet[0].WaitingFlag = 1
				IdealPlanet[0].WaitingMetal = MetalCost
				IdealPlanet[0].WaitingCrystal = CrystalCost
				IdealPlanet[0].WaitingDeut = 0
	else:
		CheckUpPower(PlanetList,TechList,FleetList,IdealPlanet,i,PowerBoost-SparePower)

def checkuprobots(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 400*2**PlanetList[i].Robots
	CrystalCost = 120*2**PlanetList[i].Robots
	DeutCost = 200*2**PlanetList[i].Robots
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,DeutCost,i)
	if PlanetList[i].Robots < 10:
		checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,DeutCost,i)
		if PlanetList[i].Resource[2]>= DeutCost and PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= DeutCost:
			print "Built Robots Level " + str(PlanetList[i].Robots + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2]-= DeutCost
			PlanetList[i].Robots += 1

def CheckUpNanites(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 1000000*2**PlanetList[i].Nanites
	CrystalCost = 500000*2**PlanetList[i].Nanites
	DeutCost = 100000*2**PlanetList[1].Nanites
	if PlanetList[i].Robots == 10 and TechLst[0].Computer >=10:
		checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,DeutCost,i)
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,0,i)
		if PlanetList[i].Resource[0]>=MetalCost and PlanetList[i].Resource[1]>=CrystalCost and PlanetList[i].Resource[2] >=DeutCost:
			print "Built Nanites Level " + str(PlanetList[i].Nanites + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			PlanetList[i].Nanites += 1
		else:
			print "Flagged Nanites"
			IdealPlanet[0].WaitingFlag = 1
			IdealPlanet[0].WaitingMetal = MetalCost
			IdealPlanet[0].WaitingCrystal = CrystalCost
			IdealPlanet[0].WaitingDeut = DeutCost

def CheckUpMissileSilo(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 20000*2**PlanetList[i].MissileSilo			
	CrystalCost = 20000*2**PlanetList[i].MissileSilo
	DeutCost = 1000*2**PlanetList[i].MissileSilo
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,DeutCost,i)
	CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,DeutCost,i)
	if PlanetList[i].Resource[0]>=MetalCost and PlanetList[i].Resource[1]>=CrystalCost and PlanetList[i].Resource[2] >=DeutCost:
		print "Built Missile Silo Level " + str(PlanetList[i].MissileSilo + 1) + " on Planet " + str(i) +"!"
		PlanetList[i].Resource[0] -= MetalCost
		PlanetList[i].Resource[1] -= CrystalCost
		PlanetList[i].Resource[2] -= DeutCost
		PlanetList[i].MissileSilo += 1

def CheckUpTerraformer(PlanetList,TechList,FleetList,IdealPlanet,i):
	CrystalCost = 50000*2**PlanetList[i].Terraformer
	DeutCost = 100000*2**PlanetList[i].Terraformer
	EnergyCost = 1000*2**PlanetList[i].Terraformer
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,0,CrystalCost,DeutCost,i)
	CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,0,CrystalCost,DeutCost,i)
	if PlanetList[i].Resource[1]>=CrystalCost and PlanetList[i].Resource[2] >=DeutCost and PlanetList[i].EnergyProd >= EnergyCost and PlanetList[i].Nanites >= 1 and TechList[0].Computer >=12:
		print "Built Terraformer Level " + str(PlanetList[i].Terraformer + 1) + " on Planet " + str(i) +"!"
		PlanetList[i].Resource[1] -= CrystalCost
		PlanetList[i].Resource[2] -= DeutCost
		PlanetList[i].Terraformer += 1

def CheckUpResearchLab(PlanetList,TechList,FleetList,IdealPlanet,i):
	if IdealPlanet[0].DeuteriumMine ==0:
		IdealPlanet[0].DeuteriumMine = 1
	MetalCost = 200*2**PlanetList[i].ResearchLab
	CrystalCost = 400*2**PlanetList[i].ResearchLab
	DeutCost = 200*2**PlanetList[i].ResearchLab
	checkupstores(PlanetList,TechList,IdealPlanet,FleetList,0,CrystalCost,DeutCost,i)
	if PlanetList[i].Resource[0] > MetalCost and PlanetList[i].Resource[1] > CrystalCost and PlanetList[i].Resource[2] > DeutCost: 
		print "Built Research Lab Level " + str(PlanetList[i].ResearchLab + 1) + " on Planet " + str(i) +"!"
		PlanetList[i].Resource[0] -= MetalCost
		PlanetList[i].Resource[1] -= CrystalCost
		PlanetList[i].Resource[2] -= DeutCost
		PlanetList[i].ResearchLab += 1

def checkupshipyard(PlanetList,TechList,FleetList,IdealPlanet,i):
	MetalCost = 400*2**PlanetList[i].Shipyard / IdealPlanet[0].ResScaleFactor
	CrystalCost =200*2**PlanetList[i].Shipyard / IdealPlanet[0].ResScaleFactor
	DeutCost = 100*2**PlanetList[i].Shipyard / IdealPlanet[0].ResScaleFactor
	if PlanetList[i].Robots >= 2:
		checkupstores(PlanetList,TechList,IdealPlanet,FleetList,MetalCost,CrystalCost,DeutCost,i)
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2]>= DeutCost:
			print "Built Shipyard Level " + str(PlanetList[i].Shipyard + 1) + " on Planet " + str(i) +"!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			PlanetList[i].Shipyard += 1
	else:
		if IdealPlanet[0].Robots < 2:
			IdealPlanet[0].Robots = 2
		checkuprobots(PlanetList,TechList,FleetList,IdealPlanet,i)
