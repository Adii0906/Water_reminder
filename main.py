import time
import winsound
try:
    print("Drinking water reminder")
    reminder_interval=int(input("Enter the time in second/hour: "))
    def water_reminder(reminder_interval):
        while True:
            print("Its time to drink water")
            winsound.Beep(1000, 500)  # Play a beep sound (frequency, duration in milliseconds)
            time.sleep(reminder_interval)
    water_reminder(reminder_interval)
except ValueError:
    print("Error: Please enter a valid number for the reminder interval.")
except KeyboardInterrupt:
    print("Reminder stopped.")
except Exception as e:
    print(f"An error occurred: {e}")