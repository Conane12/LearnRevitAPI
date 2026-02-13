# -*- coding: utf-8 -*-
__title__   = "Rename Views"
__doc__     = """Version = 1.0
Date    = 31.12.2025
________________________________________________________________
Description:

This is a template file for pyRevit Scripts.

________________________________________________________________
How-To:

-> Click on the button
-> slect views
-> Define Tenaming Rules 
-> Rename Views


________________________________________________________________
Last Updates:
- [31.12.2025] - 1.0 RELEASE

________________________________________________________________
Author: Erik Frits"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
from Autodesk.Revit.DB import *
#pyRevit
from pyrevit import revit, forms

#.NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#==================================================




#🤖 Automate Your Boring Work Here





#==================================================
# select Views
Sel_el_ids = uidoc.Selection.GetElementIds()
sel_elm = [doc.GetElement(e_id) for e_id in Sel_el_ids]
sele_views = [el for el in sel_elm if isinstance(el, View)]

# If None Selected 0 promp selectviews from pyrevit.forms.select_views()
if not sele_views:
    sele_views = forms.select_views()

# Ensure Views Selected 
if not sele_views:
    forms.alert('No Views Selected. Pleas Try Again', exitscript=True)

    
# Define Renaming Rules
prefix = 'pre'
find = 'FloorPlan'
replace = 'EF-Level'
suffix = '-suf'

# start transaction to make changes in project 
t = Transaction(doc, 'py-Rename Views')
t.Start() 

for view in sele_views:
    
    #Create new View Name
     old_name = view.Name 
     new_name = prefix + old_name.replace(find, replace) + suffix

     # Rename veiws (Ensure unige view nam )
     for i in range(20):
         try:
             view.Name = new_nameh
             print('{} -> {}' .format(old_name, new_name))
             break
         except:
             new_name += '*'

t.Commit() #

print('Done!')
             