# Makayla Farley
# february 8th, 2024

from direct.showbase.ShowBase import ShowBase
import defensePaths as defensePaths
import spaceJamClasses as spaceJamClasses
class spaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        def DrawCloudDefense(planet, nickName, centralObject):
            unitVec = defensePaths.Cloud()
            unitVec.normalize()
            spaceJamClasses.Drone(self.loader, "./assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./assets/DroneDefender/octotoad1_auv.png", position, 10)

    def sceneSetup(self):

        self.planet1 = spaceJamClasses.Planet(self.loader, "./assets/planets/protoPlanet.x", self.render,'planet1',"./assets/universe/universe.jpeg", (-6000, -3000, -800), 250)

        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.planet1, nickName, centralObject)


        #self.universe = self.loader.loadModel("./assets/universe/Universe.x")
        #self.universe.reparentTo(self.render)
        #self.universe.setScale(15000)

        #tex = self.loader.loadTexture("")
        #self.universe.setTexture(tex, 1)

        #self.planet1 = self.loader.loadModel("")
        #self.planet1.reparentTo(self.render)
        #self.planet1.setPos(1000, -3000, 67)
        #self.planet1.setScale(350)

        #tex2 = self.loader.loadTexture("./assets/planets/green.jpg")
        #self.planet1.setTexture(tex2, 1)

       # self.planet2 = self.loader.loadModel("./assets/planets/protoPlanet.x")
     #   self.planet2.reparentTo(self.render)
     #   self.planet2.setPos(1000, 4000, 67)
     #   self.planet2.setScale(350)

     #   tex3 = self.loader.loadTexture("./assets/planets/purple.jpg")
       # self.planet2.setTexture(tex3, 1)

     #   self.planet3 = self.loader.loadModel("./assets/planets/protoPlanet.x")
    #    self.planet3.reparentTo(self.render)
     #   self.planet3.setPos(3000, 5000, 67)
     #   self.planet3.setScale(350)
#
      #  tex4 = self.loader.loadTexture("./assets/planets/rocky.jpg")
      #  self.planet3.setTexture(tex4, 1)
#
      #  self.planet4 = self.loader.loadModel("./assets/planets/protoPlanet.x")
      #  self.planet4.reparentTo(self.render)
      #  self.planet4.setPos(2000, 1000, 67)
      #  self.planet4.setScale(350)

       # tex5 = self.loader.loadTexture("./assets/planets/sandy.jpg")
       # self.planet4.setTexture(tex5, 1)

       # self.planet5 = self.loader.loadModel("./assets/planets/protoPlanet.x")
      #  self.planet5.reparentTo(self.render)
      #  self.planet5.setPos(1000, 3000, 67)
       # self.planet5.setScale(350)

       # tex6 = self.loader.loadTexture("./assets/planets/mars.jpg")
       # self.planet5.setTexture(tex6, 1)

       # self.planet6 = self.loader.loadModel("./assets/planets/protoPlanet.x")
        #self.planet6.reparentTo(self.render)
        #self.planet6.setPos(-500, 5600, 67)
       # self.planet6.setScale(350)

       # tex7 = self.loader.loadTexture("./assets/planets/sun.jpg")
       # self.planet6.setTexture(tex7, 1)

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
    fullCycle = 60





app = spaceJam()  
app.sceneSetup()  
app.run()