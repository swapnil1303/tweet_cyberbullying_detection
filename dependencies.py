import subprocess

# Use pip freeze to get a list of installed packages and their versions
output = subprocess.check_output(['pip', 'freeze']).decode('utf-8')
packages = output.split('\n')

# Write the package names and versions to requirements.txt
with open('requirements.txt', 'w') as f:
    for package in packages:
        f.write(package + '\n')

print("requirements.txt file created successfully.")
