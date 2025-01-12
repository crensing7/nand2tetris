# Concepts
## Gates
- NAND
- NOT
- AND
- OR
- NOR
- XOR
## Composite
- Mux
    - Chooses between two inputs
- DMux 
    - Chooses between two outputs
## Adder
- Half
    - Adds two binary numbers, outputs sum and carry bit
    - Uses XOR + AND
- Full
    - Adds two binary strings given carry bit
    - Uses XOR + AND + MUX + NOT + OR
- Adder
    - Full addition sequence with Half and Full Adders
- ALU
    - Takes two inputs and six control bits to perform specified operation
    - Uses ADDER, NOT, AND, MUX, OR
## Time
- SRLatch
    - Latch that holds value and can be set or reset
    - Uses NAND
- DLatch
    - Variant of SRlatch that prevent double input
    - Uses NAND, NOT
- DFF (D Flip-Flop)
    - Combination of two D latches that remembers the previous state through clock cycle
    - Uses DLATCH, NOT
- Bit
    - Stores one value forever until instructed to load another value
- Register
    - Stores an array of bits that perform that same functionality
- RAM
    - An array of registers than can be addressed individually
- Counter
    - Register that can increment, load a value, reset, or output the current state
    - Used for keeping track of ALU instructions
## Machine Languages
- Elements
    - Instruction
    - Counter
    - Address
        - Read
        - Write 
### Memory
- Hierarchy
    - Registers
    - Cache
    - RAM
    - Disk
- Address Modes
    - Register
        - Add R1, R2
    - Direct
        - Add R1, M[200]
    - Indirect
        - Add R1, @A
    - Immediate
        - Add 73, R1

# Hack
- Data Memory (RAM)
- Instruction Memory (ROM)
- Central Processing Unit (CPU)
- Bus
    - Instruction
    - Data
    - Address
- Language
    - 16-bit A-instruction
        - Sets the A register to value
        - RAM[A] becomes the selected RAM register
    - 16-bit C-instructions
        - destination = computation ; jump
        - computation
            - ALU input
        - destination
            - null, M, D, MD, A, AM, AD, AMD
- Control
    - ROM loaded with program
    - Reset button pressed
    - Program begins running
- Registers
    - A register
        - 16-bit value for address 
    - D register
        - 16-bit value for data
    - M register
        - 16-bit RAM register addressed by A 
## Instruction
- A instruction
    - 0[000000000000000]
- C instruction
    - 1[xx][acccccc][ddd][jjj]
        - a bit controls A or M register
        - c bits control the operation begin performed
        - d bits
            - Null | 000
            - M    | 001
            - D    | 010
            - MD   | 011
            - A    | 100
            - AM   | 101
            - AD   | 110
            - AMD  | 111
        - j bits
            - Null | 000
            - JGT  | 001
            - JEQ  | 010
            - JGE  | 011
            - JLT  | 100
            - JNE  | 101
            - JLE  | 110
            - JMP  | 111
## Programming
- Branching
    - Controlled by jump command
    - Labels for jumps are translated in assembler
        - Declarations are not translated
    - Each reference to a label is replaced with a reference to the instruction number following that label's declaration
- Variables
    - @temp
        - CPU will find available memory unit and assign address to temp
    - Reference to a symbol that has no corresponding label declaration is treated as a reference to a variable
    - Variables are allocated to the RAM from address 16 onward

# Central Processing Unit
- 16-bits
- Executes the current instruction
    - Takes program written in some level languauge and transforms it into reality
- Determines which instruction is to be executed next
## Interface
- CPU connected to instruction memory and data memory
- INPUT
    - (16) [inM]         Data Value
    - (16) [instruction] Instruction
    - (01) [reset]       Reset Bit
- OUTPUT
    - (16) [outM]        Data Value
    - (01) [writeM]      Write?
    - (15) [addressM]    Memory Address
    - (15) [pc]          Next instruction
## Architecture
- Instruction Handling
    - A
        - Decode
            - Op-Code
            - 15-bit Value
        - Stores the value in A register
    - C
        - Decode
            - Op-Code
            - ALU Control bits
            - Destination Load bits
            - Jump bits
- ALU
    - Inputs
        - D-register
        - A-register/M-register
        - Control bits
    - Outputs
        - Destination bits
            - D, A, M register 
        - Control
            - Negative
            - Zero
- Control
    - Program Counter
        - Emits the address of the next instruction
        - Can be reset to 0 to restart the program
- Operation
    - If instruction contains D and A
        - Read from D, A register
    - If instruction is @x
        - x is stored in the A register
        - Value emitted by addressM
    - If instruction contains M on RIGHT
        - Value is read from inM
    - If instruction contains M on LEFT
        - ALU output emitted by outM
        - writeM bit is asserted
    - If jump, PC set to A-register
        - Else increment PC 
- Memory
    - Address [0 - 16383]
        - 16K RAM
        - Data Memory
    - Address [16384 - 24575]
        - 8K RAM
        - Screen Memory
    - Address [24576]
        - Register
        - Keyboard Memory
- ROM
    - Takes address returns instruction















