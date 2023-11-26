import subprocess
import os

################################################################################################################
#ASSEMBLER TEST 1
################################################################################################################

def test_assembler_program1():
    # Path to the assembler script
    assembler_path = "../vm/assembler.py"
    input_path = "as_files_ok/program1.as"
    output_path = "AS_test_output_temp.mx"
    expected_output_path = "mx_files_ok/program1.mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, input_path, output_path])
    
    # Ensure the ASSEMBLER output file exists
    assert os.path.exists(output_path), "ASSEMBLER did not create the output file"

    # Read the output from the Assembler
    with open(output_path, "r") as file:
        assembler_output = file.read()
        os.remove(output_path)

    # Read the expected output
    with open(expected_output_path, "r") as file:
        expected_output = file.read()

    # Assert that the assembler's output matches the expected output
    assert assembler_output == expected_output, "Assembler output does not match expected output for program1.as"

################################################################################################################
#ASSEMBLER TEST 2
################################################################################################################

def test_assembler_program2():
    # Path to the assembler script
    assembler_path = "../vm/assembler.py"
    program_path = "as_files_ok/program2.as"
    output_path = "AS_test_output_temp.mx"
    expected_output_path = "mx_files_ok/program2.mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, program_path, output_path])
    
    # Ensure the ASSEMBLER output file exists
    assert os.path.exists(output_path), "ASSEMBLER did not create the output file"

    # Read the output from the Assembler
    with open(output_path, "r") as file:
        assembler_output = file.read()
        os.remove(output_path)

    # Read the expected output
    with open(expected_output_path, "r") as file:
        expected_output = file.read()

    # Assert that the assembler's output matches the expected output
    assert assembler_output == expected_output, "Assembler output does not match expected output for program1.as"

################################################################################################################
#ASSEMBLER TEST 3
################################################################################################################

def test_assembler_program3():
    # Path to the assembler script
    assembler_path = "../vm/assembler.py"
    program_path = "as_files_ok/program3.as"
    output_path = "AS_test_output_temp.mx"
    expected_output_path = "mx_files_ok/program3.mx"
    
    # Run the assembler on program1.as
    subprocess.run(["python", assembler_path, program_path, output_path])

    # Ensure the ASSEMBLER output file exists
    assert os.path.exists(output_path), "ASSEMBLER did not create the output file"

    # Read the output from the Assembler
    with open(output_path, "r") as file:
        assembler_output = file.read()
        os.remove(output_path)

    # Read the expected output
    with open(expected_output_path, "r") as file:
        expected_output = file.read()

    # Assert that the assembler's output matches the expected output
    assert assembler_output == expected_output, "Assembler output does not match expected output for program1.as"