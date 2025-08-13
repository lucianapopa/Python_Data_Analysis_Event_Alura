import streamlit as st
import pandas as pd
import plotly.express as px

# --- Set Page ---
# Defines page title, icon and layout.
st.set_page_config(
    page_title="Salary Dashboard in the Data Field",
    page_icon="📊",
    layout="wide",
)

# --- Data Retrieving ---
df = pd.read_csv("https://raw.githubusercontent.com/lucianapopa/Python_Data_Analysis_Event_Alura/main/final-dataset_GoogleColab.csv")

# ---- Labels for filters ----
seniority_map = {
    "junior": "Junior",
    "mid-level": "Mid-level",
    "senior": "Senior",
    "executive": "Executive",
}

contract_map = {
    "full-time": "Full-time", "ft": "Full-time",
    "part-time": "Part-time", "pt": "Part-time",
    "contract": "Contract",   "ct": "Contract",
    "freelance": "Freelance", "fl": "Freelance",
}

size_map = {
    "s": "Small (1–50)",   "small": "Small (1–50)",
    "m": "Medium (51–250)","medium": "Medium (51–250)",
    "l": "Large (251–1000)","large": "Large (251–1000)"
}

# --- Sidebar (Filters) ---
# This section creates a sidebar for filtering the data based on various criteria such as year, seniority, contract and company size.
st.sidebar.header("🔍 Filters")

# Year Filter
# Unique years are extracted from the DataFrame and sorted for display.
available_years = sorted(df['year'].unique())
selected_years = st.sidebar.multiselect("Year", available_years, default=available_years)

# Seniority Filter
# Unique seniority levels are extracted from the DataFrame and sorted for display.
available_seniority = sorted(df['seniority'].unique())
selected_seniority = st.sidebar.multiselect("Seniority", available_seniority, default=available_seniority, format_func=lambda x: seniority_map.get(str(x).lower(), x))

# Contract Filter
# Unique contract types are extracted from the DataFrame and sorted for display.
available_contract = sorted(df['contract'].unique())
selected_contract = st.sidebar.multiselect("Contract", available_contract, default=available_contract,  format_func=lambda x: contract_map.get(str(x).lower(), x))

# Company Size Filter
# Unique company sizes are extracted from the DataFrame and sorted for display.
available_sizes = sorted(df['company_size'].unique())
selected_sizes = st.sidebar.multiselect("Company Size", available_sizes, default=available_sizes, format_func=lambda x: size_map.get(str(x).lower(), x))

# --- DataFrame Filtering ---
# The main DataFrame is filtered based on the selections made in the sidebar.
df_filtered = df[
    (df['year'].isin(selected_years)) &
    (df['seniority'].isin(selected_seniority)) &
    (df['contract'].isin(selected_contract)) &
    (df['company_size'].isin(selected_sizes))
]

# --- Main Content ---
# Title and Introduction
st.title("🎲 Salary Analysis Dashboard in the Data Field")
st.markdown("Explore salary data in the data field over the past years. Use the filters on the left to refine your analysis.")

# --- Main Metrics (KPIs) ---
# This section displays key performance indicators based on the filtered DataFrame.
st.subheader("General Metrics (Annual Salary in USD)")

if not df_filtered.empty:
    avg_salary = df_filtered['usd'].mean()
    max_salary = df_filtered['usd'].max()
    total_count = df_filtered.shape[0]
    most_common_job_position = df_filtered["job_title"].mode()[0]
else:
    avg_salary, max_salary, total_count, most_common_job_position = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg. Salary", f"${avg_salary:,.0f}")
col2.metric("Max. Salary", f"${max_salary:,.0f}")
col3.metric("Total Count", f"{total_count:,}")
col4.metric("Most Common Job Position", most_common_job_position)

st.markdown("---")

# --- Visual Analysis with Plotly ---
# This section contains various visualizations to analyze the data based on the filters applied.
st.subheader("Visuals (Charts and Graphs)")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtered.empty:
        top_job_title = df_filtered.groupby('job_title')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        graph_job_title = px.bar(
            top_job_title,
            x='usd',
            y='job_title',
            orientation='h',
            title="Top 10 Job Positions by Average Salary",
            labels={'usd': 'Avg. Annual Salary (USD)', 'Job Position': ''}
        )
        graph_job_title.update_traces(
            marker_color="#0d0887",
            marker_line_color="white",
            marker_line_width=0.5
        )
        graph_job_title.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(graph_job_title, use_container_width=True)
    else:
        st.warning("No data to display in the job positions chart.")

with col_graf2:
    if not df_filtered.empty:
        graph_hist = px.histogram(
            df_filtered,
            x='usd',
            nbins=30,
            title="Annual Salary Distribution",
            labels={'usd': 'Salary Range (USD)', 'count': ''}
        )
        graph_hist.update_traces(
            marker_color="#0d0887",
            marker_line_color="white",
            marker_line_width=0.5
        )
        graph_hist.update_layout(title_x=0.1)
        st.plotly_chart(graph_hist, use_container_width=True)
    else:
        st.warning("No data to display in the distribution chart.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtered.empty:
        remote_count = df_filtered['work_type'].value_counts().reset_index()
        remote_count.columns = ['Work Type', 'Count']
        graph_work_type = px.pie(
            remote_count,
            names='Work Type',
            values='Count',
            color='Work Type',
        color_discrete_map={
            'On-site': '#0d0887',   # dark blue
            'Hybrid':  '#d8576b',   # light purple/ pink
            'Remote':  '#9c179e'    # purple
        },
            category_orders={'Work Type': ['On-site', 'Hybrid', 'Remote']},
            title='Proportion of Work Types',
            hole=0.5
        )
        graph_work_type.update_traces(textinfo='percent+label')
        graph_work_type.update_layout(title_x=0.1)
        st.plotly_chart(graph_work_type, use_container_width=True)
    else:
        st.warning("No data to display in the work types chart.")

with col_graf4:
    if not df_filtered.empty:
        df_ds = df_filtered[df_filtered['job_title'] == 'Data Scientist']
        countries_avg = df_ds.groupby('residence_iso3')['usd'].mean().reset_index()
        graph_countries = px.choropleth(
            countries_avg,
            locations='residence_iso3',
            locationmode='ISO-3',
            color='usd',
            color_continuous_scale='RdBu',
            title='Avg. Data Scientist Salary by Country',
            labels={'usd': 'Avg. Salary (USD)', 'residence_iso3': 'Country'},
            hover_name='residence_iso3'
        )
        graph_countries.update_layout(title_x=0.1)
        st.plotly_chart(graph_countries, use_container_width=True)
    else:
        st.warning("No data to display in the countries chart.")

# --- Detailed Data Table ---
# This section displays the filtered DataFrame in a table format for detailed analysis.
st.subheader("Detailed Data Table")
st.dataframe(df_filtered)