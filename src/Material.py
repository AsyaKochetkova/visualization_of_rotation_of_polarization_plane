
class Material:
    def __init__(self,length, rotation_coef):
        self.length = length
        self.coef = rotation_coef

    def get_rotation_angle(self):
        return self.length*self.coef

