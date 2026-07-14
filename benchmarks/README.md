# Benchmark and metric guide

## Accuracy is necessary, but not sufficient

| Layer | Representative metrics | Question answered |
|---|---|---|
| Clean task accuracy | mAP, NDS, mIoU, PQ | Can the model solve the nominal task? |
| Corruption robustness | AP/mIoU under shift, RCE, mCE, mRR | How much nominal capability is retained? |
| Calibration | ECE, NLL, Brier score, risk–coverage | Does confidence remain meaningful after shift? |
| Long-tail reliability | worst-group accuracy, macro AP, tail recall | Are rare groups hidden by the average? |
| Planning-aware safety | PKL, collision rate, TTC, rule violations | Do perception errors alter downstream decisions? |
| World-model validity | physics adherence, controllability, horizon error | Does the generated future behave like a usable world? |

## Core robustness suites

### KITTI-C / nuScenes-C / Waymo-C

[Dong et al., CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Dong_Benchmarking_Robustness_of_3D_Object_Detection_to_Common_Corruptions_CVPR_2023_paper.html) organize corruptions into weather, sensor, motion, object, and alignment levels.

For a higher-is-better accuracy score (A):

```text
RCE = 100 × (A_clean − A_corrupt) / A_clean
```

Always report `A_clean` and `A_corrupt` beside RCE; a small relative drop can hide poor absolute accuracy.

### Robo3D

[Robo3D, ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Kong_Robo3D_Towards_Robust_and_Reliable_3D_Perception_against_Corruptions_ICCV_2023_paper.html) normalizes corruption error against a baseline and reports resilience across severity levels. State the baseline model and score range before comparing mCE across papers.

### RCP-Bench

[RCP-Bench, CVPR 2025](https://github.com/LuckyDush/RCP-Bench) separates global, ego-only, and connected-agent interference. This matters because collaboration may compensate for ego corruption or propagate bad remote features.

## Online adaptation protocol

A credible TTA experiment should report:

1. **stream order** and whether batches are revisited;
2. source-data availability and updated parameter subset;
3. episodic vs continual reset policy;
4. latency, memory, and number of gradient steps;
5. forgetting after the stream returns to a known domain;
6. failure detection, rollback, or update gating;
7. multiple shift orders and random seeds.

## World-model evaluation

FID/FVD measure visual distribution similarity but do not prove physical validity. Pair them with:

- action controllability and counterfactual consistency;
- multi-view/3D consistency and object permanence;
- collision, map, kinematic, and conservation-law violations;
- horizon-wise calibration and compounding error;
- downstream planning or perception improvement on held-out real domains.

[WorldModelBench, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4ec03ed08a3fcb59e1c815b5598beff1-Abstract-Datasets_and_Benchmarks_Track.html) is a useful reference for physics-adherence and instruction-following evaluation.
