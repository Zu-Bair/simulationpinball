from flask import Flask

app = Flask(__name__)


def grid_size():
    # try:
        global x, y, m, n, grid
        m, n = [int(x) for x in input("Enter values of m and n : ").split()]
        if 2 < m < 51 and 2 < n < 51:
            grid = [[0] * n for _ in range(m)]
            for item in grid:
                print(item)
            bumpers()
        else:
            print("Values are not in range please try again ...")
            grid_size()
    # except:
    #     print("Values of m or n is not correct please try again ...")
    #     grid_size()


def bumpers():
    # try:
        global value, cost, x, y
        wall_cost = int(input("Enter the cost of hitting a wall : "))
        p = int(input("Enter the number of bumpers : "))
        if p >= 0:
            for i in range(p):
                x, y, value, cost = [
                    int(x) for x in input("Enter x,y axis value and cost of bumper respectively : ").split()]
                if 1 <= x <= m and 1 <= y <= n:
                    grid[x][y] = "B"
                    for item in grid:
                        print(item)
                else:
                    print("Please enter values of x and y axis in range...")
                    bumpers()
        else:
            print("Please enter correct number of bumpers ")
            bumpers()

        balls_inputs()
    # except:
    #     print("Values of x and y axis or bumper is not correct please try again ... ")
    #     bumpers()

def move_right(lifetime):
    for i in reversed(range(lifetime)):
        step_right = grid[bx][by + 1]
        grid[bx][by + 1] = 1
        grid[bx][by] = 0
        # lifetime = lifetime-1
    for j in grid:
        print(j)


def move_up(lifetime):
    for i in range(lifetime, 0):
        step_up = grid[bx - 1][by]
        grid[bx - 1][by] = 1
        grid[bx][by] = 0
        lifetime -= 1
    for i in grid:
        print(i)

def move_left(lifetime):
    for i in range(lifetime, 0):
        step_left = grid[bx][by - 1]
        grid[bx][by - 1] = 1
        grid[bx][by] = 0
        lifetime -= 1
    for i in grid:
        print(i)


def move_down(lifetime):
    for i in range(lifetime, 0):
        grid[bx + 1][by] = 1 #next_position as 1
        grid = grid[bx + 1][by] #next position
        # grid[bx][by] = 0 #set current to 0
        lifetime -= 1 #reduce lifetime
    for i in grid:
        print(i)


def balls_inputs():
    global bx, by, dir, lifetime
    bx, by, dir, lifetime = [
        int(x) for x in input("Enter bx,by axis direction and lifetime of balls respectively : ").split()]
    bx = int(bx)
    by = int(by)
    dir = int(dir)
    lifetime = int(lifetime)

    grid[bx][by] = 1
    for item in grid:
        print(item)
    print("\n")
    direction()


def direction():
    if dir == 0:
        move_right(0)
    elif dir == 1:
        move_up(1)
    elif dir == 2:
        move_left(2)
    elif dir == 3:
        move_down(3)
    else:
        print("You entered wrong direction ... ")
        direction()


if __name__ == '__main__':
    grid_size()