import processing.serial.*;

Serial myPort;  // Create object from Serial class
String val;     // Data received from the serial po
PrintWriter output;
int AT_REST = 200;
boolean movement_detected = false;
int kickedCounter = -1;
void setup()
{
  String portName = Serial.list()[3]; 
  //change the 0 to a 1 or 2 etc. to match your port
  myPort = new Serial(this, portName, 9600); 
  output = createWriter("HFH EMG.txt");
}
int parse(String src)
{
    int start = 0; // where to start iterating
    boolean negative = false; // negative or not
    switch (src.charAt(0))
    {
        case '-':
            negative = true;
            start = 1;
            break;
        case '+':
            start = 1;
            break;
        // default: do nothing
    }
    int number = 0;
    for (int i = start; i < src.length(); i++)
    {
        number = number * 10 + Character.digit(src.charAt(i), 10);
    }
    if (negative)
    {
        number = -number;
    }
    number = number / 100 + 1;
    return number;
}
void draw()
{
  if ( myPort.available() > 0) 
  {  // If data is available,  
  String val = myPort.readStringUntil('\n'); 
  if (val != null)
  {
    output.print(val);
    int value = parse(val);
    if(value > AT_REST){
      if(!movement_detected){
              kickedCounter += 1;
              println("Kicked" + kickedCounter);
              movement_detected = true;
      }
    }
    else{
      movement_detected = false;
    }

  // read it and store it in val
  }  
  }
}

void keyPressed() {
    output.flush();  // Writes the remaining data to the file
    output.close();  // Finishes the file
    exit();  // Stops the program
}