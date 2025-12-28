from instructionType import InstructionType


class Parser:
	def __init__(self, fileObject):
		self.lines = fileObject.readlines()
		self.lines = [line.strip() for line in self.lines]
		self.lines = [line for line in self.lines
				if line != "" and not line.startswith("//")]
		self.number_of_lines = len(self.lines)
		self.line_index = 0
		return


	def __current_line(self):
		return self.lines[self.line_index]


	def hasMoreLines(self):
		return self.line_index < self.number_of_lines


	def advance(self):
		self.line_index += 1
		return


	def instructionType(self):
		current_line = self.__current_line()
		match current_line[0]:
			case '@':
				return InstructionType.A_INSTRUCTION
			case '(':
				return InstructionType.L_INSTRUCTION
			case default:
				return InstructionType.C_INSTRUCTION


	def symbol(self):
		current_line = self.__current_line()
		match current_line[0]:
			case '@':
				return current_line[1:]
			case '(':
				return current_line[1:-1]
			case default:
				raise Exception("Invalid routine usage.")


	def dest(self):
		current_line = self.__current_line()
		eq_index = current_line.find('=')
		if eq_index > 0:
			return current_line[:eq_index]
		else:
			return ""


	def comp(self):
		current_line = self.__current_line()
		semi_colon_index = current_line.find(';')
		eq_index = current_line.find('=')
		match eq_index:
			case -1:
				return current_line[:semi_colon_index]
			case default:
				if semi_colon_index < 0:
					return current_line[eq_index + 1:]
				else:
					return current_line[eq_index + 1:semi_colon_index]


	def jump(self):
		current_line = self.__current_line()
		semi_colon_index = current_line.find(';')
		if semi_colon_index < 0:
			return None
		return current_line[semi_colon_index + 1:]

