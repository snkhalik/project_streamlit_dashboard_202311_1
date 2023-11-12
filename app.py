import streamlit as st 
import pandas as pd 
import plotly.graph_objects as go 

st.title("Stroke Prediction Dashboard") 
st.markdown("The dashboard will help a researcher to get to know \ more about the given datasets and it's output") 
st.sidebar.title("Select Visual Charts") 
st.sidebar.markdown("Select the Charts/Plots accordingly:") 

data = pd.read_csv('data_input/demo_data_set.csv') 

chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
									('Line Chart', 'Bar Chart', 'Bubble Chart')) 

st.sidebar.checkbox("Show Analysis by Smoking Status", True, key = 1) 
selected_status = st.sidebar.selectbox('Select Smoking Status', 
									options = ['Formerly_Smoked', 
												'Smoked', 'Never_Smoked', 
												'Unknown']) 

fig = go.Figure() 

if chart_visual == 'Line Chart': 
	if selected_status == 'Formerly_Smoked': 
		fig.add_trace(go.Scatter(x = data.Country, y = data.formerly_smoked, 
								mode = 'lines', 
								name = 'Formerly_Smoked')) 
	if selected_status == 'Smoked': 
		fig.add_trace(go.Scatter(x = data.Country, y = data.Smokes, 
								mode = 'lines', name = 'Smoked')) 
	if selected_status == 'Never_Smoked': 
		fig.add_trace(go.Scatter(x = data.Country, y = data.Never_Smoked, 
								mode = 'lines', 
								name = 'Never_Smoked')) 
	if selected_status == 'Unknown': 
		fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown, 
								mode='lines', 
								name="Unknown")) 

elif chart_visual == 'Bar Chart': 
	if selected_status == 'Formerly_Smoked': 
		fig.add_trace(go.Bar(x=data.Country, y=data.formerly_smoked, 
							name='Formerly_Smoked')) 
	if selected_status == 'Smoked': 
		fig.add_trace(go.Bar(x=data.Country, y=data.Smokes, 
							name='Smoked')) 
	if selected_status == 'Never_Smoked': 
		fig.add_trace(go.Bar(x=data.Country, y=data.Never_Smoked, 
							name='Never_Smoked')) 
	if selected_status == 'Unknown': 
		fig.add_trace(go.Bar(x=data.Country, y=data.Unknown, 
							name="Unknown")) 

elif chart_visual == 'Bubble Chart': 
	if selected_status == 'Formerly_Smoked': 
		fig.add_trace(go.Scatter(x=data.Country, 
								y=data.formerly_smoked, 
								mode='markers', 
								marker_size=[40, 60, 80, 60, 40, 50], 
								name='Formerly_Smoked')) 
		
	if selected_status == 'Smoked': 
		fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes, 
								mode='markers', 
								marker_size=[40, 60, 80, 60, 40, 50], 
								name='Smoked')) 
		
	if selected_status == 'Never_Smoked': 
		fig.add_trace(go.Scatter(x=data.Country, 
								y=data.Never_Smoked, 
								mode='markers', 
								marker_size=[40, 60, 80, 60, 40, 50], 
								name = 'Never_Smoked')) 
	if selected_status == 'Unknown': 
		fig.add_trace(go.Scatter(x=data.Country, 
								y=data.Unknown, 
								mode='markers', 
								marker_size=[40, 60, 80, 60, 40, 50], 
								name="Unknown")) 

st.plotly_chart(fig, use_container_width=True) 
