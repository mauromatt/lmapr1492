#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install mp-api --upgrade')
import numpy as np
#from pymatgen.ext.matproj import MPRester
from mp_api.client import MPRester
from pymatgen.core.operations import SymmOp
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.electronic_structure.plotter import BSPlotter
from pymatgen.phonon.plotter import PhononBSPlotter
from jupyter_jsmol.pymatgen import quick_view
from lmapr1492 import plot_brillouin_zone, get_plot_bs, get_plot_dos, get_plot_bs_and_dos, get_branch_wavevectors
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[9]:


mp_key = "XOCzg18zLbitVQMZilg0OGK9MJ5rjMXh"
mp_id = "mp-7173"


# In[10]:


with MPRester(mp_key) as m:
    prim_struc = m.get_structure_by_material_id(mp_id)
    el_bs = m.get_bandstructure_by_material_id(mp_id)
    el_dos = m.get_dos_by_material_id(mp_id)
    ph_bs = m.get_phonon_bandstructure_by_material_id(mp_id)
    ph_dos = m.get_phonon_dos_by_material_id(mp_id)
conv_struc = SpacegroupAnalyzer(prim_struc).get_conventional_standard_structure()
symmops = SpacegroupAnalyzer(conv_struc).get_space_group_operations()


# In[12]:


print("Les 3 vecteurs de bases des son réseau direct sont:")
print(prim_struc.lattice)


# In[13]:


print("Les 3 vecteurs de bases de son réseau réciproque sont:")
print(prim_struc.lattice.reciprocal_lattice)


# In[14]:


print("son type maille est :",SpacegroupAnalyzer(prim_struc).get_lattice_type())
print("son systeme crystallin est :",SpacegroupAnalyzer(prim_struc).get_crystal_system())
print("son groupe ponctuel est :",SpacegroupAnalyzer(prim_struc).get_point_group_symbol())


# In[ ]:





# In[ ]:




