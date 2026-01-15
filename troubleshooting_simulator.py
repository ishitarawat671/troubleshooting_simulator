print("PC & Network Troubleshooting Simulator")
print("-------------------------------------")

issues = {
    1: ("No Internet Connection", "restart router"),
    2: ("Application Not Opening", "reinstall application"),
    3: ("System Running Slow", "close background applications")
}

print("\nSelect an issue:")
for key, value in issues.items():
    print(f"{key}. {value[0]}")

try:
    choice = int(input("\nEnter issue number: "))
    solution = input("Enter your solution: ").lower()

    if choice in issues:
        correct_solution = issues[choice][1]

        if solution == correct_solution:
            print("\n✅ Issue resolved successfully.")
        else:
            print("\n❌ Incorrect solution. Please try basic troubleshooting steps.")
    else:
        print("\n❌ Invalid issue number selected.")

except ValueError:
    print("\n❌ Invalid input. Please enter numeric values only.")
