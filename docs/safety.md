# Medical Safety

## Intended use

RetinaForge is an educational and research project for learning how to train
and evaluate a computer-vision model using retinal fundus photographs.

It is intended to identify image patterns associated with referable diabetic
retinopathy in the IDRiD research dataset.

## Not intended for clinical use

RetinaForge must not be used to:

- Diagnose diabetes.
- Confirm or exclude diabetic retinopathy in a real patient.
- Recommend treatment or medication.
- Replace an ophthalmologist or other healthcare professional.
- Delay professional medical evaluation.
- Process images from real patients without appropriate approval and consent.

## Meaning of a prediction

A model prediction is a statistical result, not a medical diagnosis.

For example:

> The model assigned this research image a high probability of referable
> diabetic retinopathy.

It must not be presented as:

> You have diabetic retinopathy.

## Known risks

The model may produce:

- False negatives that miss signs of disease.
- False positives that incorrectly flag an image.
- Unreliable predictions for blurry or poorly illuminated images.
- Biased results for populations or cameras not represented in the dataset.
- High confidence for an incorrect prediction.

## Data privacy

V1 uses only the publicly released IDRiD research dataset.

Personal medical records, identifying information and user-uploaded patient
images must not be added to the repository.

## Future application behavior

If RetinaForge later accepts images through an interface, it should:

- Clearly state that it is not a diagnostic device.
- Reject images that cannot be evaluated reliably.
- Avoid permanently storing uploaded images.
- Avoid collecting identifying information.
- Recommend professional evaluation instead of giving treatment advice.
- Record the model version used for every prediction.

## Regulatory boundary

A model that performs well in this educational project is not automatically
safe or approved for clinical use.

Clinical deployment would require substantially stronger evidence, external
validation, privacy controls, security review, medical oversight and applicable
regulatory approval.