const int freq = 5000;
const int ledChannel = 0;
const int resolution = 8;


/////////// variables

unsigned long TimerVel; //tiempo para calculo de velocidad
unsigned long TiempoVelAnterior = 0;// correcto definir en el momento arranca motor
unsigned long TimerAng; //tiempo para calculo de angulo
unsigned int w = 0; // rps  1/s
unsigned long rad = 0;// angulo un spot
int Vel = 50;// velocidad inicial en pwm
unsigned int i = 0;
bool flag = false;
String cad;
////////// pines
const int PinReceptor = 13;// photransistor
const int PinHall = 10;// hall sensor
const int PinMotor = 16;// motor output


//////////config
void setup() {
  Serial.begin(9600);
  delay(30);
  pinMode(PinMotor, OUTPUT);
  pinMode(PinReceptor, INPUT);
  attachInterrupt(digitalPinToInterrupt(PinReceptor), LecturaReceptor, CHANGE);// interrupcion lectura fotrotransistor
  attachInterrupt(digitalPinToInterrupt(PinHall), LecturaVel, CHANGE);// interrupcion lectura hall sensor
  ledcSetup(ledChannel, freq, resolution);
  ledcAttachPin(PinMotor, ledChannel);
}

void loop() {
  if (flag) {
    Agles();
    cad = String(i) + "," + String(rad, 3);//(# beacon, angle desde refent point)
    Serial.println(cad);
    //LecturaReceptor();
    flag = false;
  }
  ControlVel();
  //  for (int i = 0; i <= 255; i++) {// test de pwm en esp32
  //    ledcWrite(ledChannel, i);
  //    delay(25);
  //    Serial.println(i);
  //  }
  //  delay(1000);
  //  for (int i = 255; i >= 0; i--) {
  //    ledcWrite(ledChannel, i);
  //    delay(25);
  //    Serial.println(i);
  //  }
}

void LecturaReceptor() {// llamada por interupcion, lectura de tiempoNow
  TimerAng = millis();
  flag = true;
}

void LecturaVel() {//llamada por interupcion, lectura de velocidad
  TimerVel = millis();
  w = (2 * PI) / (TimerVel - TiempoVelAnterior);
  TiempoVelAnterior = TimerVel;
  i = 0;
}

void ControlVel() {// investigando PID control de motor
  if (TimerVel - TiempoVelAnterior > 200) {// si va mu lento aumenta pwm
    Vel++;
  }
  else if (TimerVel - TiempoVelAnterior < 200 ) {// si va mu rapido disminuye pwm
    Vel--;
  }
  ledcWrite(ledChannel, Vel);//salida pwm
  //analogWrite(PinMotor, Vel); cambiar por ledcwrite()
}

void Agles() {// calculo de angulo llamada poco despues de la interupcion de angulo
  rad = w / (TimerAng - TimerVel);
}
