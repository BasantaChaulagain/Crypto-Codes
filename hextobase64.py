class HexToBinary:
	def __init__(self, hex_):
		self.hex_=hex_
		self.bin_=""
		
	def table(self, key):
		switch={
			"0": "0000",
			"1": "0001",
			"2": "0010",
			"3": "0011",
			"4": "0100",
			"5": "0101",
			"6": "0110",
			"7": "0111",
			"8": "1000",
			"9": "1001",
			"A": "1010",
			"B": "1011",
			"C": "1100",
			"D": "1101",
			"E": "1110",
			"F": "1111"
		}
		return switch[key]

	def convert(self):
		for key in self.hex_:
			self.bin_+=self.table(key)
		return self.bin_


class BinToBase64:
	def __init__(self, bin_):
		self.bin_ = bin_
		self.keylist = []
		self.base64 = ""

	def table(self, key):
		switch = {
			"000000" : "A",
			"000001" : "B",
			"000010" : "C",
			"000011" : "D",
			"000100" : "E",
			"000101" : "F",
			"000110" : "G",
			"000111" : "H",
			"001000" : "I",
			"001001" : "J",
			"001010" : "K",
			"001011" : "L",
			"001100" : "M",
			"001101" : "N",
			"001110" : "O",
			"001111" : "P",
			"010000" : "Q",
			"010001" : "R",
			"010010" : "S",
			"010011" : "T",
			"010100" : "U",
			"010101" : "V",
			"010110" : "W",
			"010111" : "X",
			"011000" : "Y",
			"011001" : "Z",
			"011010" : "a",
			"011011" : "b",
			"011100" : "c",
			"011101" : "d",
			"011110" : "e",
			"011111" : "f",
			"100000" : "g",
			"100001" : "h",
			"100010" : "i",
			"100011" : "j",
			"100100" : "k",
			"100101" : "l",
			"100110" : "m",
			"100111" : "n",
			"101000" : "o",
			"101001" : "p",
			"101010" : "q",
			"101011" : "r",
			"101100" : "s",
			"101101" : "t",
			"101110" : "u",
			"101111" : "v",
			"110000" : "w",
			"110001" : "x",
			"110010" : "y",
			"110011" : "z",
			"110100" : "0",
			"110101" : "1",
			"110110" : "2",
			"110111" : "3",
			"111000" : "4",
			"111001" : "5",
			"111010" : "6",
			"111011" : "7",
			"111100" : "8",
			"111101" : "9",
			"111110" : "+",
			"111111" : "/"
		}
		return switch[key]

	def normalize(self):
		if len(self.bin_)%6 == 2:
			self.bin_ = "0000" + self.bin_
		
		if len(self.bin_)%6 == 4:
			self.bin_ = "00" + self.bin_

	def chunkstring(self, string, length):
		for i in range(0, len(string), length):
			self.keylist.append(string[0+i: length+i])

	def convert(self):
		self.normalize()
		self.chunkstring(self.bin_, 6)
		for key in self.keylist:
			self.base64 += self.table(key)
		return self.base64


def main():
	hex_ = raw_input("Enter a hex code: ")
	toBinary = HexToBinary(hex_.upper())
	binary = toBinary.convert()
	# print ("binary of hex is: {}".format(binary))

	tobase64 = BinToBase64(binary)
	base64 = tobase64.convert()
	print ("Hexadecimal: {}\nBase64: {}".format(hex_, base64))


if __name__=="__main__":
	main()