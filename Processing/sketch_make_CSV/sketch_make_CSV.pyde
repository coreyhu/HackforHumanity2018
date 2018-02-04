import time
add_library('serial')


def setup():
    print(Serial.list()[-1])
    portName = Serial.list()[-1]
    global myPort
    myPort = Serial(this, portName, 9600)
    global output
    output = createWriter("data.csv")
    global ts
    ts = time.time()


def draw():
    if myPort.available() > 0:
        val = myPort.readStringUntil(13)
        if val:
            output.print((str(time.time() - ts) + "," + val.strip()).strip() + "\n")
            
                    
def keyPressed():
    output.flush()
    output.close()
    exit()