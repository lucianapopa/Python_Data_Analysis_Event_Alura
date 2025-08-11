<!-- Banner -->
<p align="center">
  <img src="https://i.imgur.com/S8Wrwhe.png" alt="Python Data Analysis Event - Alura" width="800" height="200">
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
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](PASTE_YOUR_NOTEBOOK_LINK_HERE)

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

🖼 **Screenshots / Results:**

-- Dashboard Overview:

[Salary Analysis Dashboard in the Data Field](https://python-data-analysis-event-alura.streamlit.app/)

<img width="701" height="869" alt="Captura de tela 2025-08-11 141129" src="https://github.com/user-attachments/assets/06e5eaee-cc7c-48c4-b658-c047af7e3755" />

-- Quick Dashboard Insights:

When analysing the overall available information regarding salary and work information in Data field, some insighfull aspects can be observed if analysing the pandemic to the most recent period:

* 1. First aspects that can be highlighted are the General Metrics, which shows that during pandemic (2021-2022) the average salary and maximum salary were far lower than during the most recent period (2024-2025). The total amount of data records increased steadely showing how the data field gained new workers during a 5-6 period. Also, it is possible to see that the most common job position also changed during this period, with Data Scientist being more common during pandemic, and Software Engineer on most recent data. In addition, it is interesting to highlight that during the whole period available (2020-2025), the most commom job position is Data Scientist.

  > 2020-2021:
    <img width="1613" height="187" alt="2020-2021" src="https://github.com/user-attachments/assets/38d2c9b2-4055-4642-90fe-99414b4cd020" />

  > 2024-2025:
    <img width="1650" height="179" alt="2024-2025" src="https://github.com/user-attachments/assets/cb973148-2980-4478-ab0f-e80cc59f722d" />

* 2. Comparing the work types it is possible to see that the majority of jobs were Remote (51.9%) or Hybrid (32%) during the pandemic period of 2020-2021, while in the most recent period (2024-2025) the work type pattern changed significantly, with Remote and Hybrid representing less than 20%, while On-site jobs revealed how representative it is right now.

    > 2020-2021:
      <img width="1828" height="827" alt="2020_2021" src="https://github.com/user-attachments/assets/3ee98734-1001-40e6-bc01-fc5e4e3a79ab" />

    > 2024-2025:
      <img width="1801" height="811" alt="2024_2025" src="https://github.com/user-attachments/assets/16b41f79-95fb-45dc-b8b1-4b25187c4f69" />

* 3. Another interesting observation that can be made from the screenshots above is that the average Data Scientist salary kept strong in North America during the pandemic, while gained traction in other coutnries such as South America, and more parts of Europe, Africa and Oceany.

---

## 👩‍💻 About Me
Hi! I'm **Luciana Popa**, a Master's student in Data Analytics at **University of Niagara Falls Canada**, curious about **data analytics and visualization**.  
- Background: **Finance**
- Tools: **Python, SQL, Tableau, Power BI, Excel**
- Location: **Ontario, Canada**
- 🔗 [LinkedIn](https://www.linkedin.com/in/luciana-popa/) | [GitHub](https://github.com/lucianapopa)

---

🙏 Acknowledgments
- **Alura** for the event and learning materials.
- Dataset by **guilhermeonrails**/data-jobs.

## 📌 Notes
- This repository is **for educational purposes** only.
- Contributions, feedback, and suggestions are welcome! Open an issue or submit a pull request.

---

<p align="center">
  Made with 💙 during the <a href="https://www.alura.com.br/imersao-dados-python">Python Data Analysis Event - Alura</a>
</p>
