from itertools import combinations
import math

BARS = [2.6, 2.72]
PLATES = {
    0.6: 1.13,
    0.75: 1.16,
    0.95: 1.82,
    1.2: 2.43,
    1.25: 1.76,
    1.5: 3.09,
    1.75: 2.53,
    2.25: 3.1
}

def main():
    two_hand_dumbbell()

def two_hand_dumbbell():
    """
    Generate all possible two-hand dumbbell combinations where:
    - Each hand uses a different bar
    - Each hand uses up to 3 plates (without replacement)
    - The weights are balanced within 0.01 kg
    Output is printed and written to 'two_hand_combinations.txt' in a readable format.
    """
    plate_labels = list(PLATES.keys())
    two_hand_combinations = {}

    left_bar, right_bar = BARS[0], BARS[1]

    # Iterate over all possible plate combinations for the left hand
    for left_r in range(0, 4):
        for left_combination in combinations(plate_labels, left_r):
            left_plate_weight = sum(PLATES[label] for label in left_combination)
            # Remaining plates for the right hand
            remaining_plates = [p for p in plate_labels if p not in left_combination]
            # Iterate over all possible plate combinations for the right hand
            for right_r in range(0, 4):
                for right_combination in combinations(remaining_plates, right_r):
                    right_plate_weight = sum(PLATES[label] for label in right_combination)
                    # Calculate individual hand weights, rounded to 2 decimals
                    left_hand_weight = round(left_bar + left_plate_weight, 2)
                    right_hand_weight = round(right_bar + right_plate_weight, 2)
                    # Only include balanced combinations
                    if abs(left_hand_weight - right_hand_weight) < 0.01:
                        left_full = (left_bar,) + left_combination
                        right_full = (right_bar,) + right_combination
                        # Store by single dumbbell weight
                        two_hand_combinations[left_hand_weight] = (left_full, right_full)

    # Sort by single dumbbell weight
    two_hand_combinations = dict(sorted(two_hand_combinations.items()))

    # Print combinations (optional, for debug)
    for single_weight, (left, right) in two_hand_combinations.items():
        print(f"{single_weight:.2f}:")
        print(", ".join(str(x) for x in left))
        print(", ".join(str(x) for x in right))
        print()

    # Write combinations to file in the requested format
    with open('two_hand_combinations.txt', 'w') as f:
        for single_weight, (left, right) in two_hand_combinations.items():
            f.write(f"{single_weight:.2f}:\n")
            f.write(", ".join(str(x) for x in left) + "\n")
            f.write(", ".join(str(x) for x in right) + "\n\n")

if __name__ == "__main__":
    main()
