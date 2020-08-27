class RepeatingKey:
	def __init__(self, input_bytes):
		self.input_bytes=input_bytes
		self.key="ICE"

	def single_char_xor(self, char_value):
		output_bytes = b''
		for byte in bytearray(self.input_bytes):
			output_bytes += bytearray([byte ^ char_value])
		return output_bytes

	def compute(self):
		max_length=len(self.input_bytes)
		res=""
		for i in range(max_length):
			res+=self.single_char_xor(bytearray(self.key[i%3].encode("ascii"))[0])
		print res.decode("ascii")

def main():
	input_bytes="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	instance=RepeatingKey(input_bytes.encode("ascii"))
	instance.compute()

if __name__=='__main__':
	main()