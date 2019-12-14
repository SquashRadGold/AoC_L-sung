import numpy as np

from vm import VM, read_program


ns = read_program(13)

# Part one
vm = VM(ns)
t = 0
try:
    while True:
        _, _, tile_id = next(vm), next(vm), next(vm)
        if tile_id == 2:
            t += 1
except StopIteration:
    print(t)


# Part two
paddle_x = 0
ball_x = 0


class AI:
    @staticmethod
    def popleft():
        return np.sign(ball_x - paddle_x)


vm = VM(ns, AI)
vm[0] = 2
try:
    while True:
        x, y, tile_id = next(vm), next(vm), next(vm)
        if x == -1 and y == 0:
            score = tile_id
        elif tile_id == 3:
            paddle_x = x
        elif tile_id == 4:
            ball_x = x
except StopIteration:
    print(score)
