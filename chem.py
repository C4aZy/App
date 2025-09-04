# Computational Chemistry Learning Tool
# Author: C4aZy
# Description: Interactive CLI for basic computational chemistry calculations and explanations

import re

# Periodic table (symbol: atomic mass)
PERIODIC_TABLE = {
	'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011,
	'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305,
	'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.948,
	'K': 39.098, 'Ca': 40.078, 'Fe': 55.845, 'Cu': 63.546, 'Zn': 65.38, 'Ag': 107.87,
	'Au': 196.97, 'Pb': 207.2, 'Sn': 118.71, 'I': 126.90, 'Br': 79.904, 'Mn': 54.938,
	'Cr': 51.996, 'Ni': 58.693, 'Co': 58.933, 'Ti': 47.867, 'V': 50.942, 'Mo': 95.95,
	# Add more elements as needed
}

def parse_formula(formula):
	print("""
	Parses a chemical formula and returns a dictionary of element counts.
	Example: H2O -> {'H': 2, 'O': 1}
	""")
	pattern = r'([A-Z][a-z]?)(\d*)'
	matches = re.findall(pattern, formula)
	elements = {}
	for (element, count) in matches:
		count = int(count) if count else 1
		elements[element] = elements.get(element, 0) + count
	return elements

def calculate_molecular_weight(formula):
	elements = parse_formula(formula)
	total_weight = 0.0
	explanation = []
	for element, count in elements.items():
		atomic_mass = PERIODIC_TABLE.get(element)
		if atomic_mass is None:
			explanation.append(f"Element '{element}' not found in periodic table.")
			continue
		subtotal = atomic_mass * count
		explanation.append(f"{element}: {count} x {atomic_mass} = {subtotal}")
		total_weight += subtotal
	explanation.append(f"Total molecular weight: {total_weight}")
	return total_weight, explanation


def main_menu():
	print("\nWelcome to Computational Chemistry Learning Tool!")
	print("Select an option:")
	print("1. Calculate molecular weight")
	print("2. Balance a chemical reaction")
	print("3. Stoichiometry calculator")
	print("4. Learn quantum chemistry basics")
	print("5. Exit")
	choice = input("Enter your choice (1-5): ")
	return choice


# --- Reaction Balancer ---
def balance_reaction(equation):
	# Simple balancer for equations like H2 + O2 -> H2O
	# For learning: explain the steps
	# This is a stub for educational purposes
	explanation = ["Balancing reactions is about making sure the number of atoms of each element is the same on both sides."]
	explanation.append(f"You entered: {equation}")
	explanation.append("This tool currently supports simple reactions. For complex reactions, use advanced chemistry software.")
	# Not a real balancer, just a placeholder
	return equation, explanation

# --- Stoichiometry Calculator ---
def stoichiometry():
	print("\nStoichiometry Calculator")
	print("Calculate moles, mass, or limiting reactant.")
	formula = input("Enter chemical formula: ")
	weight, explanation = calculate_molecular_weight(formula)
	print("Molecular weight calculation:")
	for step in explanation:
		print(step)
	moles = float(input("Enter number of moles: "))
	mass = moles * weight
	print(f"Mass = moles x molecular weight = {moles} x {weight} = {mass} grams")
	print("You can use this to convert between moles and mass.")

# --- Quantum Chemistry Basics ---
def quantum_basics():
	print("\nQuantum Chemistry Basics")
	print("- Atoms are made of protons, neutrons, and electrons.")
	print("- Electrons occupy orbitals (s, p, d, f).")
	print("- Electron configuration example: Oxygen (O): 1s2 2s2 2p4")
	print("- The arrangement of electrons determines chemical properties.")
	print("- Quantum numbers: n (principal), l (angular), m (magnetic), s (spin)")
	print("- Learn more: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Quantum_Chemistry_and_Spectroscopy")

def run():
	while True:
		choice = main_menu()
		if choice == '1':
			formula = input("Enter chemical formula (e.g., H2O, CO2): ")
			weight, explanation = calculate_molecular_weight(formula)
			print("\nStep-by-step calculation:")
			for step in explanation:
				print(step)
		elif choice == '2':
			equation = input("Enter reaction (e.g., H2 + O2 -> H2O): ")
			balanced, explanation = balance_reaction(equation)
			print("\nReaction balancing steps:")
			for step in explanation:
				print(step)
			print(f"Balanced equation (stub): {balanced}")
		elif choice == '3':
			stoichiometry()
		elif choice == '4':
			quantum_basics()
		elif choice == '5':
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	run()
