"""
    Weather Agent UI Structure
    Following PydanticAI's Gradio UI documentation example
    """
    import gradio as gr
    from ..agents.weather_agent import get_weather_report

    def create_weather_ui():
        """
        Create Gradio interface for weather agent
        """
        with gr.Blocks() as demo:
            gr.Markdown("# Weather Agent")
            with gr.Row():
                locations = gr.Textbox(
                    label="Enter locations (comma separated)",
                    placeholder="e.g., London, Paris, New York"
                )
                output = gr.Textbox(label="Weather Report", interactive=False)
            
            submit = gr.Button("Get Weather")
            submit.click(
                get_weather_report,
                inputs=locations,
                outputs=output
            )
        
        return demo

    if __name__ == '__main__':
        ui = create_weather_ui()
        ui.launch()
