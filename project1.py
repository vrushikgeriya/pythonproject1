print("Welcome Interactive Personal Data Collector !")

a = input("\nPlease enter your name: ")
b = int(input("Please enter your age: "))
c = float(input("Please enter your height in meters: "))
d = int(input("Please enter your Favourite number: "))
e = 2026
f = e - b 

print("\nThank you! Here is the information we collected: ")

print(f"\nName: {a} (Type: {type(a)} Memory Address: {id(a)})")
print(f"Age: {b} (Type: {type(b)} Memory Address: {id(b)})")
print(f"Height: {c} (Type: {type(c)} Memory Address:  {id(c)})")
#print("Favourite Number: ",d, "Type: ", type(d), "Memory Address: ", id(d))
print(f"Favourite number: {d} (Type: {type(d)} Memory Address: {id(d)})")

#print(f"\nYOur birth year is approximately: ",f , "(based on your age of ", b)
print(f"\nYour birth year is approximatery: {f} (based on your age of {b})")



print("\nThank you for using the Personal Data Collector. Goodbye!")

