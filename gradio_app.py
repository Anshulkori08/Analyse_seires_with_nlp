import gradio as gr
from theme_classifier import ThemeClassifier

def get_themes(theme_list_str, subtitles_path, save_path):
    try:
        # Split the theme list string into a list of themes
        theme_list = theme_list_str.split(',')

        # Initialize the ThemeClassifier
        theme_classifier = ThemeClassifier(theme_list)

        # Get the themes from the subtitles
        output_df = theme_classifier.get_themes(subtitles_path, save_path)

        # Remove 'dialogue' from the theme list (if present)
        theme_list = [theme for theme in theme_list if theme != 'dialogue']

        # Sum the scores for each theme
        output_df = output_df[theme_list].sum().reset_index()
        output_df.columns = ['theme', 'score']

        # Create a bar plot using Gradio's BarPlot component
        output_chart = gr.BarPlot(
            output_df,
            x='theme',
            y='score',
            title='Series Themes',
            tooltip=['theme', 'score'],
            vertical=False,
            width=500,
            height=260
        )

        return output_chart

    except Exception as e:
        # Handle any errors that occur during processing
        return f"An error occurred: {str(e)}"

def main():
    # Create the Gradio interface
    with gr.Blocks() as iface:
        with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Theme Classification (Zero Shot Classification)</h1>")
            with gr.Row():
                with gr.Column():
                    plot = gr.BarPlot()
                with gr.Column():
                    theme_list = gr.Textbox(label="Themes (comma-separated)")
                    subtitles_path = gr.Textbox(label="Subtitles or Script Path")
                    save_path = gr.Textbox(label="Save Path")
                    get_themes_button = gr.Button("Get Themes")
                    get_themes_button.click(
                        get_themes,
                        inputs=[theme_list, subtitles_path, save_path],
                        outputs=[plot]
                    )

    # Launch the Gradio interface
    iface.launch(share=True)

if __name__ == '__main__':
    main()