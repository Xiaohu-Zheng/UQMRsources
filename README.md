# UQMRresources

<div align="center">

**Uncertainty Quantification & Multiscale Reliability Analysis Resources**

*Papers, Tools, Datasets, and Learning Materials*

[![GitHub stars](https://img.shields.io/github/stars/Xiaohu-Zheng/UQMRresources?style=flat-square)](https://github.com/Xiaohu-Zheng/UQMRresources/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Xiaohu-Zheng/UQMRresources?style=flat-square)](https://github.com/Xiaohu-Zheng/UQMRresources/network/members)
[![License](https://img.shields.io/github/license/Xiaohu-Zheng/UQMRresources?style=flat-square)](LICENSE)

</div>

---

## 📖 Introduction

This project systematically organizes academic papers, open-source tools, datasets, and learning resources in the field of **Uncertainty Quantification and Multiscale Reliability Analysis**, covering the complete research chain from data processing to reliability-based design.

```
┌─────────────────────────────────────────────────────────────┐
│         Uncertainty Quantification & Multiscale Reliability  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │ 1. Data      │───▶│ 2. Ensemble  │───▶│ 3. Uncertainty│   │
│  │ Processing   │    │ Modeling     │    │ Analysis ⭐   │   │
│  └──────────────┘    └──────────────┘    └──────────────┘   │
│         │                   │                   │            │
│         └───────────┬───────┴───────────────────┘            │
│                     ▼                                        │
│           ┌──────────────────┐                               │
│           │ 4. Multiscale    │                               │
│           │ Reliability      │                               │
│           └──────────────────┘                               │
│                     │                                        │
│                     ▼                                        │
│           ┌──────────────────┐                               │
│           │ 5. Uncertainty-  │                               │
│           │ Based Design     │                               │
│           └──────────────────┘                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Research Directions

---

## Direction 1: Data Processing and Analysis

**[📁 Full Documentation](resources/1-data-processing/)**

### 📖 Overview
Data processing and analysis is the foundational stage of uncertainty quantification and multiscale reliability analysis, providing high-quality input data for subsequent modeling and analysis.

### 📂 Sub-directions
- **1.1 Data Preprocessing Methods**: Data cleaning, feature extraction, missing value handling, outlier detection
- **1.2 Data Visualization Methods**: High-dimensional data visualization, uncertainty visualization, interactive visualization
- **1.3 Auto/Cross-Correlation Analysis Methods**: Autocorrelation analysis, cross-correlation analysis, time series correlation modeling

### 📄 Featured Papers (20+)

| Title | Authors | Year | Venue |
|-------|---------|------|-------|
| Data preprocessing for machine learning: A survey | Zhang, S. et al. | 2022 | IEEE TNNLS |
| A survey on missing data in machine learning | Emmanuel, T. et al. | 2021 | JMLR |
| Visualization of uncertainty: A survey | Potter, K. et al. | 2012 | IEEE TVCG |
| High-dimensional data visualization: A survey | Liu, S. et al. | 2017 | IEEE TVCG |
| Copula-based correlation analysis for UQ | Nelsen, R. B. | 2006 | Springer |

### 🛠️ Tools Quick Access

| Tool | Description | Link |
|------|-------------|------|
| pandas | Data manipulation and analysis | [pandas.pydata.org](https://pandas.pydata.org/) |
| numpy | Numerical computing | [numpy.org](https://numpy.org/) |
| scipy | Scientific computing | [scipy.org](https://scipy.org/) |
| scikit-learn | Machine learning preprocessing | [scikit-learn.org](https://scikit-learn.org/) |
| matplotlib | Visualization | [matplotlib.org](https://matplotlib.org/) |
| seaborn | Statistical visualization | [seaborn.pydata.org](https://seaborn.pydata.org/) |
| plotly | Interactive visualization | [plotly.com/python](https://plotly.com/python/) |
| bokeh | Interactive visualization | [bokeh.org](https://bokeh.org/) |
| altair | Declarative visualization | [altair-viz.github.io](https://altair-viz.github.io/) |
| statsmodels | Statistical analysis | [statsmodels.org](https://www.statsmodels.org/) |

### 📊 Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| UQ Benchmark Problems | Standard UQ test functions | [uq-world.org](https://www.uq-world.org/) |
| UCI ML Repository | Standard ML datasets | [archive.ics.uci.edu/ml](https://archive.ics.uci.edu/ml) |
| Kaggle Datasets | Diverse datasets | [kaggle.com/datasets](https://www.kaggle.com/datasets) |

---

## Direction 2: Ensemble Modeling

**[📁 Full Documentation](resources/2-ensemble-modeling/)**

### 📖 Overview
Ensemble modeling integrates multiple modeling approaches to construct unified prediction frameworks, serving as the core component connecting data processing and reliability analysis.

### 📂 Sub-directions
- **2.1 Basic Modeling Methods**: Regression models, classification models, traditional statistical modeling
- **2.2 Model Ensemble Methods**: Ensemble learning, model fusion, multi-model collaboration
- **2.3 Foundation Model Library**: Pre-trained models, model libraries, model standardization
- **2.4 Time Series Prediction Methods**: Time series analysis, sequence modeling, dynamic system prediction
- **2.5 Deep Learning-Based Physics Field Modeling**: Physics-informed neural networks, deep learning surrogate models

### 📄 Featured Papers (30+)

| Title | Authors | Year | Venue |
|-------|---------|------|-------|
| Gaussian Processes for Machine Learning | Rasmussen & Williams | 2006 | MIT Press |
| Deep Ensembles for Uncertainty Estimation | Fort, S. et al. | 2019 | NeurIPS |
| BatchEnsemble: Efficient Ensemble Learning | Wen, Y. et al. | 2020 | ICLR |
| Temporal Fusion Transformer | Lim, B. et al. | 2021 | IJF |
| N-BEATS: Neural basis expansion | Oreshkin, B. N. et al. | 2020 | ICLR |
| Physics-informed neural networks | Raissi, M. et al. | 2019 | JCP |
| Fourier Neural Operator | Li, Z. et al. | 2021 | ICLR |
| DeepONet: Learning nonlinear operators | Lu, L. et al. | 2021 | NMI |

### 🛠️ Tools Quick Access

| Tool | Description | Link |
|------|-------------|------|
| PyTorch | Deep learning framework | [pytorch.org](https://pytorch.org/) |
| TensorFlow | Deep learning framework | [tensorflow.org](https://www.tensorflow.org/) |
| scikit-learn | Classical ML algorithms | [scikit-learn.org](https://scikit-learn.org/) |
| SMT | Surrogate Modeling Toolbox | [smt.readthedocs.io](https://smt.readthedocs.io/) |
| DeepXDE | Deep learning for PDEs | [deepxde.readthedocs.io](https://deepxde.readthedocs.io/) |
| Deep-aPCE | Adaptive PCE with NN | [GitHub](https://github.com/Xiaohu-Zheng/Deep-aPCE) |
| prophet | Time series forecasting | [facebook.github.io/prophet](https://facebook.github.io/prophet/) |
| NeuralForecast | Neural forecasting models | [neuralforecast.readthedocs.io](https://nixtla.github.io/neuralforecast/) |

### 📊 Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| Monash Time Series Archive | Standard forecasting benchmarks | [forecastingdata.org](https://forecastingdata.org/) |

---

## Direction 3: Uncertainty Analysis ⭐ Core

**[📁 Full Documentation](resources/3-uncertainty-analysis/)**

### 📖 Overview
Uncertainty analysis is the core research direction, focusing on quantifying and propagating various types of uncertainties to provide scientific basis for reliable decision-making.

### 📂 Sub-directions
- **3.1 Uncertainty Calibration**: Model calibration, probability calibration, uncertainty calibration methods
- **3.2 Uncertainty Quantification in Deep Learning**: Model uncertainty (epistemic), data uncertainty (aleatoric), Bayesian neural networks, MC Dropout
- **3.3 Uncertainty Fusion Methods**: Multi-source uncertainty fusion, uncertainty propagation
- **3.4 Polynomial Chaos Expansion Methods**: PCE, sparse PCE, adaptive PCE

### 📄 Featured Papers (40+)

| Title | Authors | Year | Venue |
|-------|---------|------|-------|
| On Calibration of Modern Neural Networks | Guo, C. et al. | 2017 | ICML |
| Dropout as a Bayesian Approximation | Gal, Y. & Ghahramani, Z. | 2016 | ICML |
| Weight Uncertainty in Neural Networks | Blundell, C. et al. | 2015 | ICML |
| Simple and Scalable Predictive Uncertainty Estimation | Lakshminarayanan, B. et al. | 2017 | NeurIPS |
| Evidential Deep Learning to Quantify Classification Uncertainty | Sensoy, M. et al. | 2018 | NeurIPS |
| Laplace Approximation for Bayesian Deep Learning | Daxberger, E. et al. | 2022 | NeurIPS |
| The Wiener-Askey Polynomial Chaos for SDEs | Xiu, D. & Karniadakis, G. E. | 2002 | JCP |
| Deep Polynomial Chaos: An approximation theory approach | Zhang, D. et al. | 2021 | JCP |
| Deep learning enhanced adaptive PCE for UQ | Zheng, X. et al. | 2024 | RESS |
| A review of polynomial chaos expansion methods | Sudret, B. | 2014 | RESS |

### 🛠️ Tools Quick Access

| Tool | Description | Link |
|------|-------------|------|
| UQpy | Comprehensive UQ library | [uqpyproject.readthedocs.io](https://uqpyproject.readthedocs.io/) |
| OpenTURNS | Open-source UQ platform | [openturns.org](https://openturns.org/) |
| ChaosPy | Polynomial chaos library | [chaospy.readthedocs.io](https://chaospy.readthedocs.io/) |
| UQLab | MATLAB UQ framework | [uqlab.com](https://www.uqlab.com/) |
| Dakota | Sandia's UQ toolkit | [dakota.sandia.gov](https://dakota.sandia.gov/) |
| Uncertainty Toolbox | Uncertainty metrics and viz | [uncertainty-toolbox.readthedocs.io](https://uncertainty-toolbox.readthedocs.io/) |
| Bayesian Torch | Bayesian neural networks | [GitHub](https://github.com/IntelLabs/bayesian-torch) |
| Blitz | Bayesian layers in PyTorch | [GitHub](https://github.com/piEsposito/blitz-bayesian-deep-learning) |
| SALib | Sensitivity Analysis Library | [salib.readthedocs.io](https://salib.readthedocs.io/) |

### 📊 Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| UQ Benchmark Problems | Standard UQ test problems | [uq-world.org](https://www.uq-world.org/) |
| NASA UQ Challenge | NASA challenge problems | [nasa.gov](https://www.nasa.gov/) |

### 🏷️ Author's Core Projects

| Project | Description | Link |
|---------|-------------|------|
| Deep-aPCE | Deep learning enhanced adaptive PCE | [GitHub](https://github.com/Xiaohu-Zheng/Deep-aPCE) |
| Deep-PCE-NN | PCE neural network method | [GitHub](https://github.com/Xiaohu-Zheng/Deep-Polynomial-Chaos-Neural-Network-Method) |
| Physics-informed-Deep-MC-QR | Physics-informed deep Monte Carlo QR | [GitHub](https://github.com/Xiaohu-Zheng/Physics-informed-Deep-MC-QR) |

---

## Direction 4: Multiscale Reliability

**[📁 Full Documentation](resources/4-multiscale-reliability/)**

### 📖 Overview
Multiscale reliability analysis studies reliability assessment methods for complex systems across different temporal and spatial scales, covering key tasks such as anomaly detection, fault diagnosis, and remaining useful life prediction.

### 📂 Sub-directions
- **4.1 Anomaly Detection Methods**: Statistical process control, machine learning anomaly detection
- **4.2 Bayesian Compression Modeling**: Bayesian inference, variational inference, model compression
- **4.3 Fault Diagnosis Methods**: Fault detection, fault classification, root cause analysis
- **4.4 Remaining Useful Life Prediction**: RUL prediction, degradation modeling, reliability prediction

### 📄 Featured Papers (35+)

| Title | Authors | Year | Venue |
|-------|---------|------|-------|
| Anomaly detection: A survey | Chandola, V. et al. | 2009 | ACM Computing Surveys |
| Deep learning for anomaly detection: A review | Pang, G. et al. | 2021 | IEEE TKDE |
| Deep Autoencoding Gaussian Mixture Model | Zong, B. et al. | 2018 | ICLR |
| Anomaly Transformer | Xu, J. et al. | 2022 | ICLR |
| TimesNet: Temporal 2D-Variation Modeling | Wu, H. et al. | 2023 | ICLR |
| Deep learning for fault diagnosis: A survey | Zhao, R. et al. | 2019 | IEEE TIE |
| Remaining useful life prediction: A review | Si, X.-S. et al. | 2011 | EJOR |
| Deep learning for RUL prediction: A review | Zhang, C. et al. | 2022 | RESS |

### 🛠️ Tools Quick Access

| Tool | Description | Link |
|------|-------------|------|
| PyOD | Python outlier detection | [pyod.readthedocs.io](https://pyod.readthedocs.io/) |
| Alibi Detect | Anomaly detection | [docs.seldon.io/alibi-detect](https://docs.seldon.io/projects/alibi-detect/) |
| OpenSees | Earthquake engineering + reliability | [opensees.berkeley.edu](https://opensees.berkeley.edu/) |
| FERUM | Finite Element Reliability | [ferum.sourceforge.net](https://ferum.sourceforge.net/) |
| UQMRLib | AI-enhanced UQ & Reliability | [GitHub](https://github.com/Xiaohu-Zheng/UQMRLib) |

### 📊 Datasets

| Dataset | Description | Link |
|---------|-------------|------|
| NASA Bearing Dataset | Bearing degradation data | [NASA Repository](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/) |
| PHM Challenge | Prognostics and health management | [phmsociety.org](https://phmsociety.org/) |
| C-MAPSS | Turbofan engine degradation | [NASA Repository](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/) |
| FEMTO Bearing | Bearing accelerated life tests | [femto-st.fr](https://www.femto-st.fr/) |

---

## Direction 5: Uncertainty-Based Design

**[📁 Full Documentation](resources/5-uncertainty-design/)**

### 📖 Overview
Uncertainty-based design integrates uncertainty quantification methods into the design optimization process to achieve robustness and reliability-driven engineering design.

### 📂 Sub-directions
- **5.1 Generative Design Methods**: Generative models, design space exploration, topology optimization
- **5.2 Generative Robust Optimization Methods**: Robust optimization, robust design, optimization under uncertainty
- **5.3 Generative Reliability-Based Optimization Methods**: Reliability optimization, RBDO

### 📄 Featured Papers (28+)

| Title | Authors | Year | Venue |
|-------|---------|------|-------|
| Robust optimization: A survey | Bertsimas, D. et al. | 2011 | Mathematical Programming |
| Robust design optimization: A comprehensive survey | Beyer, H.-G. & Sendhoff, B. | 2007 | CMAME |
| Reliability-based design optimization: A historical perspective | Yao, W. et al. | 2019 | MSSP |
| RBDO: A review | Aoues, Y. & Chateauneuf, A. | 2010 | Structural Safety |
| Deep generative models for design: A review | Rego, R. et al. | 2022 | JMD |
| Data-driven topology optimization using GANs | Oh, S. et al. | 2019 | CMAME |
| Surrogate-assisted RBDO: A review | Zhou, M. et al. | 2023 | Structural Safety |

### 🛠️ Tools Quick Access

| Tool | Description | Link |
|------|-------------|------|
| Pyomo | Optimization modeling | [pyomo.org](https://www.pyomo.org/) |
| SciPy Optimize | Optimization algorithms | [docs.scipy.org/optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html) |
| NLopt | Nonlinear optimization | [nlopt.readthedocs.io](https://nlopt.readthedocs.io/) |
| Dakota | Optimization + UQ toolkit | [dakota.sandia.gov](https://dakota.sandia.gov/) |
| OpenSees | Reliability analysis + RBDO | [opensees.berkeley.edu](https://opensees.berkeley.edu/) |
| UQMRLib | AI-enhanced reliability optimization | [GitHub](https://github.com/Xiaohu-Zheng/UQMRLib) |
| GPyTorch | Gaussian processes | [gpytorch.ai](https://gpytorch.ai/) |
| PyTorch Lightning | Deep learning framework | [lightning.ai](https://lightning.ai/) |

### 🏷️ Author's Project

| Project | Description | Link |
|---------|-------------|------|
| missile-design-optimization | Missile design optimization | [GitHub](https://github.com/Xiaohu-Zheng/missile-design-optimization) |

---

## 📊 Resources Summary

### By Content Type

| Type | Count | Top Venues |
|------|-------|------------|
| 📄 Papers | **150+** | ICML, NeurIPS, ICLR, UAI, CVPR, KDD, AAAI, RESS, MSSP, CMAME, JCP, TPAMI, NMI |
| 🛠️ Tools | **35+** | Python, MATLAB, C++ libraries |
| 📊 Datasets | **10+** | NASA, PHM, UCI, Kaggle |

### By Direction

| Direction | Papers | Tools | Datasets |
|-----------|--------|-------|----------|
| 1. Data Processing | 20+ | 10 | 3 |
| 2. Ensemble Modeling | 30+ | 8 | 1 |
| 3. Uncertainty Analysis ⭐ | 40+ | 9 | 2 |
| 4. Multiscale Reliability | 35+ | 5 | 4 |
| 5. Uncertainty-Based Design | 28+ | 8 | - |

### By Keywords

| Keyword | Direction | Papers |
|---------|-----------|--------|
| Polynomial Chaos Expansion (PCE) | Direction 3 | 12+ |
| Deep Learning Uncertainty | Direction 3 | 15+ |
| Physics-Informed Neural Networks | Direction 2 | 10+ |
| Reliability-Based Design Optimization | Direction 5 | 10+ |
| Remaining Useful Life (RUL) | Direction 4 | 10+ |
| Anomaly Detection | Direction 4 | 10+ |
| Time Series Forecasting | Direction 2 | 8+ |

---

## 📚 Shared Resources

| Resource | Description | Link |
|----------|-------------|------|
| Books & Tutorials | Textbooks, courses, tutorials | [books-tutorials.md](shared/books-tutorials.md) |
| Conferences & Journals | Core journals and conferences | [conferences-journals.md](shared/conferences-journals.md) |
| Research Groups | Global research institutions | [research-groups.md](shared/research-groups.md) |

---

## 🚀 Quick Start

### For Beginners
1. 📖 Read [Direction 3: Uncertainty Analysis](resources/3-uncertainty-analysis/)
2. 🛠️ Use [UQpy](https://uqpyproject.readthedocs.io/) or [ChaosPy](https://chaospy.readthedocs.io/)
3. 📚 Refer to [Books & Tutorials](shared/books-tutorials.md)

### For Researchers
1. 📰 Check [Conferences & Journals](shared/conferences-journals.md)
2. 🔬 Browse [Research Groups](shared/research-groups.md)
3. 🛠️ Explore tools in each direction

---

## 🤝 Contributing

Contributions welcome! Fork → Add → Submit PR

### Paper Format
`| Full Title | Authors | Year | Venue | Paper Link | Code |`

---

## 📝 Citation

```bibtex
@misc{uqmrresources,
  author = {Zheng, Xiaohu},
  title = {UQMRresources: Papers and Resources for UQ and Multiscale Reliability},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Xiaohu-Zheng/UQMRresources}
}
```

---

## 📧 Contact

- **Author**: Xiaohu Zheng
- **GitHub**: [Xiaohu-Zheng](https://github.com/Xiaohu-Zheng)

---

<div align="center">

**⭐ If helpful, please Star!**

</div>
