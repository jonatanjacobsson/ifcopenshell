# -*- coding: utf-8 -*-
"""
Rensa modellen från onödiga IfcSpaces

"""
import ifcopenshell
import os
import shutil

from datetime import datetime

ifcfile = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/V-50-V-100.ifc"
ifcfileIsolering = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/V-50-V-Isolering.ifc"


timestamp = os.path.getmtime(ifcfile)

date = datetime.fromtimestamp(timestamp)

if (datetime.today() - date).days == 0:

    print("File has been modified today! Continuing...")

    print("Copying V-50-V-100 to V-50-V-Isolering...")
    shutil.copy(ifcfile, ifcfileIsolering)
    
    ifc = ifcopenshell.open(ifcfile)
    ifcIsolering = ifcopenshell.open(ifcfileIsolering)
    
    print("Removing items for V-50-V-10...")
    for i, item in enumerate(ifc.by_type('IfcCovering')): ifc.remove(item)
        
    print("Started saving... V-50-V-100.ifc")
    ifc.write(ifcfile)
    print("File saved.")
    
        
    print("Removing items for V-50-V-Isolering...")
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowController')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowFitting')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowSegment')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowTerminal')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcEnergyConversionDevice')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcBuildingElementProxy')): ifcIsolering.remove(item)
    print("Started saving... V-50-V-Isolering.ifc")
    ifcIsolering.write(ifcfileIsolering)
    
    print("Files saved.")
        
    print("Optimizing...")
    os.system("C:/Users/rvt.export01/Solibri/autorun/optimize_V-50.bat ")
    print("Done optimizing...")
    
else:
    print("File has not been modified today. Exiting.")
    


# V57

ifcfile = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/V-57-V-100.ifc"
ifcfileIsolering = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/V-57-V-Isolering.ifc"


timestamp = os.path.getmtime(ifcfile)

date = datetime.fromtimestamp(timestamp)

if (datetime.today() - date).days == 0:

    print("File has been modified today! Continuing...")

    print("Copying V-57-V-100 to V-57-V-Isolering...")
    shutil.copy(ifcfile, ifcfileIsolering)
    
    ifc = ifcopenshell.open(ifcfile)
    ifcIsolering = ifcopenshell.open(ifcfileIsolering)
    
    print("Removing items for V-57-V-10...")
    for i, item in enumerate(ifc.by_type('IfcCovering')): ifc.remove(item)
        
    print("Started saving... V-57-V-100.ifc")
    ifc.write(ifcfile)
    print("File saved.")
    
        
    print("Removing items for V-57-V-Isolering...")
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowController')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowFitting')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowSegment')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowTerminal')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowTerminalDevice')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowTreatmentDevice')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcBuildingElementProxy')): ifcIsolering.remove(item)
    print("Started saving... V-57-V-Isolering.ifc")
    ifcIsolering.write(ifcfileIsolering)
    
    print("Files saved.")
        
    print("Optimizing...")
    os.system("C:/Users/rvt.export01/Solibri/autorun/optimize_V-57.bat ")
    print("Done optimizing...")
    
else:
    print("File has not been modified today. Exiting.")


# V53

ifcfile = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/V-53-V-100.ifc"
ifcfileIsolering = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/V-53-V-Isolering.ifc"


timestamp = os.path.getmtime(ifcfile)

date = datetime.fromtimestamp(timestamp)

if (datetime.today() - date).days == 0:

    print("File has been modified today! Continuing...")

    print("Copying V-53-V-100 to V-53-V-Isolering...")
    shutil.copy(ifcfile, ifcfileIsolering)
    
    ifc = ifcopenshell.open(ifcfile)
    ifcIsolering = ifcopenshell.open(ifcfileIsolering)
    
    print("Removing items for V-53-V-10...")
    for i, item in enumerate(ifc.by_type('IfcCovering')): ifc.remove(item)
        
    print("Started saving... V-53-V-100.ifc")
    ifc.write(ifcfile)
    print("File saved.")
    
        
    print("Removing items for V-53-V-Isolering...")
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowController')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowFitting')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowSegment')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcFlowTerminal')): ifcIsolering.remove(item)
    for i, item in enumerate(ifcIsolering.by_type('IfcDistributionPort')): ifcIsolering.remove(item)
    print("Started saving... V-53-V-Isolering.ifc")
    ifcIsolering.write(ifcfileIsolering)
    
    print("Files saved.")
        
    print("Optimizing...")
    os.system("C:/Users/rvt.export01/Solibri/autorun/optimize_V-53.bat ")
    print("Done optimizing...")
    
else:
    print("File has not been modified today. Exiting.")