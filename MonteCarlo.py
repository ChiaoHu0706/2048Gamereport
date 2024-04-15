import random
import matplotlib.pyplot as plt


def estimate_circle_area(iterations):
    inside_circle_count = 0
    total_points = 0
    circle_points_x = []
    circle_points_y = []
    noncircle_points_x = []
    noncircle_points_y = []

    for i in range(iterations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle_count += 1
            circle_points_x.append(x)
            circle_points_y.append(y)
        else:
            noncircle_points_x.append(x)
            noncircle_points_y.append(y)

        total_points += 1

    circle_area = 4 * inside_circle_count / total_points
    return circle_area, circle_points_x, circle_points_y, noncircle_points_x, noncircle_points_y


def plot_circle_points(circle_points_x, circle_points_y, noncircle_points_x, noncircle_points_y):
    plt.scatter(circle_points_x, circle_points_y,
                color='blue', label='Inside Circle')
    plt.scatter(noncircle_points_x, noncircle_points_y,
                color='red', label='Outside Circle')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Monte Carlo Circle Estimation')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def main():
    iterations = 10000000
    circle_area, circle_points_x, circle_points_y, noncircle_points_x, noncircle_points_y = estimate_circle_area(
        iterations)
    print(f"Estimated Circle Area: {circle_area}")

    plot_circle_points(circle_points_x, circle_points_y,
                       noncircle_points_x, noncircle_points_y)


if __name__ == "__main__":
    main()
