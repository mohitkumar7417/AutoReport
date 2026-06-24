import plotly.express as px


def create_interactive_bar_chart(
    df,
    x_column,
    y_column,
    output_file
):
    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )

    fig.write_html(output_file)

def create_interactive_line_chart(
    df,
    x_column,
    y_column,
    output_file
):
    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} Trend"
    )

    fig.write_html(output_file)

def create_interactive_pie_chart(
    df,
    label_column,
    value_column,
    output_file
):
    fig = px.pie(
        df,
        names=label_column,
        values=value_column,
        title=f"{value_column} Distribution"
    )

    fig.write_html(output_file)