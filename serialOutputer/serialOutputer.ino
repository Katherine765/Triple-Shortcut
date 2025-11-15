int b1 = 2;
int b2 = 7;
int b3 = 13;

void setup() {
    pinMode(b1, INPUT);
    pinMode(b2, INPUT);
    pinMode(b3, INPUT);
    Serial.begin(9600);
}

void loop() {
    Serial.println(String(digitalRead(b1))+String(digitalRead(b2))+String(digitalRead(b3)));
    delay(20);
}
