# Lab Exercise 16: Dice Simulator Using Random Module
# Student: Niranjan P G | USN: 25BTRAD074
import random

def roll_dice(num_dice=2):
    return [random.randint(1, 6) for _ in range(num_dice)]

def simulate_rolls(trials=1000):
    random.seed(42)
    results = {}
    for _ in range(trials):
        s = sum(roll_dice(2))
        results[s] = results.get(s, 0) + 1
    return results

def main():
    print("=== Dice Simulator Using Random Module ===")
    print("Sample rolls of 2 dice:")
    for i in range(1, 4):
        roll = roll_dice(2)
        print(f" Roll {i}: {roll} => Sum = {sum(roll)}")
        
    print("\nSimulation: 1000 Rolls of Two Dice")
    print(f"{'Sum':<6} {'Count':<8} {'Probability':<12} {'Distribution'}")
    print("-" * 46)
    outcomes = simulate_rolls(1000)
    for total in range(2, 13):
        cnt = outcomes.get(total, 0)
        pct = (cnt / 1000) * 100
        print(f"{total:<6} {cnt:<8} {pct:>5.1f}%       {'#' * int(pct)}")
    
    top = max(outcomes.items(), key=lambda x: x[1])
    print(f"\nMost Frequent Outcome: Sum of {top[0]} ({top[1]} rolls)")

if __name__ == "__main__":
    main()
