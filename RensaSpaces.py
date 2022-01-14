# -*- coding: utf-8 -*-
"""
Rensa modellen från onödiga IfcSpaces

"""
import ifcopenshell
import os
from datetime import datetime

ifcfile = "L:/UPPDRAG/2021/210255_Syrenbersån/3 - IFC/A-40-V-100.ifc"

timestamp = os.path.getmtime(ifcfile)

date = datetime.fromtimestamp(timestamp)
print((datetime.today() - date).days)

if (datetime.today() - date).days == 0:
    print("File has been modified today! Continuing...")

    ifc = ifcopenshell.open(ifcfile)
    
    spaces = ifc.by_type('IfcSpace')
    
    for i, space in enumerate(spaces):
        if 'Area' in space.Name: ifc.remove(space)
        elif  'Atemp' in space.Name: ifc.remove(space)
        elif  'Hus' in space.Name: ifc.remove(space)
        elif  'Mörk' in space.Name: ifc.remove(space)
        
    print("Unnecessary spaces deleted. Started saving...")
    ifc.write(ifcfile)
    
    print("File saved.")
else:
    print("File has not been modified today. Exiting.")