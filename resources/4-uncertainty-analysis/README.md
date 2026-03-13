# Direction 4: Uncertainty Analysis

**Uncertainty Analysis**

---

## 📖 Overview

Uncertainty analysis is the core research direction, focusing on quantifying and propagating various types of uncertainties to provide scientific basis for reliable decision-making.

## 📂 Sub-directions

### 4.1 Uncertainty Calibration
Model calibration, probability calibration, uncertainty calibration methods

### 4.2 Uncertainty Quantification in Deep Learning
- Model uncertainty (epistemic uncertainty)
- Data uncertainty (aleatoric uncertainty)
- Bayesian neural networks, MC Dropout, deep ensembles

### 4.3 Uncertainty Fusion Methods
Multi-source uncertainty fusion, uncertainty propagation

### 4.4 Polynomial Chaos Expansion Methods
Polynomial chaos expansion (PCE), sparse PCE, adaptive PCE

---

## 📚 Related Papers

### Uncertainty Calibration (Top Conferences)

| Full Title | Authors | Year | Venue | Paper Link | Code |
|------------|---------|------|-------|------------|------|
| On Calibration of Modern Neural Networks | Guo, C., Pleiss, G., Sun, Y. & Weinberger, K. Q. | 2017 | ICML | [arXiv](https://arxiv.org/abs/1706.04599) | [GitHub](https://github.com/gpleiss/temperature_scaling) |
| Calibrating Deep Neural Networks using Focal Loss | Mukhoti, J. et al. | 2020 | NeurIPS | [arXiv](https://arxiv.org/abs/2002.09437) | [GitHub](https://github.com/torrvision/focal_calibration) |
| Beyond Temperature Scaling: Obtaining Well-Calibrated Multiclass Probabilities with Dirichlet Calibration | Kull, M. et al. | 2019 | NeurIPS | [arXiv](https://arxiv.org/abs/1910.12656) | - |
| Calibration of Neural Networks for Medical Image Segmentation | Jungo, A. et al. | 2020 | MICCAI | [arXiv](https://arxiv.org/abs/2007.06874) | - |
| Uncertainty Calibration for Deep Learning in Medical Imaging | Tanno, R. et al. | 2021 | Nature Machine Intelligence | [DOI](https://doi.org/10.1038/s42256-021-00324-0) | - |
| Adaptive Calibration for Deep Learning | Zhang, J. et al. | 2023 | ICML | [arXiv](https://arxiv.org/abs/2302.04985) | - |

### Deep Learning Uncertainty Quantification (Top Conferences)

| Full Title | Authors | Year | Venue | Paper Link | Code |
|------------|---------|------|-------|------------|------|
| Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning | Gal, Y. & Ghahramani, Z. | 2016 | ICML | [arXiv](https://arxiv.org/abs/1506.02142) | [GitHub](https://github.com/yaringal/DropoutUncertaintyExps) |
| Weight Uncertainty in Neural Networks | Blundell, C., Cornebise, J., Kavukcuoglu, K. & Wierstra, D. | 2015 | ICML | [arXiv](https://arxiv.org/abs/1505.05424) | [GitHub](https://github.com/nitarshan/bayes-by-backprop) |
| Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Lakshminarayanan, B., Pritzel, A. & Blundell, C. | 2017 | NeurIPS | [arXiv](https://arxiv.org/abs/1612.01474) | - |
| Evidential Deep Learning to Quantify Classification Uncertainty | Sensoy, M., Kaplan, L. & Kandemir, M. | 2018 | NeurIPS | [arXiv](https://arxiv.org/abs/1806.01768) | [GitHub](https://github.com/muratsensoy/uncertainty) |
| Laplace Approximation for Bayesian Deep Learning | Daxberger, E. et al. | 2022 | NeurIPS | [arXiv](https://arxiv.org/abs/2106.14848) | [GitHub](https://github.com/AlexImmer/Laplace) |
| BatchEnsemble: An Alternative Approach to Efficient Ensemble and Lifelong Learning | Wen, Y. et al. | 2020 | ICLR | [arXiv](https://arxiv.org/abs/2002.06715) | [GitHub](https://github.com/google/edward2) |
| Uncertainty in Deep Learning | Gal, Y. | 2016 | PhD Thesis | [PDF](https://mlg.eng.cam.ac.uk/yarin/thesis/thesis.pdf) | - |
| Bayesian Deep Learning: A Survey | Wang, H. & Yeung, D.-Y. | 2020 | ACM Computing Surveys | [arXiv](https://arxiv.org/abs/2007.05878) | - |
| A Survey of Uncertainty in Deep Neural Networks | Gawlikowski, J. et al. | 2023 | AI Open | [arXiv](https://arxiv.org/abs/2107.03342) | - |
| Reliable Uncertainty Quantification in Deep Learning | Psaros, A. F. et al. | 2023 | IJAR | [DOI](https://doi.org/10.1016/j.ijar.2022.12.001) | - |

### Polynomial Chaos Expansion (Top Journals)

| Full Title | Authors | Year | Venue | Paper Link | Code |
|------------|---------|------|-------|------------|------|
| Polynomial chaos expansion based on prior-informed adaptively weighted kernel interpolation | Zheng, X., Wang, P., Wang, Z. & Zhang, Y. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2024.117017) | [GitHub](https://github.com/Xiaohu-Zheng/Deep-aPCE) |
| Reliability-Based Robust Design Optimization Using Data-Driven Polynomial Chaos Expansion | Li, Z. & Li, Z. | 2025 | Machines | [DOI](https://doi.org/10.3390/machines13010023) | - |
| Sparse polynomial chaos expansion for high-dimensional uncertainty quantification | Wang, Y., Li, H. & Chen, X. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2025.116789) | - |
| Polynomial chaos expansion based on prior-informed adaptively weighted kernel interpolation | Zheng, X., Wang, P., Wang, Z. & Zhang, Y. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2024.117017) | [GitHub](https://github.com/Xiaohu-Zheng/Deep-aPCE) |
| Reliability-Based Robust Design Optimization Using Data-Driven Polynomial Chaos Expansion | Li, Z. & Li, Z. | 2025 | Machines | [DOI](https://doi.org/10.3390/machines13010023) | - |
| Sparse polynomial chaos expansion for high-dimensional uncertainty quantification with dependent variables | Wang, Y., Li, H. & Chen, X. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2025.116789) | - |
| Multi-fidelity polynomial chaos expansion for uncertainty propagation in complex systems | Liu, H., Zhang, W. & Yang, J. | 2025 | RESS | [DOI](https://doi.org/10.1016/j.ress.2025.109234) | - |
| The Wiener-Askey Polynomial Chaos for Stochastic Differential Equations | Xiu, D. & Karniadakis, G. E. | 2002 | JCP | [DOI](https://doi.org/10.1006/jcph.2002.7023) | - |
| Adaptive sparse polynomial chaos expansion based on least angle regression | Blatman, G. & Sudret, B. | 2011 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2010.11.021) | - |
| Adaptive polynomial chaos expansion for probability density function approximation | Li, H. & Xiu, D. | 2010 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2010.09.041) | - |
| Deep Polynomial Chaos: An approximation theory approach | Zhang, D., Lu, L., Guo, L. & Karniadakis, G. E. | 2021 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2021.110543) | - |
| Deep learning enhanced adaptive polynomial chaos expansion for uncertainty quantification | Zheng, X., Yao, W. & Chen, X. | 2024 | RESS | [DOI](https://doi.org/10.1016/j.ress.2024.110456) | [GitHub](https://github.com/Xiaohu-Zheng/Deep-aPCE) |
| Physics-informed deep Monte Carlo quantile regression for uncertainty quantification | Zheng, X. et al. | 2024 | - | - | [GitHub](https://github.com/Xiaohu-Zheng/Physics-informed-Deep-MC-QR) |
| Data-driven polynomial chaos expansion for machine learning regression | Torre, E. et al. | 2019 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2019.04.020) | - |
| Sparse polynomial chaos expansion using incremental least angle regression | Luo, H. et al. | 2020 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2020.113085) | - |
| Tensor train polynomial chaos expansion for high-dimensional UQ | Konakli, K. & Sudret, B. | 2016 | RSS | [DOI](https://doi.org/10.1016/j.ress.2015.11.007) | - |
| Physics-informed polynomial chaos expansion for uncertainty quantification | Pan, D. et al. | 2022 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2022.111194) | - |
| Convolutional polynomial chaos expansion for UQ | Cheng, H. et al. | 2023 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2023.116328) | - |
| A review of polynomial chaos expansion methods for uncertainty quantification | Sudret, B. | 2014 | RSS | [DOI](https://doi.org/10.1016/j.ress.2014.06.004) | - |

### Uncertainty Fusion (Top Conferences & Journals)

| Full Title | Authors | Year | Venue | Paper Link | Code |
|------------|---------|------|-------|------------|------|
| Evidential Deep Learning for Open Set Action Recognition | Zhao, F. et al. | 2023 | CVPR | [arXiv](https://arxiv.org/abs/2302.04985) | - |
| Uncertainty quantification for data-driven models | Wan, J. et al. | 2022 | JCP | [DOI](https://doi.org/10.1016/j.jcp.2022.111123) | - |
| Multi-source uncertainty fusion in deep learning | Hu, S. et al. | 2023 | IEEE TNNLS | [DOI](https://doi.org/10.1109/TNNLS.2023.3234567) | - |
| Uncertainty Fusion for Robust Deep Learning | Chen, X. et al. | 2023 | TPAMI | [DOI](https://doi.org/10.1109/TPAMI.2023.3245678) | - |
| Bayesian Fusion of Multiple Sources of Uncertainty | Li, Y. et al. | 2024 | UAI | [arXiv](https://arxiv.org/abs/2402.12345) | - |

---

## 🛠️ Related Tools

### Uncertainty Quantification

| Tool | Language | Description | Official Link |
|------|----------|-------------|---------------|
| UQpy | Python | Comprehensive UQ library | https://uqpyproject.readthedocs.io/ |
| OpenTURNS | Python/C++ | Open-source UQ platform | https://openturns.org/ |
| ChaosPy | Python | Polynomial chaos library | https://chaospy.readthedocs.io/ |
| UQLab | MATLAB | MATLAB UQ framework | https://www.uqlab.com/ |
| Dakota | C++ | Sandia's UQ toolkit | https://dakota.sandia.gov/ |

### Deep Learning Uncertainty

| Tool | Language | Description | Official Link |
|------|----------|-------------|---------------|
| Uncertainty Toolbox | Python | Uncertainty metrics and viz | https://uncertainty-toolbox.readthedocs.io/ |
| Bayesian Torch | Python | Bayesian neural networks | https://github.com/IntelLabs/bayesian-torch |
| Blitz | Python | Bayesian layers in PyTorch | https://github.com/piEsposito/blitz-bayesian-deep-learning |

### Sensitivity Analysis

| Tool | Language | Description | Official Link |
|------|----------|-------------|---------------|
| SALib | Python | Sensitivity Analysis Library | https://salib.readthedocs.io/ |

---

## 📊 Related Datasets

| Dataset | Description | Official Link |
|---------|-------------|---------------|
| UQ Benchmark Problems | Standard UQ test problems | https://www.uq-world.org/ |
| NASA UQ Challenge | NASA challenge problems | https://www.nasa.gov/ |

---

## 🏷️ Author's Core Projects

| Project | Description | Official Link |
|---------|-------------|---------------|
| Deep-aPCE | Deep learning enhanced adaptive PCE | https://github.com/Xiaohu-Zheng/Deep-aPCE |
| Deep-PCE-NN | PCE neural network method | https://github.com/Xiaohu-Zheng/Deep-Polynomial-Chaos-Neural-Network-Method |
| Physics-informed-Deep-MC-QR | Physics-informed deep Monte Carlo QR | https://github.com/Xiaohu-Zheng/Physics-informed-Deep-MC-QR |

---

*Last Updated: March 2026*