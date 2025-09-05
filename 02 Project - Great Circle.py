from math import pi, sin, cos, acos

def great_circle_distance(r, x1_deg, y1_deg, x2_deg, y2_deg):
    # Convert degrees to radians
    x1 = x1_deg * pi / 180
    y1 = y1_deg * pi / 180
    x2 = x2_deg * pi / 180
    y2 = y2_deg * pi / 180

    # Calculate the central angle using the formula
    central_angle = acos(
        sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2)
    )

    # Calculate the great-circle distance
    d = r * central_angle

    # Round to nearest hundredths
    return round(d, 2)

def main():
    print("Great Circle Calculator")
    r = float(input("Enter Radius of Sphere: "))
    x1 = float(input("Starting Point - Enter Latitude: "))
    y1 = float(input("Starting Point - Enter Longitude: "))
    x2 = float(input("Ending Point - Enter Latitude: "))
    y2 = float(input("Ending Point - Enter Longitude: "))

    distance = great_circle_distance(r, x1, y1, x2, y2)
    print(f"The Great Circle Distance is {distance}")

if __name__ == "__main__":
    main()
