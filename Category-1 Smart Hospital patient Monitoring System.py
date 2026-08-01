class ModelBasedAgent:

    def __init__(self):
        self.previous_status = "Normal"

    def evaluate(self, heart_rate, oxygen, temperature):

        if oxygen < 90 or heart_rate > 120 or temperature > 39:
            current_status = "Critical"

        elif oxygen < 95 or heart_rate > 100:
            current_status = "Warning"

        else:
            current_status = "Normal"

        print("\nPrevious Status :", self.previous_status)
        print("Current Status  :", current_status)

        if self.previous_status == "Warning" and current_status == "Critical":
            action = "🚑 Call Emergency Medical Team"

        elif current_status == "Critical":
            action = "⚠ Immediate Doctor Notification"

        elif current_status == "Warning":
            action = "👨‍⚕ Increase Patient Monitoring"

        else:
            action = "✅ Patient Stable"

        self.previous_status = current_status

        return action


agent = ModelBasedAgent()

print("=========== SMART HOSPITAL ===========")

while True:

    print("\nEnter Patient Details")

    hr = int(input("Heart Rate : "))
    oxygen = int(input("Oxygen Level : "))
    temp = float(input("Temperature : "))

    print(agent.evaluate(hr, oxygen, temp))

    choice = input("\nContinue? (yes/no): ")

    if choice.lower() != "yes":
        break
