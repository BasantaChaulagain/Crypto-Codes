from single_char_XOR import SingleCharXOR

def main():
	potential_messages=[]
	file=open("4.txt","r")
	lines=file.readlines()
	for line in lines:
		clean_line=line.split("\n")
		potential_messages.append(SingleCharXOR(clean_line[0]).compute())
		best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
	
	print("message: "+ best_score['message'])
	print("score: "+ str(best_score['score']))

if __name__=='__main__':
	main()
