#include <WebServer.h>

#include <WiFi.h>

#define ledGreen 27
#define ledWhite 25

WebServer server(80);

const char *ssid = "Umbalaxibua";
const char *pass = "Nh23102000";

void setup() {
  Serial.begin(115200);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledWhite, OUTPUT);
  WiFi.begin(ssid, pass);
  // WiFi.softAPConfig(local_ip, gateway, subnet);
  while(WiFi.status() != WL_CONNECTED){
    // digitalWrite(ledWhite,1);
    // delay(1000);
    // digitalWrite(ledWhite,0);
    // delay(1000);
  }
  Serial.print("AP IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/ongreen", onGreen);
  server.on("/offgreen", offGreen);
  server.on("/onwhite", onWhite);
  server.on("/offwhite", offWhite);
  
  server.begin();
  Serial.println("HTTP server started");
}

void handleRoot(){
  server.send(200, "text/plain", "WELCOME TO ESP32 WEBSERVER!!");
}

void onGreen(){
  digitalWrite(ledGreen,1);
  server.send(200, "text/plain", "GREEN LED WAS ON!!");
}

void offGreen(){
  digitalWrite(ledGreen,0);
  server.send(200, "text/plain", "GREEN LED WAS OFF!!");
}

void onWhite(){
  digitalWrite(ledWhite,1);
  server.send(200, "text/plain", "WHITE LED WAS ON!!");
}

void offWhite(){
  digitalWrite(ledWhite,0);
  server.send(200, "text/plain", "WHITE LED WAS OFF!!");
}

void loop() {
  server.handleClient();
  // digitalWrite(ledGreen,1);
  // delay(1000);
  // digitalWrite(ledGreen,0);
  // delay(1000);

}