from domeniu.entitate import Entitate

def testEntitate():
    entitate = Entitate("1")

    assert entitate.getIdEntitate() == "1"


def testEntitateSetteri():
    entitate = Entitate("2")

    entitate.setIdEntitate("2")
    assert entitate.getIdEntitate() == "2"
