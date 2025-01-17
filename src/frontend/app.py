import streamlit as st
    from ..agents import director

    st.title('Auto-Blogging Platform')

    topic = st.text_input('Enter blog topic:')
    if st.button('Generate'):
      with st.spinner('Creating blog plan...'):
        # Call director agent
        st.write('Blog plan generated!')
