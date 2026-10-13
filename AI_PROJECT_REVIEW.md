# AI Project Review

## Project Summary

A coursework notebook joining Melbourne traffic and road data, exploring speed/vehicle distributions, PCA structure, VAT views, KMeans clusters and an illustrative KNN cluster surface.

Chen Jiang’s original traffic-analysis coursework. The original analytic stages and the attributed provided VAT helper are retained.

## Original Engineering Strengths

The original analysis connects survey rows to road classification through an explicit lookup, then derives speed-over-limit measures and suburb/road summaries. This links data preparation to concrete transport questions before applying dimensionality reduction.

Several views of the same data are compared: raw-feature and two-component VAT heatmaps, an elbow plot, cluster scatter/centroids, parallel coordinates and a KNN decision surface. That variety makes representation choices visible rather than reporting a single unexplained clustering number.

## Technical Highlights

The original unscaled PCA choice and three-cluster descriptive analysis remain. Sampling and KMeans are now deterministic, with cleaned sample indices preserved for colours and labels.

The original full-sample KNN surface is explicitly illustrative. A separate check fits PCA/KMeans on training rows and measures held-out KNN agreement with that learned clustering, without claiming external traffic-label accuracy.

## 2026 Maintenance Improvements

- Repaired mismatched tick positions/labels and numeric missing-value handling.
- Aligned cleaned rows, colours and cluster labels; fixed seeds and explicit KMeans initialization counts.
- Clarified decision-surface axes, colours and legend while retaining the original visualization.
- Added a separate training-only held-out surrogate check, pinned dependencies, verified saved outputs and a clean-kernel runner.

The changes retain the project's original mechanisms and strengthen their execution
boundaries and verification contract. They do not substitute a new project concept.

## Verification

- All 17 code cells executed successfully from a clean Python 3.12 kernel; ten figures were generated.
- Two regression methods passed: deterministic sampling with missing-data alignment, and audited training-only PCA plus repeated held-out agreement.
- Repeat stdout metrics match exactly. The maintained descriptive silhouette is 0.732474; held-out KNN agreement with training-fitted KMeans is 0.997006 across 334 held-out rows, explicitly not real traffic-label accuracy.
- Decision-surface figure visually inspected. Schema validation and the project-local verifier passed. Evidence: TrafficAnalyse_before_execution.json, TrafficAnalyse_final_execution.json, TrafficAnalyse_unit_final.log.

Verification is limited to the commands and cases listed above; passing these checks is not a claim of universal correctness.

## Skills Demonstrated

Data joins/cleaning, transport-domain measures, PCA, VAT visualization, KMeans, interpretation of cluster metrics, aligned plotting and reproducible validation.

## Engineering Assessment

The original notebook shows an end-to-end progression from transport records to several complementary representations. Maintenance makes the workflow repeatable and states the limits of the cluster-derived evidence clearly.

## Maintenance Transparency

The original implementation is preserved in `archive/handwritten-original` at
`8e4c5045342a2e47c298b32ee81a861405c452fe`. The reviewed maintained version contains a later AI-assisted engineering
maintenance pass focused on verification, robustness, testing, and documentation
while retaining the original project approach.
