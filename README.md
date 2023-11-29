### README file for all files for assignment 3
## 1 Unit Testing
# File Structure
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

# Files
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

# Task (A)

# Task (B)

# Task (C)

# Task (D)




## 2 Disassembler

## 3 New features and Problems - Assembler

## 4 New features - Debugger