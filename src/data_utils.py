"""Validation shared by dataset inspection and split generation."""

from numbers import Real


def to_binary_label(grade):
    """Map an integer IDRiD grade in [0, 4] to the project's binary target."""
    if isinstance(grade, bool) or not isinstance(grade, Real):
        raise ValueError("Retinopathy grade must be an integer from 0 to 4")
    if not 0 <= grade <= 4 or int(grade) != grade:
        raise ValueError("Retinopathy grade must be an integer from 0 to 4")
    return "referable_dr" if grade >= 2 else "non_referable_dr"


def validate_labels(labels):
    """Reject missing or duplicate identifiers and invalid grades before splitting."""
    required = {"Image name", "Retinopathy grade"}
    if not required.issubset(labels.columns) or labels.empty:
        raise ValueError("Labels must contain image names and retinopathy grades")
    names = labels["Image name"]
    if (
        names.isna().any()
        or not names.map(
            lambda name: isinstance(name, str) and bool(name.strip())
        ).all()
    ):
        raise ValueError("Image names must be non-empty strings")
    if names.duplicated().any():
        raise ValueError("Image names must be unique")
    labels["Retinopathy grade"].map(to_binary_label)
