from panda3d.core import Vec3

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
    
class Planet(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class droneDefender(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)