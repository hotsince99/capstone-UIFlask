from flask import Flask, render_template, request
import pandas as pd
import altair as alt
import numpy as np
from flask_paginate import Pagination, get_page_parameter, get_page_args

app = Flask(__name__)


alt.data_transformers.disable_max_rows()
playstore = pd.read_csv('data/googleplaystore.csv')
playstore.drop_duplicates(subset ="App", keep = 'first', inplace=True) 
playstore.drop([10472], inplace=True)
playstore.Category = playstore.Category.astype('category')
playstore.Installs = playstore.Installs.apply(lambda x: x.replace(',',''))
playstore.Installs = playstore.Installs.apply(lambda x: x.replace('+',''))
playstore.Installs = playstore.Installs.apply(lambda x: int(x))
playstore['Size'].replace('Varies with device', np.nan, inplace = True ) 
playstore.Size = (playstore.Size.replace(r'[kM]+$', '', regex=True).astype(float) * \
             playstore.Size.str.extract(r'[\d\.]+([KM]+)', expand=False)
            .fillna(1)
            .replace(['k','M'], [10**3, 10**6]).astype(int))
playstore['Size'].fillna(playstore.groupby('Category')['Size'].transform('mean'),inplace = True)
playstore.Price = playstore.Price.apply(lambda x: x.replace('$',''))
playstore['Price'] = playstore['Price'].apply(lambda x: float(x))
playstore[['Reviews','Size','Installs']] = playstore[['Reviews','Size','Installs']].astype('int64')

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
    
    top_category = pd.crosstab(index=df['Category'],
           columns='Jumlah').sort_values(by='Jumlah',ascending=False).head(5).reset_index()
    stats = {
        'most_categories' : top_category['Category'][0],
        'total': top_category['Jumlah'][0],
        'rev_table' : df.groupby(['Category','App']).\
            agg({'Reviews' : 'sum',
                'Rating':'mean'}).\
            sort_values(['Reviews','Category'], ascending=False).\
            groupby(['Category','Reviews']).\
            head(5).reset_index().head(5).to_html(classes=['table thead-light table-striped table-bordered table-hover table-sm'])
    }
    
    return render_template('index.html',new_tables=df[(page-1)*PER_PAGE:page*PER_PAGE][cols].to_html(classes='niceTable'),pagination=pagination, stats=stats)

# This fuction for rendering the plot
@app.route("/charts")
def charts():
    
    df2 = playstore.copy()

    chart = alt.Chart(df2).mark_bar().encode(
        x='Category:N',
        y='count(Category):Q',
        color=alt.Color('Category',legend=None),
        tooltip=['Category','count(Category)']
        ).properties(width=700)
    return chart.to_json() 

@app.route("/chart_rev")
def chart_rev():
    df = playstore.copy()
    chart = alt.Chart(df).mark_point().encode(
        x='Reviews:Q',
        y='Rating:Q',
        color = 'Installs',
        size='Installs',
        tooltip=['App','Category', 'Reviews', 'Rating', 'Installs']
    )
    return chart.to_json()

@app.route("/chart_size")
def chart_size():
    brush = alt.selection(type='interval')
    points = alt.Chart(playstore).mark_circle().encode(
        x='Size:Q',
        y='Rating:Q',
        tooltip=['App','Category', 'Reviews', 'Installs','Rating'],
        color=alt.condition(brush, 'Category:N', alt.value('lightgray'),legend=None)
                ).add_selection(
                    brush
            )
    
    bars = alt.Chart(playstore).mark_bar().encode(
        y='Category:N',
        color='Category:N',
        x='count(Category):Q'
    ).transform_filter(
        brush
    )

    chart = (points & bars)
    return chart.to_json()

@app.route("/chart_price")
def chart_price():
    brush = alt.selection(type='interval')
    points = alt.Chart(playstore).mark_circle().encode(
            x='Price:Q',
            y='Rating:Q',
            tooltip=['App','Category', 'Reviews', 'Installs','Rating'],
            color=alt.condition(brush, 'Category:N', alt.value('lightgray'),legend=None)
                ).add_selection(
                    brush
            )
    bars = alt.Chart(playstore).mark_bar().encode(
        y='Category:N',
        color='Category:N',
        x='count(Category):Q'
    ).transform_filter(
        brush
    )

    chart = (points & bars)
    return chart.to_json()


if __name__ == "__main__": 
    app.run()
