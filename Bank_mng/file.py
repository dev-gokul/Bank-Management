name="gokul"
f=open(f'{name}.txt',"w")
f.write("testing")
f.close()

f=open(f'{name}.txt',"r")
print(f.read())
f.close()
