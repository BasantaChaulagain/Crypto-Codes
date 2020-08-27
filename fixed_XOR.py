from hex_binary import HexToBinary, BinaryToHex

_xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}

def xor(x, y):
	# return ''.join([_xormap[a, b] for a, b in zip(x, y)])
	return ''.join([chr(ord(i)^ord(j)) for i, j in zip(x, y)])


def main():
	hex1 = raw_input("Enter first number: ")
	hex2 = raw_input("Enter second number: ")

	bin1 = HexToBinary(hex1.upper()).convert()
	bin2 = HexToBinary(hex2.upper()).convert()

	xored = xor(bin1, bin2)
	hex3 = BinaryToHex(xored).convert().lower()

	print("The XOR of the two numbers is\n{}".format(xored))


if __name__ == "__main__":
	main()