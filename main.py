from flask import Flask

app = Flask(__name__)


def grid_size():
    try:
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
    except:
        print("Values of m or n is not correct please try again ...")
        grid_size()


def bumpers():
    try:
        global value, cost
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
    except:
        print("Values of x and y axis or bumper is not correct please try again ... ")
        bumpers()


def balls_inputs():
    global bx, by, dir, lifetime
    bx, by, ndir, lifetime = [
        int(x) for x in input("Enter bx,by axis direction and lifetime of balls respectively : ").split()]
    adir =[[1,0],[0,1],[-1,0],[0,-1]]
    grid[int(bx)][int(by)] = "ball"
    for item in grid:
        print(item)


if __name__ == '__main__':
    grid_size()