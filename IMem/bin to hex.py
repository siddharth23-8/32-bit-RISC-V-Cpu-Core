file = open('cont.txt','w')

file.write("v2.0 raw\n")

din = input()
while int(din) != -1:
    dout = (hex(int(din, 2)))
    file.write(str(dout[2:])+'\n')
    din = input()
    
file.close()
