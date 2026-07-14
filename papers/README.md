# Curated paper library

This library follows the survey lifecycle: **data coverage → model representation/training → inference-time adaptation → evaluation → predictive world models**. The default view emphasizes 2025–2026 top-venue work; 2022–2023 entries are included when they define a widely used benchmark.

Legend: **C** camera · **L** LiDAR · **VLM** vision-language model · **Occ** occupancy · **TTA** test-time adaptation.

## Data coverage, generation, and simulation

| Year | Paper | Venue | Main contribution |
|---:|---|---:|---|
| 2026 | [DrivePTS](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DrivePTS_A_Progressive_Learning_Framework_with_Textual_and_Structural_Enhancement_CVPR_2026_paper.html) | CVPR | Text- and structure-enhanced rare driving-scene generation. |
| 2026 | [SimScale](https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SimScale_Learning_to_Drive_via_Real-World_Simulation_at_Scale_CVPR_2026_paper.html) | CVPR | Scalable learning from real-world simulation. |
| 2025 | [UniScene](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UniScene_Unified_Occupancy-centric_Driving_Scene_Generation_CVPR_2025_paper.html) | CVPR | Unified occupancy, video, and LiDAR generation. |
| 2025 | [Scenario Dreamer](https://openaccess.thecvf.com/content/CVPR2025/html/Rowe_Scenario_Dreamer_Vectorized_Latent_Diffusion_for_Generating_Driving_Simulation_Environments_CVPR_2025_paper.html) | CVPR | Vectorized diffusion for scene and agent simulation. |
| 2025 | [ReconDreamer](https://openaccess.thecvf.com/content/CVPR2025/html/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online_CVPR_2025_paper.html) | CVPR | World-model knowledge for novel-trajectory reconstruction. |

## Open-world and foundation representations

| Year | Paper | Venue | Main contribution |
|---:|---|---:|---|
| 2026 | [Open-Vocabulary Domain Generalization](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.html) | CVPR | Joint unseen-domain and unseen-category segmentation. |
| 2026 | [Learning to Drive is a Free Gift](https://openaccess.thecvf.com/content/CVPR2026/html/Strong_Learning_to_Drive_is_a_Free_Gift_Large-Scale_Label-Free_Autonomy_CVPR_2026_paper.html) | CVPR | Label-free geometry/motion pretraining from unposed videos. |
| 2026 | [SGDrive](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SGDrive_Scene-to-Goal_Hierarchical_World_Cognition_for_Autonomous_Driving_CVPR_2026_paper.html) | CVPR | Driving-specific scene–agent–goal hierarchy for VLM planning. |
| 2025 | [Impromptu VLA](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6e4f0c8c6890899e2206585c3cfba4d1-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS D&B | Open data/weights for unstructured driving corner cases. |

## Robust training and test-time adaptation

| Year | Paper | Venue | Main contribution |
|---:|---|---:|---|
| 2026 | [CD-Buffer](https://openaccess.thecvf.com/content/CVPR2026/html/Song_CD-Buffer_Complementary_Dual-Buffer_Framework_for_Test-Time_Adaptation_in_Adverse_Weather_CVPR_2026_paper.html) | CVPR | Shift-aware additive/subtractive TTA. |
| 2025 | [DUO](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Adaptive_Dual_Uncertainty_Optimization_Boosting_Monocular_3D_Object_Detection_under_ICCV_2025_paper.html) | ICCV | Semantic and geometric uncertainty optimization for M3OD TTA. |
| 2025 | [CodeMerge](https://proceedings.neurips.cc/paper_files/paper/2025/hash/463a91da3c832bd28912cd0d1b8d9974-Abstract-Conference.html) | NeurIPS | Efficient codebook-guided checkpoint composition. |
| 2025 | [JarvisIR](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html) | CVPR | VLM-controlled expert restoration for coupled degradations. |
| 2025 | [Perception-Guided Self-Supervision](https://proceedings.neurips.cc/paper_files/paper/2025/hash/476c9ac41c967332dd28fb844e166b34-Abstract-Conference.html) | NeurIPS | Mitigates causal confusion with perception-based supervision. |

## Robustness and safety evaluation

| Year | Paper | Venue | Main contribution |
|---:|---|---:|---|
| 2025 | [RCP-Bench](https://openaccess.thecvf.com/content/CVPR2025/papers/Du_RCP-Bench_Benchmarking_Robustness_for_Collaborative_Perception_Under_Diverse_Corruptions_CVPR_2025_paper.pdf) | CVPR | Collaborative corruption benchmark with component-level interference. |
| 2025 | [WorldModelBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4ec03ed08a3fcb59e1c815b5598beff1-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS D&B | Instruction-following and physics-adherence evaluation. |
| 2025 | [STSBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d7b7c2ff14a479d574b971fd8a36f3e4-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS D&B | Scenario-based spatial-temporal reasoning for driving VLMs. |
| 2023 | [KITTI-C / nuScenes-C / Waymo-C](https://openaccess.thecvf.com/content/CVPR2023/html/Dong_Benchmarking_Robustness_of_3D_Object_Detection_to_Common_Corruptions_CVPR_2023_paper.html) | CVPR | Common-corruption protocol for 3D detection. |
| 2023 | [Robo3D](https://openaccess.thecvf.com/content/ICCV2023/html/Kong_Robo3D_Towards_Robust_and_Reliable_3D_Perception_against_Corruptions_ICCV_2023_paper.html) | ICCV | Normalized corruption error and resilience for 3D perception. |

## Predictive and physics-aware world models

| Year | Paper | Venue | Representation / connection |
|---:|---|---:|---|
| 2026 | [GenieDrive](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GenieDrive_Towards_Physics-Aware_Driving_World_Model_with_4D_Occupancy_Guided_CVPR_2026_paper.html) | CVPR | 4D occupancy → physics-aware multi-view video. |
| 2026 | [GaussianDWM](https://openaccess.thecvf.com/content/CVPR2026/html/Deng_GaussianDWM_3D_Gaussian_Driving_World_Model_for_Unified_Scene_Understanding_CVPR_2026_paper.html) | CVPR | Language-aligned 3D Gaussians for understanding and generation. |
| 2026 | [DriveLaW](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_DriveLaW_Unifying_Planning_and_Video_Generation_in_a_Latent_Driving_World_CVPR_2026_paper.html) | CVPR | Shared latent space for video forecasting and planning. |
| 2025 | [DIO](https://openaccess.thecvf.com/content/CVPR2025/html/Diehl_DIO_Decomposable_Implicit_4D_Occupancy-Flow_World_Model_CVPR_2025_paper.html) | CVPR | Decomposable 4D occupancy-flow completion and forecasting. |
| 2025 | [GaussianWorld](https://openaccess.thecvf.com/content/CVPR2025/papers/Zuo_GaussianWorld_Gaussian_World_Model_for_Streaming_3D_Occupancy_Prediction_CVPR_2025_paper.pdf) | CVPR | Streaming scene evolution in Gaussian space. |

## Inclusion notes

The canonical metadata lives in [`../data/papers.csv`](../data/papers.csv). When adding a paper, identify:

1. the distribution shift or long-tail failure it addresses;
2. the sensor/task and source/target assumptions;
3. whether adaptation uses target labels, source data, or online updates;
4. the evaluation protocol and whether results are open-loop or closed-loop.
