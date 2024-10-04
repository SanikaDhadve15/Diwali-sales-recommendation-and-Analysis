import streamlit as st
from streamlit_option_menu import option_menu
from data_analysis import data_analysis
from visualizations import visualizations
from recommendations import recommendations

st.set_page_config(page_title="Diwali Sales Analysis")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})

    def run(self):
        with st.sidebar:
            selected_app = option_menu(
                menu_title='Diwali Sales Dashboard',
                options=['Data Upload & Analysis', 'Visualizations', 'Recommendations'],
                icons=['file-earmark-text', 'bar-chart-line', 'lightbulb'],
                default_index=0
            )

        for app in self.apps:
            if app['title'] == selected_app:
                app['function']()

app = MultiApp()
app.add_app("Data Upload & Analysis", data_analysis)
app.add_app("Visualizations", visualizations)
app.add_app("Recommendations", recommendations)

app.run()
