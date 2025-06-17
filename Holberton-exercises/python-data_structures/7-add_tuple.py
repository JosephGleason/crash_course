#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        tuple1 = tuple_a[0]
    else:
        tuple1 = 0
        
    if len(tuple_a) > 1:
        tuple2 = tuple_a[1]
    else:
        tuple2 = 0

    if len(tuple_b) > 0:
        tuple3 = tuple_b[0]
    else:
        tuple3 = 0
        
    if len(tuple_b) > 1:
        tuple4 = tuple_b[1]
    else:
        tuple4 = 0

    return (tuple1 + tuple3, tuple2 + tuple4)
