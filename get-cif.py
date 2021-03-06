#!/usr/bin/python

import sys
import pymatgen as pm
import pymatgen.io.cifio as cif

for id in sys.argv[1:]:
    m = pm.MPRester("")
	struct = m.get_structure_by_material_id(id, False)
	ciff = cif.CifWriter(struct)

	ciff.write_file(id + '.cif')
