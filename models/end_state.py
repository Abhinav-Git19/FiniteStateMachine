from models.state import State

class EndState(State):
    def __init__(self,name):
        super(EndState, self).__init__(name)
        # End state will have no transitions