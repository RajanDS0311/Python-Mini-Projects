print("🗳️ Mini Voting System")
print("Candidates: Rajan, Ketan, Pranay")

R = 0
K = 0
P = 0

while True:
    vote = input("Enter your vote (or type 'exit' to stop): ").strip().lower()

    if vote == "rajan":
        R += 1
    elif vote == "ketan":
        K += 1
    elif vote == "pranay":
        P += 1
    elif vote == "exit":
        break
    else:
        print("❌ Invalid choice, try again")

def result():
    print("\n📊 Final Results:")
    print(f"Rajan: {R}")
    print(f"Ketan: {K}")
    print(f"Pranay: {P}")

    if R > K and R > P:
        print("🏆 Winner: Rajan")
    elif K > R and K > P:
        print("🏆 Winner: Ketan")
    elif P > R and P > K:
        print("🏆 Winner: Pranay")
    else:
        print("⚖️ It's a tie!")

result()