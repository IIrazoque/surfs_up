# surfs_up
### Overview of the statistical analysis

The goal is to move to Oahu Hawaii and open a Surf & ice cream shop business. We are to proprose this idea to a potential investor (famous surfer in the area. To determine if the Surf & ice cream shop business is sustainable year-round we collected temperature data for the months of June and December. 
We performed analysis using python and SQLAlchemy queries via a serverless engine: SQLite database. We could also use the Flask webframe to build a potential webpage to access/perform analysis to our investor.
Resources: Hawaii.sqlite database, python, pandas, SQLite, SQLAlchemy

### Results
Surprisingly the temperature in June vs December don’t different by much. Averages for each month are between 71 – 74 degrees figure A.

*Figure A – Standard Temperature Statistics for June and December*

![This is an image]( https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%20A.PNG)
 
Using the value_count function we can see the occurrences for each temperature value, but lets see how often did temperature dropped to the minimum value reported (June’s minimum = 64, December’s minimum = 56) figure B & C. We see that for June, only 1 occurrence of 64 degrees versus 194 counts of good weather at 76 degrees. We can also see for December, only 2 occurrences of 56 degrees versus 174 of 71 good weather degree. Who shy’s away from ice cream at 71 degree weather?!

*Figure B – June Temps Value Counts*

![This is an image]( https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%20B.PNG)
  
*Figure C – December Temps value count*

![This is an image]( https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%20C.PNG)
 
Plotted histograms were also created. Figures D & E

*Figure D – June Temperature frequencies*

![This is an image]( https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%20D.PNG)

 
*Figure E – December Temperature frequencies*
![This is an image]( https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%20E.PNG)

 
## Summary 
Filter the date column in the Measurements table to retrieve al the temperatures in June from  the Hawaii.sqlite file. Then convert the data of interest we converted into a list. The june_temps_list was then transformed into a DataFrame figure 1. Standard statistics were gathered figure 2. The same query was used to retieve December temperatures.

*Figure 1 – June Temperature query, to list then dataframe*

![This is an image]( https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%2001.PNG)
 

*Figure 2 – December Temperature query to list then Dataframe*

![This is an image](https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%2002.PNG)
 

Using SQLAlchemy we are also able to present on the spot analysis. Using Flask we are able to a web pages to present additional details such as precipitation, ice cream stations, static temperatures in a given time etc (Figure 3). 
By creating a function in @app.route(s) were are able to manipulate the dataset and “return” the information needed.

*Figure 3 – Creating SQLAlchemy Queries*

![This is an image](https://github.com/IIrazoque/surfs_up/blob/d8890ef9bfaca41ee4ad8307a45cb16fc2140aee/Images/figure%2003.PNG)
 
 
