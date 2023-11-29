import subprocess
import os
    
# Arrays path
arrays_path = "../vm/arrays.py"

# VM path
vm_path = "../vm/vm.py"

# Temporary Output Path
output_path = "array_allocation_test_output_temp.txt"
    
################################################################################################################
#OUT OF MEMORY TEST [DONE]
################################################################################################################

def test_vm_out_of_memory():
    # Program Name
    program = "out_of_mem"
    
    # Path to the VM script
    input_path = "as_files_ok/" + program + ".as"

    # Run the VM on the program and save error messages
    result = subprocess.run(["python", arrays_path, input_path, output_path], stderr=subprocess.PIPE, text=True)

    assert result.returncode != 0, "Arrays should have exited with an error"
    assert "AssertionError: Allocation 'array' requires too much memory" in result.stderr

    os.remove(output_path)
    
################################################################################################################
#INSTRUCTION NOT FOUND TEST [DONE]
################################################################################################################

def test_vm_instruction_not_found():
    # Program Name
    program = "inv_inst"
    
    # Path to the VM script
    input_path = "mx_files_ok/" + program + ".mx"

    # Run the VM on the program and save error messages
    result = subprocess.run(["python", vm_path, input_path, output_path], stderr=subprocess.PIPE, text=True)

    assert result.returncode != 0, "VM should have exited with an error"
    assert "Unknown op" in result.stderr
    
    os.remove(output_path)
