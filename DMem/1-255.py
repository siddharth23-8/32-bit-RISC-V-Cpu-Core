file = open('1to255.txt','w')
file.write("v2.0 raw\n")

din = 0
while int(din) != 255:
    dout = (hex(din))
    file.write(str(dout[2:])+'\n')
    din = 1+din
    
file.close()
