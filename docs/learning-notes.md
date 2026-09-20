# Learning Notes

This document records concepts and decisions encountered while building
RetinaForge.

## Initial system flow

```text
IDRiD download
      ↓
data/raw
      ↓
image preprocessing
      ↓
data/processed
      ↓
training, validation and holdout splits
      ↓
neural-network training
      ↓
models/
      ↓
evaluation charts
      ↓
reports/figures/
```

## Current lessons

- A retinal image can show diabetic retinopathy, but it cannot confirm diabetes.
- Medical images and generated model files should remain outside normal Git.
- Training, validation, and holdout data must have separate responsibilities.
- The project should make a narrow, measurable claim.

python src/inspect_data.py -> runs individual files like here it'll only run inspect_data.py
python -m src.inspect_data -> this means from the project root, run inspect_data as a module belonging to the src package

## Running Python modules

- `python src/inspect_data.py` runs that file directly.
- `python -m src.inspect_data` runs `inspect_data` as part of the `src` package,
  allowing package imports such as `from src.data_utils import ...`.