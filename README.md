# Project-Team-6  
## Stock Price Prediction 

### A web based product using machine learning models to predict future values of stock market based on the historical values.  

##Machine learning models used:  
1. Keras - tensorflow  
2. Arima model
3. Prophet   

##Technologies used:
Python for backend  
Flask framework for integration of frontend and backend  
CSS and HTML for front end  

## Steps to run:  
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
