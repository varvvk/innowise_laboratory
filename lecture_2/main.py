def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

user_name = input("Hello! Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {"name": user_name, "age": current_age, "stage": life_stage, "hobbies": hobbies}
print(f"\nProfile summary:\n"
      f"Name: {user_profile.get("name")}\n"
      f"Age: {user_profile.get("age")}\n"
      f"Life stage: {user_profile.get("stage")}")
if not hobbies:
    print("You didn't mention any hobbies")
else:
    print(f"Favorite hobbies ({len(hobbies)}): ")
    for hobby in hobbies:
        print(f"- {hobby}")