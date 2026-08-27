def test_ejemplo_basico():
    resultado = 1 + 1
    if resultado != 2:
        raise AssertionError("El resultado no es correcto")
