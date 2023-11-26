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

    # Ensure the VM output file exists
    assert os.path.exists(output_path), "VM did not create the output file"

    # Assert that the VM's output matches the expected output
    assert read_file(output_path) == read_file(expected_output_path), "VM output does not match expected output for " + program + ".mx"
    os.remove(output_path)


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

    # Ensure the VM output file exists
    assert os.path.exists(output_path), "VM did not create the output file"

    # Assert that the VM's output matches the expected output
    assert read_file(output_path) == read_file(expected_output_path), "VM output does not match expected output for " + program + ".mx"
    os.remove(output_path)

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

    # Ensure the VM output file exists
    assert os.path.exists(output_path), "VM did not create the output file"

    # Assert that the VM's output matches the expected output
    assert read_file(output_path) == read_file(expected_output_path), "VM output does not match expected output for " + program + ".mx"
    os.remove(output_path)
    
################################################################################################################
#OUT OF MEMORY TEST [DONE]
################################################################################################################

def test_vm_out_of_memory():
    # Program Name
    program = "out_of_memory"
    
    # Path to the VM script
    input_path = "mx_files_ok/" + program + ".mx"

    # Run the VM on the program and save error messages
    result = subprocess.run(["python", vm_path, input_path, output_path], stderr=subprocess.PIPE, text=True)

    assert result.returncode != 0, "VM should have exited with an error"
    assert "AssertionError: Program too long" in result.stderr

    os.remove(output_path)
    
################################################################################################################
#INSTRUCTION NOT FOUND TEST [DONE]
################################################################################################################

def test_vm_instruction_not_found():
    # Program Name
    program = "invalid_instruction"
    
    # Path to the VM script
    input_path = "mx_files_ok/" + program + ".mx"

    # Run the VM on the program and save error messages
    result = subprocess.run(["python", vm_path, input_path, output_path], stderr=subprocess.PIPE, text=True)

    assert result.returncode != 0, "VM should have exited with an error"
    assert "Unknown op" in result.stderr
    
    os.remove(output_path)
