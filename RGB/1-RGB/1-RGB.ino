#define s0 4
#define s1 5
#define s2 6
#define s3 7
#define salidaTCS 8

int limiteCapturas = 100; 
int contadorCapturas = 0; 

void setup() {
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(salidaTCS, INPUT);

  digitalWrite(s0, HIGH);
  digitalWrite(s1, LOW);

  Serial.begin(9600);
}

void loop() {

  // Rojo
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  int rojo = pulseIn(salidaTCS, LOW);
  delay(200);

  // Verde
  digitalWrite(s2, HIGH);
  digitalWrite(s3, HIGH);
  int verde = pulseIn(salidaTCS, LOW);
  delay(200);

  // Azul
  digitalWrite(s2, LOW);
  digitalWrite(s3, HIGH);
  int azul = pulseIn(salidaTCS, LOW);
  delay(200);

  // calibracion 
  float R_cal = (-14365/1957) * rojo + (21590/1957) * verde + (-7395/1957 ) * azul;
  float G_cal = (142970/25441) * rojo + (-350710/25441) * verde + (253725/25441) * azul;
  float B_cal = (184790/25441) * rojo + (-44455/25441) * verde + (-73185/25441) * azul;

  R_cal = constrain(R_cal, 0, 255);
  G_cal = constrain(G_cal, 0, 255);
  B_cal = constrain(B_cal, 0, 255);

  Serial.print((int)R_cal);
  Serial.print(",");
  Serial.print((int)G_cal);
  Serial.print(",");
  Serial.println((int)B_cal);
}
