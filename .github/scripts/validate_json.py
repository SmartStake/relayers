import json
import glob

def validate_json(json_file):
    try:
        json.load(open(json_file, 'r'))
        print(f"Valid JSON: {json_file}")
    except ValueError as e:
        print(f"Invalid JSON: {json_file}")
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    print("starting json validation")
    files = glob.glob('**/*.json', recursive=True)
    for file in files:
        validate_json(file)
    print("after json validation")
