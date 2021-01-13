import  uuid

from models.state import State


class Transition:
    def __init__(self,name,state):
        self.id=uuid.uuid1().hex
        self.name=name
        self.next_state : State=state