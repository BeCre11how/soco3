from disassembler import Disassembler
import pytest

@pytest.fixture
def disassembler():
    return Disassembler()

def test_write_to_file(disassembler):

    f = open('../exercise2/testcode_machine.mx', 'r')
    output = open('../exercise2/testcode_output.as', 'w')
    disassembler._disassemble(f.read().strip().split('\n'), output)
    output.close()
    f.close()
    with open('../exercise2/testcode_human.as', 'r') as file:
        expectedc = file.read()
        expectedl = expectedc.split()

    with open('../exercise2/testcode_output.as', 'r') as file:
        outputc = file.read()
        outputl = outputc.split()

    assert expectedl == outputl

@pytest.mark.parametrize("input_line, expected_output", [
    ("000001", ['hlt', '', '']),
    ("020002", ['ldc', "R0", 2]),
    ("010003", ['ldr', 'R0', 'R1']),
    ("020104", ['cpy', 'R1', 'R2']),
    ("030205", ['str', 'R2', 'R3']),
    ("010006", ['add', "R0", 'R1']),
    ("020007", ['sub', 'R0', 'R2']),
    ("020108", ['beq', 'R1', '@Loop2']),
    ("010009", ['bne', 'R0', '@Loop3']),
    ("00030A", ['prr', 'R3', '']),
    ("00000B", ['prm', 'R0', '']),
    ("02010C", ['swp', 'R1', 'R2']),
    ("00030D", ['inc', 'R3', '']),
    ("00020E", ['dec', 'R2', ''])
])
def test_disassemble_line(disassembler, input_line, expected_output):
    result = disassembler._disassemble_line(input_line)
    assert result == expected_output

def test_translate_params(disassembler):
    result = disassembler._Disassembler__translate_params(3)
    assert result == "R3"

