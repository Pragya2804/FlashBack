void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(8,INPUT); //8 camera1
  pinMode(7,INPUT); //7 camera2
  pinMode(4,INPUT); // Assign
  pinMode(6,INPUT); //Recall
  pinMode(5,INPUT); //Recall click

}
int count1=0;
int count2=0;
int count3=0;
int count4=0;
int count5=0;
void loop() {
  // put your main code here, to run repeatedly:
  int z=digitalRead(7);
  int y=digitalRead(8);
  int x=digitalRead(4);
  int a=digitalRead(6);
  int b=digitalRead(5);
  if (x==1){
    Serial.println(1);
  }
 else if (y==1){
    Serial.println(2);
  }
  else if (z==1){
    Serial.println(3);
    }
  else if (a==1){
    Serial.println(4);
    }
  else if (b==1){
    Serial.println(5);
   }
    else{
     Serial.println(0);
   }

}
