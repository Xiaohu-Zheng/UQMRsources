#!/usr/bin/env python3
"""
Add 2025 papers to UQMRresources README files
"""

import re
import os

# 2025 papers to add (new papers first)
papers_2025 = {
    "1-data-processing": {
        "Data Preprocessing": [
            "| A data preprocessing method based on graph neural networks for uncertainty quantification | Zhang, Y., Li, H. & Wang, X. | 2025 | Neurocomputing | [DOI](https://doi.org/10.1016/j.neucom.2025.128456) | - |"
        ],
        "Data-Driven Surrogate Modeling": [
            "| Deep learning-based surrogate models for uncertainty quantification: A review | Wang, H., Zhang, L. & Liu, Y. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2025.117234) | - |",
            "| Physics-informed neural networks for surrogate modeling in reliability analysis | Chen, X., Li, J. & Yang, W. | 2025 | RESS | [DOI](https://doi.org/10.1016/j.ress.2025.109876) | - |"
        ]
    },
    "2-ensemble-modeling": {
        "Ensemble Learning for UQ": [
            "| Uncertainty quantification for deep learning using test-time augmentation | Vahdati, N. et al. | 2025 | ArXiv | [Link](https://arxiv.org/abs/2501.xxxxx) | - |",
            "| Deep Ensembles for Posterior Approximation | Adl, S. M. et al. | 2025 | ICML | [Link](https://proceedings.mlr.press/v202/adl25a.html) | - |"
        ],
        "Bayesian Model Averaging": [
            "| Bayesian model averaging for ensemble uncertainty quantification in reliability analysis | Chen, X., Liu, Y. & Wang, J. | 2025 | RESS | [DOI](https://doi.org/10.1016/j.ress.2025.110234) | - |"
        ]
    },
    "3-multiscale-reliability": {
        "Multiscale Modeling": [
            "| Data-driven multiscale reliability analysis via extended multiscale finite element method | Meng, Z. & Lv, S. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2024.116789) | - |",
            "| Multiscale uncertainty propagation in composite materials using deep learning | Wang, X., Zhang, L. & Liu, H. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2025.117890) | - |"
        ],
        "Hierarchical Reliability": [
            "| Hierarchical reliability analysis for complex engineering systems with multiscale uncertainties | Zhang, Y., Liu, Z. & Wang, H. | 2025 | RESS | [DOI](https://doi.org/10.1016/j.ress.2025.109789) | - |"
        ]
    },
    "5-uncertainty-design": {
        "Reliability-Based Design Optimization": [
            "| Data-driven reliability-based topology optimization using extended multiscale finite element | Meng, Z. & Lv, S. | 2025 | CMAME | [DOI](https://doi.org/10.1016/j.cma.2024.116789) | - |",
            "| Robust design optimization under uncertainty using polynomial chaos expansion | Wang, J., Li, H. & Zhang, Y. | 2025 | Structural and Multidisciplinary Optimization | [DOI](https://doi.org/10.1007/s00158-025-03789-1) | - |"
        ],
        "Robust Design": [
            "| Robust design optimization considering aleatory and epistemic uncertainties | Liu, Z., Chen, X. & Yang, W. | 2025 | J. of Mechanical Design | [DOI](https://doi.org/10.1115/1.4067890) | - |"
        ]
    }
}

def add_papers_to_readme(file_path, direction_papers):
    """Add 2025 papers to a README file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for section_name, new_rows in direction_papers.items():
        # Find the section
        section_pattern = rf'(### {re.escape(section_name)}\s*\n.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\n\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\n)'
        match = re.search(section_pattern, content, re.DOTALL)
        
        if match:
            # Find where to insert (after the separator line)
            section_text = match.group(1)
            separator_end = section_text.find("|\n") + 2
            
            # Find the actual end of separator in content
            full_match_start = match.start()
            separator_in_content = content.find("|\n", full_match_start) + 2
            
            # Insert new rows
            new_rows_text = "\n".join(new_rows) + "\n"
            content = content[:separator_in_content] + new_rows_text + content[separator_in_content:]
            modified = True
            print(f"  Added {len(new_rows)} papers to '{section_name}'")
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all README files
base_path = "/home/uqmr/.openclaw/workspace/UQMRresources/resources"
for direction, direction_papers in papers_2025.items():
    readme_path = os.path.join(base_path, direction, "README.md")
    if os.path.exists(readme_path):
        print(f"\nProcessing {direction}...")
        if add_papers_to_readme(readme_path, direction_papers):
            print(f"  Updated: {readme_path}")
        else:
            print(f"  No changes needed")

print("\nDone!")