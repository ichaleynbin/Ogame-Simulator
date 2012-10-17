#! /usr/bin/env python
import math

def TotalRes(PlanetList,IdealPlanet):
	TotalMetal = TotalCrystal = TotalDeut = 0
	for x in range(len(PlanetList)):
		TotalMetal += PlanetList[x].Resource[0]
		TotalCrystal += PlanetList[x].Resource[1]
		TotalDeut += PlanetList[x].Resource[2]
	return TotalMetal, TotalCrystal,TotalDeut;


def movecargoes(PlanetList,TechList,FleetList,IdealPlanet,i,d,SCs,LCs):
	if PlanetList[i].SmallCargo > SCs:
		PlanetList[i].SmallCargo -= SCs
		PlanetList[d].SmallCargo += SCs
	if PlanetList[i].LargeCargo > LCs:
		PlanetList[i].LargeCargo -= LCs
		PlanetList[d].LargeCargo += LCs

def createcargoes(PlanetList,TechList,FleetList,IdealPlanet,i,difference):
	if PlanetList[i].Shipyard>=4 and TechList[0].CombustionDrive >=6 and PlanetList[i].Resource[0] >= 6000 and PlanetList[i].Resource[1] >= 6000:
		large = 1
		cargonum = difference / 25000
		metcargoesposs = PlanetList[i].Resource[0] / 6000 
		cryzcargoesposs = PlanetList[i].Resource[1] / 6000
		Createcargoes = int(min(cargonum, metcargoesposs, cryzcargoesposs))
		if Createcargoes > 0:
			PlanetList[i].LargeCargo += Createcargoes
			PlanetList[i].Resource[0] -= Createcargoes * 6000
			PlanetList[i].Resource[1] -= Createcargoes * 6000
			print "Built " + str(Createcargoes) + " Large Cargoes on planet " + str(i) +"!"
	elif PlanetList[i].Shipyard>=2 and TechList[0].CombustionDrive >=2 and PlanetList[i].Resource[0] >= 2000 and PlanetList[i].Resource[1] >= 2000:
		large = 0
		cargonum = difference / 5000
		metcargoesposs = PlanetList[i].Resource[0] / 2000
		cryzcargoesposs = PlanetList[i].Resource[1] / 2000
		Createcargoes = int(min(cargonum, metcargoesposs, cryzcargoesposs))
		if Createcargoes > 0:
			PlanetList[i].SmallCargo += Createcargoes
			PlanetList[i].Resource[0] -= Createcargoes * 2000
			PlanetList[i].Resource[1] -= Createcargoes * 2000
			print "Built " + str(Createcargoes) + " Small Cargoes on planet " + str(i) +"!"
	elif PlanetList[i].Shipyard < 4 and TechList[0].CombustionDrive > 6 and PlanetList[i].Shipyard >=2:
		if IdealPlanet[0].Shipyard < 4:
			IdealPlanet[0].Shipyard = 4
		large = 0
		cargonum = difference / 5000
		metcargoesposs = PlanetList[i].Resource[0] / 2000
		cryzcargoesposs = PlanetList[i].Resource[1] / 2000
		Createcargoes = int(min(cargonum, metcargoesposs, cryzcargoesposs))
		if Createcargoes > 0:
			PlanetList[i].SmallCargo += Createcargoes
			PlanetList[i].Resource[0] -= Createcargoes * 2000
			PlanetList[i].Resource[1] -= Createcargoes * 2000
			print "Built " + str(Createcargoes) + " Small Cargoes on planet " + str(i) +"!"

	else:
		Createcargoes = 0
		large = 0
	return Createcargoes,large;

def MoveRes(PlanetList,FleetList,TechList,IdealPlanet,i,d,Metal,Crystal,Deut):
	if Metal <= PlanetList[i].Resource[0] and Crystal <= PlanetList[i].Resource[1] and Deut <= PlanetList[i].Resource[2]:
		test = 1
		LCs = int((Metal+Crystal+Deut)/25000) + 1
		if LCs <= PlanetList[i].LargeCargo:
			movecargoes(PlanetList,TechList,FleetList,IdealPlanet,i,d,0,LCs)
			PlanetList[i].Resource[0] -= Metal
			PlanetList[d].Resource[0] += Metal
			PlanetList[i].Resource[1] -= Crystal
			PlanetList[d].Resource[1] += Crystal
			PlanetList[i].Resource[2] -= Deut
			PlanetList[d].Resource[2] += Deut
		else:
			remainder =  (Metal+Crystal+Deut) - PlanetList[i].LargeCargo * 25000
			SCs = int(remainder/ 5000)
			if (remainder/5000) > SCs:
				SCs += 1
			movecargoes(PlanetList,TechList,FleetList,IdealPlanet,i,d,SCs,PlanetList[i].LargeCargo)
			PlanetList[i].Resource[0] -= Metal
			PlanetList[d].Resource[0] += Metal
			PlanetList[i].Resource[1] -= Crystal
			PlanetList[d].Resource[1] += Crystal
			PlanetList[i].Resource[2] -= Deut
			PlanetList[d].Resource[2] += Deut
	else:
		test = 0
	return test;


def FindCargoesToMove(PlanetList,TechList,FleetList,IdealPlanet,d,TotalRes):
	for x in range(len(PlanetList)):
		if x != d:
			LCs = SCs = 0
			if PlanetList[x].LargeCargo > 0:
				while TotalRes > 0 and LCs <= PlanetList[x].LargeCargo:
					LCs += 1
					TotalRes -= 25000
			if PlanetList[x].SmallCargo > 0:
				while TotalRes > 0 and SCs <= PlanetList[x].SmallCargo:
					SCs += 1
					TotalRes -= 5000
			movecargoes(PlanetList,TechList,FleetList,IdealPlanet,x,d,SCs,LCs)
	if TotalRes > 0:
		for x in range(len(PlanetList)):
			cargoes, large = createcargoes(PlanetList,TechList,FleetList,IdealPlanet,x,TotalRes)
			if large == 1:
				movecargoes(PlanetList,TechList,FleetList,IdealPlanet,x,d,0,cargoes)
				TotalRes -= cargoes * 25000
			else:
				movecargoes(PlanetList,TechList,FleetList,IdealPlanet,x,d,cargoes,0)
				TotalRes -= cargoes * 5000

def FindResToMove(PlanetList,TechList,FleetList,IdealPlanet,d,Metal,Crystal,Deut):
	x = 0
	while (int(Metal) > 0 or int(Crystal) > 0 or int(Deut) > 0) and x < len(PlanetList):
		if x != d:
			if (Deut + 1) < PlanetList[x].Resource[2]:
				MoveDeut = int(Deut) + 1
			else:
				MoveDeut = int(PlanetList[x].Resource[2])
			if (Crystal + 1)< PlanetList[x].Resource[1]:
				MoveCrystal = int(Crystal) + 1
			else:
				MoveCrystal = int(PlanetList[x].Resource[1])
			if (Metal +1) < PlanetList[x].Resource[0]:
				MoveMetal = int(Metal) + 1
			else:
				MoveMetal = int(PlanetList[x].Resource[0])
			if MoveMetal < 0:
				MoveMetal = 0
			if MoveCrystal < 0:
				MoveCrystal = 0
			if MoveDeut < 0:
				Movedeut = 0
			if MoveMetal > 0 or MoveCrystal > 0 or MoveDeut > 0:
				FindCargoesToMove(PlanetList,TechList,FleetList,IdealPlanet,x,(MoveMetal + MoveCrystal + MoveDeut))
				test =  MoveRes(PlanetList,FleetList,TechList,IdealPlanet,x,d,MoveMetal,MoveCrystal,MoveDeut)
				if test:
					Metal -= MoveMetal
					Crystal -= MoveCrystal
					Deut -= MoveDeut
		x += 1	


def CheckToMove(PlanetList,TechList,FleetList,IdealPlanet,MetalCost,CrystalCost,DeutCost,d):
	TMetal, TCrystal, TDeut = TotalRes(PlanetList,IdealPlanet)
	if TMetal>=MetalCost and TCrystal>=CrystalCost and TDeut>=DeutCost and (PlanetList[d].Resource[0]<MetalCost or PlanetList[d].Resource[1]<CrystalCost or PlanetList[d].Resource[2]<DeutCost) and TechList[0].CombustionDrive >= 2:
		MetalShort = MetalCost - PlanetList[d].Resource[0]
		CrystalShort = CrystalCost - PlanetList[d].Resource[1]
		DeutShort = DeutCost - PlanetList[d].Resource[2]
		if MetalShort < 0:
			MetalShort = 0
		if CrystalShort < 0:
			CrystalShort = 0
		if DeutShort < 0:
			DeutShort = 0
		if MetalShort > 0 or CrystalShort > 0 or DeutShort > 0:
			print "Consolidating Resources to Planet " +str(d) + "!"
			FindResToMove(PlanetList,TechList,FleetList,IdealPlanet,d,MetalShort,CrystalShort,DeutShort)
	elif TechList[0].CombustionDrive <2:
		TechList[1].CombustionDrive = 2

