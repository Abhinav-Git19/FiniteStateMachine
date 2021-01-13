from models.state import State

class StartState(State):

    def __init__(self,name):
        super(StartState, self).__init__(name)
        self.transitions=[]