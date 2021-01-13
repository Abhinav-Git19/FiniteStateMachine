from services.fsm_service import FSMService
from services.state_trans_service import StateTransService
def main():
    state_trans_service = StateTransService()
    fsm_service = FSMService()

    fsm_commands =['begin_fsm','next_state','enable_notification_by_state','enable_all_notifications','curent_state']
    state_commands =['add_start_state','add_state','end_state','add_transition']

    while True:
        cmdargs = input('\nEnter Command\n')
        if cmdargs=='EXIT':
            print('Exiting FSM...')
            exit()

        base_cmd = cmdargs.split()[0]
        if base_cmd in fsm_commands:
            getattr(fsm_service,base_cmd)(cmdargs)
        elif base_cmd in state_commands:
            getattr(state_trans_service,base_cmd)(cmdargs)
        else:
            print('Invalid Command')



if __name__ == '__main__':
    main()