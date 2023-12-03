import subprocess
import os
from environment import environment

# Support function
def read_file(file_path):
    with open(file_path, 'r') as file:
        file = file.read()
        return list(filter(lambda x: x != '', file.split("\n")))
# VM path
vm_path = "../vm/vm.py"

# Temporary Output Path
output_path = "vm_test_output_temp.txt"

################################################################################################################
#VM TEST OUTPUT (OUTPUT GENERATED)
################################################################################################################

def test_vm_program_output():
    # Program Name
    program = "program1"
     
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])

    output_bool = os.path.exists(output_path)
    os.remove(output_path)
        
    # Ensure the VM output file exists
    assert output_bool, "VM did not create the output file"
    
################################################################################################################
#VM TEST EXAMPLE (Testing given example file from task)
################################################################################################################

def test_vm_program_ex():
    # Program Name
    program = "count_up"
     
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"


################################################################################################################
#VM TEST 1 (TEST VM ON .mx TO CORRESPONDING ASSEMBLER TEST ON THE SAME PROGRAM NUMBER)
################################################################################################################

def test_vm_program1():
    # Program Name
    program = "program1"
     
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"

################################################################################################################
#VM TEST 2 (TEST VM ON .mx TO CORRESPONDING ASSEMBLER TEST ON THE SAME PROGRAM NUMBER)
################################################################################################################

def test_vm_program2():
    # Program Name
    program = "program2"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"

################################################################################################################
#VM TEST 3 (TEST VM ON .mx TO CORRESPONDING ASSEMBLER TEST ON THE SAME PROGRAM NUMBER)
################################################################################################################

def test_vm_program3():
    # Program Name
    program = "program3"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"

################################################################################################################
#VM TEST 4 (TEST VM ON .mx TO CORRESPONDING ASSEMBLER TEST ON THE SAME PROGRAM NUMBER)
################################################################################################################

def test_vm_program4():
    # Program Name
    program = "program4"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"
 
################################################################################################################
#VM TEST 5 (TEST VM ON .mx TO CORRESPONDING ASSEMBLER TEST ON THE SAME PROGRAM NUMBER)
################################################################################################################

def test_vm_program5():
    # Program Name
    program = "program5"
    
    # Path to the VM script, for the .mx file, the expected output file and for the VM output file
    input_path = "mx_files_ok/" + program + ".mx"
    expected_output_path = "vm_outputs_ok/" + program + ".txt"
    
    # Run the VM on the program
    subprocess.run([environment, vm_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the VM's output matches the expected output
    assert output == expected_output, "VM output does not match expected output for " + program + ".mx"
 
################################################################################################################
#POSSIBLY FURTHER TESTS: (FROM ASSEMBLER: swp, inc, dec -> correspond to missing lines 91, 93, 95 in vm.py test coverage)
#       Add Test that coveres vm.py line 80: beq -> if self.reg[arg0] == 0: self.ip = arg1
#       Add Test that covers assembler.py line 53: elif 
################################################################################################################

