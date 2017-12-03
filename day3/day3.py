import math


def get_spiral_branch_for_number(goal):
    for i in range(0, 10000000000000):
        number = 2 * i + 1
        if goal <= math.pow(number, 2):
            return i


def get_cardinal_points_for_branch(branch):
    square_number = int(math.pow(2 * branch + 1, 2))
    return [square_number - branch,
            square_number - 3 * branch,
            square_number - 5 * branch,
            square_number - 7 * branch]


def find_closest_cardinal_point_to_number(cardinal_points, goal):
    cardinal_differences = []
    for cardinal in cardinal_points:
        cardinal_differences.append(abs(goal - cardinal))
    cardinal_differences.sort()
    return cardinal_differences[0]


def find_number_of_steps(goal):
    spiral_branch = get_spiral_branch_for_number(goal)
    cardinal_points = get_cardinal_points_for_branch(spiral_branch)
    steps_to_closest_cardinal = find_closest_cardinal_point_to_number(cardinal_points, goal)
    return steps_to_closest_cardinal + spiral_branch


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        print(find_number_of_steps(int(f.read())))
