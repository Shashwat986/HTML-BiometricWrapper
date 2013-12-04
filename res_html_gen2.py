import sys
import glob
import os
import string

try:
	basepath = sys.argv[1]
except:
	basepath = "./s1"

try:
	outfile = sys.argv[2]
except:
	outfile = "test.html"

out = open(outfile,'w')
out.write('<html>\n<body>\n<h1>Foreign Body Detection in Ear</h1>\n<table border="1" style="font-size:100%">\n')
out.write('<tr align=center>\n')
ctr=0
for file in glob.glob(basepath+"/*"):
	if (os.path.isfile(file) and string.lower(file.split(".")[-1])=='jpg'):
		print file
		print basepath+"/"+file
		out.write('<td><img src="'+file+'" height="270" width="200" /><br/>'+file.split('.')[-2].split('\\')[1]+'</td>\n')
		ctr+=1
	if ctr==6:
		ctr=0
		out.write('</tr>\n<tr align=center>\n')

out.write("</tr>")
out.write('</table>\n')
out.write('<div align=right><em>Made by Shashwat Chandra.</em></div>')	# Comment out this code if you don't want to recognize Shashwat's hard work
out.write('</body>\n</html>\n')
out.close()