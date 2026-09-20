def to_binary_label(grade):
    if grade >= 2:
        return "referable_dr"

    return "non_referable_dr"