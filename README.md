# Dumbbell Weights Combinatorics Tool

A Python command-line tool that generates all possible dumbbell weight combinations using your available bars and plates. Perfect for athletes, trainers, and gym owners who want to maximize their equipment's potential.

## Features

- **One-Hand Dumbbells**: Calculate all possible weights using one bar with up to 3 plates
- **Two-Hand Dumbbells**: Generate balanced pairs where each dumbbell uses different bars and plates
- **Flexible Configuration**: Easy-to-edit text file for your equipment setup
- **Optimized Combinations**: Prioritizes combinations with fewer plates for the same weight
- **Readable Output**: Clean text files showing weight combinations for easy reference

## Quick Start

### Prerequisites
- Python 3.13+
- uv package manager (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dumbbell_weights
```

2. Install dependencies:
```bash
uv sync
```

### Usage

1. Configure your equipment in `equipment_config.txt`
2. Run the tool:
```bash
uv run python main.py
```

3. View results in:
   - `one_hand_combinations.txt` - Single dumbbell combinations
   - `two_hand_combinations.txt` - Balanced two-dumbbell pairs

## Configuration

Edit `equipment_config.txt` to match your dumbbell equipment:

```ini
[BARS]
# Bar weights in kg
2.60 kg
2.72 kg

[PLATES]
# Format: labeled_weight kg: actual_weight kg
0.60 kg: 1.13 kg
0.75 kg: 1.16 kg
0.95 kg: 1.82 kg
```

### Configuration Details

- **Bars**: List all your dumbbell bars with their weights
- **Plates**: Each plate has a labeled weight (what you think you're using) and actual weight (what it really weighs)
- **Constraints**:
  - One-hand: 1 bar + up to 3 plates
  - Two-hand: 2 different bars + up to 3 plates each, plates not shared between hands
  - Two-hand combinations must be balanced within 0.01 kg

## Output Format

### One-Hand Combinations
```
3.73:
2.6, 0.6

4.89:
2.6, 0.6, 0.75
```

Shows total weight followed by the bar and plate combination.

### Two-Hand Combinations
```
5.03:
2.6, 1.2
2.72, 0.95
```

Shows the single dumbbell weight, then the combination for each hand.

## Example Use Cases

- **Workout Planning**: Know exactly what weights you can achieve
- **Equipment Shopping**: Identify gaps in your weight range
- **Gym Setup**: Help clients understand available options
- **Training Logs**: Reference exact plate combinations used

## Technical Details

- **Algorithm**: Uses itertools.combinations for efficient weight calculation
- **Optimization**: Prefers combinations with fewer plates for the same weight
- **Precision**: Weights rounded to 2 decimal places
- **Balance Check**: Two-hand combinations balanced within 0.01 kg tolerance

**Built with Python 3.13+** | **Uses uv for dependency management**
