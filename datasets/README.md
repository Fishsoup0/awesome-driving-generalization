# Dataset atlas

The useful question is not only “How large is the dataset?” but **which deployment gap does it expose?** This atlas groups datasets by the shift dimensions they make measurable.

## 2025–2026 additions

| Dataset | Venue | Modalities | Scale / conditions | Best use |
|---|---:|---|---|---|
| [CARD](https://openaccess.thecvf.com/content/CVPR2026/html/Elazab_CARD_A_Multi-Modal_Automotive_Dataset_for_Dense_3D_Reconstruction_in_CVPR_2026_paper.html) | CVPR 2026 | Stereo, LiDAR, wheel traces | 110 km; irregular surfaces; Germany/Italy | Dense geometry and road-topography transfer. |
| [SearchAD](https://openaccess.thecvf.com/content/CVPR2026/html/Embacher_SearchAD_Large-Scale_Rare_Image_Retrieval_Dataset_for_Autonomous_Driving_CVPR_2026_paper.html) | CVPR 2026 | Camera | 423K+ frames; 90 rare classes | Long-tail retrieval and targeted data curation. |
| [URScenes](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_URScenes_A_Multi-scenario_Dataset_for_Unstructured_Road_Environments_CVPR_2026_paper.html) | CVPR 2026 | LiDAR, radar, camera | 472 scenes; eight conditions | Unstructured-road detection, tracking, occupancy. |
| [V2U4Real](https://openaccess.thecvf.com/content/CVPR2026/html/Li_V2U4Real_A_Real-world_Large-scale_Dataset_for_Vehicle-to-UAV_Cooperative_Perception_CVPR_2026_paper.html) | CVPR 2026 | Vehicle/UAV LiDAR + RGB | 56K+ frames per modality; 700K boxes | Cross-view cooperative perception. |
| [CleanBench](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html) | CVPR 2025 | Camera + language | 230K instruction-response pairs | Coupled-degradation restoration and downstream perception. |
| [RCP-Bench](https://github.com/LuckyDush/RCP-Bench) | CVPR 2025 | Multi-agent camera | Three corruption suites; six collaboration cases | Robustness attribution across ego and connected agents. |
| [STSnu](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d7b7c2ff14a479d574b971fd8a36f3e4-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2025 | Multi-view video/LiDAR + language | 43 scenarios; 971 verified questions | Spatial-temporal reasoning in driving VLMs. |

## Shift-oriented selection guide

| Research question | Recommended datasets / suites |
|---|---|
| Weather and illumination robustness | ACDC, SHIFT, URScenes, KITTI-C/nuScenes-C |
| Geographic transfer | Waymo, nuScenes, BDD100K, Cityscapes, SHIFT |
| Sensor corruption or density shift | KITTI-C, Robo3D, MSC-Bench, CARD |
| Semantic novelty and long tail | SearchAD, OVDG benchmark, Impromptu VLA |
| Collaborative perception failure | RCP-Bench, V2U4Real, DAIR-V2X-C |
| Temporal/world-model reasoning | STSnu, WorldModelBench, Argoverse 2 occupancy forecasting |

## Reporting checklist

- State whether “year” means data release, preprint, or peer-reviewed publication.
- Report sensor configuration, calibration assumptions, and any unavailable modality.
- Keep clean and corrupted/source and target splits disjoint.
- Identify synthetic corruptions separately from naturally captured adverse conditions.
- For aggregate scores, document which corruption types are applicable to each modality.

The machine-readable catalog is available at [`../data/datasets.csv`](../data/datasets.csv).
