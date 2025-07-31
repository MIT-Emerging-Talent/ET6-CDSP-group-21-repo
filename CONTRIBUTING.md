# Contributing Guidelines

Welcome to the ET6-CDSP Group 21 project!

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&pause=1000&color=CF1F4E&width=435&lines=The+Hypatia+Circle)](https://git.io/typing-svg)
We're excited to collaborate with you.

This guide explains how to set up your environment,
follow our contribution workflow, and meet code/documentation
standards so everything runs smoothly.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo.git
cd ET6-CDSP-group-21-repo
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install ruff pylint nbqa black flake8
```

---

## 🔧 Development Environment

* **Python:** 3.8 or higher  
* **Preferred tools:** VSCode, Jupyter, or Google Colab  
* **Version Control:** Git & GitHub

---

## Workflow for Contributions

### 1. Branching

Before starting, create your feature or fix branch:

```bash
git checkout -b your-branch-name
```

> Name your branch clearly: `4-pos-tagging-update`, `fix-readme-link`, etc.

### 2. Make Your Changes

* Keep changes scoped to one issue/feature  
* Follow our folder structure for milestones:

```markdown
- `0_domain_study/`
- `1_datasets/`
- `2_data_preparation/`
- `3_data_exploration/`
- `4_data_analysis/`
- `5_communication_strategy/`
- `6_final_presentation/`
- `collaboration/`
```

---

## Code Quality Checks

### Python Scripts

Instead of formatting the entire repo,
format individual files to avoid accidental changes:

```bash
ruff format your_file.py
ruff check your_file.py
pylint your_file.py
```

### Jupyter Notebooks

Before pushing notebooks, run:

```bash
nbqa black your_notebook.ipynb
nbqa flake8 your_notebook.ipynb
```

Note: Conflicts between `ruff` and `flake8` can occur. If so:

* Run: `ruff format your_file.py --diff`  
* Manually apply `ruff` suggestions in a way that also satisfies `flake8`

### Markdown

CI will automatically check:

* Proper heading structure  
* Line length ≤ 79 characters  
* Blank lines between sections and code blocks

---

## Commit & Push

Use file-specific staging to avoid accidental changes:

```bash
git add path/to/your_file.py
git commit -m "Descriptive message: what/why"
git push origin your-branch-name
```

Then open a **Pull Request (PR)** on GitHub.

---

## Pull Request Guidelines

* **Link issues** using `#issue-number`  
* **Assign reviewers**  
* PR title should be clear (e.g., `Fix markdown formatting in POS tagging`)  
* Ensure **CI passes** for Python and Markdown  
* Request at least **1 team review** before merging

---

## Folder Usage

| Folder                             | Purpose                           |
| ---------------------------------- | --------------------------------- |
| [`0_domain_study/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/0_domain_study)                  | Domain research & context         |
| [`1_datasets/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/1_datasets)                      | Raw & cleaned data files          |
| [`2_data_preparation/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/2_data_preparation)              | Scripts for cleaning, wrangling   |
| [`3_data_exploration/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/3_data_exploration)             | EDA notebooks and insights        |
| [`4_data_analysis/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/4_data_analysis)                | POS tagging, classification, etc. |
| [`5_communication_strategy/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/5_communication_strategy)        | Storytelling, visuals, summaries  |
| [`6_final_presentation/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/6_final_presentation)            | Final slides, project pitch       |
| [`collaboration/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/collaboration) | Agreements, group norms, notes    |

---

## Team Communication

* Use clear and informative commit messages  
* Respect review feedback and coding styles  
* Pair program or ask questions if you're stuck  
* Document major changes/decisions clearly

---

## Final Checklist Before PR

* [ ] CI checks are passing  
* [ ] Markdown is well-formatted  
* [ ] Python follows `ruff`, `flake8`, and `pylint`  
* [ ] Notebooks are cleaned with `nbqa black` and `nbqa flake8`  
* [ ] Files are placed in the correct milestone folder  
* [ ] The PR links to an issue or milestone

---

Thanks for contributing to **Group 21 – MIT Emerging Talent**!  
