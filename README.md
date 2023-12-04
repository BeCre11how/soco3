# README file for all files for assignment 3
## 1 Unit Testing
### File Structure
- exercise1/
  - pytest.ini
  - .coveragerc
  - as_files_ok/
    - program1.as
    - program2.as
    - ...
  - mx_files_ok/
    - program1.mx
    - program2.mx
    - ...
  - vm_outputs_ok/
    - program1.txt
    - program2.txt
    - ...
  - tests/
    - environment.py
    - test_A_assembler.py
    - test_B_vm.py
    - test_C.py

### Files
- `exercise1/`: The directory where all the files for the first part of the assignment are stored.
- `pytest.ini`: Configuration file for `pytest`; sets `--cov` as default argument for entire directory, allows coverage report to be called with just `pytest`.
- `.coveragerc`: Configuration file `pytest coverage`; specifies the line coverage and which lines are to be excluded.
- `as_files_ok/`: A directory containing correct `.as` files used to test `assembler.py` on specific instructions.
- `mx_files_ok/`: A directory containing correct `.mx` files used to compare the `assembler.py` output with and to test `vm.py` on specific instructions.
- `vm_outputs_ok/`: A directory containing correct `.txt` files used to compare the `vm.py` output with.
- `test/`: A directory containing all the test files that are ran using the `pytest` command.
- `environment.py`: A file to define Python version; `python` as default; change to `python3` if needed.
- `test_A_assembler.py`: A file containing tests that are ran on `assembler.py`.
- `test_B_vm.py`: A file containing tests that are ran on `vm.py`.
- `test_C.py`: A file containing all tests that are ran on `array.py` and `vm.py`.

### Pytest
The `pytest` testing framework has been implemented.
From inside this task directory `exercise 1/` all tests will be run returning a test coverage report.
`pytest` has been configured to use `--cov` as a default argument when called using `pytest` from the command line.

- `pytest.ini`: Configuration file for `pytest`.

Usage (from command line):
- Inside the `exercise 1` directory:
    `pytest`
- Not inside the `exercise 1` directory:
    `pytest [file path to 'exercise 1/']`

Further explanation under # Task (D)

### Task (A)
- `test_A_assembler.py`: Main file for this task; containing extensive tests on the `assembler.py`.
This is the test suite for the assembler. It contains test for the functionality and correctness of the assembler.
It imports the `subprocess` and `os` modules and environment from `environment.py` that defines the default python version.

It uses the assembler at location `../vm/assembler.py` and test files in the `as_files_ok/` directory and compares them to corresponding files from `mx_files_ok/`. 

Tests
- `test_assembler_program_output`: Checks if the assembler creates an output file for a basic program.
- `test_assembler_program_ex`: Tests a specific example program from the lecture, comparing its output against expected output.
- `test_assembler_program1 to test_assembler_program5`: Each function tests different sets of assembly instructions, ensuring that the assembler handles various instructions correctly.

Missing
- Additional tests for new instructions implemented in later tasks of assignment.

### Task (B)
- `test_B_vm.py`: Main file for this task; containing extensive tests on the `vm.py`.
This is the test suite for the vm. It contains test for the functionality and correctness of the vm.
It imports the `subprocess` and `os` modules and environment from `environment.py` that defines the default python version.

It uses the assembler at location `../vm/vm.py` and test files in the `mx_files_ok/` directory and compares them to corresponding files from `vm_outputs_ok/`. 

Tests
- `test_vm_program_output`: Checks if the assembler creates an output file for a basic program.
- `test_vm_program_ex`: Tests a specific example program from the lecture, comparing its output against expected output.
- `test_vm_program1 to test_vm_program5`: Each function tests different sets of vm instructions, ensuring that the vm handles various instructions correctly.

Missing
- Additional tests for new instructions implemented in later tasks of assignment.

### Task (C)
- `test_C.py`: Main file for this task; containing selected tests on `arrays.py` and `vm.py`.
This is a test suite for the vm.py and arrays.py.
It imports the `subprocess` and `os` modules and environment from `environment.py` that defines the default python version.

- `test_vm_out_of_memory`: This test runs an instance of arrays.py with a `.as`-file that tries allocate space that exceeds the maximum memory. The test checks for the error message `AssertionError: Allocation 'array' requires too much memory`.
- `test_vm_instruction_not_found`: This test runs an instance of vm.py with a `.mx`-file that contains an invalid instruction. The test checks if the error message contains `Unknown op`.

### Task (D)
Test coverage is reported in % for all tests when ran using `pytest` from the `exercise 1` directory.
Line coverage is configured within the `.coveragerc` file in the `exercise 1/` directory.

The files to be reported are defined in `source`: all files inside the `../vm/` directory.
Comment-out the `omit`-section to omit coverage for `arrays.py` (which is not completely to be tested from Task 1 in this assignment).

Lines to be excluded from the coverage report are the following:
- Lines that are just `pass`: Unless specifically desired should be excluded.
- Lines with just a docstring or `pragma: no cover`: Usefully if selected lines should be excluded (used during solving of further tasks).
- Lines with defensive programming assertions: All lines that are not ran when files are called from tests.

## 2 Disassembler
The disassembler serves as a translator from machine code back to human-readable assembly code. It is specifically designed to work with the architecture defined in `architecture.py`, which includes operation IDs, register numbers and values.

### Usage
To use the disassembler, run it from the terminal, using the following command:
`python disassemble.py input_file.mx output_file.as` with
- `input_file.mx`: The machine code file to be disassembled.
- `output_file.as`: The assembly code file where the disassembled output will be written.

### Functionality
The disassembler performs the following steps:

1. Reads the machine code instructions from the input file.
2. Processes the instructions, identifying operation codes, registers, values and loops.
3. Converts the machine code to assembly code.
4. Writes the disassembled output to the specified output file.

### Features
- Loop Detection: Recognizes and adds loop labels for instructions ending with specific values (0x9 or 0x8).
- Parameter Translation: Translates register numbers to assembly code format (e.g., R1).
- Output Formatting: Writes the disassembled output with proper formatting.

### Testing
The disassembler was thoroughly tested on its functionalities using pytest. This can be done via terminal the same way as in exercise 1:
1. Head to directory "exercise2": `cd exercise2`
2. Run the tests: `pytest`

## 3 New features and Problems - Assembler
In the exercise 3 subdirectory one can find the files for the tasks described below. To run the files and see examples produced by the new operation:
- `python ../vm/assembler.py desired_example.as desired_assembler_output.mx` followed by
- `python ../vm/vm.py desired_assembler_output.mx desired_vm_output.txt`
For exercise 3.3, replace `assembler.py` with `arrays.py`.

### 3.1 Increment and decrement
The assembly language now has the following two additional commands:
- `inc` increases the value stored at the specified register by 1
- `dec` decreases the values stored at the specified register by 1

How to use it, format is r- (Register, nothing):
- inc R1
- dec R2

### 3.2 Swap values
The assembly language now has the following additional feature:
- `swp` swaps the two values at the specified addresses

How to use it, format is rr (Register, Register):
- swp R1 R2

### 3.3 Reverse array in place
How the program works:
1. Sets the length of the array. The user can choose the length of at most the number specified in line 81.
2. Initializes the array consisting of the numbers from the array length to 1 and prints it simultaneously.
3. Uses 4 registers for swapping: 2 registers with indices and 2 storage registers.
4. Loads values of head- and tailpointer and swaps them.
5. Increases headpointer by one.
6. Checks break condition for even array length.
7. Decreases the tailpointer by one.
8. Checks break condition for odd array length.
9. Prints reversed array.

How to use it:
- Specify the desired array length in line 4 of the code (replace the "14")
- Convert and run the program as described above.

## 4 New features - Debugger
to run the debugger you have different options, run `vm_step.py` for `4.1`, `vm_extend.py` for `4.3`, and `vm_break.py` for `all` features
one additional note, when vm_base or vm_step is run, command have to be specified by either only the initial char of the method or the entire name

### Usage(bash):
Inside the `debugger` directory:
- `python desired_level.py desired_program.mx`

### 4.1 Show Memory range
with this feature the user now has 3 options:
- print entire memory
- print memory at certain address
- print the range from initial address to end address including end

to achieve the above described behaviour the user can for example run `m`, for option 1,
`m 2` for option 2 and `m 2 10` for option 3

### 4.2 Breakpoint Addresses 
For this feature to be enabled the user needs to run the vm_break.py. The user now has the following options:
- set a breakpoint at the specified address if no address specified ip taken as address
- clear a breakpoint at the specified address

to run this feature the user only has to specify `b 2`, to set a breakpoint at address 2, or `c 2`, to clear a breakpoint at address 2

### 4.3 Command Completion
Only vm_extend.py has to be run, it also works with vm_break.py. The user can now type any leading matching characters of the commands he wants to execute
and the vm takes care of it.
The user can choose from the following options:
- `disassemble` writes the disassembled command at the address location
- `ip` shows the ip, can also be seen on the very left of console
- `memory` shows memory(more in 4.1)
- `quit` quits the vm
- `run` runs the program
- `step` executes the next step of the program
- `break` sets a breakpoint at the specified address(more in 4.2)
- `clear` clears a breakpoint at the specified address(more in 4.2)
- `watchpoint` sets a watchpoint at the specified address(more in 4.4)
- `erasewatchpoint` deletes the watchpoint at that address(more in 4.4)

For example if the user wants to run `memory`, he can achieve that by running `m`, `me`, `mem`

### 4.4 Watchpoints
For this to be enabled one needs to run vm_break.py. The user can now watch value at certain memory address or register address:
- set a watchpoint at the specified address, if the address is smaller than both register and ram size, a new watchpoint for both register and memory at that address is set if no address specified ip taken as address
- erase watchpoint deletes the before set watchpoint, both if both were set

To run this the user can specify `w 20`, to set an address at position 20, and `e 20` to delete a watchpoint at address 20