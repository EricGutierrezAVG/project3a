import sqlite3
from flask import Flask, render_template, request, flash
import pygal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route("/stocks, methods=['GET', 'POST']")
def stocks():
    
    if request.method == "POST":
        #process form data and flash error message if error
        
        symbol = request.form['symbol'] 
        chart_type = request.form['chart_type']
        time_series = request.form['time_series']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        

       
       #Generate Symbols
        if not symbol:
            flash("Symbol is required.")
        else:
            return
        
        
       #Generate Chart Type
        if not chart_type:
            flash("Chart type is required.")
        elif chart_type == '1':
            chart = pygal.Bar(x_label_rotation=45)
        elif chart_type == '2':
            chart = pygal.Line(x_label_rotation=45)
        
            
         #Generate Time Series
         #VVYFBPRGDKHX0K93
        try:
            if time_series == '1':
                url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=VVYFBPRGDKHX0K93&datatype=csv"
                
            elif time_series == '2':
                url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=VVYFBPRGDKHX0K93&datatype=csv"
                
            elif time_series == '3':
                url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=VVYFBPRGDKHX0K93&datatype=csv"
                
            elif time_series == '4':
                url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=VVYFBPRGDKHX0K93&datatype=csv"
        finally:
            not time_series 
            flash("Time Series is required.")
    
        
        
        #Generate Start Date
        
        
        #Generate End Date
        












            if symbol == "":
                flash("Symbol is required")
        #if no errors, query the API
            elif chart_type == "":
                flash("Chart type is required")
            elif time_series == "":
                flash("Chart type is required")
            elif start_date == "":
                flash("You must have a start date!")
            elif end_date == "":
                flash("You must have a start date!")
                
            else:
                return render_template("stocks.html")
            
        return render_template("stocks.html")
app.run
