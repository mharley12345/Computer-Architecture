
"""CPU functionality."""

import sys

# Hardcoding variables for branch table
LDI = 0b10000010
PRN = 0b01000111

HLT = 0b00000001



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256  # Ram with size of 256 bytes
        self.reg = [0] * 8
        # Below are Internal Registers
        self.pc = 0  # Program Counter
        self.ir = "00000000"
        # Added instructions set
        self.instruction = {}
        self.instruction[LDI] = self.handle_LDI
        self.instruction[PRN] = self.handle_PRN
      


# Functions for RAM read/write


    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self, program):
        """Load a program into memory."""

        address = 0
        # For now, we've just hardcoded a program:

        program = [
             # From print8.ls8
             0b10000010,  # LDI R0,8
             0b00000000,
             0b00001000,
             0b01000111,  # PRN R0
             0b00000000,
             0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
     
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def handle_LDI(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
        self.pc += 3

    def handle_PRN(self, operand_a, operand_b):
        print(f"Print to Console - {self.reg[operand_a]}")
        self.pc += 2


    def run(self):
        """Run the CPU."""
        # Perform REPL style execution
        running = True
        # Before the loop starts, initialize stack pointer
       # self.reg[SP] = 0xF4
        while running:
            # Start the CPU. start storing instructions in IR
            self.ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)

         
            if self.ir == HLT:
                running = False
                break
            # try to engage the reads from program and excecute instructions
            try:
                self.instruction[self.ir](operand_a, operand_b)
            except:
                print(f"Error: Unknown Command {self.ir}")
                sys.exit(1)

