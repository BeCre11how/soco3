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
#ASSEMBLER TEST 0 (OUTPUT GENERATED)
################################################################################################################

def test_assembler_program_output():
    # Program Name
    program = "program1"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])
    
    output_bool = os.path.exists(output_path)
    os.remove(output_path)
    
    # Ensure the ASSEMBLER output file exists
    assert output_bool, "ASSEMBLER did not create the output file"
    
################################################################################################################
#ASSEMBLER TEST 1 (Testing ldc, ldr, cpy, str)
################################################################################################################

def test_assembler_program1():
    # Program Name
    program = "program1"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the assembler's output matches the expected output
    assert output == expected_output, "Assembler output does not match expected output for " + program + ".as"

################################################################################################################
#ASSEMBLER TEST 2 (Testing add, sub, beq)
################################################################################################################

def test_assembler_program2():
    # Program Name
    program = "program2"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])

    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the assembler's output matches the expected output
    assert output == expected_output, "Assembler output does not match expected output for " + program + ".as"

################################################################################################################
#ASSEMBLER TEST 3 (Testing bne, prr, prm)
################################################################################################################

def test_assembler_program3():
    # Program Name
    program = "program3"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])
    
    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the assembler's output matches the expected output
    assert output == expected_output, "Assembler output does not match expected output for " + program + ".as"

################################################################################################################
#ASSEMBLER TEST 4 (Testing bne, prr)
################################################################################################################

def test_assembler_program4():
    # Program Name
    program = "program4"
    
    # Path to the assembler script
    input_path = "as_files_ok/" + program + ".as"
    expected_output_path = "mx_files_ok/" + program + ".mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])

    output = read_file(output_path)
    expected_output = read_file(expected_output_path)
    os.remove(output_path)

    # Assert that the assembler's output matches the expected output
    assert output == expected_output, "Assembler output does not match expected output for " + program + ".as"