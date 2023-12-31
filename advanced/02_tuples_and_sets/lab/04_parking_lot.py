number_of_commands = int(input())
parking_lot = set()

for _ in range(number_of_commands):
    command, car_number = input().split(", ")
    if command == "IN" and car_number not in parking_lot:
        parking_lot.add(car_number)
    elif command == "OUT" and car_number in parking_lot:
        parking_lot.remove(car_number)
if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print("Parking Lot is Empty")