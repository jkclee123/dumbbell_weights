# Dumbbell Weights Combinatorics Tool

A Python command-line tool that generates all possible dumbbell weight combinations using your available bars and plates. 
**For equipment where labelled weights don't match actual weights** - a common issue with budget or older dumbbell sets.

## Features

- **Single-Hand Dumbbells**: Calculate all possible weights using one bar with up to 3 plates
- **Two-Hand Dumbbells**: Generate balanced pairs where each dumbbell uses different bars and plates
- **Flexible Configuration**: Easy-to-edit text file for your equipment setup
- **Optimized Combinations**: Prioritizes combinations with fewer plates for the same weight
- **Readable Output**: Clean text files showing weight combinations for easy reference

## The Labelled Weight Problem

Many dumbbell sets (especially budget or older equipment) have plates where the **labelled weight** (what the plate says it is) doesn't match the **actual weight** (what it really weighs). For example:
- A plate marked "0.60 kg" might actually weigh 1.13 kg
- A plate marked "1.25 kg" might actually weigh 1.76 kg

This tool accounts for both weights, so you know exactly what combinations will give you your target weight. No more guesswork or inconsistent results during workouts!

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
  - Single-hand: 1 bar + up to 3 plates
  - Two-hand: 2 different bars + up to 3 plates each, plates not shared between hands
  - Two-hand combinations must be balanced within 0.01 kg

## Output Format

### Single-Hand Combinations
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

- **Accurate Weight Calculation**: Know your exact achievable weights when labelled weights are misleading
- **Workout Planning**: Plan sessions with confidence using real weights, not advertised ones
- **Equipment Assessment**: Discover what your current setup can actually achieve
- **Equipment Shopping**: Identify weight gaps and avoid buying plates that won't help
- **Training Logs**: Record exact plate combinations used for reproducible workouts

## Technical Details

- **Algorithm**: Uses itertools.combinations for efficient weight calculation
- **Optimization**: Prefers combinations with fewer plates for the same weight
- **Precision**: Weights rounded to 2 decimal places
- **Balance Check**: Two-hand combinations balanced within 0.01 kg tolerance

**Built with Python 3.13+** | **Uses uv for dependency management**
