# Model

## Prediction task

RetinaForge V1 is a binary image-classification project.

Given one retinal fundus photograph, the model predicts:

- `non_referable_dr`
- `referable_dr`

IDRiD grades 0 and 1 will map to `non_referable_dr`. Grades 2, 3 and 4 will
map to `referable_dr`.

## Baseline

Before training a neural network, RetinaForge will measure a simple
majority-class baseline.

The baseline always predicts the most common label in the training data. It is
not useful medically, but it tells us the minimum performance a learned model
should beat.

For example, if 70% of the images are non-referable, a model could achieve 70%
accuracy by predicting `non_referable_dr` for every image. Accuracy alone would
make that model look better than it really is.

## Initial neural network

V1 will begin with a pretrained ResNet-18 image classifier.

ResNet-18 was selected because:

- It is relatively small and fast.
- It can run locally on the available Mac.
- It is widely used and well documented.
- It is suitable for learning transfer-learning concepts.
- Its pretrained visual features reduce the amount of medical data required.

## Transfer learning

Training a neural network entirely from the beginning would require a much
larger dataset.

Instead, RetinaForge will start with a model that has already learned general
visual features from a large image dataset. These features include edges,
shapes, textures and color patterns.

We will replace the model's final classification layer so that it learns the
two RetinaForge labels.

The initial process will be:

1. Load pretrained ResNet-18 weights.
2. Freeze the general visual-feature layers.
3. Replace the final classification layer.
4. Train the new layer using IDRiD images.
5. Evaluate it on images excluded from training.
6. Later, experiment with unfreezing a small part of the network.

## Image preprocessing

The initial preprocessing pipeline will:

- Load each image as RGB.
- Remove unnecessary black borders when appropriate.
- Resize images to a consistent size.
- Convert images into numerical tensors.
- Normalize them using the values expected by the pretrained model.

Training-only augmentation may later include small rotations, flips and limited
brightness changes. Validation and holdout images must not use random
augmentation.

We will inspect real dataset samples before choosing final preprocessing
settings.

## Training output

Training will produce:

- A saved model checkpoint
- Training loss history
- Validation loss history
- Evaluation metrics
- A confusion matrix
- A record of the configuration used

Saved model files will remain under `models/` and outside normal Git tracking.

## Model status

No model has been trained yet.