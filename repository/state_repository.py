from typing import Dict, List

from models.start_state import StartState
from models.state import State


class StateRepository:
    state_repo: Dict[str, State] = {}

    def get_state_by_name(self, name) -> State:
        return self.state_repo.setdefault(name, None)

    def add_state(self, state_obj: State):
        self.state_repo[state_obj.name] = state_obj

    def get_all_states(self) -> List[State]:
        return list(self.state_repo.values())

    def get_start_state(self) ->StartState:

        for key,val in self.state_repo.items():
            if isinstance(val,StartState):
                return val
        return None
