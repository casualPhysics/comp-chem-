import os

basis_sets = [
    "6-31G*", "6-31G**", "cc-pVDZ", "aug-cc-pVDZ", "cc-pVTZ",
    "aug-cc-pVTZ", "cc-pVQZ", "aug-cc-pVQZ", "cc-pV5Z", "aug-cc-pV5Z"
]

for basis in basis_sets:
    dir_name = basis.replace('*', 's')
    
    # Create directory
    os.makedirs(dir_name, exist_ok=True)
    
    # Write UHF file
    uhf_file_path = os.path.join(dir_name, 'uhf.inp')
    rhf_ccsd_file_path = os.path.join(dir_name, 'rhf_ccsd.inp')

    with open(xyz_file_path, 'w') as f:
        f.write(xyz_content)
    
      # Run ORCA for UHF calculation
    uhf_output_path = os.path.join(dir_name, 'uhf.out')
    subprocess.run(["orca", uhf_file_path], stdout=open(uhf_output_path, 'w'), stderr=subprocess.STDOUT)
    
    # Run ORCA for RHF CCSD calculation
    rhf_ccsd_output_path = os.path.join(dir_name, 'rhf_ccsd.out')
    subprocess.run(["orca", rhf_ccsd_file_path], stdout=open(rhf_ccsd_output_path, 'w'), stderr=subprocess.STDOUT)