from collections import Counter
from pathlib import Path

import pandas as pd
from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]

TRAIN_LABELS = (
    PROJECT_ROOT
    / "data/raw/idrid/B. Disease Grading/2. Groundtruths"
    / "a. IDRiD_Disease Grading_Training Labels.csv"
)

TRAIN_IMAGES = (
    PROJECT_ROOT
    / "data/raw/idrid/B. Disease Grading/1. Original Images"
    / "a. Training Set"
)

TEST_LABELS = (
    PROJECT_ROOT
    / "data/raw/idrid/B. Disease Grading/2. Groundtruths"
    / "b. IDRiD_Disease Grading_Testing Labels.csv"
)

TEST_IMAGES = (
    PROJECT_ROOT
    / "data/raw/idrid/B. Disease Grading/1. Original Images"
    / "b. Testing Set"
)


def to_binary_label(grade):
    if grade >= 2:
        return "referable_dr"

    return "non_referable_dr"


def inspect_images(split_name, images_directory, labels):
    image_paths = sorted(images_directory.glob("*.jpg"))
    image_names = {image_path.stem for image_path in image_paths}
    label_names = set(labels["Image name"])

    missing_images = label_names - image_names
    unlabeled_images = image_names - label_names

    image_formats = Counter()
    image_sizes = Counter()
    image_modes = Counter()
    unreadable_images = []

    for image_path in image_paths:
        try:
            with Image.open(image_path) as image:
                image.load()
                image_formats[image.format] += 1
                image_sizes[image.size] += 1
                image_modes[image.mode] += 1
        except OSError:
            unreadable_images.append(image_path.name)

    print()
    print(f"{split_name} image files:", len(image_names))
    print(f"{split_name} label records:", len(label_names))
    print(f"{split_name} labels without images:", len(missing_images))
    print(f"{split_name} images without labels:", len(unlabeled_images))
    print(f"{split_name} image formats:", dict(image_formats))
    print(f"{split_name} image sizes:", dict(image_sizes))
    print(f"{split_name} image modes:", dict(image_modes))
    print(f"{split_name} unreadable images:", len(unreadable_images))


labels = pd.read_csv(
    TRAIN_LABELS,
    usecols=["Image name", "Retinopathy grade"],
)

labels["target"] = labels["Retinopathy grade"].map(to_binary_label)

print(labels.head())
print()
print("Number of training samples:", len(labels))
print()
print("Training examples per grade:")
print(labels["Retinopathy grade"].value_counts().sort_index())
print()
print("Training V1 target distribution:")
print(labels["target"].value_counts())

test_labels = pd.read_csv(
    TEST_LABELS,
    usecols=["Image name", "Retinopathy grade"],
)

test_labels["target"] = test_labels["Retinopathy grade"].map(
    to_binary_label
)

print()
print("Number of holdout samples:", len(test_labels))
print()
print("Holdout examples per grade:")
print(test_labels["Retinopathy grade"].value_counts().sort_index())
print()
print("Holdout V1 target distribution:")
print(test_labels["target"].value_counts())

inspect_images("Training", TRAIN_IMAGES, labels)
inspect_images("Holdout", TEST_IMAGES, test_labels)