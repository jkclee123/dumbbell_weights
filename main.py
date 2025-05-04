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
    single_hand_dumbbell()
    two_hand_dumbbell()


def single_hand_dumbbell():
    # Get all possible combinations of weights
    plate_labels = list(PLATES.keys())
    single_hand_combinations = {}
    
    # Generate combinations of different lengths (1 to 3)
    for bar_weight in BARS:
        for r in range(0, 3 + 1):
            combinations_r = list(combinations(plate_labels, r))
            for combination in combinations_r:
                plate_weight = sum(PLATES[label] for label in combination)
                full_combination = (bar_weight,) + combination
                total_weight = bar_weight + plate_weight
                total_weight = math.floor(total_weight * 100) / 100
                single_hand_combinations[total_weight] = full_combination
    
    # Sort the dictionary by total weight
    # single_hand_combinations = dict(sorted(single_hand_combinations.items()))
    # for total_weight, combination in single_hand_combinations.items():
    #     print(f"{total_weight:.2f}: {combination}")

    # Write combinations to file
    with open('single_hand_combinations.txt', 'w') as f:
        for total_weight, combination in single_hand_combinations.items():
            f.write(f"{total_weight:.2f}: {combination}\n")


def two_hand_dumbbell():
    # Get all possible combinations of weights
    plate_labels = list(PLATES.keys())
    two_hand_combinations = {}
    
    # Generate combinations for each hand
    for left_bar in BARS:
        # Get remaining bars for right hand
        remaining_bars = [b for b in BARS if b != left_bar]
        for right_bar in remaining_bars:
            # Generate combinations for left hand (0 to 3 plates)
            for left_r in range(0, 3 + 1):
                left_combinations = list(combinations(plate_labels, left_r))
                for left_combination in left_combinations:
                    # Get remaining plates for right hand
                    remaining_plates = [p for p in plate_labels if p not in left_combination]
                    
                    # Generate combinations for right hand (0 to 3 plates)
                    for right_r in range(0, 3 + 1):
                        right_combinations = list(combinations(remaining_plates, right_r))
                        for right_combination in right_combinations:
                            # Calculate weights
                            left_plate_weight = sum(PLATES[label] for label in left_combination)
                            right_plate_weight = sum(PLATES[label] for label in right_combination)
                            
                            # Calculate individual hand weights
                            left_hand_weight = left_bar + left_plate_weight
                            right_hand_weight = right_bar + right_plate_weight
                            
                            # Check if weights are balanced within 0.01 kg
                            if abs(left_hand_weight - right_hand_weight) <= 0.01:
                                # Create full combinations
                                left_full = (left_bar,) + left_combination
                                right_full = (right_bar,) + right_combination
                                
                                # Use single dumbbell weight (average of left and right)
                                single_weight = (left_hand_weight + right_hand_weight) / 2
                                single_weight = math.floor(single_weight * 100) / 100
                                
                                # Store combination
                                two_hand_combinations[single_weight] = (left_full, right_full)
    
    # Sort the dictionary by single dumbbell weight
    two_hand_combinations = dict(sorted(two_hand_combinations.items()))
    
    # Print combinations
    for single_weight, (left, right) in two_hand_combinations.items():
        print(f"{single_weight:.2f}: {left} | {right}")
    
    # Write combinations to file
    with open('two_hand_combinations.txt', 'w') as f:
        for single_weight, (left, right) in two_hand_combinations.items():
            f.write(f"{single_weight:.2f}: {left} | {right}\n")

if __name__ == "__main__":
    main()
