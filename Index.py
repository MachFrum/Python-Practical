# Function to calculate the number of snacks one can consume before the inevitable deadline
def calculate_snacks(time_until_deadline, snack_speed):
    # Let’s be honest here, if you can’t eat at least one snack per minute, we need to re-evaluate life choices
    if snack_speed >= 1:
        # The math is simple: how many snacks can you devour in the time you have left? Let’s do some high-calorie arithmetic.
        total_snacks = time_until_deadline * snack_speed
        return total_snacks
    else:
        # If snack speed is too slow, you’ll be dining in despair... and hunger. Adjust your snack intake, darling.
        print("Surely, you're not telling me you can’t manage at least one snack per minute? Up the game!")
        return 0

# And thus, the loop continues... like an epic tale of snacking and deadlines.
while True:
    # The user, contemplating the fate of their impending deadline, must now input the time left.
    time_until_deadline_input = float(input("Enter the time left until your deadline (in minutes, obviously): "))
    
    # Now, for the most crucial of all data: How quickly can you snack? A true test of one’s abilities.
    snack_speed_input = float(input("Enter your snack speed (how many snacks per minute are you capable of?): "))

    # Call the calculate_snacks function—here we combine time, skill, and snack-loving ambition.
    total_snacks = calculate_snacks(time_until_deadline_input, snack_speed_input)

    # Deliver the result with an air of grace and a touch of culinary sophistication
    print(f"Voilà! You can consume {total_snacks} snacks before your deadline. Bon appétit, my snack connoisseur!")

    # A true intellectual would ask: “Shall we continue this gastronomic calculation?”
    continue_calc = input("Would you like to perform another snack calculation? (yes/no): ").strip().lower()
    
    # Only the truly determined answer yes. Should you opt out, well, I’ll gracefully exit.
    if continue_calc not in ('yes', 'y'):
        print("Very well. Farewell, noble snack enthusiast. May your snacks be ever abundant.")
        break  # And with that, the snack saga ends—until next time, of course.

