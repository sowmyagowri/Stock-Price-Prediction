# Project-Team-6  
## Stock Price Prediction 
### Learn about the product at: https://www.youtube.com/watch?v=jAdHvbbOOYs

A web based product using machine learning models to predict future stock values based on the historical values.  

## Machine learning models used:  
1. Keras - tensorflow  
2. Arima model
3. Prophet   

## Technologies used:
Python for backend  
Flask framework for integration of frontend and backend  
JavaScript frame work with CSS and HTML for front end  
Dygraphs for plotting  

## Steps to run the code:  
1. Clone the github and goto the folder  
        $git clone https://github.com/SJSU272LabF17/Project-Team-6  
        $cd ./Project-Team-6/  
2. create a virtual environment with python3  
	$virtualenv -p /usr/local/bin/python3 Dependencies  
3. Activate the virtual environment  
	$source Dependencies/bin/activate  
4. Install dependencies numpy, scipy, requests, pyyaml, tensorflow, keras  
	$pip install -r requirements.txt  
5. Run "Command Prompt Run/prophet.py" -- this starts the http server using python flask  
6. Open the port on browser and use the site.  

## Site available at: http://13.57.46.92:5000/ 
![Alt text](images/homepage.jpeg?raw=true) 

In homepage, when the company ticker symbol is given, it fetches real time data using yahoo finance api.    
![Alt text](images/runtime_data_fetch.jpeg?raw=true) 

The machine learning model tries to for the entire time period, predicting the data at each step using the previous data and learning from it. This helps in predicting the anamolies over the years.  

In the graph below, the blue line was the prediction based on previous data at every point. And green line is the original closing stock values. In the site, the graph is interactive, drag to zoom into particular period. Double-click to zoom out.
![Alt text](images/graph.jpeg?raw=true)

You can also get company information and finance news in the second page.  
