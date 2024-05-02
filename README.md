# Repository Overview

This repository contains scripts designed to optimize and clean IFC files, specifically targeting unnecessary elements and spaces for improved performance and clarity. The primary focus is on the scripts `RensaIsolering.py` and `RensaSpaces.py`.

## `RensaIsolering.py`

This script is designed to clean the model from unnecessary IfcSpaces and optimize it for better performance. It processes multiple IFC files to remove unnecessary elements and optimize them for use.

### How to Run

1. Ensure Python and `ifcopenshell` are installed on your system.
2. Place your IFC file in the designated directory.
3. Run the script using the command: `python RensaIsolering.py`.
4. Follow the on-screen instructions to complete the process.

## `RensaSpaces.py`

This script aims to clean the model from unnecessary IfcSpaces for better performance and clarity. It identifies and removes unnecessary IfcSpace elements based on their names.

### How to Run

1. Ensure Python and `ifcopenshell` are installed on your system.
2. Use the command line to navigate to the script's directory.
3. Execute the script with the command: `python RensaSpaces.py <path_to_ifc_file>`.
4. The script will process the specified IFC file and remove unnecessary spaces.

## Dependencies

To run these scripts, you will need:

- Python (3.6 or newer)
- `ifcopenshell` library

Ensure these are installed and properly configured on your system before attempting to run the scripts.

