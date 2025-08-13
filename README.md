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
</p>


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

├─ final-dataset_GoogleColab.csv # Processed dataset created using Google Colab and used by the app

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

Processed file used by the app: final-dataset.csv
Please review the original license/terms of use from the source.

**Load directly in Python:**

python

import pandas as pd
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)
df.head()


4. **Run the cells step-by-step** following the notebook instructions.

---

## 📓 Notebook Highlights

- In this section I include a few key visuals produced in Google Colab analyzing the data for the whole period (2020-2025) before building the Streamlit dashboard on VS Code. The values shown are **nominal USD**.

**_1. Avg. Data Scientist Wage by Country_**

  - North America is highest, some Western Europe and Oceania countries also show higher averages. White/blank regions indicate **no data**. Country differences should be read cautiously due to **uneven sample sizes**.

  <p> <img width="837" height="525" alt="newplot (2)" src="https://github.com/user-attachments/assets/91253cf6-c366-4b25-8f99-4555f076e463" /> </p>

**_2. Work Type Proportion_**

  - On-site roles dominate (~80%), Hybrid is ~21%, and Remote has a very small share.

  <p> <img width="671" height="525" alt="newplot (3)" src="https://github.com/user-attachments/assets/8c549383-0736-4eeb-8432-749998bb4cbf" /> </p> 

**_3. Salary Boxplot_**

  - Salaries are **right-skewed**, with a long right tail and many high-end outliers (up to ~$800k). The mean is pulled upward.

  <p> <img width="644" height="470" alt="boxplot_googlecolab" src="https://github.com/user-attachments/assets/75b68405-a209-4992-a52a-b68c044e8d4c" /> </p> 

---

## 📊 Dashboard

**🧭 Dashboard Overview**

 🔗 [Salary Analysis Dashboard in the Data Field](https://python-data-analysis-event-alura.streamlit.app/)
       
  <p> <img width="603" height="904" alt="Captura de tela 2025-08-13 141252" src="https://github.com/user-attachments/assets/788b94ff-a3bc-465f-a017-618238fa27cf" /> </p>

**💭 Dashboard Insights**

- When analyzing the overall available information regarding salary and work information in data field, some insightful trends can be observed if analyzing the pandemic (2020-2021) to the most recent period (2024-2025):

**_1. General Metrics (Annual Salary, USD)_**

  - Average and maximum salaries are **higher in 2024–2025** than in **2020–2021** (salaries are nominal USD, not inflation-adjusted). 
  
  - The total record count is much larger in 2024–2025; this may reflect **more rows collected** and does **not necessarily** mean industry headcount growth. Additionally, trends may also reflect changes in the sample mix (countries, roles, company sizes) across periods, not just time.
  
  - The most common job position **shifts** from **Data Scientist** (2020–2021) to **Software Engineer** (2024–2025).
  
  - The Max Salary number **should be interpreted cautiously** since it can be driven by a single extreme value (outlier).

> _2020-2021:_
  
  <p> <img width="1613" height="187" alt="2020-2021" src="https://github.com/user-attachments/assets/38d2c9b2-4055-4642-90fe-99414b4cd020" /> </p>

> _2024-2025:_
  
  <p> <img width="1650" height="179" alt="2024-2025" src="https://github.com/user-attachments/assets/cb973148-2980-4478-ab0f-e80cc59f722d" /> </p>

**_2. Work Type_**
  
  - In **2020–2021**, most roles were **Hybrid (~52%)** or **Remote (~32%)**.  
  
  - In **2024–2025**, **On-site** becomes the majority, while **Remote + Hybrid** together drop below 20%.  

> _2020-2021:_
    
  <p> <img width="3865" height="1925" alt="2020-2021" src="https://github.com/user-attachments/assets/f7be97e1-35f5-4583-bca6-6412f43936d5" /> </p>

> _2024-2025:_
    
   <p> <img width="3837" height="1903" alt="2024-2025" src="https://github.com/user-attachments/assets/c7aac2d4-9173-4068-b870-638041fdc9a2" /> </p>

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
