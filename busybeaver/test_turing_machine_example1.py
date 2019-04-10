from turing_machine import TuringMachine

transitions = {
        ('q0', '#'): ('saw_#', '#', 'R'),
        ('saw_#', '#'): ('saw_##', '#', 'R'),
        ('saw_##', ''): ('qa', '', 'R'),
}

def print_transitions(transition_mapping):
    states = set()

    for (start, finish) in transition_mapping.items():
        (s1, _) = start
        (s2, _, _) = finish

        states.add(s1)
        states.add(s2)

    print("The Turing machine has", len(states), "states:")
    for i in states:
        print(i)
    print()



if __name__ == "__main__":
    print_transitions(transitions)

    # This turing machine accepts only the ## string
    # It rejects on any other input
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w)
        print()

    # SHOULD ACCEPT
    run("##")

    # SHOULD REJECT
    run("#####")

    # SHOULD REJECT
    run("#_#_")