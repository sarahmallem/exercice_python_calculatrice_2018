def display_menu():
    print("*****************************************")
    print("* Calculatrice en Python  *")
    print("*****************************************")
    print("1 ou + pour l'addition")
    print("2 ou - pour la soustraction")
    print("3 ou * pour la multiplication")
    print("4 ou / pour la division")
    print("5 ou ^ pour la puissance")
    print("6 ou sqrt pour la racine carrée")
    print("7 pour Quitter")
    print("*****************************************")

def select_operation():
    display_menu()
    try:
        operation_choice = input("Opération (numéro ou symbole): ")
        if operation_choice not in ['1', '+', '2', '-', '3', '*', '4', '/', '5', '^', '6', 'sqrt', '7']:
            print("Choix invalide. Veuillez entrer un numéro d'opération valide ou un symbole.")
            return select_operation()
        return operation_choice
    except ValueError:
        print("Entrée non valide. Veuillez entrer un numéro ou un symbole.")
        return select_operation()

def run_calculator():
    while True:
        try:
            chosen_operation = select_operation()

            if chosen_operation in ['7', 'q', 'quit', 'exit']:
                print("Fin du programme.")
                break

            if chosen_operation in ['6', 'sqrt']:
                value = float(input("Entrez un nombre: "))
                if value < 0:
                    print("La racine carrée d'un nombre négatif n'est pas définie dans les réels.")
                    continue
                result = value ** 0.5
                print(f"Le résultat est: {result}")
            else:
                # Pour les autres opérations, demander deux nombres
                first_number = float(input("Entrez le premier nombre: "))
                second_number = float(input("Entrez le second nombre: "))

                # Traiter les différentes opérations
                if chosen_operation in ['1', '+']:
                    result = first_number + second_number
                elif chosen_operation in ['2', '-']:
                    result = first_number - second_number
                elif chosen_operation in ['3', '*']:
                    result = first_number * second_number
                elif chosen_operation in ['4', '/']:
                    if second_number == 0:
                        print("Erreur: Division par zéro.")
                        continue
                    result = first_number / second_number
                elif chosen_operation in ['5', '^']:
                    result = first_number ** second_number

                print(f"Le résultat est: {result}")

            user_choice = input("Voulez-vous effectuer une autre opération ? (oui/non) ")
            if user_choice.lower() not in ['oui']:
                print("Fin du programme.")
                break

        except Exception as e:
            print("Vous ne pouvez pas faire cela.")


run_calculator()
