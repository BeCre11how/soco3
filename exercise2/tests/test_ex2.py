import subprocess
import os

# Support function
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Assembler Path
assembler_path = "../vm/assembler.py"

# Temporary Output Path
output_path = "AS_test_output_temp.mx"

################################################################################################################
#ASSEMBLER TEST - OUTPUT GENERATED
################################################################################################################

def test_assembler_program_output():
    # Program Name
    program = "program1"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])
    
    # Ensure the ASSEMBLER output file exists
    assert os.path.exists(output_path), "ASSEMBLER did not create the output file"
    os.remove(output_path)


################################################################################################################
#ASSEMBLER TEST 1
################################################################################################################

def test_assembler_program1():
    # Program Name
    program = "program1"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])

    # Assert that the assembler's output matches the expected output
    assert read_file(output_path) == read_file(expected_output_path), "Assembler output does not match expected output for " + program + ".as"
    os.remove(output_path)

################################################################################################################
#ASSEMBLER TEST 2
################################################################################################################

def test_assembler_program2():
    # Program Name
    program = "program2"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])

    # Assert that the assembler's output matches the expected output
    assert read_file(output_path) == read_file(expected_output_path), "Assembler output does not match expected output for " + program + ".as"
    os.remove(output_path)

################################################################################################################
#ASSEMBLER TEST 3
################################################################################################################

def test_assembler_program3():
    # Program Name
    program = "program3"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])

    # Assert that the assembler's output matches the expected output
    assert read_file(output_path) == read_file(expected_output_path), "Assembler output does not match expected output for " + program + ".as"
    os.remove(output_path)