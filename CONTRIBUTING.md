# Contributing Guidelines

Welcome to the ET6-CDSP Group 21 project! We're excited to collaborate with you.

This guide explains how to set up your environment,
follow our contribution workflow, and meet code/documentation
 standards so everything runs smoothly.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo.git
cd ET6-CDSP-group-21-repo
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install ruff pylint
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

  0_domain_study/
  1_datasets/
  2_data_preparation/
  3_data_exploration/
  4_data_analysis/
  5_communication_strategy/
  6_final_presentation/
  notes/

---

## Code Quality Checks

Before pushing code:

### Python

```bash
ruff format .
ruff check .
pylint **/*.py
```

### Markdown

CI automatically checks Markdown files for:

* Proper headings structure
* Line length (≤ 79 chars)
* Blank lines between sections/code blocks

---

## Commit & Push

```bash
git add .
git commit -m "Descriptive message: what/why"
git push origin your-branch-name
```

Then open a **Pull Request (PR)** on GitHub.

---

## Pull Request Guidelines

* **Link issues** using `#issue-number`
* **Assign reviewers**
* PR title: clear and concise (e.g., `Update POS tagging markdown formatting`)
* Ensure **CI passes** (Python + Markdown)
* Get at least **1 review** before merging

---

## Folder Usage

| Folder                      | Purpose                           |
| --------------------------- | --------------------------------- |
| `0_domain_study/`           | Domain research & context         |
| `1_datasets/`               | Raw & cleaned data files          |
| `2_data_preparation/`       | Scripts for cleaning, wrangling   |
| `3_data_exploration/`       | EDA notebooks and insights        |
| `4_data_analysis/`          | POS tagging, classification, etc. |
| `5_communication_strategy/` | Storytelling, visuals, summaries  |
| `6_final_presentation/`     | Final slides, project pitch       |
| `notes/`                    | Team notes, reflections           |

---

## Team Communication

* Use clear commit messages
* Respect peer review feedback
* Ask questions or pair-program if stuck
* Document major decisions

---

## Final Checklist

Before submitting a PR:

* [ ] CI checks are passing
* [ ] Markdown is formatted cleanly
* [ ] Code follows `ruff` and `pylint` standards
* [ ] Work is in the correct folder
* [ ] PR is linked to an issue or milestone

---

Thanks for contributing to **Group 21 – MIT Emerging Talent**! 🚀
Together, we're building meaningful insights from data.
