# -*- coding: utf-8 -*-
"""
Script to clean the model from unnecessary IfcSpaces for better performance and clarity.

This script opens an IFC file, identifies and removes unnecessary IfcSpace elements based on their names.
"""

import ifcopenshell
import os
import sys
from datetime import datetime

# Configuration for file path
ifcfile_path = sys.argv[1] if len(sys.argv) > 1 else "default/ifc/file/path.ifc"

def remove_unnecessary_spaces(ifcfile):
    """
    Removes unnecessary IfcSpace elements from the IFC file.
    
    :param ifcfile: Path to the IFC file
    """
    try:
        ifc = ifcopenshell.open(ifcfile)
        spaces = ifc.by_type('IfcSpace')
        
        for space in spaces:
            if any(keyword in space.Name for keyword in ['Area', 'Atemp', 'Hus', 'Mörk']):
                ifc.remove(space)
                
        print("Unnecessary spaces deleted. Started saving...")
        ifc.write(ifcfile)
        print("File saved successfully.")
    except Exception as e:
        print(f"Error processing file {ifcfile}: {e}")

def main():
    """
    Main function to execute the script.
    """
    timestamp = os.path.getmtime(ifcfile_path)
    date = datetime.fromtimestamp(timestamp)
    
    if (datetime.today() - date).days == 0:
        print("File has been modified today! Continuing...")
        remove_unnecessary_spaces(ifcfile_path)
    else:
        print("File has not been modified today. Exiting.")

if __name__ == "__main__":
    main()
