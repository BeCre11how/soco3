import subprocess
import os

# Support function
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
        
# VM path
vm_path = "../vm/vm.py"

# Temporary Output Path
output_path = "vm_test_output_temp.txt"

################################################################################################################
#VM TEST 0 (OUTPUT GENERATED)
################################################################################################################

def test_vm_program_output():
    # Program Name
    program = "program1"
     
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run(["python", vm_path, input_path, output_path])

    output_bool = os.path.exists(output_path)
    os.remove(output_path)
        
    # Ensure the VM output file exists
    assert output_bool, "VM did not create the output file"

################################################################################################################
#VM TEST 1
################################################################################################################

def test_vm_program1():
    # Program Name
    program = "program1"
     
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run(["python", vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"

################################################################################################################
#VM TEST 2
################################################################################################################

def test_vm_program2():
    # Program Name
    program = "program2"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run(["python", vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"

################################################################################################################
#VM TEST 3
################################################################################################################

def test_vm_program3():
    # Program Name
    program = "program3"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run(["python", vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"

################################################################################################################
#VM TEST 4
################################################################################################################

def test_vm_program4():
    # Program Name
    program = "program4"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run(["python", vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"
 
    

