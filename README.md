# 🧮 Project 2: The Mighty Python Calculator

*A basic arithmetic calculator in Python that once calculated the exact number of snacks I could eat before my next deadline.*

This isn’t just a calculator. It’s a poetic journey of productivity, procrastination, and processed carbs. With time ticking and hunger rising, this Python script helps determine what truly matters—**how many snacks you can inhale before doom arrives**.

---

## 🎯 Project Summary

**Objective:**  
To develop a playful yet practical Python calculator that:
- Accepts user input for time left before a deadline
- Calculates total snack intake based on user’s snack speed
- Encourages healthy snacking ambition with dramatic flair

**Key Concept:**  
Basic function definition, input handling, loops, and conditional logic.

---

## 🍪 Code Breakdown

```python
def calculate_snacks(time_until_deadline, snack_speed):
```
A noble function. It calculates the snack potential based on:
- `time_until_deadline` (in minutes)
- `snack_speed` (snacks per minute)

---

```python
if snack_speed >= 1:
    total_snacks = time_until_deadline * snack_speed
    return total_snacks
```
If you snack like a champion (1+ per minute), we do the delicious math and deliver the goods.

---

```python
else:
    print("Surely, you're not telling me you can’t manage at least one snack per minute? Up the game!")
    return 0
```
If you fall below the acceptable snacking threshold, the code roasts you with compassion.

---

```python
while True:
```
A never-ending loop—like deadlines, or your craving for cookies.

---

Inside the loop:
- The user inputs time and snack speed.
- The function calculates snack count.
- The total is printed with a toast to your taste.
- You’re asked if you wish to continue this snacking prophecy.

```python
if continue_calc not in ('yes', 'y'):
    print("Very well. Farewell, noble snack enthusiast. May your snacks be ever abundant.")
    break
```
The exit is graceful. The goodbye, heartfelt.

---

## 🧠 Concepts Practiced

- Function creation and return values
- Input casting (`float`)
- String formatting with `f-strings`
- Loops and conditional exits
- Building user-friendly (and snack-friendly) CLI tools

---

## 🛠 Output Example

```
Enter the time left until your deadline (in minutes, obviously): 45  
Enter your snack speed (how many snacks per minute are you capable of?): 1.5  
Voilà! You can consume 67.5 snacks before your deadline. Bon appétit, my snack connoisseur!  
Would you like to perform another snack calculation? (yes/no): no  
Very well. Farewell, noble snack enthusiast. May your snacks be ever abundant.
```

---

## 🍴 Notes & Ideas for Expansion

- Add support for snack types (e.g., pretzels vs. pastries—each with its own difficulty tier)
- Include a timer that warns when the deadline is near (snack urgency intensifies)
- Introduce random snack facts as easter eggs to keep the spirit high

---

## ✨ Final Thoughts

This project is less about arithmetic, more about attitude. It's a microcosm of time management, nutrition, and denial—all wrapped up in Python.

Bon appétit, deadline dodger.
