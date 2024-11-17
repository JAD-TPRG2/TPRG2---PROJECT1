from vending_machine_JAD import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    # new machine object
    vending = VendingMachine()
    # add states
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())

    # Reset state is "waitng for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'

    # add a toonie
    vending.event = '200' # a toonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200

    # add a loonie
    vending.event = '100' # a loonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 300

    # add a quarter
    vending.event = '25' # a quarter
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 325

    # add a dime
    vending.event = '10' # a dime
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 335

    # add a nickel
    vending.event = '5' # a nickel
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 340
