#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"/Users/huangheting/Desktop/secret_message")
	
	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))

rename_files()