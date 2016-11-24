import urllib

def read_text():
	quotes = open("/Users/huangheting/Desktop/profanity.txt")
	contents_of_file=quotes.read()
	# print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	#google's website should be connect via vpn
	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) 
	output=connection.read()
	# print(output)
	connection.close()
	if "true" in output:
		print("profanity alert!")
	elif "false" in output:
		print("this document has no curse word!")
	else:
		print("could not scan the document properly.")


read_text()