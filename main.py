from flask import Flask
app = Flask(__name__)


def grid_size():
    try:
        global x, y, m, n, grid
        m, n = [int(y) for y in input("Enter values of m and n : ").split()]
        if 2 < m < 51 and 2 < n < 51:
            grid = [[0] * n for _ in range(m)]
            for item in grid:
                print(item)
        else:
            print("Values are not in range please try again ...")
            grid_size()
    except:
        print("Values of m or n is not correct please try again ...")
        grid_size()


def bumpers_input():
    global value, cost, x, y
    wall_cost = int(input("Enter the cost of hitting a wall : "))
    p = int(input("Enter the number of bumpers : "))
    if p >= 0:
        for i in range(p):
            x, y, value, cost = [
                int(x) for x in input("Enter x,y axis value and cost of bumper respectively : ").split()]
            print(x)
            if 1 <= x <= m and 1 <= y <= n:
                grid[x][y] = "B"
                for item in grid:
                    print(item)
            else:
                print("Please enter values of x and y axis in range...")
                bumpers_input()
    else:
        print("Please enter correct number of bumpers ")
        bumpers_input()


def direction():
    if dir == 0:
        move_right(lifetime, bx, by)
    if dir == 1:
        move_up(lifetime, bx, by)
    if dir == 2:
        move_left(lifetime, bx, by)
    if dir == 3:
        move_down(lifetime, bx, by)


def move_right(lifetime, bx, by):
    for i in reversed(range(lifetime)):
        if grid[bx][by] == grid[x][y]:
            grid[bx][by] = "B"
            grid[bx + 1][by] = 1
            for j in grid:
                print(j)
        else:
            grid[bx][by] = 0
            grid[bx][by + 1] = 1
            lifetime -= 1
            by += 1
            for j in grid:
                print(j)
            print("\n")


def move_up(lifetime, bx, by):
    for i in reversed(range(lifetime)):
        if grid[bx][by] == grid[x][y]:
            grid[bx][by] = "B"
            grid[bx][by + 1] = 1
            for j in grid:
                print(j)
            print("\n")

        elif is_wall(dir):
            by = rebound_wall(lifetime, bx, by)
        else:
            grid[bx][by] = 0
            grid[bx - 1][by] = 1
            lifetime -= 1
            bx -= 1
            for j in grid:
                print(j)
            print("\n")


def move_left(lifetime, bx, by):
    for i in reversed(range(lifetime)):
        if grid[bx][by] == grid[x][y]:
            grid[bx][by] = "B"
            grid[bx - 1][by] = 1
            for j in grid:
                print(j)
            print("\n")
        else:
            grid[bx][by] = 0
            grid[bx][by - 1] = 1
            lifetime -= 1
            by -= 1
            for j in grid:
                print(j)
            print("\n")


def move_down(lifetime, bx, by):
    for i in reversed(range(lifetime)):
        if grid[bx][by] == grid[x][y]:
            grid[bx][by] = "B"
            grid[bx][by - 1] = 1
            for j in grid:
                print(j)
            print("\n")
        else:
            grid[bx][by] = 0
            grid[bx + 1][by] = 1
            lifetime -= 1
            bx += 1
            for j in grid:
                print(j)
            print("\n")


def is_wall(dir):
    while lifetime > 0:
        if bx == 0 and dir == 1:
            dir = 0
            print("ball hits the wall ... ")
            return True
        if by == 0 and dir == 2:
            dir = 1
            print("ball hits the wall ... ")
            return True


def rebound_wall(lifetime, bx, by):
    grid[bx][by] == 0
    print("current:", bx, by)
    by = by + 1
    grid[bx][by] = 1
    print("new:", bx, by)
    lifetime -= 1
    for j in grid:
        print(j)
    print("\n")
    return by


def balls_inputs():
    global bx, by, dir, lifetime
    bx, by, dir, lifetime = [
        int(x) for x in input("Enter bx,by axis direction and lifetime of balls respectively : ").split()]
    bx = int(bx)
    by = int(by)
    dir = int(dir)
    lifetime = int(lifetime)
    grid[bx][by] = 1
    print("The ball is placed at: \n")
    for item in grid:
        print(item)
    print("\n")
    direction()


if __name__ == '__main__':
    grid_size()
    bumpers_input()
    balls_inputs()
