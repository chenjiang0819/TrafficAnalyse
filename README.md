# Melbourne Traffic Survey Analysis

A coursework notebook joining Melbourne traffic and road data, exploring speed/vehicle distributions, PCA structure, VAT views, KMeans clusters and an illustrative KNN cluster surface.

Chen Jiang’s University of Melbourne computing coursework.

University: University of Melbourne  

## Implementation

Numeric cleaning, road-segment lookup, speed-limit differences, suburb summaries, distribution plots, a 1,000-row sample, PCA/VAT views, an elbow study, cluster sizes/silhouette and a KNN decision surface.

## Technical approach

The original unscaled PCA choice and three-cluster descriptive analysis remain. Sampling and KMeans are now deterministic, with cleaned sample indices preserved for colours and labels.

The original full-sample KNN surface is explicitly illustrative. A separate check fits PCA/KMeans on training rows and measures held-out KNN agreement with that learned clustering, without claiming external traffic-label accuracy.

## Run

Use Python 3.12: `python3 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.txt`. Open the original notebook from this directory, or run `.venv/bin/python -B verify_notebook.py` for schema validation, a fresh kernel, HTML/notebook artifacts in `.build/`, and regression tests.

## Checks and results

- All 17 code cells executed successfully from a clean Python 3.12 kernel; ten figures were generated.
- Two regression methods passed: deterministic sampling with missing-data alignment, and audited training-only PCA plus repeated held-out agreement.
- Repeat stdout metrics match exactly. The maintained descriptive silhouette is 0.732474; held-out KNN agreement with training-fitted KMeans is 0.997006 across 334 held-out rows, explicitly not real traffic-label accuracy.

## 2026 maintenance

- Repaired mismatched tick positions/labels and numeric missing-value handling.
- Aligned cleaned rows, colours and cluster labels; fixed seeds and explicit KMeans initialization counts.
- Clarified decision-surface axes, colours and legend while retaining the original visualization.
- Added a separate training-only held-out surrogate check, pinned dependencies, verified saved outputs and a clean-kernel runner.

These changes are 2026 AI-assisted maintenance of the original student implementation.

## Usage notes

- Clusters and the silhouette are descriptive; no independent labelled traffic-classification accuracy was established.
- The original PCA interpretation depends on unscaled features and the selected sample.
- The full-sample visualization and separate held-out surrogate check answer different questions.
