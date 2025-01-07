#pip install plotly
import plotly.graph_objects as go
data={
    'id':["A","B","C","D","E","F","G"],
    'parent':["","A","A","B","B","C","D"],
    'value':[10,15,7,8,12,6,5],
}
    
fig=go.Figure(go.Sunburst(
    labels=data['id'],
    parents=data['parent'],
    values=data['value']
))

fig.update_layout(title_text="Sunburst chart")
fig.show()