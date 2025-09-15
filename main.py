from itertools import combinations
import math

def load_equipment_config(config_file="equipment_config.txt"):
    """
    Load dumbbell equipment configuration from a text file.

    Returns:
        tuple: (bars_list, plates_dict)
            bars_list: List of bar weights in kg
            plates_dict: Dict of labeled_weight_kg: actual_weight_kg
    """
    bars = []
    plates = {}

    try:
        with open(config_file, 'r') as f:
            current_section = None
            for line in f:
                line = line.strip()

                # Skip comments and empty lines
                if not line or line.startswith('#'):
                    continue

                # Section headers
                if line == '[BARS]':
                    current_section = 'bars'
                    continue
                elif line == '[PLATES]':
                    current_section = 'plates'
                    continue

                # Parse data based on current section
                if current_section == 'bars':
                    # Extract weight from "X.XX kg" format
                    if 'kg' in line:
                        weight_str = line.split()[0]
                        try:
                            bars.append(float(weight_str))
                        except ValueError:
                            print(f"Warning: Could not parse bar weight: {line}")

                elif current_section == 'plates':
                    # Extract labeled weight and actual weight from "X.XX kg: Y.YY kg" format
                    if ':' in line and 'kg' in line:
                        try:
                            labeled_part, actual_part = line.split(':')
                            labeled_weight = float(labeled_part.split()[0])
                            actual_weight = float(actual_part.split()[0])
                            plates[labeled_weight] = actual_weight
                        except (ValueError, IndexError):
                            print(f"Warning: Could not parse plate data: {line}")

    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        return [], {}

    return bars, plates

# Load configuration
BARS, PLATES = load_equipment_config()

def main():
    single_hand_dumbbell()
    two_hand_dumbbell()

def single_hand_dumbbell():
    """
    Generate all possible single-hand dumbbell combinations where:
    - Uses one bar
    - Uses at most 3 plates
    - For the same weight, uses the combination with the least plates
    Output is printed and written to 'single_hand_combinations.txt' in a readable format.
    """
    plate_labels = list(PLATES.keys())
    single_hand_combinations = {}

    bar = BARS[0]  # Use the first bar

    # Iterate over all possible plate combinations (0 to 3 plates)
    for r in range(0, 4):
        for combination in combinations(plate_labels, r):
            plate_weight = sum(PLATES[label] for label in combination)
            total_weight = round(bar + plate_weight, 2)

            # Create the full combination tuple (bar + plates)
            full_combination = (bar,) + combination

            # If this weight already exists, keep the one with fewer plates
            # If same number of plates, keep any (they should be equivalent)
            if total_weight not in single_hand_combinations or len(combination) < len(single_hand_combinations[total_weight][1:]):
                single_hand_combinations[total_weight] = full_combination

    # Sort by total weight
    single_hand_combinations = dict(sorted(single_hand_combinations.items()))

    # Print combinations (optional, for debug)
    for weight, combination in single_hand_combinations.items():
        print(f"{weight:.2f}kg:")
        print(", ".join(str(x) for x in combination))
        print()

    # Write combinations to file in the requested format
    with open('single_hand_combinations.txt', 'w') as f:
        for weight, combination in single_hand_combinations.items():
            f.write(f"{weight:.2f}kg:\n")
            f.write(", ".join(str(x) for x in combination) + "\n\n")

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
        print(f"{single_weight:.2f}kg:")
        print(", ".join(str(x) for x in left))
        print(", ".join(str(x) for x in right))
        print()

    # Write combinations to file in the requested format
    with open('two_hand_combinations.txt', 'w') as f:
        for single_weight, (left, right) in two_hand_combinations.items():
            f.write(f"{single_weight:.2f}kg:\n")
            f.write(", ".join(str(x) for x in left) + "\n")
            f.write(", ".join(str(x) for x in right) + "\n\n")

if __name__ == "__main__":
    main()
