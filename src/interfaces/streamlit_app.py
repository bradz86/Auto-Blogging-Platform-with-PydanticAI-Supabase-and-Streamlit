"""
    Streamlit UI for Multi-Agent System
    Following Streamlit's official documentation
    """
    import streamlit as st
    from pydantic_ai import RunResult
    from ..agents.director_agent import director_agent, ContentRequest
    from ..config.dependencies import AppDependencies

    def main():
        """
        Main Streamlit application following official documentation
        """
        # Set page configuration
        st.set_page_config(
            page_title="Content Creation System",
            page_icon="📝",
            layout="centered"
        )

        # Sidebar for authentication (future implementation)
        with st.sidebar:
            st.title("Authentication")
            st.markdown("""
            Future authentication will be implemented here using Supabase.
            Users will be able to:
            - Log in/out
            - Manage profile
            - View history
            """)

        # Main content area
        st.title("📝 Content Creation System")
        st.markdown("Create high-quality content using our AI-powered system")

        # Form for content creation
        with st.form("content_creation_form"):
            st.subheader("Content Parameters")
            
            # Input fields
            col1, col2 = st.columns(2)
            with col1:
                user_id = st.text_input("User ID", value="123")
                topic = st.text_input("Topic", value="AI in Content Creation")
            with col2:
                keywords = st.text_input("Keywords (comma separated)", value="AI, content creation, SEO")
                content_type = st.selectbox(
                    "Content Type",
                    ["blog", "article", "guide", "whitepaper"]
                )
            
            # Additional options
            publish = st.checkbox("Publish Content", value=False)
            
            # Submit button
            submitted = st.form_submit_button("Create Content")

        if submitted:
            # Create dependencies
            deps = AppDependencies(
                supabase_url='your-supabase-url',
                supabase_key='your-supabase-key',
                openai_api_key='your-openai-api-key'
            )

            # Create content request
            request = ContentRequest(
                user_id=user_id,
                topic=topic,
                keywords=[k.strip() for k in keywords.split(",")],
                content_type=content_type,
                publish=publish
            )

            # Progress bar and status
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Run the director agent
            try:
                status_text.text("Initializing content creation...")
                progress_bar.progress(10)

                result: RunResult = director_agent.run_sync(
                    f"Create content about {topic}",
                    deps=deps
                )

                progress_bar.progress(100)
                status_text.text("Content creation complete!")

                # Display results
                if result.data.status == "success":
                    st.success(result.data.message)
                    if result.data.content_url:
                        st.markdown(f"**Content URL:** [{result.data.content_url}]({result.data.content_url})")
                    
                    # Show usage statistics in expander
                    with st.expander("View Usage Statistics"):
                        st.json(result.usage().dict())
                else:
                    st.error(result.data.message)

            except Exception as e:
                progress_bar.progress(100)
                status_text.text("Content creation failed!")
                st.error(f"An error occurred: {str(e)}")

    if __name__ == '__main__':
        main()
