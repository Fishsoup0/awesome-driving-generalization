# 自动驾驶感知泛化与适应研究库

本项目是论文 **《Generalization and Adaptation in Real-World Autonomous Driving Perception: A Survey》** 的持续维护资源库，按照“数据层—模型层—评测层—未来智能体”的逻辑整理近年顶会论文、数据集、基准和开源项目。

![研究框架](assets/taxonomy.svg)

## 核心内容

- [顶会论文库](papers/README.md)：重点覆盖 2023–2026 年 CVPR、ICCV、NeurIPS 等工作；
- [数据集地图](datasets/README.md)：按照天气、地理、传感器、长尾语义、协同感知和时间推理分类；
- [评测指南](benchmarks/README.md)：包含 RCE、mCE/mRR、校准、规划安全和世界模型物理一致性；
- [论文数据表](data/papers.csv)与[数据集数据表](data/datasets.csv)：便于检索、统计与二次开发。

## 收录原则

项目重点收录能够回答以下问题的工作：

1. 解决了哪一种真实分布偏移或长尾问题？
2. 使用什么传感器、任务和源域/目标域假设？
3. 是否需要目标标签、源数据或在线梯度更新？
4. 是否同时报告干净域与偏移域性能？
5. 是否讨论适应稳定性、物理一致性或闭环安全？

欢迎通过 Issue 或 Pull Request 推荐新论文。请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。
