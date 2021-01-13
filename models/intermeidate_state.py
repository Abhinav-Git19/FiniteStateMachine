from models.state import State

class IntermediateState(State):

    def __init__(self,name):
        super(IntermediateState, self).__init__(name)
        self.transitions=[]