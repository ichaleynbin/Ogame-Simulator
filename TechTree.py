#! /usr/bin/env python
import math
from movingres import CheckToMove, TotalRes

class Technologies():
    Techs = {'Energy':0,'Laser':0,'Ion':0,'Hyperspace':0,'Plasma':0,'CombustionDrive':0
            ,'ImpulseDrive':0,'HyperDrive':0,'Espionage':0,'Computer':0,'Astrophysics':0
            ,'IGRN':0,'Grav':0,'Weapons':0,'Shielding':0,'Armor':0}
    def __init__(self):
        setattr(self,Techs,Techs)
    
#############  BEGIN RESEARCHING FUNCTIONS.

def CheckUpEnergy(PlanetList,FleetList,TechList,IdealPlanet):
	CrystalCost = 800*2**TechList[0].Energy / IdealPlanet[0].ResScaleFactor
	DeutCost = 400*2**TechList[0].Energy / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 1:
			print "Researched Energy Tech level " + str(TechList[0].Energy + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].Energy += 1

def CheckUpComputer(PlanetList,FleetList,TechList,IdealPlanet):
	CrystalCost = 400*2**TechList[0].Computer / IdealPlanet[0].ResScaleFactor
	DeutCost = 600*2**TechList[0].Computer / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 1:
			print "Researched Computer Tech level " + str(TechList[0].Computer + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].Computer += 1

def CheckUpCombustion(PlanetList,FleetList,TechList,IdealPlanet):
	TMetal,TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
	MetalCost = 400*2**TechList[0].CombustionDrive / IdealPlanet[0].ResScaleFactor
	DeutCost = 600*2**TechList[0].CombustionDrive / IdealPlanet[0].ResScaleFactor
	if TMetal >= MetalCost and TDeut >= DeutCost and PlanetList[0].ResearchLab >= 1 and TechList[0].CombustionDrive >=2 and (PlanetList[0].Resource[0] < MetalCost or PlanetList[0].Resource[2] < DeutCost):
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,0,DeutCost,0)
		print "Consolidated resources!"
	if PlanetList[0].Resource[0] > MetalCost and PlanetList[0].Resource[2] > DeutCost:
		print "Researched Combustion Drive level " + str(TechList[0].CombustionDrive + 1) + " on planet 1!"
		PlanetList[0].Resource[0] -= MetalCost
		PlanetList[0].Resource[2] -= DeutCost
		TechList[0].CombustionDrive += 1

def CheckUpLaser(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 200*2**TechList[0].Laser / IdealPlanet[0].ResScaleFactor
	CrystalCost = 100*2**TechList[0].Laser / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].ResearchLab >= 1:
			print "Researched Laser Tech level " + str(TechList[0].Laser + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			TechList[0].Laser += 1

def CheckUpArmor(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 1000*2**TechList[0].Armor / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].ResearchLab >= 2:
			print "Researched Armor Tech level " + str(TechList[0].Armor + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			TechList[0].Armor += 1

def CheckUpImpulse(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 2000*2**TechList[0].ImpulseDrive / IdealPlanet[0].ResScaleFactor
	CrystalCost = 4000*2**TechList[0].ImpulseDrive / IdealPlanet[0].ResScaleFactor
	DeutCost = 600*2**TechList[0].ImpulseDrive / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 2:
			print "Researched Impulse Drive level " + str(TechList[0].ImpulseDrive + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].ImpulseDrive += 1
	if TechList[0].ImpulseDrive >=5:
		FleetList[0].SmallCargo = 10000

def CheckUpEspionage(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 200*2**TechList[0].Espionage / IdealPlanet[0].ResScaleFactor
	CrystalCost = 1000*2**TechList[0].Espionage / IdealPlanet[0].ResScaleFactor
	DeutCost = 200*2**TechList[0].Espionage / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] > MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 3:
			print "Researched Espionage Tech level " + str(TechList[0].Espionage + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].Espionage += 1	

def CheckUpAstrophysics(PlanetList,FleetList,IdealPlanet,TechList):
	MetalCost = 100*round(40*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
	CrystalCost = 100*round(80*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
	DeutCost = 100*round(40*1.75**TechList[0].Astrophysics) / IdealPlanet[0].ResScaleFactor
	TMetal,TCrystal,TDeut = TotalRes(PlanetList,IdealPlanet)
	if TMetal >= MetalCost and TCrystal >= CrystalCost and TDeut >= DeutCost and PlanetList[0].ResearchLab >= 3:
		CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,DeutCost,0)
		print "Consolidated resources!"
	else:
		if IdealPlanet[0].WaitingFlag == 0 and TCrystal >= 0.8*CrystalCost: 
			IdealPlanet[0].WaitingFlag = 1
			IdealPlanet[0].WaitingMetal = MetalCost
			IdealPlanet[0].WaitingCrystal = CrystalCost
			IdealPlanet[0].WaitingDeut = DeutCost
	if PlanetList[0].Resource[0] >= MetalCost and PlanetList[0].Resource[1] >= CrystalCost and PlanetList[0].Resource[2] >= DeutCost and PlanetList[0].ResearchLab >= 3:
			IdealPlanet[0].WaitingFlag = 0
			print "Found Planet was enough for astro!"
			print "Researched Astrophysics level " + str(TechList[0].Astrophysics + 1) + "!"
			PlanetList[0].Resource[0] -= MetalCost
			PlanetList[0].Resource[1] -= CrystalCost
			PlanetList[0].Resource[2] -= DeutCost
			TechList[0].Astrophysics += 1
			IdealPlanet[0].WaitingFlag = 0

def CheckUpWeapons(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 200*2**TechList[0].Weapons / IdealPlanet[0].ResScaleFactor
	CrystalCost = 100*2**TechList[0].Weapons / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].ResearchLab >= 4:
			print "Researched Weapons Tech level " + str(TechList[0].Weapons + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			TechList[0].Weapons += 1

def CheckUpIon(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 1000*2**TechList[0].Ion / IdealPlanet[0].ResScaleFactor
	CrystalCost = 300*2**TechList[0].Ion / IdealPlanet[0].ResScaleFactor
	DeutCost = 100*2**TechList[0].Ion / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 4:
			print "Researched Ion Tech level " + str(TechList[0].Ion + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].Ion += 1

def CheckUpPlasma(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 2000*2**TechList[0].Plasma / IdealPlanet[0].ResScaleFactor
	CrystalCost = 4000*2**TechList[0].Plasma / IdealPlanet[0].ResScaleFactor
	DeutCost = 1000*2**TechList[0].Plasma / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 4:
			print "Researched Plasma Tech level " + str(TechList[0].Plasma + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].Plasma += 1

def CheckUpShielding(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 200*2**TechList[0].Shielding / IdealPlanet[0].ResScaleFactor
	CrystalCost = 600*2**TechList[0].Shielding / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].ResearchLab >= 6:
			print "Researched Shielding Tech level " + str(TechList[0].Shielding + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			TechList[0].Shielding += 1

def CheckUpHyperspace(PlanetList,FleetList,TechList,IdealPlanet):
	CrystalCost = 4000*2**TechList[0].Hyperspace / IdealPlanet[0].ResScaleFactor
	DeutCost = 2000*2**TechList[0].Hyperspace / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 8:
			print "Researched Hyperspace Tech level " + str(TechList[0].Hyperspace + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].Hyperspace += 1

def CheckUpHyperDrive(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 10000*2**TechList[0].HyperDrive / IdealPlanet[0].ResScaleFactor
	CrystalCost = 20000*2**TechList[0].HyperDrive / IdealPlanet[0].ResScaleFactor
	DeutCost = 6000*2**TechList[0].HyperDrive / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 8:
			print "Researched HyperDrive level " + str(TechList[0].HyperDrive + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].HyperDrive += 1
	if TechList[0].HyperDrive >=8:
		FleetList[0].Bomber = 5000

def CheckUpIGRN(PlanetList,FleetList,TechList,IdealPlanet):
	MetalCost = 240000*2**TechList[0].IGRN / IdealPlanet[0].ResScaleFactor
	CrystalCost = 400000*2**TechList[0].IGRN / IdealPlanet[0].ResScaleFactor
	DeutCost = 120000*2**TechList[0].IGRN / IdealPlanet[0].ResScaleFactor
	for i in range(len(PlanetList)):
		if PlanetList[i].Resource[0] >= MetalCost and PlanetList[i].Resource[1] >= CrystalCost and PlanetList[i].Resource[2] >= DeutCost and PlanetList[i].ResearchLab >= 10:
			print "Researched IGRN level " + str(TechList[0].IGRN + 1) + " on planet " + str(i) + "!"
			PlanetList[i].Resource[0] -= MetalCost
			PlanetList[i].Resource[1] -= CrystalCost
			PlanetList[i].Resource[2] -= DeutCost
			TechList[0].IGRN += 1

def CheckUpGrav(PlanetList,FleetList,TechList,IdealPlanet):
	for i in range(len(PlanetList)):
		if PlanetList[i].EnergyProd > 300000 and PlanetList[i].ResearchLab >= 12:
			TechList[0].Grav = 1
			print "Researched Grav on planet " + str(i) + "!"

#####################################  END RESEARCHING FUNCTIONS

def teching(PlanetList,TechList,FleetList,IdealPlanet):

#######################################  START DEPENDENCY TREE

	if TechList[1].Energy > TechList[0].Energy:
		if IdealPlanet[0].ResearchLab >=1 and TechList[0].Energy <4:
			CheckUpEnergy(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			IdealPlanet[0].ResearchLab = 1

	if TechList[1].Computer > TechList[0].Computer:
		if IdealPlanet[0].ResearchLab >=1:
			CheckUpComputer(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			IdealPlanet[0].ResearchLab = 1

	if TechList[1].CombustionDrive > TechList[0].CombustionDrive:
		if IdealPlanet[0].ResearchLab >=1 and TechList[0].Energy >=1:
			CheckUpCombustion(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			if IdealPlanet[0].ResearchLab < 1:
				IdealPlanet[0].ResearchLab = 1
			if TechList[1].Energy < 1:
				TechList[1].Energy = 1 

	if TechList[1].Laser > TechList[0].Laser:
		if IdealPlanet[0].ResearchLab >=1 and TechList[0].Energy >=2 and TechList[0].Laser < 12:
			CheckUpLaser(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			if IdealPlanet[0].ResearchLab < 1:
				IdealPlanet[0].ResearchLab = 1
			if TechList[1].Energy < 2:
				TechList[1].Energy = 2 

	if TechList[1].Armor > TechList[0].Armor:
		if IdealPlanet[0].ResearchLab >=2:
			CheckUpArmor(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			IdealPlanet[0].ResearchLab = 2

	if TechList[1].ImpulseDrive > TechList[0].ImpulseDrive:
		if IdealPlanet[0].ResearchLab >= 2 and TechList[0].Energy >= 1:
			CheckUpImpulse(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			if TechList[0].Energy < 1 and TechList[1].Energy < 1:
				TechList[1].Energy = 1
			if IdealPlanet[0].ResearchLab < 2:
				IdealPlanet[0].ResearchLab = 2

	if TechList[1].Espionage > TechList[0].Espionage:
		if IdealPlanet[0].ResearchLab >= 3:
			CheckUpEspionage(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			IdealPlanet[0].ResearchLab = 3

	if TechList[1].Astrophysics > TechList[0].Astrophysics:
		if TechList[0].Espionage >= 4 and TechList[0].ImpulseDrive >= 3 and IdealPlanet[0].ResearchLab >= 3:
			CheckUpAstrophysics(PlanetList,FleetList,IdealPlanet,TechList)
		else:
			if TechList[1].Espionage < 4:
				TechList[1].Espionage = 4
			if TechList[1].ImpulseDrive < 3:
				TechList[1].ImpulseDrive = 3
			if IdealPlanet[0].ResearchLab < 3:
				IdealPlanet[0].ResearchLab = 3

	if TechList[1].Weapons > TechList[0].Weapons:
		if IdealPlanet[0].ResearchLab >= 4:
			CheckUpWeapons(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			IdealPlanet[0].ResearchLab = 4

	if TechList[1].Ion > TechList[0].Ion:
		if IdealPlanet[0].ResearchLab >=4 and TechList[0].Energy >=4 and TechList[0].Laser >= 5 and TechList[0].Ion <5:
			CheckUpIon(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			if IdealPlanet[0].ResearchLab < 4:
				IdealPlanet[0].ResearchLab = 4
			if TechList[1].Energy < 4:
				TechList[1].Energy = 4
			if TechList[1].Laser < 5:
				TechList[1].Laser = 5

	if TechList[1].Plasma > TechList[0].Plasma:
		if IdealPlanet[0].ResearchLab >=4 and TechList[0].Energy >=8 and TechList[0].Laser >= 10 and TechList[0].Ion >= 5 and TechList[0].Plasma < 7:
			CheckUpPlasma(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			if IdealPlanet[0].ResearchLab < 4:
				IdealPlanet[0].ResearchLab = 4
			if TechList[1].Energy < 8:
				TechList[1].Energy = 8
			if TechList[1].Laser < 10:
				TechList[1].Laser = 10
			if TechList[1].Ion < 5:
				TechList[1].Ion = 5

	if TechList[1].Shielding > TechList[0].Shielding:
		if IdealPlanet[0].ResearchLab >= 6 and TechList[0].Energy >= 3:
			CheckUpShielding(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			if TechList[1].Energy < 3:
				TechList[1].Energy = 3
			if IdealPlanet[0].ResearchLab < 6:
				IdealPlanet[0].ResearchLab = 6

	if TechList[1].Hyperspace > TechList[0].Hyperspace:
		if TechList[0].Shielding >= 5 and TechList[0].Energy >= 5 and IdealPlanet[0].ResearchLab >= 7 and TechList[0].Hyperspace < 8:
			CheckUpHyperspace(PlanetList,FleetList,IdealPlanet,TechList)
		else:
			if TechList[1].Shielding < 5:
				TechList[1].Shielding = 5
			if TechList[1].Energy < 5:
				TechList[1].Energy = 5
			if IdealPlanet[0].ResearchLab < 7:
				IdealPlanet[0].ResearchLab = 7

	if TechList[1].HyperDrive > TechList[0].HyperDrive:
		if TechList[0].Hyperspace >= 3 and IdealPlanet[0].ResearchLab >= 7:
			CheckUpHyperDrive(PlanetList,FleetList,IdealPlanet,TechList)
		else:
			if TechList[1].Hyperspace < 3:
				TechList[1].Hyperspace = 3
			if IdealPlanet[0].ResearchLab < 7:
				IdealPlanet[0].ResearchLab = 7

	if TechList[1].IGRN > TechList[0].IGRN:
		if TechList[0].Computer >= 8 and TechList[0].Hyperspace >= 8 and IdealPlanet[0].ResearchLab >= 10:
			CheckUpIGRN(PlanetList,FleetList,IdealPlanet,TechList)
		else:
			if TechList[1].Computer < 8:
				TechList[1].Computer = 8
			if TechList[1].Hyperspace < 8:
				TechList[1].Hyperspace = 8
			if IdealPlanet[0].ResearchLab < 10:
				IdealPlanet[0].ResearchLab = 10

	if TechList[1].Grav > TechList[0].Grav: 
		if IdealPlanet[0].ResearchLab >=12 and TechList[0].Grav < 1:
			CheckUpGrav(PlanetList,FleetList,TechList,IdealPlanet)
		else:
			IdealPlanet[0].ResearchLab = 12

#######################  END DEPENDENCY TREE

