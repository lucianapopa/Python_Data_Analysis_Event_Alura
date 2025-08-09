<!-- Banner -->
<p align="center">
  <img src="https://i.imgur.com/xOUAoGb.png" alt="Python Data Analysis Event - Alura" width="800" height="200">
</p>

<h1 align="center">📊 Python Data Analysis Event - Alura</h1>

<p align="center">
  <em>Exploring Python for data cleaning, visualization, and insights generation.</em>
</p>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  
  <a href="https://colab.research.google.com/github/lucianapopa/Python_Data_Analysis_Event_Alura/blob/main/notebooks/Class_01_Data_Analysis_Alura.ipynb">
    <img src="https://img.shields.io/badge/Open%20in-Colab-orange?logo=googlecolab&logoColor=white" alt="Open in Colab">
  </a>
  
  <img src="https://img.shields.io/github/last-commit/lucianapopa/Python_Data_Analysis_Event_Alura?label=Last%20update&color=brightgreen" alt="Last update">
  
  <a href="https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv">
    <img src="https://img.shields.io/badge/Dataset-salaries.csv-brightgreen" alt="Dataset link">
  </a>
  
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow" alt="Status">
</p>


---

## 🚀 Overview
This repository contains the code, notes, and datasets used during the **Data Analysis with Python** event hosted by [Alura](https://www.alura.com.br/).  
The project focuses on **practical applications of Python for data analysis**, covering data cleaning, transformation, and visualization techniques.

---

## 📅 Event Schedule
| Day | Topic |
|-----|-------|
| **Day 1** | Introduction to Python for Data Analysis |
| **Day 2** | Data Cleaning & Transformation |
| **Day 3** | Data Visualization with Matplotlib & Seaborn |
| **Day 4** | Insights & Conclusions |

---

## 🛠 Technologies & Libraries
- **Python 3.x** — Programming language used for data analysis
- [Pandas](https://pandas.pydata.org/) — Data manipulation & analysis
- [NumPy](https://numpy.org/) — Numerical computing
- [Matplotlib](https://matplotlib.org/) — Data visualization
- [Seaborn](https://seaborn.pydata.org/) — Statistical visualization
- [Google Colab](https://colab.research.google.com/) — Cloud-based interactive environment for running Python notebooks

---

## 📂 Repository Structure
```
📦 Python_Data_Analysis_Event_Alura
 ┣ 📁 data          → [salaries.csv](https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv)
 ┣ 📁 notebooks     → Google Colab notebooks with code and analysis
 ┣ 📁 images        → Charts and visualizations generated from the notebooks (coming soon)
 ┗ 📄 README.md     → Project documentation (this file)
```

---

## 💡 How to Run (Google Colab)

You can run this project directly in **Google Colab** — no installation required.

1. **Open the notebook in Google Colab** by clicking the badge below:  
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](PASTE_YOUR_NOTEBOOK_LINK_HERE)

2. *(Optional)* **Mount Google Drive** if your notebook needs to read/write files:  
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Dataset used in this project**:  
   The dataset is publicly available at:  
   [salaries.csv](https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv)  
   You can load it directly in your notebook using:
   ```python
   import pandas as pd
   url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
   df = pd.read_csv(url)
   df.head()
   ```

4. **Run the cells step-by-step** following the notebook instructions.

---

## 👩‍💻 About Me
Hi! I'm **Luciana Popa**, a Master's student in Data Analytics at **University of Niagara Falls Canada**, curious about **data analytics and visualization**.  
- 💼 Background in **Finance**
- 📊 Knowledge in **Python, SQL, Tableau, Power BI, Excel**  
- 🌎 Based in **Ontario, Canada**  
- 🔗 [LinkedIn](https://www.linkedin.com/in/luciana-popa/) | [GitHub](https://github.com/lucianapopa)

---

## 📌 Notes
- This repository is **for educational purposes** only.
- Contributions, feedback, and suggestions are welcome! Open an issue or submit a pull request.

---

<p align="center">
  Made with 💙 during the <a href="https://www.alura.com.br/imersao-dados-python">Python Data Analysis Event - Alura</a>
</p>
