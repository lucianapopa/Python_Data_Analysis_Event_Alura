<h1 align="center">📊 Python Data Analysis Event - Alura</h1>

<p align="center">
  <em>Exploring Python for data cleaning, visualization, and insights generation.</em>
</p>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">

  <a href="https://colab.research.google.com/github/lucianapopa/Python_Data_Analysis_Event_Alura/blob/main/notebooks/Classes_Alura.ipynb">
    <img src="https://img.shields.io/badge/Open%20in-Colab-orange?logo=googlecolab&logoColor=white" alt="Open in Colab">
  </a>

  <a href="https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv">
    <img src="https://img.shields.io/badge/Dataset-salaries.csv-brightgreen" alt="Dataset link">
  </a>

  <a href="https://python-data-analysis-event-alura.streamlit.app/">
  <img src="https://img.shields.io/badge/Live%20App-Streamlit-ff4b4b?logo=streamlit&logoColor=white" alt="Live Streamlit App">
</a>

  <img src="https://img.shields.io/badge/Status-Concluded-brightgreen" alt="Status: Concluded">

  <img src="https://img.shields.io/github/last-commit/lucianapopa/Python_Data_Analysis_Event_Alura?label=Last%20update&color=brightgreen" alt="Last update">

---

## 🚀 Overview
This repository contains my work from the **Data Analysis with Python** event by [Alura](https://www.alura.com.br/).  
I explored **data cleaning**, **transformations**, and **visualizations**, and wrapped up with a small **Streamlit** dashboard using the final processed dataset.

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
- **Python 3.11+**
- **Pandas**, **NumPy**
- **Plotly Express** (interactive visuals)
- **Streamlit** (dashboard)
- **Google Colab** (notebooks)
- (Extras used as needed: `pycountry`, etc.)

---

## 📂 Repository Structure

📦 Python_Data_Analysis_Event_Alura  

├─ app.py # Streamlit app

├─ requirements.txt # Exact versions for reproducibility

├─ final-dataset.csv.csv # Processed dataset used by the app (current filename)

├─ notebooks/ # Colab notebooks

│ └─ Classes_Alura.ipynb

└─ README.md

---

## 💡 How to Run (Google Colab)

You can run this project directly in **Google Colab** — no installation required.

1. **Open the notebook in Google Colab** by clicking the badge below:  
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lucianapopa/Python_Data_Analysis_Event_Alura/blob/main/notebooks/Classes_Alura.ipynb)

2. *(Optional)* **Mount Google Drive** if your notebook needs to read/write files:  
   ```python
   from google.colab import drive
   drive.mount('/content/drive')

   ```

3. **Dataset used in this project**:  
Source: Data Jobs — salaries.csv

Processed file used by the app: data/final_dataset.csv
Please review the original license/terms of use from the source.

Load directly in Python:

import pandas as pd
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)
df.head()

4. **Run the cells step-by-step** following the notebook instructions.

---

## 📊 Dashboard:

**🧭 Dashboard Overview:**

 🔗 [Salary Analysis Dashboard in the Data Field](https://python-data-analysis-event-alura.streamlit.app/)
       
  <p> <img width="701" height="869" alt="Captura de tela 2025-08-11 141129" src="https://github.com/user-attachments/assets/06e5eaee-cc7c-48c4-b658-c047af7e3755" /> </p>

**💭 Dashboard Insights:**

- When analysing the overall available information regarding salary and work information in data field, some insightful trends can be observed if analysing the pandemic (2020-2021) to the most recent period (2024-2025):

**_1. General Metrics (Annual Salary, USD)_**

  - Average and maximum salaries are **higher in 2024–2025** than in **2020–2021** (salaries are nominal USD, not inflation-adjusted). 
  
  - The total record count is much larger in 2024–2025; this may reflect **more rows collected** and does **not necessarily** mean industry headcount growth. Additionally, trends may also reflect changes in the sample mix (countries, roles, company sizes) across periods, not just time.
  
  - The most common job position **shifts** from **Data Scientist** (2020–2021) to **Software Engineer** (2024–2025).
  
  - The Max Salary number must be cautiously interpreted since it can be driven by a single extreme value (outlier).

> _2020-2021:_
  
  <p> <img width="1613" height="187" alt="2020-2021" src="https://github.com/user-attachments/assets/38d2c9b2-4055-4642-90fe-99414b4cd020" /> </p>

> _2024-2025:_
  
  <p> <img width="1650" height="179" alt="2024-2025" src="https://github.com/user-attachments/assets/cb973148-2980-4478-ab0f-e80cc59f722d" /> </p>

**_2. Work Type_**
  
  - In **2020–2021**, most roles were **Remote (~52%)** or **Hybrid (~32%)**.  
  
  - In **2024–2025**, **On-site** becomes the majority, while **Remote + Hybrid** together drop below 20%.  

> _2020-2021:_
    
  <p> <img width="1828" height="827" alt="2020_2021" src="https://github.com/user-attachments/assets/3ee98734-1001-40e6-bc01-fc5e4e3a79ab" /> </p>

> _2024-2025:_
    
   <p> <img width="1801" height="811" alt="2024_2025" src="https://github.com/user-attachments/assets/16b41f79-95fb-45dc-b8b1-4b25187c4f69" /> </p>

**_3. Geography (Average Salary Behavior per Country)_**

  - **North America** remains high in both periods. In the recent period, higher averages also **appear** in parts of **South America, Europe, Africa, and Oceania** in this sample.  
  
  - White areas are **missing data**, not zero. Country averages can be volatile with **small sample sizes**, so we must compare cautiously.

**_4. Salary Distribution_**

  - In both periods, salaries are **right-skewed**: most values fall in a lower band, with a **small number of very high earners** stretching the right tail (outliers).  
  
  - Most salaries fall between **$60k–$120k** in **2020–2021**, and **$100k–$200k** in **2024–2025**.  
  
  - Because of the right tail, the **mean (average) is pulled upward**. Therefore, the median better represents a typical salary than the mean.
  
  - When comparing the two periods, we must keep x-axis limits and bin width the same, otherwise apparent differences can be due to scale, not distribution changes.

---

## 👩‍💻 About Me
Hi! I'm **Luciana Popa**, a Master's student in Data Analytics at **University of Niagara Falls Canada**, curious about **data analytics and visualization**.  
- Background: **Finance**
- Tools: **Python, SQL, Tableau, Power BI, Excel**
- Location: **Ontario, Canada**
- 🔗 [LinkedIn](https://www.linkedin.com/in/luciana-popa/) | [GitHub](https://github.com/lucianapopa)

---

## 🙏 Acknowledgments
- **Alura** for the event and learning materials.
- Dataset by **guilhermeonrails**/data-jobs.

## 📌 Notes
- This repository is **for educational purposes** only.
- Contributions, feedback, and suggestions are welcome! Open an issue or submit a pull request.

---

<p align="center">
  Made with 💙 by Luciana Popa during the <a href="https://www.alura.com.br/imersao-dados-python">Python Data Analysis Event - Alura</a>
</p>
