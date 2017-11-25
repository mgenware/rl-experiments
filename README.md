# RL Experiments
RL Experiments.

## Setup
**Assume Python 3 and virtualenv installed**.

```sh
virtualenv -p python3 .
source bin/activate
```

## value-iteration
Apply value iteration on a classic grid world.

* noise: `0.2`.
* discount factor: `0.9`.
* end states: `+1` and `-9`.

Iteration: `1`:
```sh
python value-iteration.py 1
```

Output:
```
   0.0←    0.0←   0.72→     1.0
   0.0←     0.0    0.0↑    -9.0
   0.0←    0.0←    0.0←    0.0↓
```

Iteration: `1000`:
```sh
python value-iteration.py 1000
```

Output:
```
 0.544→  0.633→    0.8→     1.0
  0.43↑     0.0  0.094↑    -9.0
 0.369↑  0.292←   0.24←  0.114↓
```
