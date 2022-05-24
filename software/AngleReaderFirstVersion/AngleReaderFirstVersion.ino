const int freq = 5000;
const int ledChannel = 0;
const int resolution = 8;


/////////// variables

unsigned long TimerVel; //tiempo para calculo de velocidad
unsigned long TiempoVelAnterior = 0;// correcto definir en el momento arranca motor
unsigned long TimerAng; //tiempo para calculo de angulo
unsigned int dt = 0;
double w = 205; // rps  1/s
float rad = 0;// angulo un spot
int Vel = 240;// velocidad inicial en pwm
unsigned int i = 0;
bool flag = false;
bool Flagv = false;
String cad;
bool p = true;
int c0 = 0;
int c1 = 0;
int c2 = 0;
int v = 0;
int beacon = 0;
//int nSensorV = 1;

////////// pines
const int PinReceptor = 13;// photransistor
const int PinHall = 26;// hall sensor
const int PinMotor = 16;// motor output
const int ledR = 25;
const int ledG = 14;
const int ledB = 27;

///////FUNCIONS



//////////config
void setup() {
  Serial.begin(9600);
  delay(30);
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(PinMotor, OUTPUT);
  pinMode(PinReceptor, INPUT);
  digitalWrite(ledR, HIGH); //LOGICA ESTA INVERTIDA HIGH ES OFF
  digitalWrite(ledG, HIGH);
  digitalWrite(ledB, HIGH);
  attachInterrupt(digitalPinToInterrupt(PinReceptor), LecturaReceptor, FALLING);// interrupcion lectura fotrotransistor
  attachInterrupt(digitalPinToInterrupt(PinHall), LecturaVel, FALLING);// interrupcion lectura hall sensor
  ledcSetup(ledChannel, freq, resolution);
  ledcAttachPin(PinMotor, ledChannel);
  delay(500);
  ControlVel();
}

void loop() {
  if (flag) {
    Agles();
    cad = String(beacon) + "," + String(rad, 3);//(# beacon, angle desde refent point)
    Serial.println(cad);
    //LecturaReceptor();
    flag = false;
  }
  v++;
  if (!Flagv and v > 100) {
    digitalWrite(ledR, p);
    digitalWrite(ledG, HIGH);
    digitalWrite(ledB, HIGH);
    p = !p;
    v = 0;
  }
  if (Flagv) {
    switch (i) {//error programing
      case 0:
        c0++;
        if (c0 > 4) {
          digitalWrite(ledR, LOW);
          digitalWrite(ledG, HIGH);
          digitalWrite(ledB, HIGH);
          c1 = 0;
          c2 = 0;
        }
        break;
      case 1:
        c0 = 0;
        c1++;
        if (c1 > 4) {
          digitalWrite(ledR, LOW);
          digitalWrite(ledG, LOW);
          digitalWrite(ledB, HIGH);
          c2 = 0;
        }
        break;
      case 2:
        c0 = 0;
        c1 = 0;
        c2 ++ ;
        if (c2 > 4) {
          digitalWrite(ledR, HIGH);
          digitalWrite(ledG, LOW);
          digitalWrite(ledB, HIGH);
        }
        break;
      default:
        digitalWrite(ledR, HIGH);
        digitalWrite(ledG, HIGH);
        digitalWrite(ledB, LOW);
        break;

    }
    Flagv = false;
  }
  //delay(10);

  
  //    for (int i = 0; i <= 255; i++) {// test de pwm en esp32
  //      ledcWrite(ledChannel, i);
  //      delay(25);
  //      Serial.println(i);
  //    }
  //    delay(1000);
  //    for (int i = 255; i >= 0; i--) {
  //      ledcWrite(ledChannel, i);
  //      delay(25);
  //      Serial.println(i);
  //    }
}

void LecturaReceptor() {// llamada por interupcion, lectura de tiempoNow
  TimerAng = millis();
  beacon++;
  flag = true;
}

void LecturaVel() {//llamada por interupcion, lectura de velocidad ??IRAM_ATTR
  TimerVel = millis();
  dt = (TimerVel - TiempoVelAnterior);// / nSensorV;
  if (dt > 30)w = 6.2831/(dt*1000);
  TiempoVelAnterior = TimerVel;
  beacon = 0;
  v = 0;
  Flagv = true;
  //  Serial.println(w);
  //    Serial.print("vel: ");
  //  Serial.println(Vel);

  //  digitalWrite(ledG, p);
  //  p = !p;
}

void ControlVel() {// investigando PID control de motor
  //    if (w > 200 and Vel < 255) {// si va mu lento aumenta pwm
  //      Vel++;
  //    }
  //    else if (w < 200 and Vel > 100) {// si va mu rapido disminuye pwm
  //      Vel--;
  //    }
  ledcWrite(ledChannel, Vel);//salida pwm
  //analogWrite(PinMotor, Vel); cambiar por ledcwrite()

}

void Agles() {// calculo de angulo llamada poco despues de la interupcion de angulo
  rad =w * (TimerAng - TimerVel);
}
