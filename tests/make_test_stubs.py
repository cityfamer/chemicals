#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

tests = ['test_acentric', 'test_combustion', 'test_critical', 'test_dipole', 'test_dippr', 'test_elements', 'test_environment', 'test_heat_capacity', 'test_interface', 'test_lennard_jones', 'test_miscdata', 'test_permittivity', 'test_phase_change', 'test_rachford_rice', 'test_reactions', 'test_refractivity', 'test_solubility', 'test_temperature', 'test_thermal_conductivity', 'test_triple', 'test_utils', 'test_vapor_pressure', 'test_vectorized', 'test_virial', 'test_viscosity', 'test_volume']
try:
    os.remove("monkeytype.sqlite3")
except:
    pass

for t in tests:
    os.system("python3 -m monkeytype run manual_runner.py %s" %t)
for t in tests:
    mod = t[5:]
    os.system("python3 -m monkeytype stub chemicals.%s > ../chemicals/%s.pyi" %(mod, mod))
    type_hit_path = "../chemicals/%s.pyi" %mod
    dat = open(type_hit_path, 'r').read()
    imports = 'from typing import List\n'
    dat = '# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!\n' + imports + dat
    dat = dat.replace('Union[int, float]', 'float')
    dat = dat.replace('Union[float, int]', 'float')
    dat += '\n__all__: List[str]'
    open(type_hit_path, 'w').write(dat)

try:
    os.remove("monkeytype.sqlite3")
except:
    pass
