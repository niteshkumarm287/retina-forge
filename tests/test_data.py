import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd
from src import create_splits
from src.data_utils import to_binary_label, validate_labels


class DataTests(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(
            [to_binary_label(g) for g in range(5)],
            ["non_referable_dr"] * 2 + ["referable_dr"] * 3,
        )
        for grade in [-1, 5, 2.5, float("nan"), float("inf"), True, None, "2"]:
            with self.subTest(grade=grade), self.assertRaises(ValueError):
                to_binary_label(grade)

    def test_invalid_identifiers(self):
        for names in [["x", "x"], ["x", ""], ["x", None]]:
            with self.subTest(names=names), self.assertRaises(ValueError):
                validate_labels(
                    pd.DataFrame({"Image name": names, "Retinopathy grade": [0, 2]})
                )

    def test_synthetic_splits_are_disjoint_and_reproducible(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            training = root / "training.csv"
            holdout = root / "holdout.csv"
            output = root / "splits"
            pd.DataFrame(
                {
                    "Image name": [f"train-{i}" for i in range(100)],
                    "Retinopathy grade": [i % 5 for i in range(100)],
                }
            ).to_csv(training, index=False)
            pd.DataFrame({"Image name": ["held-out"], "Retinopathy grade": [2]}).to_csv(
                holdout, index=False
            )
            with (
                patch.multiple(
                    create_splits,
                    TRAIN_LABELS=training,
                    HOLDOUT_LABELS=holdout,
                    SPLITS_DIRECTORY=output,
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                create_splits.main()
                first = {p.name: p.read_bytes() for p in output.iterdir()}
                create_splits.main()
                self.assertEqual(
                    first, {p.name: p.read_bytes() for p in output.iterdir()}
                )
                train = pd.read_csv(output / "train.csv")
                validation = pd.read_csv(output / "validation.csv")
                self.assertEqual((len(train), len(validation)), (80, 20))
                self.assertFalse(
                    set(train["Image name"]) & set(validation["Image name"])
                )
                pd.DataFrame(
                    {"Image name": ["train-0"], "Retinopathy grade": [2]}
                ).to_csv(holdout, index=False)
                with self.assertRaisesRegex(ValueError, "overlapping"):
                    create_splits.main()
                self.assertEqual(
                    first, {p.name: p.read_bytes() for p in output.iterdir()}
                )
