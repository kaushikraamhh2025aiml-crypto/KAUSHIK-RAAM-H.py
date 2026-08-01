class SimpleReflexAgent:

    def decide_action(self, motion, door, smoke, temperature):

        if smoke:
            return "🔥 Smoke Detected -> Activate Fire Alarm"

        elif motion and door == "Open":
            return "🚨 Intruder Alert -> Notify Owner"

        elif temperature > 40:
            return "❄ High Temperature -> Turn ON Air Conditioner"

        elif motion:
            return "👤 Motion Detected -> Switch ON Lights"

        else:
            return "✅ Everything Normal -> Continue Monitoring"


agent = SimpleReflexAgent()

print("========== SMART HOME SECURITY ==========")

motion = input("Motion detected? (yes/no): ").lower() == "yes"
door = input("Door Status (Open/Closed): ").capitalize()
smoke = input("Smoke detected? (yes/no): ").lower() == "yes"
temperature = float(input("Temperature: "))

print("\nDecision")
print("-----------------------------------")
print(agent.decide_action(motion, door, smoke, temperature))
