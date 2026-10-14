# Melbourne Traffic Survey Analysis

## Academic Context

University: University of Melbourne  
Course: Coursework; exact course number not independently established  
Year: Exact original submission year not independently established  
Project type: individual


## Overview

A coursework notebook joining Melbourne traffic and road data, exploring speed/vehicle distributions, PCA structure, VAT views, KMeans clusters and an illustrative KNN cluster surface.

## Original Context

Chen Jiang’s original traffic-analysis coursework. The original analytic stages and the attributed provided VAT helper are retained. The preserved pre-maintenance snapshot is `8e4c5045342a2e47c298b32ee81a861405c452fe`;
its most recent original commit is dated 2022-01-13. This date describes Git evidence,
not necessarily the complete implementation period.

## What I Implemented

Numeric cleaning, road-segment lookup, speed-limit differences, suburb summaries, distribution plots, a 1,000-row sample, PCA/VAT views, an elbow study, cluster sizes/silhouette and a KNN decision surface.

## Technical Approach

The original unscaled PCA choice and three-cluster descriptive analysis remain. Sampling and KMeans are now deterministic, with cleaned sample indices preserved for colours and labels.

The original full-sample KNN surface is explicitly illustrative. A separate check fits PCA/KMeans on training rows and measures held-out KNN agreement with that learned clustering, without claiming external traffic-label accuracy.

## Build / Run

Use Python 3.12: `python3 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.txt`. Open the original notebook from this directory, or run `.venv/bin/python -B verify_notebook.py` for schema validation, a fresh kernel, HTML/notebook artifacts in `.build/`, and regression tests.

## Testing

- All 17 code cells executed successfully from a clean Python 3.12 kernel; ten figures were generated.
- Two regression methods passed: deterministic sampling with missing-data alignment, and audited training-only PCA plus repeated held-out agreement.
- Repeat stdout metrics match exactly. The maintained descriptive silhouette is 0.732474; held-out KNN agreement with training-fitted KMeans is 0.997006 across 334 held-out rows, explicitly not real traffic-label accuracy.
- Decision-surface figure visually inspected. Schema validation and the project-local verifier passed. Evidence: TrafficAnalyse_before_execution.json, TrafficAnalyse_final_execution.json, TrafficAnalyse_unit_final.log.

## 2026 Maintenance

- Repaired mismatched tick positions/labels and numeric missing-value handling.
- Aligned cleaned rows, colours and cluster labels; fixed seeds and explicit KMeans initialization counts.
- Clarified decision-surface axes, colours and legend while retaining the original visualization.
- Added a separate training-only held-out surrogate check, pinned dependencies, verified saved outputs and a clean-kernel runner.

The later work is AI-assisted maintenance, separate from the original implementation.
The exact original snapshot remains on `archive/handwritten-original`.
See [AI_PROJECT_REVIEW.md](AI_PROJECT_REVIEW.md) for a technical review.

## Known Limitations

- Clusters and the silhouette are descriptive; no independent labelled traffic-classification accuracy was established.
- The original PCA interpretation depends on unscaled features and the selected sample.
- The full-sample visualization and separate held-out surrogate check answer different questions.
