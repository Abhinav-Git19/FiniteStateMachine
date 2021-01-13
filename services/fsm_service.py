from models.current_state import CurrentState
from models.end_state import EndState
from repository.state_repository import StateRepository



class FSMService:

    state_repository = StateRepository()
    current_state = CurrentState()

    def begin_fsm(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) != 1:
            print('invalid begin command')
            return

        start_state =self.state_repository.get_start_state()
        if start_state is None:
            print('StartState Not Specified')
            return
        self.current_state.cur_state=start_state

    def curent_state(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist)!=1:
            print('Invalid current state command')
            return

        if self.current_state.cur_state is None:
            print('FSM Not begun yet!')
            return
        print('Current state {}'.format(self.current_state.cur_state))

    def next_state(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist)!=2:
            print('invalid next_state command')
            return
        transition_name = cmdlist[1]

        for trans in self.current_state.cur_state.transitions:
            if trans.name==transition_name:
                self.current_state.cur_state=trans.next_state
                if isinstance(self.current_state.cur_state, EndState):
                    print('End State {} reached'.format(self.current_state.cur_state.name))

                if self.current_state.cur_state.notification:
                    print('State Changed to {}'.format(self.current_state.cur_state.name))
                return

        print('Transition not found')

    def enable_notification_by_state(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) != 2:
            print('invalid notification command')
            return
        state_name = cmdlist[1]
        state = self.state_repository.get_state_by_name(state_name)
        if state is None:
            print('No such state')
            return
        state.notification=True

    def enable_all_notifications(self,cmdargs):
        cmdlist = cmdargs.split()
        if len(cmdlist) != 1:
            print('invalid all_notification command')
            return

        state_list = self.state_repository.get_all_states()
        for state in state_list:
            state.notification=True









