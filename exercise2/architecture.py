NUM_REG = 4  # number of registers
RAM_LEN = 256  # number of words in RAM

OPS = {
    0x1: {"code": "hlt", "fmt": "--"},  # Halt program
    0x2: {"code": "ldc", "fmt": "rv"},  # Load value
    0x3: {"code": "ldr", "fmt": "rr"},  # Load register
    0x4: {"code": "cpy", "fmt": "rr"},  # Copy register
    0x5: {"code": "str", "fmt": "rr"},  # Store register
    0x6: {"code": "add", "fmt": "rr"},  # Add
    0x7: {"code": "sub", "fmt": "rr"},  # Subtract
    0x8: {"code": "beq", "fmt": "rv"},  # Branch if equal
    0x9: {"code": "bne", "fmt": "rv"},  # Branch if not equal
    0xA: {"code": "prr", "fmt": "r-"},  # Print register
    0xB: {"code": "prm", "fmt": "r-"},  # Print memory
    0xC:{"code": "swp", "fmt": "rr"},
    0xD: {"code": "inc", "fmt": "r-"},
    0xE : {"code": "dec", "fmt": "r-"},
}

OP_MASK = 0xFF  # select a single byte
OP_SHIFT = 8  # shift up by one byte
OP_WIDTH = 6  # op width in characters when printing
