from calculatrice import addition, multiplication, division

def test_addition():
    """Teste la fonction addition"""
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    print("✅ Test addition réussi!")

def test_multiplication():
    """Teste la fonction multiplication"""
    assert multiplication(3, 4) == 12
    assert multiplication(5, 0) == 0
    assert multiplication(-2, 3) == -6
    print("✅ Test multiplication réussi!")

def test_division():
    """Teste la fonction division"""
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(5, 0) == "Erreur: division par zéro!"
    print("✅ Test division réussi!")

if __name__ == "__main__":
    print("🧪 Lancement des tests...")
    test_addition()
    test_multiplication()
    test_division()
    print("🎉 Tous les tests sont passés!")
