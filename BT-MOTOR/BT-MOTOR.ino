#include <PS2X_lib.h>  //for MOEBIUS
#include "FaBoPWM_PCA9685.h"

// Código feito pela MOEBIUS, fornecedor da base Mecanum, fiz algumas alterações para compatibilização.

//#include "servo.hpp"

FaBoPWM faboPWM;
int pos = 290;
int posi = 0;
//int SERVO_PIN9 = 9; //490Hz
//int SERVO_PIN6 = 6; //980Hz
int MAX_VALUE = 2000;   // 电机速度限制
int MIN_VALUE = 300;

#define DIRA1 0
#define DIRA2 1
#define DIRB1 2
#define DIRB2 3
#define DIRC1 4
#define DIRC2 5
#define DIRD1 6
#define DIRD2 7
#define WEBCAM 8

//电机控制，前进、后退、停止
#define MOTORA_FORWARD(pwm)    do{faboPWM.set_channel_value(DIRA1,pwm);faboPWM.set_channel_value(DIRA2, 0);}while(0)
#define MOTORA_STOP(x)         do{faboPWM.set_channel_value(DIRA1,0);faboPWM.set_channel_value(DIRA2, 0);}while(0)
#define MOTORA_BACKOFF(pwm)    do{faboPWM.set_channel_value(DIRA1,0);faboPWM.set_channel_value(DIRA2, pwm);}while(0)

#define MOTORB_FORWARD(pwm)    do{faboPWM.set_channel_value(DIRB1,pwm);faboPWM.set_channel_value(DIRB2, 0);}while(0)
#define MOTORB_STOP(x)         do{faboPWM.set_channel_value(DIRB1,0);faboPWM.set_channel_value(DIRB2, 0);}while(0)
#define MOTORB_BACKOFF(pwm)    do{faboPWM.set_channel_value(DIRB1,0);faboPWM.set_channel_value(DIRB2, pwm);}while(0)

#define MOTORC_FORWARD(pwm)    do{faboPWM.set_channel_value(DIRC1,pwm);faboPWM.set_channel_value(DIRC2, 0);}while(0)
#define MOTORC_STOP(x)         do{faboPWM.set_channel_value(DIRC1,0);faboPWM.set_channel_value(DIRC2, 0);}while(0)
#define MOTORC_BACKOFF(pwm)    do{faboPWM.set_channel_value(DIRC1,0);faboPWM.set_channel_value(DIRC2, pwm);}while(0)

#define MOTORD_FORWARD(pwm)    do{faboPWM.set_channel_value(DIRD1,pwm);faboPWM.set_channel_value(DIRD2, 0);}while(0)
#define MOTORD_STOP(x)         do{faboPWM.set_channel_value(DIRD1,0);faboPWM.set_channel_value(DIRD2, 0);}while(0)
#define MOTORD_BACKOFF(pwm)    do{faboPWM.set_channel_value(DIRD1,0);faboPWM.set_channel_value(DIRD2, pwm);}while(0)

#define SERIAL  Serial

//#define SERIAL  Serial3

#define LOG_DEBUG

#ifdef LOG_DEBUG
#define M_LOG SERIAL.print
#else
#define M_LOG 
#endif

//PWM参数
#define MAX_PWM   2000
#define MIN_PWM   300

int Motor_PWM = 1300;
 
//控制电机运动    宏定义
//    ↑A-----B↑   
//     |  ↑  |
//     |  |  |
//    ↑C-----D↑
void ADVANCE(uint8_t pwm_A,uint8_t pwm_B,uint8_t pwm_C,uint8_t pwm_D)
{
  MOTORA_BACKOFF(Motor_PWM);MOTORB_FORWARD(Motor_PWM);    
  MOTORC_BACKOFF(Motor_PWM);MOTORD_FORWARD(Motor_PWM);    
}

//    ↓A-----B↓ 
//     |  |  |
//     |  ↓  |
//    ↓C-----D↓
void BACK()
{
  MOTORA_FORWARD(Motor_PWM);MOTORB_BACKOFF(Motor_PWM);
  MOTORC_FORWARD(Motor_PWM);MOTORD_BACKOFF(Motor_PWM);
}
//    =A-----B↑   
//     |   ↖ |
//     | ↖   |
//    ↑C-----D=
void LEFT_1()
{
  MOTORA_STOP(Motor_PWM);MOTORB_FORWARD(Motor_PWM);
  MOTORC_BACKOFF(Motor_PWM);MOTORD_STOP(Motor_PWM);
}

//    ↓A-----B↑   
//     |  ←  |
//     |  ←  |
//    ↑C-----D↓
void LEFT_2()
{
  MOTORA_FORWARD(Motor_PWM);MOTORB_FORWARD(Motor_PWM);
  MOTORC_BACKOFF(Motor_PWM);MOTORD_BACKOFF(Motor_PWM);
}
//    ↓A-----B=   
//     | ↙   |
//     |   ↙ |
//    =C-----D↓
void LEFT_3()
{
  MOTORA_FORWARD(Motor_PWM);MOTORB_STOP(Motor_PWM);
  MOTORC_STOP(Motor_PWM);MOTORD_BACKOFF(Motor_PWM);
}
//    ↑A-----B=   
//     | ↗   |
//     |   ↗ |
//    =C-----D↑
void RIGHT_1()
{
  MOTORA_BACKOFF(Motor_PWM);MOTORB_STOP(Motor_PWM);
  MOTORC_STOP(Motor_PWM);MOTORD_FORWARD(Motor_PWM);
}
//    ↑A-----B↓   
//     |  →  |
//     |  →  |
//    ↓C-----D↑
void RIGHT_2()
{
  MOTORA_BACKOFF(Motor_PWM);MOTORB_BACKOFF(Motor_PWM);
  MOTORC_FORWARD(Motor_PWM);MOTORD_FORWARD(Motor_PWM);
}
//    =A-----B↓   
//     |   ↘ |
//     | ↘   |
//    ↓C-----D=
void RIGHT_3()
{
  MOTORA_STOP(Motor_PWM);MOTORB_BACKOFF(Motor_PWM);
  MOTORC_FORWARD(Motor_PWM);MOTORD_STOP(Motor_PWM);
}

//    ↑A-----B↓   
//     | ↗ ↘ |
//     | ↖ ↙ |
//    ↑C-----D↓
void rotate_1()  //tate_1(uint8_t pwm_A,uint8_t pwm_B,uint8_t pwm_C,uint8_t pwm_D) 
{
  MOTORA_BACKOFF(Motor_PWM);MOTORB_BACKOFF(Motor_PWM);
  MOTORC_BACKOFF(Motor_PWM);MOTORD_BACKOFF(Motor_PWM);
}

//    ↓A-----B↑   
//     | ↙ ↖ |
//     | ↘ ↗ |
//    ↓C-----D↑
void rotate_2()  // rotate_2(uint8_t pwm_A,uint8_t pwm_B,uint8_t pwm_C,uint8_t pwm_D)
{
  MOTORA_FORWARD(Motor_PWM);MOTORB_FORWARD(Motor_PWM);
  MOTORC_FORWARD(Motor_PWM);MOTORD_FORWARD(Motor_PWM);
}
//    =A-----B=  
//     |  =  |
//     |  =  |
//    =C-----D=
void STOP()
{
  MOTORA_STOP(Motor_PWM);MOTORB_STOP(Motor_PWM);
  MOTORC_STOP(Motor_PWM);MOTORD_STOP(Motor_PWM);
}

void WEBCAM_CIMA()
{
  if(pos <= 420)
  {
    posi = pos - 10;
    do {
     posi = posi + 1;
     faboPWM.set_channel_value(WEBCAM, posi); 
     delay(15);   
    } while(pos!=posi);
  } else {
    pos = pos - 10;
  }
}


void WEBCAM_BAIXO()
{
  if(pos >= 290)
  {
    posi = pos + 10;
    do {
     posi = posi - 1;
     faboPWM.set_channel_value(WEBCAM, posi); 
     delay(15);   
    } while(pos!=posi);
  } else {
    pos = pos + 10;
  }
}


//串口输入控制
void UART_Control()
{
  char Uart_Date=0;
  if(SERIAL.available())
  {
    Uart_Date = SERIAL.read();
  }
  switch(Uart_Date)
  {
     case 'E':  ADVANCE(1500,1500,1500,1500);  M_LOG("Run!\r\n"); break;
     case 'D':  RIGHT_1();  M_LOG("Right up!\r\n");       break;
     case 'C':  rotate_2(); M_LOG("Left rotation!\r\n");  break;      
     case 'B':  RIGHT_3();  M_LOG("Right down!\r\n");     break;
     case 'A':  BACK();     M_LOG("Run Back!\r\n");       break;
     case 'F':  LEFT_3();   M_LOG("Left down!\r\n");      break;
     case 'G':  rotate_1(); M_LOG("Right rotation!\r\n"); break;         
     case 'H':  LEFT_1();   M_LOG("Left up!\r\n");        break;
     case 'Z':  STOP();     M_LOG("Stop!\r\n");           break;
     case 'z':  STOP();     M_LOG("Stop!\r\n");           break;
     case 'b':  LEFT_2();   M_LOG("Left!\r\n");           break;
     case 'd':  RIGHT_2();  M_LOG("Right!\r\n");          break;
     case 'L':  pos = pos + 10; WEBCAM_CIMA(); Serial.println(pos); M_LOG("WEBCAM CIMA\r\n");     break;
     case 'M':  pos = pos - 10; WEBCAM_BAIXO(); Serial.println(pos); M_LOG("WEBCAM BAIXO\r\n");      break;     
//     case 'L':  analogWrite(SERVO_PIN9, 50);  M_LOG("WEBCAM+\r\n");     break;
//     case 'M':  analogWrite(SERVO_PIN9, 150);  M_LOG("WEBCAM-\r\n");      break;
//     case 'L':  Motor_PWM = 1500; STOP();  M_LOG("1500\r\n");     break;
//     case 'M':  Motor_PWM = 1000;  STOP();  M_LOG("1000\r\n");      break;     
   }
}

void IO_init()
{
  STOP();
}

void setup()
{
  SERIAL.begin(9600);
  IO_init();
  if(faboPWM.begin()) 
  {
    Serial.println("Find PCA9685");
    faboPWM.init(300);
  }
  faboPWM.set_hz(50);
  SERIAL.print("Start");
//  pinMode(SERVO_PIN9, OUTPUT);
//  pinMode(SERVO_PIN6, OUTPUT);
  faboPWM.set_channel_value(WEBCAM, pos);
}



void loop()
{
    UART_Control();//串口接收处理 
    //CAR_Control();//小车控制
}
