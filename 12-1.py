# Realistic Voter System in Python

print("=== Voter System ===")
print("Enter 4 candidate names:")

candidates = {}
for i in range(4):
    name = input(f"Candidate {i+1} name: ").strip()
    while name in candidates or name == "":
        print("Name already taken or empty. Try again.")
        name = input(f"Candidate {i+1} name: ").strip()
    candidates[name] = 0

print("\nVoting has started! Type 'exit' to end voting.")
voted_users = set()

while True:
    voter_id = input("\nEnter your Voter ID (or type 'exit' to finish): ").strip()
    if voter_id.lower() == "exit":
        break
    if voter_id in voted_users:
        print("You have already voted!")
        continue

    print("Candidates:")
    for idx, candidate in enumerate(candidates.keys(), start=1):
        print(f"{idx}. {candidate}")
    
    try:
        choice = int(input("Enter the number of the candidate you want to vote for: "))
        if 1 <= choice <= 4:
            selected_candidate = list(candidates.keys())[choice - 1]
            candidates[selected_candidate] += 1
            voted_users.add(voter_id)
            print(f"Vote recorded for {selected_candidate}.")
        else:
            print("Invalid candidate number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Show results
print("\n=== Voting Results ===")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes} vote(s)")

# Determine winner(s)
max_votes = max(candidates.values())
winners = [name for name, count in candidates.items() if count == max_votes]

if len(winners) == 1:
    print(f"\n🎉 Winner is: {winners[0]} with {max_votes} votes!")
else:
    print("\n🤝 It's a tie between: " + ", ".join(winners) + f" with {max_votes} votes each!")
