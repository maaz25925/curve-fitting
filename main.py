import pandas as pd

def solve_two(a1, b1, d1, a2, b2, d2):
    # Solves 2x2 system of linear equations
    D = a1 * b2 - b1 * a2
    Dx = d1 * b2 - b1 * d2
    Dy = a1 * d2 - d1 * a2
    if D != 0:
        a = Dx / D
        b = Dy / D
        return a, b
    else:
        raise ValueError("No unique solution exists.")

def solve_three(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    # Solves 3x3 system of linear equations
    D = a1 * (b2 * c3 - b3 * c2) - b1 * (a2 * c3 - a3 * c2) + c1 * (a2 * b3 - a3 * b2)
    Dx = d1 * (b2 * c3 - b3 * c2) - b1 * (d2 * c3 - d3 * c2) + c1 * (d2 * b3 - d3 * b2)
    Dy = a1 * (d2 * c3 - d3 * c2) - d1 * (a2 * c3 - a3 * c2) + c1 * (a2 * d3 - a3 * d2)
    Dz = a1 * (b2 * d3 - b3 * d2) - b1 * (a2 * d3 - a3 * d2) + d1 * (a2 * b3 - a3 * b2)
    if D != 0:
        a = Dx / D
        b = Dy / D
        c = Dz / D
        return a, b, c
    else:
        raise ValueError("No unique solution exists.")

# Input data
x = list(map(float, input("Enter X: ").split()))
y = list(map(float, input("Enter Y: ").split()))
choice = input("Enter 1 for straight line and 2 for parabola: ")

if choice == "1":
    # For straight-line fitting
    df = pd.DataFrame({'x': x, 'y': y})
    df['x^2'] = df['x'] ** 2
    df['x*y'] = df['x'] * df['y']

    print(df)
    sum_x = df['x'].sum()
    sum_y = df['y'].sum()
    sum_x2 = df['x^2'].sum()
    sum_xy = df['x*y'].sum()
    n = len(df)

    print("∑x:", sum_x)
    print("∑y:", sum_y)
    print("∑x^2:", sum_x2)
    print("∑xy:", sum_xy)
    print("n:", n)

    # Print normal equations
    print("The normal equations are:")
    print(f"{sum_y} = a * {n} + b * {sum_x}")
    print(f"{sum_xy} = a * {sum_x} + b * {sum_x2}")

    # Solve for coefficients a and b
    a, b = solve_two(n, sum_x, sum_y, sum_x, sum_x2, sum_xy)
    print(f"a = ({a}), b = ({b})")
    print("Thus, the equation of the straight line is: y = a + bx")
    print(f"y = ({a}) + ({b})x")

elif choice == "2":
    # For parabolic fitting
    df = pd.DataFrame({'x': x, 'y': y})
    df['x^2'] = df['x'] ** 2
    df['x^3'] = df['x'] ** 3
    df['x^4'] = df['x'] ** 4
    df['x*y'] = df['x'] * df['y']
    df['x^2*y'] = df['x^2'] * df['y']

    print(df)
    sum_x = df['x'].sum()
    sum_y = df['y'].sum()
    sum_x2 = df['x^2'].sum()
    sum_x3 = df['x^3'].sum()
    sum_x4 = df['x^4'].sum()
    sum_xy = df['x*y'].sum()
    sum_x2y = df['x^2*y'].sum()
    n = len(df)

    print("∑x:", sum_x)
    print("∑y:", sum_y)
    print("∑x^2:", sum_x2)
    print("∑x^3:", sum_x3)
    print("∑x^4:", sum_x4)
    print("∑xy:", sum_xy)
    print("∑x^2y:", sum_x2y)
    print("n:", n)

    # Print normal equations
    print("The normal equations are:")
    print(f"{sum_y} = a * {n} + b * {sum_x} + c * {sum_x2}")
    print(f"{sum_xy} = a * {sum_x} + b * {sum_x2} + c * {sum_x3}")
    print(f"{sum_x2y} = a * {sum_x2} + b * {sum_x3} + c * {sum_x4}")

    # Solve for coefficients a, b, and c
    a, b, c = solve_three(n, sum_x, sum_x2, sum_y, sum_x, sum_x2, sum_x3, sum_xy, sum_x2, sum_x3, sum_x4, sum_x2y)
    print(f"a = ({a}), b = ({b}), c = ({c})")
    print("Thus, the equation of the parabola is: y = a + bx + cx^2")
    print(f"y = ({a}) + ({b})x + ({c})x^2")

else:
    print("Select a valid choice.")
