# example_3_3.as

# Reverse array in place
ldc R0 0  # Initialize index i to 0
ldc R1 1  # Initialize index j to (length - 1)

loop_start:
    ldr R2 R0
ldr R3 R1
str R3 R0
str R2 R1
inc R0
dec R1
beq loop_start
hlt
