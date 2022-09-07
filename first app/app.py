import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

dataframe = pd.DataFrame(
    {
        "Fruit": ["banana", "maça", "pera", "uva", "mamão"],
        "Amount": [1,2,3,4,5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal"]
    }
)

fig = px.bar(dataframe, x = "Fruit", y = "Amount", color = "City")

app.layout = html.Div(
    children = [
        html.H1("dashboard with python"),
        dcc.Graph(figure=fig)
    ]
)


if __name__ == "__main__":
    app.run_server(debug = True)