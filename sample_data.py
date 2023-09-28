import RPi.GPIO as GPIO
import time
from datetime import datetime
#Date and time


    # Get the current date and time
now = datetime.now()

    # Format the date and time
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Print the date and time
print("Current Date and Time: ", formatted_date_time)

# Use the Broadcom SOC channel numbering scheme
GPIO.setmode(GPIO.BCM)

# Set up input pin (e.g., pin 21)
input_pin = 21
GPIO.setup(input_pin, GPIO.IN)

# Set up output pin (e.g., pin 20)
output_pin = 20
GPIO.setup(output_pin, GPIO.OUT)

try:
    while True:

        #Print Date and time
        now = datetime.now()

        # Format the date and time
        formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Print the date and time
        print("Current Date and Time: ", formatted_date_time)

        # Read from input pin and print value
        input_value = GPIO.input(input_pin)
        print(f"Read {input_value} from input pin {input_pin}")

        # Write to output pin
        GPIO.output(output_pin, GPIO.HIGH)
        print(f"Wrote HIGH to output pin {output_pin}")
        time.sleep(3)

        # Write to output pin
        GPIO.output(output_pin, GPIO.LOW)
        print(f"Wrote LOW to output pin {output_pin}")
        time.sleep(3)

except KeyboardInterrupt:
    # Reset the GPIO pins to a safe state
    GPIO.cleanup()

