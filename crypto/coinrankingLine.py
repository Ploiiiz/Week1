import requests
import pandas as pd
import plotly.graph_objects as go
import json
import datetime
import plotly.express as px
import header
import sqlite3

def line(uuid):

    # Connect to the database
    conn = sqlite3.connect("coinranking.db")

    # Create a cursor
    cursor = conn.cursor()

    # Set the API key in the request header
    headers = header.headers


    # Make a request to the Coinranking API
    url = "https://coinranking1.p.rapidapi.com/coin/" + uuid + "/history"
    params = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h"}
    response = requests.get(url, params=params, headers=headers)

    # Check the status code of the response
    if response.status_code != 200:
        print("Error: Could not retrieve data from Coinranking API")
        exit()

    data = json.loads(response.text)
    df = pd.DataFrame(data["data"]["history"])

    # Store the coin data in a DataFrame


    df['timestamp']= df['timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df.to_excel('coinrankingline.xlsx', sheet_name='line', index=True)

    df.to_sql("priceBTC" , conn, if_exists="replace")

    # Create a line chart


    cryt = pd.read_excel('coinrankingline.xlsx')

    # line_g = px.line(data_frame=cryt,x = 'timestamp',y = 'price')
    line_g = go.Scatter(x = cryt.timestamp ,y = cryt.price, line_color='#0066FF')
    # print(line_g)

    # Create the figure and show the plot
    # fig = go.Figure(line_g)

    # fig.show()

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()

    # return fig.show()
    return line_g

# line("Qwsogvtv82FCd")