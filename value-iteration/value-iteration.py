import numpy as np
import operator
import sys

# grid size
WIDTH       = 4
HEIGHT      = 3
# probabilities of each actions
PROB_ACT_1  = .8
PROB_ACT_2  = .1
PROB_ACT_3  = .1
# number of possible actions
ACT_MAX     = 3
# action names
ACT_LEFT    = '←'
ACT_RIGHT   = '→'
ACT_UP      = '↑'
ACT_DOWN    = '↓'

# discount factor
DISC_FACTOR = .9

def new_states():
    return np.zeros((HEIGHT, WIDTH))

def out_of_bounds(state, blocked_states):
    (row, col) = state
    if col < 0 or row < 0 or col >= WIDTH or row >= HEIGHT or state in blocked_states:
        return True
    return False

def next_policies(state, blocked_states):
    def add_action(action, prob, list):
        if action == ACT_LEFT:
            offset = (0, -1)
        elif action == ACT_RIGHT:
            offset = (0, 1)
        elif action == ACT_UP:
            offset = (-1, 0)
        else:
            offset = (1, 0)

        next = tuple(map(operator.add, state, offset))
        if not out_of_bounds(next, blocked_states):
            list.append({
                'action': action,
                'state': next,
                'prob': prob
            })
        
    (row, col) = state

    result = []
    # 4 possible actions: l(left) r(right) u(up) d(down)
    for action in [ACT_LEFT, ACT_RIGHT, ACT_UP, ACT_DOWN]:
        policy = []
        if action == ACT_LEFT or action == ACT_RIGHT:
            add_action(action, PROB_ACT_1, policy)
            add_action(ACT_UP, PROB_ACT_2, policy)
            add_action(ACT_DOWN, PROB_ACT_3, policy)
        else:
            add_action(action, PROB_ACT_1, policy)
            add_action(ACT_LEFT, PROB_ACT_2, policy)
            add_action(ACT_RIGHT, PROB_ACT_3, policy)
        result.append(policy)
    return result

def expected_value(current_state, policy, values, blocked_states):
    if not len(policy):
        raise Exception('No action found in this policy')

    def get_value(state, values, fallback_value, blocked_states):
        (row, col) = state
        if out_of_bounds(state, blocked_states):
            return fallback_value
        return values[state]

    current_value = values[current_state]
    ev = 0
    for action in policy:
        ev += get_value(action['state'], values, current_value, blocked_states) * action['prob']

    ev *= DISC_FACTOR
    return { 'action': policy[0]['action'], 'ev': ev }

def main():
    args = sys.argv[1:]
    if not len(args):
        sys.exit(1)
    iteration_count = int(args[0])
    
    # initialize all values to zero
    values = new_states()
    # set goal and dead end
    values[0, 3] = 1
    values[1, 3] = -9

    # selected actions
    actions = np.zeros((HEIGHT, WIDTH), dtype=str)

    # states you can't access
    blocked_states = set([(1, 1)])
    # games ends when you enters end states
    end_states = set([(0, 3), (1, 3)])
    # both blocked states and end states won't be enumerated
    ignored_states = blocked_states | end_states

    enumerable_values = [index for index in np.ndindex(values.shape) if not index in ignored_states]

    for _ in range(iteration_count):
        new_values = np.copy(values)
        for state in enumerable_values:
            policies = next_policies(state, blocked_states)
            # max expected value
            max_policy = max([expected_value(state, policy, values, blocked_states) for policy in policies], key=lambda x:x['ev'])
            new_values[state] = max_policy['ev']
            actions[state] = max_policy['action']
        values = new_values
    
    result = np.round(np.matrix(values), 3)

    for x in range(0, HEIGHT):
        for y in range(0, WIDTH):
            action = actions[x, y]
            print((str(round(values[x, y], 3)) + action).rjust(7), end=' ')
        print()

if __name__ == "__main__":
    main()
