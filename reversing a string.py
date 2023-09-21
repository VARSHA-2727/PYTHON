fdr=open("input.txt","r")
fdw=open("output.txt","w")
content=fdr.read()
content_reverse=content[::-1]
fdw.write(content_reverse)
fdr.close()
fdw.close()
