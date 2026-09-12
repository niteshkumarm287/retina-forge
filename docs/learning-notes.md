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