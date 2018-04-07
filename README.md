# Project-Team-6  
## Stock Price Prediction 
### Team Members
1. [Sowmya Gowrishankar](https://github.com/sowmyagowri)
2. [Indira Priyadarshini Bobburi](https://github.com/IndiraBobburi)
3. [Vijay Yadav](https://github.com/vijay8608)
4. [Niral Koradia](https://github.com/vijay8608)

### Learn about the product at: https://www.youtube.com/watch?v=jAdHvbbOOYs
### Demo of our Project is at: https://www.youtube.com/watch?v=k9y4nsVdkIE&feature=youtu.be
A web based product using machine learning models to predict future stock values based on the historical values.  

## Machine learning models used:  
FB Prophet

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
5. Run "Stock Market Prediction/prophet.py" -- this starts the http server using python flask  
6. Open the port on browser and use the site.  

## Site available at: http://13.57.46.92:5000/ 
![Alt text](images/homepage.jpeg?raw=true) 

In homepage, when the company ticker symbol is given, it fetches real time data using yahoo finance api.   
Once in a while, an error comes in retrieving data from yahoo finance as they check for captcha to make sure no automated system is using their data.  
In that case, just go back to the homepage and try again. 
![Alt text](images/runtime_data_fetch.jpeg?raw=true) 

The machine learning model tries to for the entire time period, predicting the data at each step using the previous data and learning from it. This helps in predicting the anamolies over the years.  

In the graph below, the blue line was the prediction based on previous data at every point. And green line is the original closing stock values. In the site, the graph is interactive, drag to zoom into particular period. Double-click to zoom out.
![Alt text](images/graph.jpeg?raw=true)

You can also get company information and finance news in the second page.  
