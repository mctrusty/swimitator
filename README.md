swimitator
==========

swimitator

swimitator is a tool for parsing swim-style workouts of the form:

    500 SKIPS
    2 x {
        4 x 50 K @1
        2 x 100 dr @1:45
    }
    10 x 100 K EN3 @1:30
    ...

The idea is to use PLY python lex/yacc to generate a small DSL representing the kind of notation you might use to input a workout.
The output will be tailored toward entering in a database containing information about workouts and sets in order to track
swimming workout information.

