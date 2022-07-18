import plotly.graph_objects as go

values = [0, 100, 150, 40, 25, 75, 30, 25, 20, 50, 25, 15, 15, 10]
labels = [
    "calcs",
    "M&B",
    "BAA",
    "KIER",
    "M&B D-R",
    "M&B A-R",
    "BAA D-R",
    "BAA A-R",
    "BAA A-D",
    "BAA BenStat",
    "BAA PINCs",
    "KIER SMPI",
    "KIER LifeStyle",
    "KIER PINCs",
]
parents = [
    "",
    "calcs",
    "calcs",
    "calcs",
    "M&B",
    "M&B",
    "BAA",
    "BAA",
    "BAA",
    "BAA",
    "BAA",
    "KIER",
    "KIER",
    "KIER",
]

fig = go.Figure(
    go.Treemap(labels=labels, values=values, parents=parents, marker_colorscale="Blues")
)

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig.show()
