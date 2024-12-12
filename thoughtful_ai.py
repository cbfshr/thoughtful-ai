# Thoughtful AI - Robotic Automation Factory - Main
import robotic_automation_factory

# Main Function
def main():
    print("Welcome to Thoughtful’s Robotic Automation Factory!")

    # Simple Test cases
    print(robotic_automation_factory.sort(2, 3, 4, 15))
    print(robotic_automation_factory.sort(151, 3, 4, 15))
    print(robotic_automation_factory.sort(2, 3, 4.0, 20))
    print(robotic_automation_factory.sort(2.1, 999, 4, 42))

if __name__ == "__main__":
    main()
