# Project overview and setup instructions
# Autonomous System Analysis with LLM

## Overview
This project explores the use of Large Language Models (LLMs) to analyze Autonomous System (AS) relationships and identify potential cybersecurity threats.

## Setup
1. Install dependencies:
```bash
pip install requests openai
```

2. Configure API keys in `config.py`.

3. Run the project:
```bash
python main.py
```

Local Model Hosting (Optional):

4. **Set Up Local LLM Hosting (Optional)**
    - **Ollama**
        1. **Install Ollama**
            Follow the installation instructions on the [Ollama GitHub Repository](https://github.com/jmorganca/ollama).
        
        2. **Start Ollama Server**
            ```bash
            ollama serve
            ```
        
        3. **Configure Ollama**
            Ensure `ollama_config.py` has the correct API URL and model settings:
            ```python
            OLLAMA_API_URL = "http://localhost:11434"
            OLLAMA_MODEL = "internet_expert"
            ```

    - **OpenWebUI**
        1. **Install OpenWebUI**
            Follow the installation instructions on the [OpenWebUI GitHub Repository](https://github.com/open-webui/open-webui).
        
        2. **Start OpenWebUI Server**
            ```bash
            python webui.py
            ```
        
        3. **Configure OpenWebUI**
            Ensure `openwebui_config.py` has the correct API URL and model settings:
            ```python
            OPENWEBUI_API_URL = "http://localhost:12345"
            OPENWEBUI_MODEL = "cybersecurity_expert"
            ```

**Run the Application**
    ```bash
    python main.py
    ```
    - **Usage**:
        - **Enter ASN**: When prompted, input the ASN you wish to analyze.
        - **Select LLM Engine** (if applicable): Modify `main.py` or use configuration to choose between OpenAI, Ollama, or OpenWebUI for analysis.

# File Descriptions
main.py: Entry point of the application.
data_retrieval.py: Handles API calls to fetch ASN-related data.
data_processing.py: Structures and preprocesses the data.
llm_analysis.py: Executes LLM-driven analysis.
utils.py: Utility functions for file I/O and logging.
config.py: Centralized API keys and configurations.
ollama_config.py: Configuration for integrating with Ollama.
openwebui_config.py: Configuration for integrating with OpenWebUI.
templates/initial_prompt.txt: Prompt template used for LLM initialization.



## Additional Resources
    - **Ollama GitHub Repository**: [https://github.com/jmorganca/ollama](https://github.com/jmorganca/ollama)
    - **OpenWebUI GitHub Repository**: [https://github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)
    - **RIPEstat API Documentation**: [https://stat.ripe.net/docs/](https://stat.ripe.net/docs/)