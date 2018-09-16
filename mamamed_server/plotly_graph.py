import plotly from conf import plotly_conf
# Create random data with numpy
import numpy as np def my_handler(event, context):
    message = 'Hello {} {}!'.format(event['medications'],
                                    event['diagnoses'],
                                    event['appointments'])
    return {
        'message' : message
    }
def create_linegraph(random_x, random_y):
    # Create a trace
    trace = go.Scatter(
        x=random_x,
        y=random_y
    )
    #print(random_x, '\n', random_y)
    data = [trace]
    print("end1")
    py.plot(data, filename='basic-line_cfwarnoc')
    return 'Yay' import plotly.plotly as py import plotly.graph_objs as go def 
createplot_timeline(plot_type, x_axis, y_axis, yaxis_title, type_color, text):
    timeline_x = np.linspace(0, 39, 20)
    label_timeline_x = ["Week {}".format(int(i)) for i in timeline_x]
    trace1 = go.Scatter(
        x=x_axis,
        y=y_axis,
        text=text_hover,
        hoverinfo='text',
        mode = 'markers',
        marker=dict(
            size=8,
            color = type_color, #set color equal to a variable
        )
    )
    data = [trace1]
    layout = go.Layout(
        xaxis=dict(
            title='Weeks',
            showgrid=False,
            zeroline=False,
            showline=False,
            titlefont=dict(
                family='Arial, sans-serif',
                size=18,
                color='black'
            ),
            showticklabels=True,
            #tickangle=45, range=x_axis,
            ticktext=label_timeline_x,
            tickvals=timeline_x,
            tickfont=dict(
                family='Old Standard TT, serif',
                size=14,
                color='black'
            ),
            exponentformat='e',
            showexponent='all'
        ),
        yaxis=dict(
            title= yaxis_title,
            showgrid=False,
            zeroline=False,
            showline=False,
            titlefont=dict(
                family='Arial, sans-serif',
                size=18,
                color='black'
            ),
            showticklabels=False,
            #tickangle=45,
            tickfont=dict(
                family='Old Standard TT, serif',
                size=14,
                color='black'
            ),
            exponentformat='e',
            showexponent='all'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    response_url = py.plot(fig, filename='patient_timeline_{}'.format(plot_type))
    return response_url if __name__ == "__main__":
    response_colors = {
        'symptoms': {'color':'blue', 'yaxis_title': ' Google Home Responses'},
        'diagnosis': {'color':'red','yaxis_title':'Diagnoses'},
        'encounters': {'color':'purple', 'yaxis_title': 'Visits'},
        'medications': {'color': 'green', 'yaxis_title': 'Medications'}
    }
    for key, values in response_colors.items():
        x_axis = [1, 5, 7, 10, 14, 23, 32, 39]
        y_axis = [0]*len(x_axis)
        yaxis_title = values['yaxis_title']
        text_hover = values['text']
        plot_type = key
        type_color = values['color']
        plot_url = createplot_timeline(plot_type, x_axis, y_axis, yaxis_title, type_color, 
text_hover)
        print(plot_url)
    plotly.tools.set_credentials_file(username=plotly_conf.login_details['username'],
                                      api_key=plotly_conf.login_details['password'])
