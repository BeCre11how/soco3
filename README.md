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


### Task (B)
- `test_B_vm.py`: Main file for this task; containing extensive tests on the `vm.py`.

### Task (C)
- `test_C.py`: Main file for this task; containing selected tests on `arrays.py` and `vm.py`.

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

## 3 New features and Problems - Assembler

## 4 New features - Debugger