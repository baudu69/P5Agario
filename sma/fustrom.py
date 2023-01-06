from pygame import Vector2

radiusBase = 15

class Fustrom:
    def __init__(self, parent=None):
        self.parent = parent
        self.radius = radiusBase * parent.taille
        self.objetsPercus = []

    def inside(self, obj):
        if not hasattr(obj, "position"):
            return False
        if not isinstance(obj.position, Vector2):
            return False
        if obj.position.distance_to(self.parent.position) < self.radius:
            return True
        return False

    def insideObject(self, obj):
        if not hasattr(obj, "position"):
            return False
        if not isinstance(obj.position, Vector2):
            return False
        if obj.position.distance_to(self.parent.position) < self.parent.taille:
            return True
        return False

    def majRadius(self):
        self.radius = radiusBase * self.parent.taille
