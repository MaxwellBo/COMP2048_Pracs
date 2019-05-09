from turing_machine import TuringMachine

two = TuringMachine( 
    { 
        ('q0', '0'): ('Expect0', 'd', 'R'),
        ('q0', '1'): ('Expect1', 'd', 'R'),
        ('Expect0', '0'): ('Expect0', '0', 'R'),
        ('Expect0', '1'): ('Expect0', '1', 'R'),
        ('Expect0', '#'): ('Need0', '#', 'R'),
        ('Expect1', '0'): ('Expect1', '0', 'R'),
        ('Expect1', '1'): ('Expect1', '1', 'R'),
        ('Expect0', '#'): ('Need0', '#', 'R'),
        ('Expect0', '#'): ('Need0', '#', 'R'),
    }
)

multiplier.debug('111#111', step_limit=300) # output 1111111111