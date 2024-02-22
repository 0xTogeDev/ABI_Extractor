import os
import json

def extract_and_save_abi(current_directory):
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            if file.endswith('.json'):
                # Construct the full file path
                full_file_path = os.path.join(root, file)
                
                # Open and read the .json file
                with open(full_file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    # Extract the ABI part
                    abi = data.get('abi')
                    if abi:
                        # Generate the new file name and path
                        new_file_name = f"{os.path.splitext(file)[0]}ABI.json"
                        new_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), new_file_name)
                        
                        # Write the ABI part to a new .json file
                        with open(new_file_path, 'w', encoding='utf-8') as new_json_file:
                            json.dump(abi, new_json_file, indent=4)
                            print(f"ABI extracted and saved to {new_file_path}")

if __name__ == "__main__":
    # Pass the current directory of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    extract_and_save_abi(current_directory)
