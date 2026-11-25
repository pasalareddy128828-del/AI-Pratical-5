
# Rule-Based Expert System for Health Advisory

print("===================================")
print("   HEALTH EXPERT SYSTEM")
print("===================================")

print("\nAnswer the following questions (yes/no):")

fever = input("Do you have fever? ").lower()
cough = input("Do you have cough? ").lower()
cold = input("Do you have a cold? ").lower()
headache = input("Do you have headache? ").lower()
sneezing = input("Do you have sneezing? ").lower()
body_pain = input("Do you have body pain? ").lower()

print("\n----- DIAGNOSIS RESULT -----")

# Rule 1
if fever == "yes" and cough == "yes" and body_pain == "yes":
    print("Possible condition: Flu")
    print("Advice: Rest, drink fluids and seek medical advice.")

# Rule 2
elif cold == "yes" and sneezing == "yes" and fever == "no":
    print("Possible condition: Common Cold")
    print("Advice: Rest and drink warm fluids.")

# Rule 3
elif fever == "yes" and headache == "yes":
    print("Possible condition: Fever-related illness")
    print("Advice: Monitor temperature and consult a doctor.")

# Rule 4
elif cough == "yes" and cold == "yes":
    print("Possible condition: Respiratory infection")
    print("Advice: Seek medical advice if symptoms continue.")

# Rule 5
elif headache == "yes" and fever == "no":
    print("Possible condition: Headache")
    print("Advice: Rest and drink enough water.")

# Default Rule
else:
    print("Condition not identified.")
    print("Please consult a qualified doctor.")

print("\nThis is only a basic educational expert system.")
print("It does not provide a medical diagnosis.")
