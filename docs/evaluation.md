# Evaluation

## Why evaluation matters

A model is useful only if it performs well on images it did not train on.

Medical-image classification cannot be judged using accuracy alone. A model
could obtain high accuracy by repeatedly predicting the most common category
while missing important disease cases.

## Dataset boundaries

RetinaForge uses three dataset groups.

### Training set

The model learns from these images and labels.

### Validation set

The validation set is used to:

- Compare experiments.
- Select model settings.
- Choose a classification threshold.
- Detect overfitting.
- Decide whether a model change should be kept.

The model does not directly train on validation images.

### Holdout set

The holdout set acts as the final exam.

It must not be repeatedly inspected or used to adjust the model. It should be
evaluated only after the model design has been selected using the training and
validation sets.

RetinaForge will preserve the official IDRiD test split as the holdout set. A
portion of the official training data will become the validation set.

## Preventing data leakage

Data leakage happens when information from an evaluation image influences
training.

To reduce leakage:

- The same image must never appear in multiple splits.
- Processed copies of an image must stay in the same split as the original.
- Augmented versions of an image must remain in the training set.
- Preprocessing statistics must be calculated using training data only.
- Images from the same patient should remain in one split when patient
  identifiers are available.

## Confusion matrix

The confusion matrix counts four prediction outcomes:

| Outcome | Meaning |
| --- | --- |
| True positive | Referable disease correctly detected |
| True negative | Non-referable disease correctly identified |
| False positive | Non-referable image incorrectly flagged |
| False negative | Referable disease incorrectly missed |

False negatives are particularly important because the model failed to flag an
image containing referable disease.

## Metrics

### Sensitivity

Sensitivity measures how many referable cases the model detects.

```text
sensitivity = true positives / (true positives + false negatives)
```

High sensitivity means fewer disease cases are missed.

### Specificity

Specificity measures how many non-referable cases the model correctly rejects.

```text
specificity = true negatives / (true negatives + false positives)
```

High specificity means fewer unnecessary referrals.

### Precision

Precision measures how many images flagged as referable are actually
referable.

```text
precision = true positives / (true positives + false positives)
```

### F1 score

The F1 score balances precision and sensitivity in one number.

### Accuracy

Accuracy measures the percentage of all predictions that are correct.

Accuracy will be reported, but it will not be treated as the only measure of
model quality.

### ROC AUC

ROC AUC evaluates how well the model ranks referable images above
non-referable images across different classification thresholds.

## Threshold selection

The neural network will produce probabilities rather than absolute medical
facts.

For example:

```text
referable_dr probability = 0.82
```

A threshold converts that probability into a class prediction. With a threshold
of 0.50, the example would be classified as `referable_dr`.

Threshold selection must use the validation set, never the holdout set.

## Model comparison

Every trained model will be compared against:

1. The majority-class baseline.
2. The current best validation result.
3. Previously recorded experiments.

A more complicated model should be kept only when evidence shows a meaningful
benefit.

## Reproducibility

Every experiment should record:

- Model architecture
- Pretrained weights
- Image size
- Training epochs
- Batch size
- Learning rate
- Random seed
- Dataset split version
- Evaluation metrics

## Current status

No evaluation has been run yet.