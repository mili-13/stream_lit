# Define remedies, procedures, and dosage guidelines
remedies_data = {
    "headache": {
        "remedies": [
            {"name": "Ginger Tea", "description": "Boil ginger slices in water for 10 minutes and drink.",
             "dosage": "1-2 cups daily as needed."},
            {"name": "Peppermint Oil Massage", "description": "Apply diluted peppermint oil on temples and massage gently.",
             "dosage": "Use 2-3 times a day."}
        ],
        "acupressure": "Apply pressure to the base of the skull and temples."
    },
    "cold": {
        "remedies": [
            {"name": "Honey and Lemon Tea", "description": "Mix honey and lemon in hot water and drink.",
             "dosage": "1 cup, 2-3 times a day."},
            {"name": "Steam Inhalation", "description": "Inhale steam from hot water with a few drops of eucalyptus oil.",
             "dosage": "5-10 minutes, 2-3 times a day."}
        ],
        "acupressure": "Press the area between the thumb and index finger."
    },
    # Add more conditions and remedies here
}

dosage_guidelines = {
    "child": "1/2 the adult dosage.",
    "adult": "Standard dosage.",
    "elderly": "Consult a doctor for personalized dosage."
}

def get_age_group(age):
    """Determine the age group for dosage guidelines."""
    if age < 18:
        return "child"
    elif age < 65:
        return "adult"
    else:
        return "elderly"

def provide_remedies(problem, age_group):
    """Provide remedies and procedures based on the problem and age group."""
    if problem in remedies_data:
        remedies = remedies_data[problem]['remedies']
        acupressure = remedies_data[problem]['acupressure']
        
        print(f"Remedies for {problem}:")
        for remedy in remedies:
            print(f"- {remedy['name']}: {remedy['description']}")
            print(f"  Dosage: {remedy['dosage']}")
        
        print(f"\nAcupressure Technique: {acupressure}")
        
        dosage = dosage_guidelines.get(age_group, "Consult a doctor for personalized dosage.")
        print(f"\nDosage Guidelines: {dosage}")
    else:
        print("Sorry, we don't have information for this problem.")

def main():
    print("Welcome to the Health Remedies and Dosage App!")
    problem = input("Please describe your problem (e.g., headache, cold): ").strip().lower()
    age = int(input("Please enter your age: "))
    
    age_group = get_age_group(age)
    
    print("\nFetching remedies and dosage information...")
    provide_remedies(problem, age_group)

if __name__ == "__main__":
    main()
