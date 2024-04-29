#!/usr/bin/env python3
import argparse
import sys
import time
import os
import random
import json

# Function to get the terminal width
def get_terminal_width():
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:  # If unable to get terminal size
        return None

def split_float(number, parts):
    if parts == 1:
        return [number]
    elif parts > number:
        # Generate random splits for each part
        splits = sorted(random.sample(range(1, number + parts - 1), parts - 1))
        # Add random noise to each split
        splits = [split + random.uniform(0, 50) for split in splits]
        # Calculate the differences between consecutive splits
        diffs = [splits[0]] + [splits[i] - splits[i - 1] for i in range(1, len(splits))] + [number + parts - 1 - splits[-1]]
    else:
        # Generate x-1 random splits
        splits = sorted(random.sample(range(1, number), parts - 1))
        # Add random noise to each split
        splits = [split + random.uniform(-0.5, 0.5) for split in splits]
        # Calculate the differences between consecutive splits
        diffs = [splits[0]] + [splits[i] - splits[i - 1] for i in range(1, len(splits))] + [number - splits[-1]]
    # Convert to floats
    diffs = [float(diff) for diff in diffs]
    return diffs

# JSONDecoder subclass to strip comments from JSON strings
class JSONCommentStripper(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(JSONCommentStripper, self).__init__(
            *args, object_hook=self._object_hook, **kwargs
        )

    def _object_hook(self, obj):
        return obj

    def decode(self, s, *args, **kwargs):
        return super(JSONCommentStripper, self).decode(
            self._strip_comments(s), *args, **kwargs
        )

    def _strip_comments(self, s):
        in_string = False
        in_single_comment = False
        in_multi_comment = False
        out = ''
        i = 0

        while i < len(s):
            if in_string:
                if s[i] == '"' and (i == 0 or s[i - 1] != '\\'):
                    in_string = False
                out += s[i]
                i += 1
            else:
                if in_single_comment:
                    if s[i] == '\n':
                        in_single_comment = False
                    i += 1
                elif in_multi_comment:
                    if s[i:i + 2] == '*/':
                        in_multi_comment = False
                        i += 2
                    else:
                        i += 1
                else:
                    if s[i] == '"':
                        in_string = True
                    elif s[i:i + 2] == '//':
                        in_single_comment = True
                        i += 2
                    elif s[i:i + 2] == '/*':
                        in_multi_comment = True
                        i += 2
                    else:
                        out += s[i]
                        i += 1

        return out

# Function to load the JSON config file
def load_config(filename):
    try:
        with open(filename, 'r') as f:
            return json.loads(f.read(), cls=JSONCommentStripper)
    except FileNotFoundError:
        # If config file not found, use default path
        default_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
        print("Config file not found. Using default path:", default_config_path)
        return load_config(default_config_path)
    except json.JSONDecodeError:
        print("Invalid JSON format in config file.")
        sys.exit(1)

# Function to save the updated config to file
def save_config(filename, config):
    try:
        with open(filename, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error saving config file: {e}")
        sys.exit(1)

# Function to create and display the progress bar
def create_bar(config):
    totalProgress = 0
    individualProgress = [0] * len(config["textList"])  # Initialize individual progress for each bar
    progressBarsList = []
    fracs = []
    topMargin = '\n'
    length = config["length"]
    totalBarText = config["totalBarText"]
    introRotationCount = config["introRotationCount"]
    introWordCount = config["introWordCount"]
    textList = config["textList"]
    totalTime = config["totalTime"]
    lastText = config["lastText"]
    quantity = len(textList)
    timings = [0.01,1.5,0.25,0,1,0.01,0.25,0.1,0.01,0.25,0.02,0.01,0.25,0.2,0.25,0,0.1,0.01,0.25,0.1,0.01,0.25,0.02,0.01,0.25,0.2,0.25,0,0.1,0.01,0.25,0.1,0.01,0.25,0.02,0.01,0.25,0.2,]
    
    for i in range(introRotationCount*2):

      sys.stdout.write('\r' + 'initializing |')
      time.sleep(0.1)
      os.system('clear')
      sys.stdout.write('\r' + 'initializing /')
      time.sleep(0.1)
      os.system('clear')
      sys.stdout.write('\r' + 'initializing -')
      time.sleep(0.1)
      os.system('clear')
      sys.stdout.write('\r' + 'initializing \\')
      time.sleep(0.1)
      os.system('clear')

    sys.stdout.write('\r' + 'initializing |')

    for i in range(introWordCount):
      sys.stdout.write('\n' + random.choice(textList))
      time.sleep(random.choice(timings))

    sys.stdout.write('\n\n\n'+ 'All Done!')

    time.sleep(1)

    os.system("clear")

    for i in range(introRotationCount*2):

      sys.stdout.write('\r' + 'All Done, now starting critical processes |')
      time.sleep(0.1)
      os.system('clear')
      sys.stdout.write('\r' + 'All Done, now starting critical processes /')
      time.sleep(0.1)
      os.system('clear')
      sys.stdout.write('\r' +'All Done, now starting critical processes -')
      time.sleep(0.1)
      os.system('clear')
      sys.stdout.write('\r' +  'All Done, now starting critical processes \\')
      time.sleep(0.1)
      os.system('clear')

    sys.stdout.write('\r' + 'All Done, now starting critical processes |')

    time.sleep(1)

    os.system("clear")

    time.sleep(1)

    while totalProgress <= 100:
        totalProgress += 1  # Increment total progress
        
        totalBarProgress = int(length * (totalProgress / 100))
        totalBarRemaining = length - int(totalBarProgress)

        # Update individual progress for each bar
        for i in range(len(textList)):
        # Add each fraction to individualProgress[i]
            fractions = split_float(totalTime, quantity - 1)
            for frac in fractions:
                fracs.append(int(abs(frac)))
            if fracs[i] <= 0:
                fracs[i] = 1 
            individualProgress[i] += fracs[i]

        # Construct progress bars
        progressBarsList = []
        for i in range(len(textList)):
            # Calculate percentage and progress for the current bar
            percent = str(int(min(individualProgress[i], 100))) + '%'  
            barProgress = min(individualProgress[i], 100) / 100 * length  
            barRemaining = length - int(barProgress)

            # Construct the progress bar string
            if barProgress >= length:
                percent = '100%'
                bar = '[' + '#' * length + ']'
            else:
                bar = '[' + '#' * int(barProgress) + '-' * int(barRemaining) + ']'

            # Calculate margin to align the bar with text and percentage
            indBuffer = ' ' * (5 - len(percent))  
            margin = ' ' * (get_terminal_width() - (len(bar) + len(textList[i]) + len(percent) + len(indBuffer)))  

            # Construct the final line
            line = textList[i] + margin + bar + indBuffer + percent + '\n'
            progressBarsList.append(line)

        bars = ''.join(progressBarsList)

        # Clear previous output and print current progress bars
        os.system('clear')
        sys.stdout.write(topMargin + bars)

        # Construct total progress bar
        totalPercent = str(int(totalProgress - 1)) + '%' 
        totalBar = '[' + '#' * int(totalBarProgress) + '-' * int(totalBarRemaining) + ']' 
        buffer = ' ' * (5 - len(totalPercent))
        rightAlign = ' ' * (get_terminal_width() - (len(totalBar) + len(totalBarText) + len(totalPercent) + len(buffer) ))
        totalBar = totalBarText + rightAlign + totalBar + buffer + totalPercent

        # Print total progress bar
        sys.stdout.write('\n' + totalBar)

        # Delay between frames
        delay = totalTime / 100
        time.sleep(delay)

        # Clearing top margin
        topMargin = ''

    time.sleep(5)
    os.system("clear")
    sys.stdout.write('\n' + lastText + '\n')

# Main function
def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description='Current config file path: config.json')
    parser.add_argument('-c', '--config', dest='config', type=str, help='Path to the config file (optional)', default='config.json', nargs='?')
    parser.add_argument('--resetConf', action='store_true', help='Reset the config file path to default')
    parser.add_argument('-L', '--Length', dest='length', type=int, help='Overrides length parameter in config')
    parser.add_argument('-T', '--Time', dest='totalTime', type=int, help='Overrides totalTime parameter in config')

    # Parse command-line arguments
    args = parser.parse_args()

    # Reset config file path if requested
    if args.resetConf:
        default_config_path = os.path.abspath('config.json')
        print("Resetting config file path to default:", default_config_path)
        args.config = default_config_path

    # If config path is not provided, use the default path
    if args.config is None:
        args.config = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

    # Get absolute path of config file
    config_path = os.path.abspath(args.config)
    print("Current config file path:", config_path)

    # Load config from file
    config = load_config(config_path)

    # Override config parameters if provided as arguments
    if args.length is not None:
        config["length"] = args.length

    if args.totalTime is not None:
        config["totalTime"] = args.totalTime

    # Create and display progress bar
    create_bar(config)

    # Update config file path if provided as argument
    if args.config:
        config["config_path"] = os.path.abspath(args.config)
        save_config('config.json', config)



# Execute main function if script is run directly
if __name__ == "__main__":
    main()
