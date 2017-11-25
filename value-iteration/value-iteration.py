import numpy as np
import operator
import sys

WIDTH = 4
HEIGHT = 3
# probabilities of each actions
PROB_ACT_1 = .8
PROB_ACT_2 = .1
PROB_ACT_3 = .1
# number of actions 
ACT_COUNT = 3

# discount factor
DISC_FACTOR = .9

def new_states():
    return np.zeros((HEIGHT, WIDTH))

def next_policies(state, ignored_states):
    def add_action(action, prob, list):
        if action == 'l':
            offset = (0, -1)
        elif action == 'r':
            offset = (0, 1)
        elif action == 'u':
            offset = (-1, 0)
        else:
            offset = (1, 0)

        next = tuple(map(operator.add, state, offset))
        if not next in ignored_states:
            list.append({
                'action': action,
                'state': next,
                'prob': prob
            })
        
    (row, col) = state

    result = []
    # 4 possible actions: l(left) r(right) u(up) d(down)
    for action in 'lrud':
        policy = []
        if action == 'l' or action == 'r':
            add_action(action, PROB_ACT_1, policy)
            add_action('u', PROB_ACT_2, policy)
            add_action('d', PROB_ACT_3, policy)
        else:
            add_action(action, PROB_ACT_1, policy)
            add_action('l', PROB_ACT_2, policy)
            add_action('r', PROB_ACT_3, policy)
        result.append(policy)
    return result

def expected_value(current_state, policy, values, blocked_states):
    def get_value(state, values, fallback_value, blocked_states):
        (row, col) = state
        if col < 0 or row < 0 or col >= WIDTH or row >= HEIGHT or state in blocked_states:
            return fallback_value
        return values[state]

    current_value = values[current_state]
    ev = 0
    for action in policy:
        ev += get_value(action['state'], values, current_value, blocked_states) * action['prob']

    ev *= DISC_FACTOR
    # if ev:
    #     print("---GOT ", state, action, 'v1', value1, 's2', state2, 'v2', value2, 's3', state3, 'v3', value3, ev)
    return ev

def main():
    args = sys.argv[1:]
    if not len(args):
        sys.exit(1)
    iteration_count = int(args[0])
    
    # initialize all values to zero
    values = new_states()
    # set goal and dead end
    values[0, 3] = 1
    values[1, 3] = -1

    # states you can't access
    blocked_states = set([(1, 1)])
    # games ends when you enters end states
    end_states = set([(0, 3), (1, 3)])
    # both blocked states and end states won't be enumerated
    ignored_states = blocked_states | end_states

    enumerable_values = [index for index in np.ndindex(values.shape) if not index in ignored_states]
    print('Enumerated states ', enumerable_values)

    for _ in range(iteration_count):
        new_values = np.copy(values)
        for state in enumerable_values:
            print("eee ", state)
            policies = next_policies(state, blocked_states)
            # max expected value
            new_values[state] = max([expected_value(state, policy, values, blocked_states) for policy in policies])
        values = new_values
    
    print(np.matrix(values))

if __name__ == "__main__":
    main()
