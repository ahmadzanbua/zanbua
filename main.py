import streamlit as st
import pandas as pd
from PIL import Image
from database import *
from database import edit_task_data
import plotly.express as px


# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"




def main():

    img = Image.open('a.png')
    st.set_page_config(page_title="TO-Do List",page_icon=img)
    

    padding = 1
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
            padding-right: {padding}rem;
            padding-left: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)

    st.title("To-Do List")
    menu = ["Create","Read","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)       
    if choice == "Create":
        st.subheader("Add Tasks")
        create_table()
        col1,col2 = st.beta_columns(2)    
        with col1:
            task = st.text_area("Task To Do")
            task_description = st.text_area("Description")
        with col2:
            task_status = st.selectbox("Status",["To-Do","Doing","Done"])
            task_due_date = st.date_input("Due Date")
        if st.button("Add Task"):
            add_data(task,task_status,task_due_date,task_description)
            st.success("Succefuly added {}".format(task))
    elif choice == "Read":
        st.subheader("View the Tasks")
        result = view_all_data()
        df = pd.DataFrame(result,columns = ['Task','Status','Description','Due Date'])
        st.dataframe(df)
        with st.beta_expander("View All Data"):
            st.write(result)
        with st.beta_expander("Task Status"):
            task_df = df['Status'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names = 'index', values = 'Status')
            st.plotly_chart(p1)
        with st.beta_expander("Task Date"):
            task_df = df['Due Date'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names = 'index', values = 'Due Date')
            st.plotly_chart(p1)
    elif choice == "Update":
        st.subheader("Edit or Update Items")
        result = view_all_data()
        df = pd.DataFrame(result,columns = ['Task','Status','Description','Due Date'])
        with st.beta_expander("Current Data"):
            st.dataframe(df)    
        list_of_task =[i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Edit", list_of_task)
        selected_result = get_task(selected_task)
        st.write(selected_result)
        if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]
            task_description = selected_result[0][3]
            col1,col2 = st.beta_columns(2)
            with col1:
            	new_task = st.text_area("Task To Do",task)
            	new_task_description = st.text_area("Description",task_description)
            with col2:
            	new_task_status = st.selectbox(task_status,["To-Do","Doing","Done"])
            	new_task_due_date = st.date_input(task_due_date)
            if st.button("Update Task"):
            	edit_task_data(new_task,new_task_status,new_task_description,new_task_due_date,task,task_status,task_due_date,task_description)
            	st.success("Successfully Updated:: {} To ::{} ".format(task,new_task))
        result2 = view_all_data()
        df = pd.DataFrame(result2,columns = ['Task','Status','Description','Due Date'])
        with st.beta_expander("Updated Data"):
        	st.dataframe(df)
    elif choice == "Delete":
        st.subheader("Delete Item")
        result = view_all_data()
        df = pd.DataFrame(result,columns = ['Task','Status','Description','Due Date'])
        with st.beta_expander("Current Data"):
        	st.dataframe(df)
        list_of_task =[i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Delete", list_of_task)
        st.warning("Do you want to delete ::{}".format(selected_task))
        if st.button("Delete Task"):
            delete_task(selected_task)
            st.success("Task has been successfully Deleted")
        new_result = view_all_data()
        df2 = pd.DataFrame(new_result,columns = ['Task','Status','Description','Due Date'])
        with st.beta_expander("Updated Data"):
            	st.dataframe(df2)
    
    elif choice == "About":
        st.markdown("""TO DO List is an app made with pure [python](http://www.python.org) that can compete with
        famous app like Notion
            """)
if __name__ == "__main__":
    main()