from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_utils import to_binary_label, validate_labels

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TRAIN_LABELS = (
    PROJECT_ROOT
    / "data/raw/idrid/B. Disease Grading/2. Groundtruths"
    / "a. IDRiD_Disease Grading_Training Labels.csv"
)

SPLITS_DIRECTORY = PROJECT_ROOT / "data/splits"

HOLDOUT_LABELS = (
    PROJECT_ROOT
    / "data/raw/idrid/B. Disease Grading/2. Groundtruths"
    / "b. IDRiD_Disease Grading_Testing Labels.csv"
)

VALIDATION_SIZE = 0.20
RANDOM_STATE = 42


def main():
    development_labels = pd.read_csv(
        TRAIN_LABELS,
        usecols=["Image name", "Retinopathy grade"],
    )

    validate_labels(development_labels)

    holdout_labels = pd.read_csv(
        HOLDOUT_LABELS, usecols=["Image name", "Retinopathy grade"]
    )
    validate_labels(holdout_labels)
    if set(development_labels["Image name"]) & set(holdout_labels["Image name"]):
        raise ValueError("Development and holdout splits contain overlapping images")
    holdout_labels["target"] = holdout_labels["Retinopathy grade"].map(to_binary_label)
    holdout_labels = holdout_labels.sort_values("Image name").reset_index(drop=True)

    development_labels["target"] = development_labels["Retinopathy grade"].map(
        to_binary_label
    )

    train_labels, validation_labels = train_test_split(
        development_labels,
        test_size=VALIDATION_SIZE,
        random_state=RANDOM_STATE,
        stratify=development_labels["Retinopathy grade"],
    )

    train_image_names = set(train_labels["Image name"])
    validation_image_names = set(validation_labels["Image name"])
    development_image_names = set(development_labels["Image name"])

    overlapping_names = train_image_names & validation_image_names
    combined_names = train_image_names | validation_image_names

    if overlapping_names:
        raise ValueError("Training and validation splits contain overlapping images")

    if combined_names != development_image_names:
        raise ValueError("Training and validation splits do not cover every image")

    train_labels = train_labels.sort_values("Image name").reset_index(drop=True)
    validation_labels = validation_labels.sort_values("Image name").reset_index(
        drop=True
    )

    print("Development samples:", len(development_labels))
    print("Training samples:", len(train_labels))
    print("Validation samples:", len(validation_labels))

    print()
    print("Training grade distribution:")
    print(train_labels["Retinopathy grade"].value_counts().sort_index())

    print()
    print("Validation grade distribution:")
    print(validation_labels["Retinopathy grade"].value_counts().sort_index())

    print()
    print("Training target distribution:")
    print(train_labels["target"].value_counts())

    print()
    print("Validation target distribution:")
    print(validation_labels["target"].value_counts())

    SPLITS_DIRECTORY.mkdir(parents=True, exist_ok=True)

    train_split_path = SPLITS_DIRECTORY / "train.csv"
    validation_split_path = SPLITS_DIRECTORY / "validation.csv"
    holdout_split_path = SPLITS_DIRECTORY / "holdout.csv"

    train_labels.to_csv(train_split_path, index=False)
    validation_labels.to_csv(validation_split_path, index=False)
    holdout_labels.to_csv(holdout_split_path, index=False)

    print()
    print("Saved training split to:", train_split_path)
    print("Saved validation split to:", validation_split_path)
    print("Saved holdout split to:", holdout_split_path)

    print()
    print("Overlapping images:", len(overlapping_names))
    print("Images covered by both splits:", len(combined_names))


if __name__ == "__main__":
    main()
