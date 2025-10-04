# ζητάμε από το χρήστη να καταχωρήσει τις ηλικίες δύο ατόμων
# στη συνέχεια υπολογίζουμε πόσα χρόνια διαφορά έχουν τα δύο άτομα

age_person_1 = input("Καταχώρησε την ηλικία του πρώτου ατόμου: ")
age_person_2 = input("Καταχώρησε την ηλικία του δεύτερου ατόμου: ")

age_difference = int(age_person_1) - int(age_person_2)
age_difference = abs(age_difference)

print("Η διαφορά ηλικίας των δύο ατόμων είναι",age_difference,"χρόνια")