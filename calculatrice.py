def addition(a, b):
    """Additionne deux nombres"""
    return a + b

def multiplication(a, b):
    """Multiplie deux nombres"""
    return a * b

def division(a, b):
    """Divise deux nombres"""
    if b == 0:
        return "Erreur: division par zéro!"
    return a / b

# Programme principal
if __name__ == "__main__":
    print("=== Calculatrice ===")
    print(f"5 + 3 = {addition(5, 3)}")
    print(f"4 × 6 = {multiplication(4, 6)}")
    print(f"10 ÷ 2 = {division(10, 2)}")
    print("Programme terminé avec succès!")
