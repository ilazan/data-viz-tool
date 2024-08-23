import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data from a CSV file
@st.cache(allow_output_mutation=True)
def load_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

# Function to generate Plotly plot code as a string
def generate_plotly_code(df_name, x_col, y_col, kind='line'):
    if kind == 'line':
        code = f"import plotly.express as px\n\ndf = pd.read_csv('{df_name}')\nfig = px.line(df, x='{x_col}', y='{y_col}')\nfig.show()"
    elif kind == 'bar':
        code = f"import plotly.express as px\n\ndf = pd.read_csv('{df_name}')\nfig = px.bar(df, x='{x_col}', y='{y_col}')\nfig.show()"
    # Add more plot types as needed
    return code

# Main function for the Streamlit app
def main():
    st.title("Let's plot something :blue[cool] :call_me_hand:")
    st.subheader("Data Visualization from CSV :bar_chart:")


    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = load_csv(uploaded_file)
        if st.checkbox('Show raw data'):
            st.write(data)

        # Let users select the plot type and columns to plot
        plot_type = st.selectbox("Select Plot Type", ['Line', 'Bar'])  # Extend with more plot types as needed
        columns = data.columns.tolist()
        
        x_axis = st.selectbox("Choose X-axis", columns)
        y_axis = st.selectbox("Choose Y-axis", columns, index=1 if len(columns) > 1 else 0)

        # Generate and display the plot
        if st.button("Generate Plot"):
            plot_with_plotly(data, x_axis, y_axis, kind=plot_type.lower())
            code = generate_plotly_code("your_uploaded_file.csv", x_axis, y_axis, kind=plot_type.lower())
            st.code(code, language='python')

def plot_with_plotly(df, x_col, y_col, kind='line'):
    if kind == 'line':
        fig = px.line(df, x=x_col, y=y_col)
    elif kind == 'bar':
        fig = px.bar(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
