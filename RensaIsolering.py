# -*- coding: utf-8 -*-
"""
Script to clean the model from unnecessary IfcSpaces and optimize it.

This script processes multiple IFC files to remove unnecessary elements and optimize them.
"""

import ifcopenshell
import os
import shutil
from datetime import datetime

# Function to remove items based on their type
def remove_items(ifc, types):
    """
    Removes items of specified types from the IFC file.
    
    :param ifc: The IFC file object
    :param types: A list of types to remove
    """
    for item_type in types:
        for item in ifc.by_type(item_type):
            ifc.remove(item)

# Function to process and optimize IFC files
def process_ifc_file(ifcfile, ifcfileIsolering, types_to_remove, optimize_script):
    """
    Processes an IFC file by copying it, removing specified items, and optimizing it.
    
    :param ifcfile: Path to the original IFC file
    :param ifcfileIsolering: Path to the IFC file for isolering
    :param types_to_remove: A list of item types to remove
    :param optimize_script: Path to the optimization script
    """
    try:
        timestamp = os.path.getmtime(ifcfile)
        date = datetime.fromtimestamp(timestamp)
        if (datetime.today() - date).days == 0:
            print(f"File {ifcfile} has been modified today! Continuing...")
            shutil.copy(ifcfile, ifcfileIsolering)
            ifc = ifcopenshell.open(ifcfile)
            ifcIsolering = ifcopenshell.open(ifcfileIsolering)
            remove_items(ifc, ['IfcCovering'])
            ifc.write(ifcfile)
            remove_items(ifcIsolering, types_to_remove)
            ifcIsolering.write(ifcfileIsolering)
            print(f"Files {ifcfile} and {ifcfileIsolering} saved.")
            os.system(optimize_script)
            print("Done optimizing.")
        else:
            print(f"File {ifcfile} has not been modified today. Exiting.")
    except Exception as e:
        print(f"Error processing file {ifcfile}: {e}")

# Configuration for file paths and types to remove
config = {
    "V-50": {
        "ifcfile": "path/to/V-50-V-100.ifc",
        "ifcfileIsolering": "path/to/V-50-V-Isolering.ifc",
        "types_to_remove": ['IfcFlowController', 'IfcFlowFitting', 'IfcFlowSegment', 'IfcFlowTerminal', 'IfcEnergyConversionDevice', 'IfcBuildingElementProxy'],
        "optimize_script": "path/to/optimize_V-50.bat"
    },
    "V-57": {
        "ifcfile": "path/to/V-57-V-100.ifc",
        "ifcfileIsolering": "path/to/V-57-V-Isolering.ifc",
        "types_to_remove": ['IfcFlowController', 'IfcFlowFitting', 'IfcFlowSegment', 'IfcFlowTerminal', 'IfcFlowTerminalDevice', 'IfcFlowTreatmentDevice', 'IfcBuildingElementProxy'],
        "optimize_script": "path/to/optimize_V-57.bat"
    },
    "V-53": {
        "ifcfile": "path/to/V-53-V-100.ifc",
        "ifcfileIsolering": "path/to/V-53-V-Isolering.ifc",
        "types_to_remove": ['IfcFlowController', 'IfcFlowFitting', 'IfcFlowSegment', 'IfcFlowTerminal', 'IfcDistributionPort'],
        "optimize_script": "path/to/optimize_V-53.bat"
    }
}

# Main execution
if __name__ == "__main__":
    for key, value in config.items():
        process_ifc_file(value["ifcfile"], value["ifcfileIsolering"], value["types_to_remove"], value["optimize_script"])
