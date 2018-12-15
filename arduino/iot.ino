char response = 0;
//int pin = LED_BUILTIN;
int pin = 5;
int val;
int state;
void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  response=int(Serial.read());
  if(response == '1'){
    digitalWrite(pin, HIGH);
    }
  if(response=='0'){
      digitalWrite(pin, LOW);
      
     }
}
