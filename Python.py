import serial
import time

# Replace 'COM3' with the correct port
arduino = serial.Serial('COM3', 9600)  
time.sleep(2)  # Allow connection to establish

while True:
    command = input("Enter 'phishing' or 'safe': ").strip().lower()

    if command in ["phishing", "safe"]:
        # Send command with newline character
        arduino.write((command + "\n").encode())
        print(f"Sent: {command}")
        
        # Wait for Arduino to respond
        time.sleep(0.5)  # Ensure the Arduino has time to respond

        while arduino.in_waiting > 0:
            response = arduino.readline().decode().strip()
            print(f"Arduino Response: {response}")
    else:
        print("Invalid input. Enter 'phishing' or 'safe'.")
