from typing import List

from models.end_state import EndState
from models.start_state import StartState
from models.state import State
from models.transition import Transition
from repository.state_repository import StateRepository
from models.intermeidate_state import IntermediateState


class StateTransService:
    state_repository = StateRepository()



    def add_start_state(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist)!=2:
            print('Invalid Command')
            return

        name = cmdlist[1]
        state_list : List[State] = self.state_repository.get_all_states()

        for state in state_list:
            if isinstance(state,StartState):
                print('Start State already present cannot add multiple start state')
                return

        start_state = StartState(name)
        self.state_repository.add_state(start_state)

        print('Start State added')




    def add_state(self, cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) != 2:
            print('Invalid Add State Command')
            return

        name: str = cmdlist[1]
        state_obj = self.state_repository.get_state_by_name(name)
        if state_obj is not None:
            print('State already present')
            return

        new_state = IntermediateState(name)
        self.state_repository.add_state(new_state)
        print('Added State {}'.format(new_state.id))


    def end_state(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) != 2:
            print('Invalid End State Command')
            return
        name = cmdlist[1]

        state_obj = self.state_repository.get_state_by_name(name)
        if state_obj is not None:
            print('State already present')
            return

        end_state = EndState(name)
        self.state_repository.add_state(end_state)
        print('End State {} Added'.format(end_state.id))

    def add_transition(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) != 4:
            print('Invalid Transition State Command')
            return

        trans_name,first_state_name,next_state_name = cmdlist[1:]

        first_state= self.state_repository.get_state_by_name(first_state_name)
        second_state = self.state_repository.get_state_by_name(next_state_name)

        if first_state is None or second_state is None:
            print('Invalid Transition')
            return
        if isinstance(first_state,EndState):
            print('First state cannot be end state')
            return

        transition = Transition(trans_name,second_state)
        first_state.transitions.append(transition)


        print('Transtion {} added'.format(transition))






