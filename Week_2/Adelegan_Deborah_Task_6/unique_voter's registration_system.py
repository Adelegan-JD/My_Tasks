# TASK 4: Create a unique Voter's Registration System
voters_name = input("Kindly input your names for the registration: ")
voters_names = set(voters_name)
voter1 = voters_names.add(input("Kindly input your name: "))
if voter1 == voters_names:
    print(f"Warning: {voter1} is in the registration file. You have previously registered.")

voter2 = voters_names.add(input("Kindly input your name: "))
if voter2 == voter1:
    print(f"Warning: {voter2} is in the registration file. You have previously registered.")
else:
    print(f"The name of the registered voters are: {len(voters_name)}")