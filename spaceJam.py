# Makayla Farley
# february 8th, 2024

from direct.showbase.ShowBase import ShowBase
import defensePaths as defensePaths
import spaceJamClasses as spaceJamClasses
class spaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)   
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position, 5)
        

    def sceneSetup(self):

        self.universe = spaceJamClasses.universe(self.loader, "./assets/universe/Universe.x", self.render,'universe',"./assets/universe/universe.jpeg", (0, 0, 0), 10000)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/green.jpg", (-6000, -3000, -800), 250)
        self.planet2 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/purple.jpg", (0, 6000, 0), 300)
        self.planet3 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/rocky.jpg", (-6000, -5000, 200), 500)
        self.planet4 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/sandy.jpg", (300, 6000, 500), 150)
        self.planet5 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/mars.jpg", (700, 2000, 100), 500)
        self.planet6 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/planets/sun.jpg", (0, -900, -1400), 700)

        fullCycle = 60

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.planet1, nickName)
            self.DrawBaseballSeams(self.planet2, nickName, 1, 3)

        #self.ship = self.loader.loadModel("./assets/spaceShip/Khan.x")
       # self.ship.reparentTo(self.render)
      #  self.ship.setPos(450, -4000, 67)
      #  self.ship.setScale(10)

      #  tex8 = self.loader.loadTexture("./assets/spaceShip/Khan.jpg")
      #  self.ship.setTexture(tex8, 1)

       # self.spaceStation = self.loader.loadModel("./assets/spaceStation/spaceStation.x")
       # self.spaceStation.reparentTo(self.render)
      #  self.spaceStation.setPos(5000, -5000, 67)
       # self.spaceStation.setScale(100)

        #tex9 = self.loader.loadTexture("./assets/spaceStation/SpaceStation1_Dif2.png")
       # self.spaceStation.setTexture(tex9, 1)
    





app = spaceJam()  
app.sceneSetup()  
app.run()