import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="User-Based Analysis", layout="wide")

DATA_URL = 'signupCount.csv'
RETAINED_DATA_URL = 'RetainedCount.csv'

line1_spacer1, line1_1, line1_spacer2 = st.columns((0.1, 3.0, 1.0))


with line1_1:
    #st.title('Cohort Based Analysis on Sign-Up and Retention',)
    st.markdown("<h1 style='text-align: Left; color: White;'>Cohort Based Analysis on Sign-Up and Retention</h1>", unsafe_allow_html=True)

def load_data():
    data = pd.read_csv(DATA_URL, index_col=0)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data['CohertMonth'] = pd.to_datetime(data['CohertMonth'], format='%Y%m%d', errors='ignore')
    return data

row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)
with row3_1:
    st.subheader('Monthly User Sign Up')
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text("Done! (using st.cache_data)")

    if st.checkbox('Show raw data', key= 1):
        st.subheader('Raw data')
        st.write(data)

    # fig, ax = plt.subplots()
    # ax.bar(data['CohertMonth'], data['NumberOfUsers'])
    # ax.set_xlabel('Sign-Up Month')
    # ax.set_ylabel('Number of Users')
    # ax.set_title('User Sign-Ups by Month')
    
    data_df = pd.DataFrame(data).reset_index()
    data_df['CohertMonth'] = data_df['CohertMonth'].astype(str) 

    figs = px.bar(
        data_df,
        x="CohertMonth",
        y="NumberOfUsers",
        title="User Sign-Ups by Month",
        color_discrete_sequence=["#9EE6CF"])
    
    figs.update_layout(xaxis_type='category')
    figs.update_xaxes(title='Cohert Month')
    figs.update_yaxes(title='User Count')


    # fig, ax = plt.subplots()
    # bars = ax.bar(data['CohertMonth'], data['NumberOfUsers'])
    
    # # Adding the data labels on the bars
    # for bar in bars:
    #     yval = bar.get_height()
    #     ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', color='Black', fontdict={'size': 8})

    # ax.set_xlabel('Sign-Up Month')
    # ax.set_ylabel('Number of Users')
    # ax.set_title('User Sign-Ups by Month')
    # ax.set_yticks(np.arange(0, 4, 1))    

# figs.update_layout({
#     'plot_bgcolor': 'black',
#     'paper_bgcolor': 'black',
#     'font_color': 'white'
# })
    st.plotly_chart(figs, theme="streamlit", use_container_width=True)

# Display the chart in Streamlit
    #st.pyplot(fig)
    st.markdown(
    """
    As per the above bar chart, The year started with a low number of sign-ups in March, followed by a slight increase in April and May. In the month of June, July and August there were no sign up.  \n
    Then, recovery to 2 sign-ups in September suggests a renewed interest or the effectiveness of corrective measures taken after the mid-year. With no sign-ups in October and November and only 1 in December, the activity remains low towards the year's end. 
    """
    )
    

with row3_2:
    st.subheader('Retention Rate By Sign-Up Cohort')
    data_load_state2 = st.text('Loading data...')
    data2 = pd.read_csv(RETAINED_DATA_URL, index_col=0)
    data_load_state2.text("Done! (using st.cache_data)")

    if st.checkbox('Show raw data', key=2):
        st.subheader('Raw data')
        st.write(data2)
        
    st.write("**Note:** Retention rate is calculated from the first Order Month in each cohert.  \n `RetentionRate = No. of Active Users/ TotalUserCount` ")

    #fig, ax = plt.subplots()
    #ax.bar(data['CohertMonth'], data['NumberOfUsers'])
    # ax.set_xlabel('Sign-Up Month')
    # ax.set_ylabel('Number of Users')
    # ax.set_title('User Sign-Ups by Month')
    
    data_df = pd.DataFrame(data2).reset_index()
    #data_df['CohertMonth'] = data_df['CohertMonth'].astype(str) 

    figs = px.line(
        data_df,
        x="RetentionMonth",
        y="RetentionRate",
        title="Retention rate per Cohort",
        color="SignupMonth")
    
    
    figs.update_xaxes(title='Retention Month')
    figs.update_yaxes(title='Retention Rate (%)')
    
    st.plotly_chart(figs, theme="streamlit", use_container_width=True)
    st.markdown(
        """
        - **2021-03** Cohort, High initial engagement but no retention in the following months.
        - **2021-04** Cohort, shows an irregular retention pattern.
        - **2021-05** Cohort, there is an initial engagement that doesn't persist.
        - **2021-09** Cohort, Strong start followed by a total drop-off and partial recovery.
        - **2021-12** Cohort, Like the first and third cohorts, this group shows good initial engagement with no subsequent retention.
        """
    )
st.markdown (
    """
    ## Conclusion 
    👉  \t There is a noticeable trend of strong initial engagement across all cohorts, but retention dramatically drops in the second month for most cohorts.  \n
    👉  \t This indicates a potential gap in maintaining user interest or satisfaction beyond the initial interaction.  \n
    👉  \t The fluctuations in retention rates, especially in the second and third cohorts, suggest inconsistencies in the user experience
    """
)
# fig, ax = plt.subplots()
# bars = ax.bar(data['CohertMonth'], data['NumberOfUsers'])
    
    # # Adding the data labels on the bars
    # for bar in bars:
    #     yval = bar.get_height()
    #     ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', color='Black', fontdict={'size': 8})

    # ax.set_xlabel('Sign-Up Month')
    # ax.set_ylabel('Number of Users')
    # ax.set_title('User Sign-Ups by Month')
    # ax.set_yticks(np.arange(0, 4, 1))    

# figs.update_layout({
#     'plot_bgcolor': 'black',
#     'paper_bgcolor': 'black',
#     'font_color': 'white'
# })
    # st.plotly_chart(figs, theme="streamlit", use_container_width=True)

# Display the chart in Streamlit
    #st.pyplot(fig)
#    st.markdown(
#        "As per the above bar chart the sign up in the first three months increased significantly. In the month of June, July and August there were no sign up and again the sign up started from September. "
#    )