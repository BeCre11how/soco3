import subprocess
import os
import pytest

################################################################################################################
#VM TEST 1
################################################################################################################

def test_vm_program1():
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    vm_path = "../vm/vm.py"
    input_path = "mx_files_ok/program1.mx"
    output_path = "vm_test_output_temp.txt"
    expected_output_path = "vm_outputs_ok/output1.txt"
    
    # Run the VM on program1.mx
    subprocess.run(["python", vm_path, input_path, output_path])

    # Ensure the VM output file exists
    assert os.path.exists(output_path), "VM did not create the output file"

    # Read the output from the VM
    with open(output_path, "r") as file:
        vm_output = file.read()
        os.remove(output_path)

    # Read the expected output
    with open(expected_output_path, "r") as file:
        expected_output = file.read()

    # Assert that the VM's output matches the expected output
    assert vm_output == expected_output, "VM output does not match expected output for program1.mx"


################################################################################################################
#VM TEST 2
################################################################################################################

def test_vm_program2():
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    vm_path = "../vm/vm.py"
    input_path = "mx_files_ok/program2.mx"
    output_path = "vm_test_output_temp.txt"
    expected_output_path = "vm_outputs_ok/output2.txt"
    
    # Run the VM on program1.mx
    subprocess.run(["python", vm_path, input_path, output_path])

    # Ensure the VM output file exists
    assert os.path.exists(output_path), "VM did not create the output file"

    # Read the output from the VM
    with open(output_path, "r") as file:
        vm_output = file.read()
        os.remove(output_path)

    # Read the expected output
    with open(expected_output_path, "r") as file:
        expected_output = file.read()

    # Assert that the VM's output matches the expected output
    assert vm_output == expected_output, "VM output does not match expected output for program1.mx"

################################################################################################################
#VM TEST 3
################################################################################################################

def test_vm_program3():
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    vm_path = "../vm/vm.py"
    input_path = "mx_files_ok/program3.mx"
    output_path = "vm_test_output_temp.txt"
    expected_output_path = "vm_outputs_ok/output3.txt"
    
    # Run the VM on program1.mx
    subprocess.run(["python", vm_path, input_path, output_path])

    # Ensure the VM output file exists
    assert os.path.exists(output_path), "VM did not create the output file"

    # Read the output from the VM
    with open(output_path, "r") as file:
        vm_output = file.read()
        os.remove(output_path)

    # Read the expected output
    with open(expected_output_path, "r") as file:
        expected_output = file.read()

    # Assert that the VM's output matches the expected output
    assert vm_output == expected_output, "VM output does not match expected output for program1.mx"
    
################################################################################################################
#OUT OF MEMORY TEST [DONE]
################################################################################################################


def test_vm_out_of_memory():
    # Path to the VM script
    vm_path = "../vm/vm.py"
    input_path = "mx_files_ok/out_of_memory.mx"
    output_path = "vm_test_output_temp.txt"

    result = subprocess.run(["python", vm_path, input_path, output_path], stderr=subprocess.PIPE, text=True)

    assert result.returncode != 0, "VM should have exited with an error"
    assert "AssertionError: Program too long" in result.stderr

    os.remove(output_path)
    
################################################################################################################
#INSTRUCTION NOT FOUND TEST [DONE]
################################################################################################################

def test_vm_instruction_not_found():
    # Path to the VM script
    vm_path = "../vm/vm.py"
    input_path = "mx_files_ok/invalid_instruction.mx"
    output_path = "vm_test_output_temp.txt"

    result = subprocess.run(["python", vm_path, input_path, output_path], stderr=subprocess.PIPE, text=True)

    assert result.returncode != 0, "VM should have exited with an error"
    assert "Unknown op" in result.stderr
    
    os.remove(output_path)
