# AI-Powered Content Creation System 🚀

    ![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
    ![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
    ![License](https://img.shields.io/badge/license-MIT-green)

    An advanced AI-powered content creation system using PydanticAI, Streamlit, and Supabase. This system provides a multi-agent workflow for creating high-quality, SEO-optimized content.

    ## Features ✨

    - **Multi-Agent System**: Orchestrates content creation through specialized AI agents
    - **Streamlit UI**: User-friendly interface for content creation
    - **Supabase Integration**: Secure storage and user management
    - **SEO Optimization**: Built-in SEO tools and recommendations
    - **Content Types**: Supports blogs, articles, guides, and whitepapers
    - **Publishing Options**: Direct publishing to WordPress (optional)

    ## Getting Started 🛠️

    ### Prerequisites

    - Python 3.9+
    - [Supabase](https://supabase.io/) account
    - [OpenAI](https://openai.com/) API key

    ### Installation

    1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/content-creation-system.git
    cd content-creation-system
    ```

    2. **Set up virtual environment**
    ```bash
    python -m venv .venv
    ```

    3. **Activate the environment**
    ```bash
    # Windows
    .venv\Scripts\activate.bat

    # macOS/Linux
    source .venv/bin/activate
    ```

    4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

    5. **Set up environment variables**
    Create a `.env` file in the root directory:
    ```bash
    SUPABASE_URL=your-supabase-url
    SUPABASE_KEY=your-supabase-key
    OPENAI_API_KEY=your-openai-api-key
    ```

    ### Running the Application

    Start the Streamlit app:
    ```bash
    streamlit run src/interfaces/streamlit_app.py
    ```

    The application will open in your default browser at `http://localhost:8501`

    ## Project Structure 📂

    ```
    content-creation-system/
    ├── src/
    │   ├── agents/               # AI agent implementations
    │   ├── config/               # Configuration and dependencies
    │   ├── interfaces/           # User interfaces
    │   ├── tools/                # Utility functions and tools
    │   └── tests/                # Test cases
    ├── .env.example              # Environment variables template
    ├── requirements.txt          # Project dependencies
    └── README.md                 # This file
    ```

    ## Usage Guide 📖

    ### Creating Content

    1. Open the Streamlit UI
    2. Fill in the content parameters:
       - User ID
       - Topic
       - Keywords
       - Content Type
    3. Choose publishing options
    4. Click "Create Content"
    5. View results and usage statistics

    ### Managing Content

    - View created content in Supabase dashboard
    - Edit content parameters
    - Track content performance

    ## Configuration ⚙️

    ### Environment Variables

    | Variable          | Description                          |
    |-------------------|--------------------------------------|
    | `SUPABASE_URL`    | Supabase project URL                 |
    | `SUPABASE_KEY`    | Supabase API key                     |
    | `OPENAI_API_KEY`  | OpenAI API key                       |
    | `WORDPRESS_URL`   | WordPress site URL (optional)        |
    | `WORDPRESS_AUTH`  | WordPress authentication (optional)  |

    ### Customization

    - Edit `src/config/settings.py` for system-wide configurations
    - Modify agent prompts in respective agent files
    - Customize UI in `src/interfaces/streamlit_app.py`

    ## Contributing 🤝

    We welcome contributions! Please follow these steps:

    1. Fork the repository
    2. Create a new branch (`git checkout -b feature/AmazingFeature`)
    3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
    4. Push to the branch (`git push origin feature/AmazingFeature`)
    5. Open a Pull Request

    Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

    ## License 📄

    This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

    ## Acknowledgments 🎓

    - [PydanticAI](https://pydantic-ai.com/) for the AI framework
    - [Streamlit](https://streamlit.io/) for the UI framework
    - [Supabase](https://supabase.io/) for database and authentication
    - [OpenAI](https://openai.com/) for language models

    ## Support 💬

    For support, please open an issue on GitHub or contact us at support@contentcreation.com

    ---

    Made with ❤️ by Content Creation Team
