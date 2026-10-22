from hello1 import register_patient


def test_register_patient_alice():
    result = register_patient("Alice", 25)
    expected = "New Registration → Patient Alice, Age: 25"
    assert result == expected


def test_register_patient_john():
    result = register_patient("John", 30)
    expected = "New Registration → Patient John, Age: 30"
    assert result == expected
