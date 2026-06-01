# japan_trip_v1_basic.py
print("=== Japan Trip Hisab Kitab V1 ===")
total_budget = 1000000
dost = ["Aman", "Rohan", "Priya", "Sneha", "Karan"]
kharcha = [0, 0, 0, 0, 0]

while True:
    print("\n1. Kharcha Add Karo")
    print("2. Sabka Hisab Dekho")
    print("3. Kaun Kisko Kitna Dega")
    print("4. Band Karo")
    choice = input("Option chuno 1-4: ")

    if choice == "1":
        for i in range(5):
            print(f"{i+1}. {dost[i]}")
        kiska = int(input("Kisne kiya? 1-5: "))-1  
        kitna = float(input("Kitna ₹? "))
        kharcha[kiska] = kharcha[kiska]+ kitna

    elif choice == "2":
        total = sum(kharcha)
        for i in range(5):
            print(f"{dost[i]}: ₹{kharcha[i]}")
        print(f"Total: ₹{total} | Per Head: ₹{total/5}")
    elif choice == "3":
        total = sum(kharcha)
        per_head = total / 5
        print("\n--- Settlement ---")
        for i in range(5):
            diff = kharcha[i] - per_head
            if diff > 0:
                print(f"{dost[i]} ko ₹{round(diff,2)} milenge")
            elif diff < 0:
                print(f"{dost[i]} ko ₹{round(-diff,2)} dene hain")
            else:
                print(f"{dost[i]} ka hisab barabar hai")
    elif choice == "4":
        break
