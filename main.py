import streamlit as st
from streamlit_option_menu import option_menu

# Import the page modules
import data_analysis, visualizations, recommendations, about

st.set_page_config(page_title="Diwali Sales Analysis")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Diwali Sales Analysis',
                options=['Data Upload & Analysis', 'Visualizations', 'Recommendations', 'About'],
                icons=['upload', 'bar-chart', 'lightbulb', 'info-circle'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        for app in self.apps:
            if app['title'] == app:
                app['function']()

# Create an instance of the MultiApp class
app = MultiApp()

# Add pages
app.add_app("Data Upload & Analysis", data_analysis.app)
app.add_app("Visualizations", visualizations.app)
app.add_app("Recommendations", recommendations.app)
app.add_app("About", about.app)

# Run the app
app.run()
