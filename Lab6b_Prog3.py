# Kyle Mrosko
# Lab6b_Prog3
# An Aggie does not lie, cheat or steal or tolerate those who do

print("This program stores usernames and passwords")

times = int(input("How many username/password combonations do you plan on entering?: "))

usernames = []
passwords = []

# stores input
for i in range(times):
    name = input("Enter a username: ")
    usernames.append(name)

for i in range(times):
    password = input("Enter a password: ")
    passwords.append(password)

pairs = {}

# stores entries as a dict
for i in range(times):
    pairs[usernames[i]] = passwords[i]

# method to validate passwords
while True:
    tryUser = input("Enter a username to login with: ")
    if not(tryUser in pairs):
        print("Username not in database.")
        continue
    tryPass = input("Enter a password to login with: ")
    print(f"tryUser {tryUser} actual pass {pairs.get(tryUser)} tryPass {tryPass}")
    if(pairs.get(tryUser)==tryPass):
        print("Access Granted.")
    else:
        print("Access Denied.")




