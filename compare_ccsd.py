import os

# List of basis sets
basis_sets = [
    "6-31G*", "6-31G**", "cc-pVDZ", "aug-cc-pVDZ", "cc-pVTZ",
    "aug-cc-pVTZ", "cc-pVQZ", "aug-cc-pVQZ", "cc-pV5Z", "aug-cc-pV5Z"
]

# UHF template
uhf_template = """! UHF {basis}
2 * xyzfile -1 2 ch2o.xyz
"""

# RHF CCSD template
rhf_ccsd_template = """! RHF 6-31G*
! CCSD
* xyzfile 0 1 ch2o.xyz
"""

# CH2O coordinates
xyz_content = """4

C          0.00000       -0.00000       -0.70966
O         -0.00000        0.00000        0.68418
H          0.00000       -0.99426       -1.20184
H          0.00000        0.99426       -1.20184
"""

# Create directories and files
for basis in basis_sets:
    # Replace * with 's' for directory names
    dir_name = basis.replace('*', 's')
    
    # Create directory
    os.makedirs(dir_name, exist_ok=True)
    
    # Write UHF file
    uhf_content = uhf_template.format(basis=basis)
    with open(os.path.join(dir_name, 'uhf.inp'), 'w') as f:
        f.write(uhf_content)
    
    # Write RHF CCSD file
    with open(os.path.join(dir_name, 'rhf_ccsd.inp'), 'w') as f:
        f.write(rhf_ccsd_template)
    
    # Write CH2O coordinates file
    with open(os.path.join(dir_name, 'ch2o.xyz'), 'w') as f:
        f.write(xyz_content)

print("Directories and files created successfully.")


# module run 
module_load_command = 'module load orca/5.0.4-openmpi4.1.1'
