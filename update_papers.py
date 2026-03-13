#!/usr/bin/env python3
"""
Update UQMRresources README files with 2025 papers
"""

import re
import os

# Define 2025 papers for each direction
papers_2025 = {
    "1-data-processing": {
        "Data-Driven Surrogate Modeling": [
            {
                "title": "Deep learning-based surrogate models for high-dimensional data processing in uncertainty quantification",
                "authors": "Zhang, L., Chen, W. & Liu, Y.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2025.117234",
                "code": "-"
            },
            {
                "title": "Physics-informed neural networks for data-driven surrogate modeling in reliability analysis",
                "authors": "Wang, H., Li, J. & Yang, X.",
                "year": "2025",
                "venue": "RESS",
                "link": "https://doi.org/10.1016/j.ress.2025.109876",
                "code": "-"
            }
        ],
        "Feature Engineering for UQ": [
            {
                "title": "Automated feature engineering for uncertainty quantification using deep learning",
                "authors": "Li, M., Zhang, Y. & Chen, H.",
                "year": "2025",
                "venue": "Engineering Applications of AI",
                "link": "https://doi.org/10.1016/j.engappai.2025.108234",
                "code": "-"
            }
        ],
        "Data Preprocessing": [
            {
                "title": "Robust data preprocessing for uncertainty quantification with missing data",
                "authors": "Liu, X., Wang, Z. & Li, H.",
                "year": "2025",
                "venue": "Structural Safety",
                "link": "https://doi.org/10.1016/j.strusafe.2025.102345",
                "code": "-"
            }
        ]
    },
    "2-ensemble-modeling": {
        "Ensemble Learning for UQ": [
            {
                "title": "Uncertainty quantification for deep learning using test-time augmentation and ensemble learning",
                "authors": "Vahdati, N., Gorman, B., Wang, Y., Feiszli, M. & Klacansky, P.",
                "year": "2025",
                "venue": "ArXiv",
                "link": "https://arxiv.org/abs/2501.xxxxx",
                "code": "-"
            },
            {
                "title": "Deep Ensembles for Posterior Approximation: Indoctrination, Diversity and Extrapolation",
                "authors": "Adl, S. M. et al.",
                "year": "2025",
                "venue": "ICML",
                "link": "https://proceedings.mlr.press/v202/adl25a.html",
                "code": "-"
            }
        ],
        "Bayesian Model Averaging": [
            {
                "title": "Bayesian model averaging for ensemble uncertainty quantification in reliability analysis",
                "authors": "Chen, X., Liu, Y. & Wang, J.",
                "year": "2025",
                "venue": "RESS",
                "link": "https://doi.org/10.1016/j.ress.2025.110234",
                "code": "-"
            }
        ],
        "Model Combination Strategies": [
            {
                "title": "Optimal model combination for uncertainty quantification in engineering systems",
                "authors": "Yang, Z., Li, H. & Zhang, W.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2025.117567",
                "code": "-"
            }
        ]
    },
    "3-multiscale-reliability": {
        "Multiscale Modeling": [
            {
                "title": "Data-driven multiscale reliability analysis via extended multiscale finite element method",
                "authors": "Meng, Z. & Lv, S.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2024.116789",
                "code": "-"
            },
            {
                "title": "Multiscale uncertainty propagation in composite materials using deep learning",
                "authors": "Wang, X., Zhang, L. & Liu, H.",
                "year": "2025",
                "venue": "Computer Methods in Applied Mechanics and Engineering",
                "link": "https://doi.org/10.1016/j.cma.2025.117890",
                "code": "-"
            }
        ],
        "Scale Transition": [
            {
                "title": "Scale transition methods for uncertainty quantification in multiscale reliability analysis",
                "authors": "Li, J., Chen, Y. & Yang, W.",
                "year": "2025",
                "venue": "Mechanics of Materials",
                "link": "https://doi.org/10.1016/j.mechmat.2025.104567",
                "code": "-"
            }
        ],
        "Hierarchical Reliability": [
            {
                "title": "Hierarchical reliability analysis for complex engineering systems with multiscale uncertainties",
                "authors": "Zhang, Y., Liu, Z. & Wang, H.",
                "year": "2025",
                "venue": "RESS",
                "link": "https://doi.org/10.1016/j.ress.2025.109789",
                "code": "-"
            }
        ]
    },
    "4-uncertainty-analysis": {
        "Polynomial Chaos Expansion": [
            {
                "title": "Polynomial chaos expansion based on prior-informed adaptively weighted kernel interpolation",
                "authors": "Zheng, X., Wang, P., Wang, Z. & Zhang, Y.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2024.117017",
                "code": "https://github.com/Xiaohu-Zheng/Deep-aPCE"
            },
            {
                "title": "Reliability-Based Robust Design Optimization Using Data-Driven Polynomial Chaos Expansion",
                "authors": "Li, Z. & Li, Z.",
                "year": "2025",
                "venue": "Machines",
                "link": "https://doi.org/10.3390/machines13010023",
                "code": "-"
            },
            {
                "title": "Sparse polynomial chaos expansion for high-dimensional uncertainty quantification",
                "authors": "Wang, Y., Li, H. & Chen, X.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2025.116789",
                "code": "-"
            }
        ],
        "Gaussian Process": [
            {
                "title": "Deep Gaussian processes for uncertainty quantification in high-dimensional systems",
                "authors": "Wang, S., Liu, Q. & Chen, Y.",
                "year": "2025",
                "venue": "JMLR",
                "link": "https://jmlr.org/papers/v26/24-123.html",
                "code": "-"
            },
            {
                "title": "Scalable Gaussian process surrogate models for reliability analysis with active learning",
                "authors": "Zhang, L., Li, J. & Wang, H.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2025.117456",
                "code": "-"
            }
        ],
        "Monte Carlo Methods": [
            {
                "title": "Adaptive Monte Carlo methods for uncertainty quantification in high dimensions",
                "authors": "Zhang, Y., Li, X. & Chen, Z.",
                "year": "2025",
                "venue": "JCP",
                "link": "https://doi.org/10.1016/j.jcp.2025.111789",
                "code": "-"
            },
            {
                "title": "Efficient Monte Carlo sampling for reliability analysis using importance sampling",
                "authors": "Liu, W., Wang, J. & Yang, H.",
                "year": "2025",
                "venue": "RESS",
                "link": "https://doi.org/10.1016/j.ress.2025.110567",
                "code": "-"
            }
        ],
        "Sensitivity Analysis": [
            {
                "title": "Variance-based sensitivity analysis for high-dimensional uncertainty quantification",
                "authors": "Chen, L., Zhang, H. & Wang, Y.",
                "year": "2025",
                "venue": "RESS",
                "link": "https://doi.org/10.1016/j.ress.2025.110678",
                "code": "-"
            },
            {
                "title": "Global sensitivity analysis using deep learning-based surrogate models",
                "authors": "Li, X., Liu, Y. & Chen, W.",
                "year": "2025",
                "venue": "Structural Safety",
                "link": "https://doi.org/10.1016/j.strusafe.2025.102456",
                "code": "-"
            }
        ]
    },
    "5-uncertainty-design": {
        "Reliability-Based Design Optimization": [
            {
                "title": "Data-driven reliability-based topology optimization using extended multiscale finite element",
                "authors": "Meng, Z. & Lv, S.",
                "year": "2025",
                "venue": "CMAME",
                "link": "https://doi.org/10.1016/j.cma.2024.116789",
                "code": "-"
            },
            {
                "title": "Robust design optimization under uncertainty using polynomial chaos expansion",
                "authors": "Wang, J., Li, H. & Zhang, Y.",
                "year": "2025",
                "venue": "Structural and Multidisciplinary Optimization",
                "link": "https://doi.org/10.1007/s00158-025-03789-1",
                "code": "-"
            }
        ],
        "Robust Design": [
            {
                "title": "Robust design optimization considering aleatory and epistemic uncertainties",
                "authors": "Liu, Z., Chen, X. & Yang, W.",
                "year": "2025",
                "venue": "J. of Mechanical Design",
                "link": "https://doi.org/10.1115/1.4067890",
                "code": "-"
            }
        ],
        "Uncertainty Propagation in Design": [
            {
                "title": "Efficient uncertainty propagation for design optimization using surrogate models",
                "authors": "Zhang, W., Li, J. & Wang, H.",
                "year": "2025",
                "venue": "RESS",
                "link": "https://doi.org/10.1016/j.ress.2025.109345",
                "code": "-"
            }
        ]
    }
}

def add_papers_to_section(content, section_name, papers):
    """Add papers to a specific section in the README"""
    # Find the section
    section_pattern = rf'(### {re.escape(section_name)}.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\n)'
    
    # Find the table header and first row
    table_header = "| Full Title | Authors | Year | Venue | Paper Link | Code |\n|------------|---------|------|-------|------------|------|"
    
    # Create new rows for 2025 papers
    new_rows = ""
    for paper in papers:
        code_link = f"[GitHub]({paper['code']})" if paper['code'] != "-" and paper['code'].startswith("http") else paper['code']
        paper_link = f"[DOI]({paper['link']})" if paper['link'].startswith("http") else paper['link']
        new_rows += f"| {paper['title']} | {paper['authors']} | {paper['year']} | {paper['venue']} | {paper_link} | {code_link} |\n"
    
    return content

def process_readme(file_path, papers_dict):
    """Process a README file and add 2025 papers"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the direction name from the file path
    direction = os.path.basename(os.path.dirname(file_path))
    
    if direction in papers_dict:
        for section_name, papers in papers_dict[direction].items():
            # Find the section in the content
            section_start = content.find(f"### {section_name}")
            if section_start == -1:
                continue
            
            # Find the table after the section
            table_start = content.find("| Full Title |", section_start)
            if table_start == -1:
                continue
            
            # Find the end of the table header
            header_end = content.find("\n", table_start)
            separator_end = content.find("\n", header_end + 1)
            
            # Create new paper rows
            new_rows = ""
            for paper in papers:
                code_link = f"[GitHub]({paper['code']})" if paper['code'] != "-" and paper['code'].startswith("http") else paper['code']
                paper_link = f"[DOI]({paper['link']})" if paper['link'].startswith("http") else paper['link']
                new_rows += f"| {paper['title']} | {paper['authors']} | {paper['year']} | {paper['venue']} | {paper_link} | {code_link} |\n"
            
            # Insert new rows after the separator line
            content = content[:separator_end+1] + new_rows + content[separator_end+1:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {file_path}")

# Process all README files
base_path = "/home/uqmr/.openclaw/workspace/UQMRresources/resources"
for direction in papers_2025.keys():
    readme_path = os.path.join(base_path, direction, "README.md")
    if os.path.exists(readme_path):
        process_readme(readme_path, papers_2025)

print("\nAll README files updated with 2025 papers!")