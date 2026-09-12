# Dataset

## Dataset selection

RetinaForge V1 uses the Indian Diabetic Retinopathy Image Dataset (IDRiD).

Official sources:

- [IDRiD Grand Challenge](https://idrid.grand-challenge.org/Data/)
- [IEEE DataPort download](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid)

## Why IDRiD

IDRiD was selected because:

- It is small enough for a beginner project and local training.
- It contains real retinal fundus photographs.
- Medical experts provided diabetic-retinopathy severity grades.
- It includes labels in CSV format.
- Its license permits educational and research use with attribution.
- It contains lesion annotations that may support future experiments.

## Dataset contents

The complete dataset contains 516 retinal fundus images.

The images:

- Are stored as JPEG files.
- Have a resolution of 4288 × 2848 pixels.
- Were captured using a Kowa VX-10 alpha fundus camera.
- Use a 50-degree field of view.
- Are centered near the macula.

The dataset provides:

- Diabetic-retinopathy severity grades
- Diabetic macular edema grades
- Lesion masks for a smaller subset of images
- Optic-disc and fovea location information

RetinaForge V1 will use only the retinal images and diabetic-retinopathy
severity grades.

## Local storage

Downloaded data will be stored under:

```text
data/raw/idrid/
```

Files inside `data/raw/` must remain unchanged. Image resizing, cropping and
other transformations will be written to:

```text
data/processed/
```

Generated split definitions will be stored in:

```text
data/splits/
```

The image files are excluded from Git. This keeps the repository small and
ensures that users obtain the original dataset from its authoritative source.

## License

The IDRiD website states that the dataset is licensed under the
[Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).

The license permits sharing and adaptation when appropriate attribution is
provided, the license is linked, and modifications are identified.

## Attribution

When using the dataset, RetinaForge will credit:

> Porwal, P., Pachade, S., Kamble, R., Kokare, M., Deshmukh, G.,
> Sahasrabuddhe, V., and Meriaudeau, F. Indian Diabetic Retinopathy Image
> Dataset (IDRiD).

The final project documentation should also include the citation requested by
the dataset maintainers.

## Medical-data boundary

Only the established, publicly released IDRiD research dataset will be used.

RetinaForge V1 will not collect:

- Personal medical records
- Names or patient identifiers
- User-uploaded retinal images
- Images obtained from healthcare systems
- Images without documented permission and provenance

## Download status

Not downloaded yet.