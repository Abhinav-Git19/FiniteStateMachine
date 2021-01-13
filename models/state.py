import  uuid
class State:

    def __init__(self,name):
        self.id=uuid.uuid1().hex
        self.name=name
        self.notification : bool =False
