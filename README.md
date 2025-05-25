## Python Graphics
### ✅ Moving Image
With background image and moving another image. In this example we use the following coding languages to implement the idea of moving image over the background of another image:

1- Python with Flask (Flask for web server and API)
2- HTML page
3- Java Script to move the image
4- SQLite (SQL to keep one record)

We need to open windows session in MS windows and run:
```
python app.py
```
After we run the command above in the windows session, we can go to the browser http://127.0.0.1:5000. The refersh happens every 2 seconds

### ✅ Bar
The Bar chart will read the label and value from SQLite database and buil the chart depending on the data in the database. The table has two columns label and value. The label is pre-defined in the array and value genertes randomly. 

To geenrate the bar dynamically, we will need:

1- Python with Flask (Flask for web server and API)
2- HIML page
3- Java Script to build the bars
4- SQLite to keep the number of labels with their random values

Run the script to build the database in SQLite
```
python setup_bar_data.py
```

To run the flask the flask server
```
python app.py
```

After we run the command above, we can goto http://127.0.0.1:5000 to check the bar. The resfersh happens every 5 second. 

We can the python "python setup_bar_data.py" after that the data generates. Ater that when the refersh happens for web,we can see the changes for the bar charts.

### ✅ Moving-dot
### ✅ Stock
