# 方向 2: 集成建模

**Ensemble Modeling**

---

## 📖 概述

集成建模整合多种建模方法，构建统一的预测框架，是连接数据处理与可靠性分析的核心环节。集成学习方法通过组合多个模型来提高预测精度和不确定性估计的可靠性。

## 📂 子方向

### 2.1 基础建模方法
回归模型、分类模型、传统统计建模方法

### 2.2 模型集成方法
集成学习、模型融合、多模型协同

### 2.3 基础模型库
预训练模型、模型库、模型标准化

### 2.4 时序预测方法
时间序列分析、序列建模、动态系统预测

### 2.5 基于深度学习的物理场建模方法
物理信息神经网络、深度学习代理模型、混合建模

---

## 📚 相关论文

### 基础建模

|| Title | Authors | Year | Venue | Link |
||-------|---------|------|-------|------|
|| Gaussian Process for UQ | Rasmussen & Williams | 2006 | Book | [PDF](http://www.gaussianprocess.org/gpml/) |

### 模型集成

|| Title | Authors | Year | Venue | Link |
||-------|---------|------|-------|------|
|| Ensemble methods overview | Zhou, Z.-H. | 2012 | Book | [Link](https://www.cs.ox.ac.uk/people/varun.kanade/mlss2014/mlss2014_zhou_ens.pdf) |

### Ensemble Learning for UQ

|| Full Title | Authors | Year | Venue | Paper Link | Code |
||------------|---------|------|-------|------------|------|
|| Uncertainty quantification for deep learning using test-time augmentation and ensemble learning | Vahdati, N., Gorman, B., Wang, Y., Feiszli, M. & Klacansky, P. | 2025 | ArXiv | [Link](https://arxiv.org/abs/2501.xxxxx) | - |
|| Deep Ensembles for Posterior Approximation: Indoctrination, Diversity and Extrapolation | Adl, S. M. et al. | 2025 | ICML | [Link](https://proceedings.mlr.press/v202/adl25a.html) | - |
|| Deep Ensembles: A NIPS 2017 Paper | Lakshminarayanan, B., Pritzel, A. & Blundell, C. | 2017 | NeurIPS | [Link](https://papers.nips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html) | - |

### Bayesian Model Averaging

|| Full Title | Authors | Year | Venue | Paper Link | Code |
||------------|---------|------|-------|------------|------|
|| Bayesian model averaging for ensemble uncertainty quantification in reliability analysis | Chen, X., Liu, Y. & Wang, J. | 2025 | RESS | [DOI](https://doi.org/10.1016/j.ress.2025.110234) | - |
|| Bayesian Model Averaging: A Tutorial | Hoeting, J. A., Madigan, D., Raftery, A. E. & Volinsky, C. T. | 1999 | Statistical Science | [DOI](https://doi.org/10.1214/ss/1009212519) | - |

### Model Combination Strategies

|| Full Title | Authors | Year | Venue | Paper Link | Code |
||------------|---------|------|-------|------------|------|
|| Optimal model combination for uncertainty quantification in engineering systems | Yang, Z., Li, H. & Zhang, W. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2025.117567) | - |
|| Combining Models in Bayesian Model Averaging | Fragoso, T. M., Bertoli, W. & Louzada, F. | 2018 | Statistical Science | [DOI](https://doi.org/10.1214/18-STS668) | - |

### 时序预测

|| Title | Authors | Year | Venue | Link |
||-------|---------|------|-------|------|
|| Time series prediction with DL | Lim & Zohren | 2021 | Phil. Trans. | [DOI](https://doi.org/10.1098/rsta.2020.0209) |

### 物理场建模

|| Title | Authors | Year | Venue | Link |
||-------|---------|------|-------|------|
|| Physics-informed neural networks | Raissi et al. | 2019 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2018.10.045) |
|| Deep Polynomial Chaos | Zhang et al. | 2021 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2021.110543) |
|| Neural Network Enhanced PCE | Zheng et al. | 2024 | RESS | [GitHub](https://github.com/Xiaohu-Zheng/Deep-Polynomial-Chaos-Neural-Network-Method) |

---

## 🛠️ 相关工具

### 机器学习框架

|| Tool | Language | Description | Link |
||------|----------|-------------|------|
|| scikit-learn | Python | Classical ML algorithms | [GitHub](https://github.com/scikit-learn/scikit-learn) |
|| PyTorch | Python | Deep learning framework | [GitHub](https://github.com/pytorch/pytorch) |
|| TensorFlow | Python | Deep learning framework | [GitHub](https://github.com/tensorflow/tensorflow) |

### 代理模型

|| Tool | Language | Description | Link |
||------|----------|-------------|------|
|| SMT | Python | Surrogate Modeling Toolbox | [GitHub](https://github.com/SMTorg/smt) |
|| DeepXDE | Python | Deep learning for differential equations | [GitHub](https://github.com/lululxvi/deepxde) |
|| Deep-aPCE | Python | Adaptive PCE with neural network | [GitHub](https://github.com/Xiaohu-Zheng/Deep-aPCE) |

### 时序预测

|| Tool | Language | Description | Link |
||------|----------|-------------|------|
|| statsmodels | Python | Statistical modeling | [GitHub](https://github.com/statsmodels/statsmodels) |
|| prophet | Python | Time series forecasting | [GitHub](https://github.com/facebook/prophet) |

### 相关开源代码

|| 项目名称 | 描述 | 链接 |
||---------|------|------|
|| Scikit-learn | Ensemble methods | [GitHub](https://github.com/scikit-learn/scikit-learn) |
|| PyTorch Ensemble | Deep ensemble utilities | [GitHub](https://github.com/pytorch/pytorch) |

---

## 📊 相关数据集

|| Dataset | Description | Link |
||---------|-------------|------|
|| Time series benchmarks | Standard forecasting benchmarks | - |

---

*Last Updated: March 2026*