import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_table
import dash_html_components as html
import colorlover
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

first_col_img=['','','M3 (only images)', '','','','','','Deepface', '','','']
first_col_mix=['','','M3 (images + names)', '']
first_col_name = ['','','“Gender” R (SSA)', '','','','“Gender” R (IPUMS)', '','','','Gender_Guesser', '']

second_col_img=['IMDB', 'WIKI', 'OUI','Twitter','Gender Shade','Scholar','IMDB', 'WIKI', 'OUI','Twitter','Gender Shade','Scholar']
second_col_mix=['IMDB', 'WIKI', 'Twitter','Scholar']
second_col_name= ['IMDB', 'WIKI', 'Twitter','Scholar','IMDB', 'WIKI', 'Twitter','Scholar','IMDB', 'WIKI','Twitter', 'Scholar']

coverage_img= [1,1,1,1,1,1,0.57,0.48,0.57,0.45,0.85,0.85]
precision_img= [0.76,0.89,0.69,0.87,0.95,0.95,0.78,0.92,0.66,0.85,0.84,0.88]
recall_img= [0.76,0.89,0.69,0.84,0.94,0.95,0.78,0.91,0.66,0.83,0.78,0.85]
f1_score_img= [0.76,0.88,0.69,0.84,0.94,0.95,0.78,0.90,0.63,0.83,0.76,0.84]

coverage_mix= [1,1,1,1]
precision_mix= [0.94,0.96,0.91,0.96]
recall_mix= [0.94,0.96,0.90,0.96]
f1_score_mix= [0.94,0.96,0.90,0.96]

coverage_name = [0.874,0.823,0.434,0.797,0.851,0.812,0.460,0.769,0.890,0.865,0.475,0.768]
precision_name = [0.965,0.957,0.943,0.968,0.909,0.929,0.846,0.917,0.965,0.969,0.954,0.978]
recall_name = [0.965,0.954,0.943,0.968,0.907,0.928,0.843,0.916,0.965,0.968,0.954,0.978]
f1_score_name = [0.965,0.955,0.942,0.968,0.905,0.928,0.842,0.916,0.965,0.968,0.955,0.978]

coverage_img_male= [1,1,1,1,1,1,0.53,0.45,0.83,0.47,0.82,0.87]
precision_img_male= [0.77,0.9,0.67,0.7,0.91,0.93,0.78,0.91,0.58,0.76,0.71,0.78]
recall_img_male= [0.84,0.98,0.63,0.95,0.99,0.97,0.84,0.98,0.94,0.99,1.0,1.0]
f1_score_img_male= [0.81,0.94,0.65,0.81,0.95,0.95,0.81,0.94,0.71,0.86,0.83,0.87]

coverage_img_female= [1,1,1,1,1,1,0.62,0.63,0.87,0.38,0.89,0.82]
precision_img_female= [0.74,0.87,0.71,0.96,0.99,0.97,0.79,0.94,0.83,0.98,1.0,1.0]
recall_img_female= [0.65,0.55,0.74,0.75,0.87,0.92,0.71,0.72,0.55,0.70,0.52,0.67]
f1_score_img_female= [0.69,0.68,0.72,0.84,0.93,0.95,0.75,0.81,0.66,0.81,0.69,0.80]

df_img = pd.DataFrame({'Model': first_col_img, 'Dataset':second_col_img, 'Coverage':coverage_img, 'Precision':precision_img, 'Recall':recall_img,
                  'F1-score': f1_score_img})

df_mix = pd.DataFrame({'Model': first_col_mix, 'Dataset':second_col_mix, 'Coverage':coverage_mix, 'Precision':precision_mix, 'Recall':recall_mix,
                  'F1-score': f1_score_mix})

df_name = pd.DataFrame({'Model': first_col_name, 'Dataset':second_col_name, 'Coverage':coverage_name, 'Precision':precision_name, 'Recall':recall_name,
                  'F1-score': f1_score_name})

df_img_gender = pd.DataFrame({'Model': first_col_img, 'Dataset':second_col_img, 'Coverage_male':coverage_img_male, 'Precision_male':precision_img_male, 
	'Recall_male':recall_img_male,'F1-score_male': f1_score_img_male, 'Coverage_female':coverage_img_female, 'Precision_female':precision_img_female, 
	'Recall_female':recall_img_female,'F1-score_female': f1_score_img_female})


def discrete_background_color_bins(df, n_bins=5, columns='all'):
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == 'all':
        if 'id' in df:
            df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
        else:
            df_numeric_columns = df.select_dtypes('number')
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [
        ((df_max - df_min) * i) + df_min
        for i in bounds
    ]
    styles = []
    legend = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        backgroundColor = colorlover.scales[str(n_bins)]['seq']['YlOrRd'][i - 1]
        color = 'white' if i > len(bounds) / 2. else 'inherit'

        for column in df_numeric_columns:
            styles.append({
                'if': {
                    'filter_query': (
                        '{{{column}}} >= {min_bound}' +
                        (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                    ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                    'column_id': column
                },
                'backgroundColor': backgroundColor,
                'color': color,
                'border' : '1px solid '+ backgroundColor
            })
        legend.append(
            html.Div(style={'display': 'inline-block', 'width': '60px'}, children=[
                html.Div(
                    style={
                        'backgroundColor': backgroundColor,
                        'borderLeft': '1px rgb(50, 50, 50) solid',
                        'height': '10px'
                    }
                ),
                html.Small(round(min_bound, 2), style={'paddingLeft': '2px'})
            ])
        )
        styles.extend([{
    	'if': {
    		'column_id': ['Dataset','Model'],
    	},
    	'backgroundColor': 'white',
        'color': 'black',
        'border': '1px solid white',
        'textAlign': 'right',
        'width': '80px'
    	},
    	{
            'if': {
                'filter_query': '{Dataset} = "Scholar"'
            },
            'border-bottom': '3px solid white'
        },
        {
            'if': {
                'column_id': 'F1-score_male'
            },
            'border-right': '3px solid white'
        }
        ])

    return (styles, html.Div(legend, style={'padding': '5px 0 5px 0'}))

(styles_img, legend_img) = discrete_background_color_bins(df_img)
(styles_mix, legend_mix) = discrete_background_color_bins(df_mix)
(styles_name, legend_name) = discrete_background_color_bins(df_name)

(styles_img_gender, legend_img_gender) = discrete_background_color_bins(df_img_gender)

white_button_style = {'background-color': 'white',
                      'color': 'black',
                      # 'height': '50px',
                      'width': '120px',
                      'margin-bottom': '50px',
                      'margin-left': '10px',
                      'textAlign': 'center',
                      'padding': '0'}
                      # 'paddingLeft': '5px'

red_button_style = {'background-color': '#add8e6',
                    'color': 'white',
                    # 'height': '50px',
                    'width': '120px',
                    'margin-bottom': '50px',
                    'margin-left': '10px',
                    'textAlign': 'center',
                    'padding': '0'}

app.layout = html.Div([
html.Button('Images only', id='images', n_clicks_timestamp=0),
html.Button('Names only', id='names', n_clicks_timestamp=0),
html.Button('Images + Names', id='mixed', n_clicks_timestamp=0),
# html.Button('F1-score', id='f1-score', n_clicks=0),
# html.Button('All', id='all', n_clicks=1),
html.Div(legend_img, style={'float': 'right'}, id='legend'),
dash_table.DataTable(
    id='table',
    columns=[
    	{'name': 'Model', 'id': 'Model', 'type': 'text'},
        {'name': 'Dataset', 'id': 'Dataset', 'type': 'text'},
        {'name': 'Coverage', 'id': 'Coverage', 'type': 'numeric', 'hideable':True},
        {'name': 'Precision', 'id': 'Precision', 'type': 'numeric', 'hideable':True},
        {'name': 'Recall', 'id': 'Recall', 'type': 'numeric', 'hideable':True},
        {'name': 'F1-score', 'id': 'F1-score', 'type': 'numeric', 'hideable':True}
    ],
    hidden_columns=['Precision','Recall'],
    style_table={'margin-bottom': '50px'},
    data=df_img.to_dict('records'),
    style_cell={'textAlign': 'center'},
    style_data_conditional=styles_img,
    style_header_conditional=[
    {
    	'backgroundColor': 'white',
        'color': 'black',
        'border': '1px solid white',
        'fontWeight': 'bold',
        'textAlign': 'center'
    },
    {
            'if': {
                'column_id': ['Dataset','Model']
            },
            'textAlign': 'right'
        }
       ]
), 
html.Div(legend_img_gender, style={'float': 'right'}, id='legend_gender'),
dash_table.DataTable(
    id='table_gender',
    columns=[
    	{'name': ['','Model'], 'id': 'Model', 'type': 'text'},
        {'name': ['','Dataset'], 'id': 'Dataset', 'type': 'text'},
        {'name': ['Male','Coverage'], 'id': 'Coverage_male', 'type': 'numeric', 'hideable':True},
        {'name': ['Male', 'Precision'], 'id': 'Precision_male', 'type': 'numeric', 'hideable':True},
        {'name': ['Male','Recall'], 'id': 'Recall_male', 'type': 'numeric', 'hideable':True},
        {'name': ['Male','F1-score'], 'id': 'F1-score_male', 'type': 'numeric', 'hideable':True},
        {'name': ['Female','Coverage'], 'id': 'Coverage_female', 'type': 'numeric', 'hideable':True},
        {'name': ['Female', 'Precision'], 'id': 'Precision_female', 'type': 'numeric', 'hideable':True},
        {'name': ['Female','Recall'], 'id': 'Recall_female', 'type': 'numeric', 'hideable':True},
        {'name': ['Female','F1-score'], 'id': 'F1-score_female', 'type': 'numeric', 'hideable':True}
    ],
    hidden_columns=['Precision_male','Precision_female', 'Recall_male', 'Recall_female'],
    data=df_img_gender.to_dict('records'),
    # style_table={'marginTop': '50px'},
    merge_duplicate_headers=True,
    style_cell={'textAlign': 'center'},
    style_data_conditional=styles_img_gender,
    style_header_conditional=[
    {
    	'backgroundColor': 'white',
        'color': 'black',
        'border': '1px solid white',
        'fontWeight': 'bold',
        'textAlign': 'center'
    },
    # {
    #         'if': {
    #             'column_id': ['Dataset','Model']
    #         },
    #         'textAlign': 'center'
    #     }
       ]
)
])

output = [Output("table", "data"), Output("legend", "children"), Output("table", "style_data_conditional"), Output("table", "hidden_columns")]
output.extend([Output(i, "style") for i in ['images', 'names', 'mixed']])

@app.callback(
    output,
    [Input(i, "n_clicks_timestamp") for i in ['images', 'names', 'mixed']],
)

def change_button_style(*n_clicks_timestamp):
	if all(v == 0 for v in n_clicks_timestamp):
		return df_img.to_dict('records'), legend_img, styles_img, ['Precision','Recall'], red_button_style, white_button_style, white_button_style
	max_index = n_clicks_timestamp.index(max(i for i in n_clicks_timestamp if i is not None))
	if max_index == 0:
		return df_img.to_dict('records'), legend_img, styles_img, ['Precision','Recall'], red_button_style, white_button_style, white_button_style
	elif max_index == 1:
		return df_name.to_dict('records'), legend_name, styles_name, ['Precision','Recall'], white_button_style, red_button_style, white_button_style
	elif max_index == 2:
		return df_mix.to_dict('records'), legend_mix, styles_mix, ['Precision','Recall'], white_button_style, white_button_style, red_button_style
        

if __name__ == '__main__':
    app.run_server(debug=True,
        port='8050',
        host='194.95.75.11')