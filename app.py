from flask import Flask, render_template, request
import pandas as pd
import altair as alt
from flask_paginate import Pagination, get_page_parameter, get_page_args

app = Flask(__name__)

alt.data_transformers.disable_max_rows()
playstore = pd.read_csv('data/googleplaystore.csv')
@app.route("/")
# This fuction for rendering the table
def index():
    df = playstore.copy()
      #adding the data frame
    df.index +=1 #adding index in table
    PER_PAGE = 5 #limit data per page
    cols = ['App', 'Reviews', 'Category']
    
    search = False
    q = request.args.get('q')
    if q:
        search = True
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    pagination = Pagination(page=page, total=len(df), search=search, record_name='records',per_page=PER_PAGE, show_single_page=True,css_framework='bootstrap4')
    
    new_df = pd.crosstab(index=df['Category'],
           columns='Jumlah').sort_values(by='Jumlah',ascending=False).head(5).reset_index()
    stats = {
        'most_categories' : new_df['Category'][0],
        'total': new_df['Jumlah'][0]
    }
    
    return render_template('index.html',new_tables=df[(page-1)*PER_PAGE:page*PER_PAGE][cols].to_html(classes='niceTable'),pagination=pagination, stats=stats)

# This fuction for rendering the plot
@app.route("/charts")
def charts():
    
    df2 = playstore.copy()

    chart = alt.Chart(playstore).mark_bar().encode(
    x='Category:N',
    y='count(Category):Q',
    color=alt.Color('Category',legend=None),
    tooltip=['Category','count(Category)']
    )
    return chart.to_json() 

if __name__ == "__main__": 
    app.run()
