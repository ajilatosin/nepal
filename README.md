# Nepal Earthquake Building Damage Prediction

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)
![Logistic Regression](https://img.shields.io/badge/Model-Logistic%20Regression-green.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

---

##  Overview

This project analyzes building damage caused by the **2015 Gorkha earthquake in Nepal**, focusing on buildings located in **district 36**.

Using structural and geographic building characteristics collected before the earthquake, the project predicts whether a building suffered **severe damage** (`damage_grade > 3`) using a **Logistic Regression** model implemented within a **scikit-learn pipeline**.

The model achieves approximately **71% accuracy**, outperforming the majority-class baseline.

---

##  Project Highlights

- ✅ Data extraction from an SQLite database
- ✅ Exploratory Data Analysis (EDA)
- ✅ Binary classification for severe building damage
- ✅ Handling imbalanced classes
- ✅ One-hot encoding and feature scaling
- ✅ Logistic Regression pipeline with scikit-learn
- ✅ Feature interpretation using odds ratios
- ✅ Model persistence using `joblib` and `pickle`

---

##  Dataset

The SQLite database (`nepal_eq.db`) contains three primary tables:

| Table | Description |
|---|---|
| `id_map` | Mapping of building IDs to district IDs |
| `building_structure` | Pre-earthquake structural features |
| `building_damage` | Earthquake damage grades (1–5) |

Only records from **district 36** are used for this analysis.

---

##  Target Variable

The original target variable:

```python
damage_grade
```

is converted into a binary classification problem:

```python
severe_damage = 1 if damage_grade > 3 else 0
```

### Class Distribution

- Severe damage: **63.7%**
- Non-severe damage: **36.3%**

This indicates an **imbalanced dataset**, making baseline evaluation important.

---

##  Features

All features are based on **pre-earthquake building attributes**. Any columns containing `post_eq` are removed.

| Feature | Type | Description |
|---|---|---|
| `age_building` | Numeric | Building age in years |
| `foundation_type` | Categorical | Foundation material/type |
| `ground_floor_type` | Categorical | Ground floor material |
| `height_ft_pre_eq` | Numeric | Building height in feet |
| `land_surface_condition` | Categorical | Flat, moderate slope, steep slope |
| `other_floor_type` | Categorical | Upper floor material |
| `plan_configuration` | Categorical | Building shape/layout |
| `plinth_area_sq_ft` | Numeric | Plinth area in square feet |
| `position` | Categorical | Building attachment position |
| `roof_type` | Categorical | Roof material |
| `superstructure` | Categorical | Main structural material |

---

##  Methodology

###  Data Wrangling

The preprocessing pipeline begins with SQL extraction and cleaning:

- SQL query joins the three database tables
- Records filtered for **district 36**
- Columns containing `"post_eq"` removed
- `damage_grade` converted to integer
- Binary target `severe_damage` created
- `count_floors_pre_eq` removed

---

##  Exploratory Data Analysis (EDA)

### Baseline Accuracy

Since the dataset is imbalanced, predicting the majority class gives:

| Metric | Value |
|---|---|
| Baseline Accuracy | 63.7% |

---

### Foundation Type vs Severe Damage

Average severe damage rate by foundation type:

| Foundation Type | Severe Damage Rate |
|---|---|
| RC | 2.7% |
| Mud mortar-Stone/Brick | 68.4% |
| Other | 80.1% |

### Key Insight

Buildings with **reinforced concrete (RC)** foundations are significantly more resistant to severe earthquake damage than buildings constructed with mud mortar or stone structures.

 A horizontal bar chart visualizing foundation type vs. severe damage rate is included in the notebook.

---

##  Preprocessing Pipeline

A complete **scikit-learn Pipeline** is used for preprocessing and modeling.

### Pipeline Components

| Step | Purpose |
|---|---|
| `OneHotEncoder` | Encodes categorical variables |
| `StandardScaler` | Scales numeric features |
| `LogisticRegression` | Binary classification model |

### Encoded Features

Categorical variables are transformed into binary columns while preserving feature names using `category_encoders`.

---


## Model Performance

| Metric | Value |
|---|---|
| Baseline Accuracy | 63.69% |
| Training Accuracy | 71.45% |
| Test Accuracy | 70.87% |

### Performance Summary

The Logistic Regression model improves performance by approximately **7 percentage points** over the baseline model, indicating that structural features are meaningful predictors of earthquake damage severity.

---

## Feature Importance (Odds Ratios)

Feature importance is interpreted using **odds ratios**:

```python
np.exp(coef)
```

---

### Features Increasing Severe Damage Risk

| Feature | Approx. Odds Ratio |
|---|---|
| `superstructure_mud_mortar_stone` | ~1.23 |
| `foundation_type_Mud mortar-Stone/Brick` | ~1.15 |
| `superstructure_stone_flag` | ~1.20 |

These features increase the probability of severe earthquake damage.

---

### Protective Features

| Feature | Approx. Odds Ratio |
|---|---|
| `foundation_type_RC` | 0.80 |
| `superstructure_cement_mortar_brick` | 0.77 |
| `roof_type_RCC/RB/RBC` | 0.83 |

These features reduce the likelihood of severe damage.

---


##  Usage

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Example `requirements.txt`

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
category_encoders
joblib
```

Additional built-in libraries used:

- `sqlite3`
- `collections.Counter`

---

###  Run the Notebook

Ensure the database file is available:

```text
nepal_eq.db
```

Run notebook cells sequentially.

---

###  Load and Predict on New Data

```python
import joblib

model = joblib.load('nepal_model.pkl')

pred = model.predict(X_new)
```

> `X_new` must contain the same columns used during training.

---

## File Structure

```text
.
├── nepal2.ipynb               # Main analysis notebook
├── nepal_eq.db                # SQLite database (not included in repo)
├── nepal_model.pkl            # Saved pipeline (joblib)
├── model.pkl                  # Saved pipeline (pickle)
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Category Encoders
- SQLite
- Joblib

---
.
