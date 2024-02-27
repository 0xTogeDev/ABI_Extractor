#
#   ╔═╗╔╗ ╦  ╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
#   ╠═╣╠╩╗║  ║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
#   ╩ ╩╚═╝╩  ╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
#       By Toge - 2024
#

import os
import json

def extract_and_save_abi(current_directory):
    # Define the directory to store the extracted ABIs
    abi_directory = os.path.join(current_directory, "extracted ABIs")
    
    # Check if the directory exists, if not, create it
    if not os.path.exists(abi_directory):
        os.makedirs(abi_directory)
        print(f"Created directory: {abi_directory}")

    for root, dirs, files in os.walk(current_directory):
        for file in files:
            if file.endswith('.json'):
                # Construct the full file path
                full_file_path = os.path.join(root, file)
                
                # Open and read the .json file
                with open(full_file_path, 'r', encoding='utf-8') as json_file:
                    try:
                        data = json.load(json_file)
                        # Skip files where data is a list or there's no ABI key in a dict
                        if isinstance(data, list) or 'abi' not in data:
                            continue
                            
                        abi = data['abi']
                        if abi:
                            # Construct the output file name and path
                            output_file_name = f"{file[:-5]}ABI.json"
                            output_file_path = os.path.join(abi_directory, output_file_name)
                            
                            # Write the ABI to a new .json file
                            with open(output_file_path, 'w', encoding='utf-8') as abi_file:
                                json.dump(abi, abi_file, indent=4)
                            
                            print(f"ABI extracted and saved to {output_file_path}")
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from file {full_file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    extract_and_save_abi(current_directory)
