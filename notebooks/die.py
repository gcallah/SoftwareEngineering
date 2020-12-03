import random

DEF_FACES = 6

class Die():
    '''
    A class to represent a die for playing games with.
    Contains two data members:
    num_faces: how many faces does this die have?
    up_face: which face is up?
    '''
    def __init__(self, faces=DEF_FACES):
        if not isinstance(faces, int):
            raise(TypeError("faces must be an integer"))
        if faces < 2:
            raise(ValueError("faces must be > 1"))
        num_faces = faces
        self.num_faces = faces
        self.up_face = None

    def roll(self):
        self.up_face = random.randint(1, self.num_faces)
        return self.up_face

    def get_value(self):
        if self.up_face is None:
            raise(ValueError("Must roll before getting value!"))
        return self.up_face

    def __str__(self):
        return "{}-sided die with face value of {}".format(self.num_faces, 
                                                           self.get_value())

    def __call__(self):
        return self.roll()
