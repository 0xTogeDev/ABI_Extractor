╔═╗╔╗ ╦  ╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
╠═╣╠╩╗║  ║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
╩ ╩╚═╝╩  ╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═


This Python script automatically searches for `.json` files containing smart contract ABIs in a specified directory and its subdirectories. It extracts the ABI part from each `.json` file and saves it into a new `.json` file in a folder named `extracted ABIs`. This tool is particularly useful for developers working with Ethereum smart contracts who need to manage and organize ABIs efficiently.

## Features

- **Recursive File Search:** Automatically searches the current directory and all subdirectories for `.json` files.
- **ABI Extraction:** Extracts the `abi` field from smart contract `.json` files.
- **Automated Folder Organization:** Saves extracted ABIs in a separate directory, keeping your workspace tidy.
- **Error Handling:** Gracefully handles errors, such as invalid JSON files or missing ABI fields.

## Requirements

- Python 3.x

## Installation

No additional installation is required, as the script utilizes the Python Standard Library. Simply clone or download this repository to your local machine to get started.

## Usage

1. Place `abi_extractor.py` in the root directory where your smart contract `.json` files are located.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `abi_extractor.py`.
4. Run the script using Python:

   ```bash
   python abi_extractor.py
   