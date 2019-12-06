# Google Play Store Analytics

## Introduction
The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market. Using this dataset we are going to analysis as a developer, we should know the best constraints to focus on when launching our first app. And we definitely have no intention of getting lost in this vast ocean of versatile apps.

## Data Summary
The google play store data consists of the following variables:
- `App` : Application name                
- `Category` : Category the app belongs to
- `Rating` : Overall user rating of the app (as when scraped)
- `Reviews` : Number of user reviews for the app (as when scraped)         
- `Size` : Size of the app (as when scraped)           
- `Installs` : Number of user downloads/installs for the app (as when scraped)     
- `Type` : Paid or Free           
- `Price` : Price of the app (as when scraped)        
- `Content Rating` : Age group the app is targeted at - Children / Mature 21+ / Adult   
- `Genres` : An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.        
- `Last Updated` : Date when the app was last updated on Play Store (as when scraped) 
- `Current Ver` : Current version of the app available on Play Store (as when scraped)   
- `Android Ver` : Min required Android version (as when scraped)  

## Rubrics
### Data Preproses and Exploratory Data Analysis
- Demonstrated how to apply some data preprocess to make sure that your data is “ready”, such as change the data types to the proper format, handling duplicate data and missing values, drop wrong row, and changes row values.
- Demonstrated how to split row values into two parts and save them to a new column. 

### Data Wrangling
- Apply group by and cross tab to make new data frames.

### Data Visualization
- Duplicate or reproduce plot that visualize which top 10 catgegories rules in playstore market using bar plot 
- Duplicate or reproduce plot that visualize primary genre and secondary genre of application using stacked bar plot. 

### Build Flask App
- Demonstrated how to create new instance from Flask class
- Demonstrated how to route and make view function for plotting 
- Demonstrated how to create templates for main page in Flask application
- Demonstrated how to render table and plot to html page
- Demonstrated how to run Flask application in local host
