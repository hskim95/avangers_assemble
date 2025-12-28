import re


class Code:
	def dest(self, string):
		bit_A = '1' if string.find('A') >= 0 else '0'
		bit_D = '1' if string.find('D') >= 0 else '0'
		bit_M = '1' if string.find('M') >= 0 else '0'
		return "".join([bit_A, bit_D, bit_M])


	def comp(self, string):
		try:
			z = int(string[-1])
			match z:
				case 0:
					return "0101010"
				case 1:
					return "0111111"
				case -1:
					return "0111010"
		except:
			a = '0' if string.find('M') < 0 else '1'
			c6 = []
			index_D = string.find('D')
			if index_D < 0: # 5-cases
				cx = "11"
				c6.append(cx)
				if string.find('+') >= 0:
					c6.append("0100")
				elif string.endswith('1'):
					c6.append("0010")
				else:
					match string[0]:
						case '!':
							c6.append("0001")
						case '-':
							c6.append("0011")
						case default:
							c6.append("0000")
			else: #10-cases
				zx = '0'
				c6.append(zx)
				if string.endswith("+1"):
					c6.append("11111")
				else:
					if a == '0': # choose A
						if string.endswith("-A"):
							c6.append("10011")
						elif string.endswith("|A"):
							c6.append("10101")
						else:
							nx = '0'
							c6.append(nx)
							if string.startswith("A"):
								c6.append("0111")
							else:
								if string.endswith("A"):
									cy = "00"
									c6.append(cy)
									match string[1]:
										case "+":
											c6.append("10")
										case default:
											c6.append("00")
								else:
									cy = "11"
									c6.append(cy)
									if string.startswith("D"):
										c6.append("00")
									elif string.startswith("!"):
										c6.append("01")
									elif string.startswith("-"):
										c6.append("11")
									else:
										c6.append("10")
					else: # choose M
						if string.endswith("-M"):
							c6.append("10011")
						elif string.endswith("|M"):
							c6.append("10101")
						else:
							nx = '0'
							c6.append(nx)
							if string.startswith('M'): # M-D
								c6.append("0111")
							else:
								if string.endswith('M'):
									cy = "00"
									c6.append(cy)
									match string[1]:
										case '+': # D+A
											c6.append("10")
										case '&': # D&A
											c6.append("00")
								else:
									cy = "11"
									c6.append(cy)
									match string:
										case 'D':
											c6.append("00")
										case "!D":
											c6.append("01")
										case "-D":
											c6.append("11")
										case "D-1":
											c6.append("10")
			return "".join([a, *c6])


	def jump(self, string):
		match string:
			case None:
				return "000"
			case "JGT":
				return "001"
			case "JEQ":
				return "010"
			case "JGE":
				return "011"
			case "JLT":
				return "100"
			case "JNE":
				return "101"
			case "JLE":
				return "110"
			case "JMP":
				return "111"

