from plotly.subplots import make_subplots
import plotly.graph_objects as go



fig = make_subplots(
    insets=[{
        'cell': (1, 1),
        'l': 0.6,
        'b': 0.6
    }]
)

fig.add_trace(
    go.Scatter(x=[1,2,3,4], y=[10,20,15,25]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=[1,2],
        y=[15,20],
        xaxis='x2',
        yaxis='y2'
    )
)

fig.show()