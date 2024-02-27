#
#   ╔═╗╔╗ ╦  ╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
#   ╠═╣╠╩╗║  ║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
#   ╩ ╩╚═╝╩  ╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
#       By Toge - 2024
#

import os
import json

def create_directory_if_not_exists(directory_path):
    """Ensures the specified directory exists, creating it if necessary."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")

def is_valid_json_file(file_path):
    """Checks if the file is a valid JSON file with an 'abi' key."""
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            # Check if data is a dictionary and has an 'abi' key
            return isinstance(data, dict) and 'abi' in data
    except (json.JSONDecodeError, FileNotFoundError):
        # Invalid JSON or file not found
        return False
    except Exception as e:
        print(f"Unexpected error when validating JSON file {file_path}: {e}")
        return False

def extract_and_write_abi(source_file, target_path):
    """Extracts ABI from the source file and writes it to the target path."""
    with open(source_file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        abi = data['abi']
        
    with open(target_path, 'w', encoding='utf-8') as abi_file:
        json.dump(abi, abi_file, indent=4)
    print(f"ABI extracted and saved to {target_path}")

def process_directory_for_abi_files(directory):
    """Processes all JSON files in the directory and its subdirectories for ABIs."""
    abi_directory = os.path.join(directory, "extracted ABIs")
    create_directory_if_not_exists(abi_directory)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                full_file_path = os.path.join(root, file)
                if is_valid_json_file(full_file_path):
                    output_file_name = f"{file[:-5]}ABI.json"
                    output_file_path = os.path.join(abi_directory, output_file_name)
                    extract_and_write_abi(full_file_path, output_file_path)

def main():
    """Main function to execute the script."""
    current_directory = os.getcwd()
    process_directory_for_abi_files(current_directory)

if __name__ == "__main__":
    main()
