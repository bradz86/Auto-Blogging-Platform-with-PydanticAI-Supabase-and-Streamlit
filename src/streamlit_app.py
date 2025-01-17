"""
    Streamlit Application
    Provides user interface for the platform
    """
    import streamlit as st
    from agents.managers import research_manager_agent

    st.title('Auto-Blogging Platform')

    topic = st.text_input('Enter blog topic:')
    if st.button('Generate'):
      with st.spinner('Creating blog plan...'):
        result = research_manager_agent.research_manager.run_sync(
          topic,
          deps=research_manager_agent.ResearchDependencies(
            topic=topic,
            user_id='123'
          )
        )
        st.write(result.data)
