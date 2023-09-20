import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

def main():
    # Get user input for the radius
    radius = float(input("Enter the radius of the sphere: "))

    # Check if the radius is non-negative
    if radius >= 0:
        # Calculate the volume
        volume = calculate_sphere_volume(radius)
        print(f"The volume of the sphere with radius {radius} is {volume:.2f} cubic units.")
    else:
        print("Error: The radius must be non-negative.")

if __name__ == "__main__":
    main()
