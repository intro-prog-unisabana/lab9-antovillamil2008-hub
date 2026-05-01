from aircraft import Aircraft

from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    my_aircraft = Aircraft(model)

    while True:
        user_input = input("Enter command (A for ascent, D for descent, X to exit): ")
    
        if user_input.upper() == "X":
            break

        parts = user_input.split()
        command = parts[0].upper()
        feet = int(parts[1])
        
        if command == "A":
            my_aircraft.climb(feet)
        elif command == "D":
            my_aircraft.descend(feet)


    print(f"Final altitude: {my_aircraft.altitude} feet")

if __name__ == "__main__":
    main()