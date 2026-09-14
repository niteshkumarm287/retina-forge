from pathlib import Path
import pandas as pd

from PIL import Image

from collections import Counter

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

labels = pd.read_csv(
    TRAIN_LABELS,
    usecols=["Image name", "Retinopathy grade"],
)

print(labels.head())
print()
print("Number of training samples:", len(labels))
print()
print("Examples per grade:")
print(labels["Retinopathy grade"].value_counts().sort_index())

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
            unreadable_images.append(image_path)

    print()
    print(f"{split_name} image files:", len(image_names))
    print(f"{split_name} label records:", len(label_names))
    print(f"{split_name} labels without images:", len(missing_images))
    print(f"{split_name} images without labels:", len(unlabeled_images))
    print(f"{split_name} image formats:", dict(image_formats))
    print(f"{split_name} image sizes:", dict(image_sizes))
    print(f"{split_name} image modes:", dict(image_modes))
    print(f"{split_name} unreadable images:", len(unreadable_images))

labels["target"] = labels["Retinopathy grade"].map(to_binary_label)
print()
print("V1 target distribution:")
print(labels["target"].value_counts())

image_paths = sorted(TRAIN_IMAGES.glob("*.jpg"))

image_names = {
    image_path.stem
    for image_path in image_paths
}

label_names = set(labels["Image name"])

missing_images = label_names - image_names
unlabeled_images = image_names - label_names

print()
print("Image files:", len(image_names))
print("Label records:", len(label_names))
print("Labels without images:", len(missing_images))
print("Images without labels:", len(unlabeled_images))

sample_image_path = image_paths[0]

with Image.open(sample_image_path) as image:
    print()
    print("Sample image:", sample_image_path.name)
    print("Image format:", image.format)
    print("Image size:", image.size)
    print("Image mode:", image.mode)\

image_sizes = Counter()
image_modes = Counter()
unreadable_images = []

for image_path in image_paths:
    try:
        with Image.open(image_path) as image:
            image.load()
            image_sizes[image.size] += 1
            image_modes[image.mode] += 1
    except OSError:
        unreadable_images.append(image_path)

print()
print("Image sizes:", dict(image_sizes))
print("Image modes:", dict(image_modes))
print("Unreadable images:", len(unreadable_images))

test_labels = pd.read_csv(
    TEST_LABELS,
    usecols=["Image name", "Retinopathy grade"],
)

test_labels["target"] = test_labels["Retinopathy grade"].map(to_binary_label)

print()
print("Number of testing samples:", len(test_labels))
print()
print("Holdout examples per grade:")
print(test_labels["Retinopathy grade"].value_counts().sort_index())
print()
print("Holdout V1 target distribution:")
print(test_labels["target"].value_counts())

test_image_paths = sorted(TEST_IMAGES.glob("*.jpg"))

test_image_names = {
    image_path.stem
    for image_path in test_image_paths
}

test_label_names = set(test_labels["Image name"])

test_missing_images = test_label_names - test_image_names
test_unlabeled_images = test_image_names - test_label_names

test_image_sizes = Counter()
test_image_modes = Counter()
test_unreadable_images = []

for image_path in test_image_paths:
    try:
        with Image.open(image_path) as image:
            image.load()
            test_image_sizes[image.size] += 1
            test_image_modes[image.mode] += 1
    except OSError:
        test_unreadable_images.append(image_path)

print()
print("Holdout image files:", len(test_image_names))
print("Holdout label records:", len(test_label_names))
print("Holdout labels without images:", len(test_missing_images))
print("Holdout images without labels:", len(test_unlabeled_images))
print("Holdout image sizes:", dict(test_image_sizes))
print("Holdout image modes:", dict(test_image_modes))
print("Holdout unreadable images:", len(test_unreadable_images))

inspect_images("Training", TRAIN_IMAGES, labels)
inspect_images("Holdout", TEST_IMAGES, test_labels)