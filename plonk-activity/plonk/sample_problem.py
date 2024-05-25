from .copy_constraint import find_permutation
from .constraint import add_mul_constarint, add_add_constarint, add_constant_constraint

def gen_witness():
    # Prove that we know (x, y, z) such that x^2 + y^2 = z^2
    x = 3
    y = 4
    z = 5

    a = [x, y, x*x, y*y, z*z, x*x + y*y]
    b = [x, y, 1, 1, 1, 1]
    c = [x*x, y*y, x*x, y*y, z*z, z*z]

    return (a, b, c)


def is_satisfied_witness(a, b, c):
    assert a[0] * b[0] == c[0]
    assert a[1] * b[1] == c[1]
    assert a[2] * b[2] == c[2]
    assert a[3] * b[3] == c[3]
    assert a[4] * b[4] == c[4]
    assert a[5] == c[5]


def gen_constraints():
    # Prove that we know (x, y, z) such that x^2 + y^2 = z^2

    Ql = []
    Qr = []
    Qm = []
    Qo = []
    Qc = []

    # set constraints
    Ql, Qr, Qm, Qo, Qc = add_mul_constarint(Ql, Qr, Qm, Qo, Qc)  # x * x = x^2
    Ql, Qr, Qm, Qo, Qc = add_mul_constarint(Ql, Qr, Qm, Qo, Qc)  # y * y = y^2
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 1)  # 1
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 1)  # 1
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 1)  # 1
    Ql, Qr, Qm, Qo, Qc = add_add_constarint(Ql, Qr, Qm, Qo, Qc)  # x^2 + y^2 = z^2

    return (Ql, Qr, Qm, Qo, Qc)


def gen_copy_constraints():
    # copy constraints
    # a = [x, y, x*x, y*y, z*z, x*x + y*y]
    # b = [x, y, 1, 1, 1, 1]
    # c = [x*x, y*y, x*x, y*y, z*z, z*z]
    # inputs = [x, y, x*x, y*y, z*z, x*x + y*y,
    #           x, y, 1, 1, 1, 1,
    #           x*x, y*y, x*x, y*y, z*z, z*z]

    copy_constraints = [0, 6, 12, 1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 16, 5, 11, 17]

    eval_domain = range(0, len(copy_constraints))

    x_a_prime = find_permutation(copy_constraints[0:6], eval_domain[0:6])
    x_b_prime = find_permutation(copy_constraints[6:12], eval_domain[6:12])
    x_c_prime = find_permutation(copy_constraints[12:18], eval_domain[12:18])

    return (x_a_prime, x_b_prime, x_c_prime, copy_constraints)


def setup():
    Ql, Qr, Qm, Qo, Qc = gen_constraints()
    perm_x, perm_y, perm_z, copy_constraints = gen_copy_constraints()

    return (Ql, Qr, Qm, Qo, Qc, perm_x, perm_y, perm_z, copy_constraints)
