from parser import Parser
from instructionType import InstructionType
from code import Code
import sys


class SymbolTable:
	symbol_table = {}
	def __init__(self):
		for i in range(0, 16):
			self.addEntry(f"R{i}", i)
			self.addEntry("SP", 0)
			self.addEntry("LCL", 1)
			self.addEntry("ARG", 2)
			self.addEntry("THIS", 3)
			self.addEntry("THAT", 4)
			self.addEntry("SCREEN", 16384)
			self.addEntry("KBD", 24576)


	def addEntry(self, symbol, address):
		self.symbol_table[symbol] = address


	def contains(self, symbol):
		return symbol in self.symbol_table


	def getAddress(self, symbol):
		return self.symbol_table[symbol]


arguments = sys.argv[1:]
address_ready = 16

code = Code()
symbol_table = SymbolTable()

with open(f"{arguments[0]}", 'r', encoding="utf-8") as fr:
	parser = Parser(fr)
	label_count = 0
	while parser.hasMoreLines():
		inst_type = parser.instructionType()
		match inst_type:
			case InstructionType.L_INSTRUCTION:
				label_count += 1
				symbol = parser.symbol()
				if not symbol_table.contains(symbol):
					position = parser.line_index + 1 - label_count
					symbol_table.addEntry(symbol, position)
		parser.advance()


with open(arguments[0], 'r', encoding="utf-8") as fr:
	with open(arguments[0].replace("asm", "hack"), 'w', encoding="utf-8") as fw:
		parser = Parser(fr)
		hack_lines = []
		while parser.hasMoreLines():
			inst_type = parser.instructionType()
			if inst_type == InstructionType.C_INSTRUCTION:
				comp = parser.comp()
				dest = parser.dest()
				jump = parser.jump()
				bit_comp = code.comp(comp)
				bit_dest = code.dest(dest)
				bit_jump = code.jump(jump)

				hack_line = "".join(["111", bit_comp, bit_dest, bit_jump])
				hack_lines.append(hack_line)
			elif inst_type == InstructionType.A_INSTRUCTION:
				symbol = parser.symbol()
				if not symbol_table.contains(symbol):
					symbol_table.addEntry(symbol, address_ready)
					address_ready += 1
				address = symbol_table.getAddress(symbol)
				hack_line = f"{address:016b}"
				hack_lines.append(hack_line)
			parser.advance()
		fw.write('\n'.join(hack_lines))

