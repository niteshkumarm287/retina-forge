# Project Scope

## Problem statement

RetinaForge is an educational computer-vision project that detects signs of
referable diabetic retinopathy in retinal fundus photographs.

It does not diagnose diabetes or replace evaluation by a qualified healthcare
professional.

## Input

One color retinal fundus photograph.

The image should show the retina clearly enough for analysis.

## V1 output

The V1 model produces one of two labels:

- `non_referable_dr`
- `referable_dr`

The model will also produce a probability representing its confidence in the
prediction.

## Label mapping

The IDRiD diabetic-retinopathy grades will be converted as follows:

| IDRiD grade | Meaning | RetinaForge label |
| --- | --- | --- |
| 0 | No diabetic retinopathy | `non_referable_dr` |
| 1 | Mild diabetic retinopathy | `non_referable_dr` |
| 2 | Moderate diabetic retinopathy | `referable_dr` |
| 3 | Severe diabetic retinopathy | `referable_dr` |
| 4 | Proliferative diabetic retinopathy | `referable_dr` |

This mapping treats moderate or more severe disease as requiring referral.

## V1 goals

- Download and document the IDRiD dataset.
- Inspect the images and label distribution.
- Create reproducible training and validation splits.
- Build a simple baseline model.
- Build a transfer-learning image classifier.
- Evaluate the model on data it did not train on.
- Report sensitivity, specificity, precision, recall, F1 score and a confusion
  matrix.
- Record experiments and learning notes.

## Non-goals

V1 will not:

- Diagnose diabetes.
- Recommend medication or treatment.
- Accept real patient uploads.
- Be deployed for clinical use.
- Claim regulatory or medical approval.
- Predict all possible retinal diseases.
- Replace an ophthalmologist.

## Success criteria

V1 is successful when:

1. The complete pipeline runs from image loading through evaluation.
2. Dataset boundaries prevent training images from leaking into evaluation.
3. Results are reproducible from documented commands.
4. Performance is compared with a simple baseline.
5. Model limitations and mistakes are documented honestly.

A particular accuracy percentage is not a V1 success requirement. The purpose
is to build and understand a trustworthy evaluation pipeline.