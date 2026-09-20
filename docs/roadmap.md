# RetinaForge V1 Roadmap

RetinaForge V1 is approximately 40% complete.

## Completed

- [x] Define the project scope and medical-safety boundary
- [x] Create the Python project structure
- [x] Configure PyTorch with Apple MPS support
- [x] Download and verify the IDRiD dataset
- [x] Inspect image dimensions, formats, modes, and readability
- [x] Map IDRiD grades to V1 binary targets
- [x] Create reproducible training, validation, and holdout manifests
- [x] Verify that training and validation images do not overlap

## Remaining

### PyTorch data pipeline

- [ ] Create a custom PyTorch `Dataset`
- [ ] Load images and numeric labels from manifests
- [ ] Resize images to the model input size
- [ ] Add normalization and training augmentation
- [ ] Create training, validation, and holdout `DataLoader` objects
- [ ] Test a complete batch

### Model training

- [ ] Establish a simple prediction baseline
- [ ] Load a pretrained ResNet-18
- [ ] Replace its final classification layer
- [ ] Train using Apple MPS
- [ ] Track training and validation loss
- [ ] Save the best model checkpoint

### Evaluation

- [ ] Measure accuracy, precision, recall, specificity, and F1
- [ ] Generate a confusion matrix
- [ ] Calculate ROC AUC
- [ ] Select a decision threshold using validation data
- [ ] Evaluate the final model once on the holdout set
- [ ] Review incorrect predictions

### Project completion

- [ ] Save evaluation charts under `reports/figures`
- [ ] Add automated tests
- [ ] Document training and evaluation commands
- [ ] Record model limitations
- [ ] Publish the completed V1 repository

## Definition of done

V1 is complete when another developer can reproduce the data splits, train the
model, evaluate it on the untouched holdout set, and understand its limitations
using only the repository documentation.