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


class BinaryToHex:
	def __init__(self, bin_):
		self.bin_=bin_
		self.keylist = []
		self.hex_=""
		
	def table(self, key):
		switch={
			"0000" : "0",
			"0001" : "1",
			"0010" : "2",
			"0011" : "3",
			"0100" : "4",
			"0101" : "5",
			"0110" : "6",
			"0111" : "7",
			"1000" : "8",
			"1001" : "9",
			"1010" : "A",
			"1011" : "B",
			"1100" : "C",
			"1101" : "D",
			"1110" : "E",
			"1111" : "F"
		}
		return switch[key]

	def convert(self):
		for key in self.hex_:
			self.bin_+=self.table(key)
		return self.bin_

	def normalize(self):
		if len(self.bin_)%4 == 2:
			self.bin_ = "00" + self.bin_

	def chunkstring(self, string, length):
		for i in range(0, len(string), length):
			self.keylist.append(string[0+i: length+i])

	def convert(self):
		self.normalize()
		self.chunkstring(self.bin_, 4)
		for key in self.keylist:
			self.hex_ += self.table(key)
		return self.hex_
