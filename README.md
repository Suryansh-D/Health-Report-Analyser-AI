Here's the updated README with a better balance between text and code snippets:

---

# 🧪 Medical Report Analysis with Google Gemini API

This project utilizes Google Gemini API, Streamlit, and CrewAI to analyze medical reports, especially blood test PDFs. It provides detailed insights, relevant articles, and personalized health recommendations through a user-friendly interface.

## ✨ Features

- **PDF Upload & Text Extraction**: Upload and extract text from blood test reports in PDF format.
- **Automated Analysis**: Analyze blood test data, highlight abnormal values, and explain health implications.
- **Health Research**: Find and summarize relevant medical articles based on blood test results.
- **Personalized Recommendations**: Get tailored health advice based on analysis and research findings.
- **Streamlit Interface**: Easy-to-use web interface for non-technical users.

## 🚀 The Power of CrewAI

### What is CrewAI?

CrewAI manages multiple AI agents to achieve complex tasks. Each agent specializes in a specific aspect, ensuring high accuracy and relevance.

### Usage and Benefits of CrewAI

- **Specialized Agents**: Each task is handled by an expert agent, improving accuracy.
- **Task Orchestration**: Manages the sequence and interaction between tasks for a smooth workflow.
- **Scalability**: Easily add more agents or tasks as the project grows.
- **Parallel Processing**: Handle multiple tasks simultaneously to speed up processing.
- **Error Handling**: Robust structure with fallback mechanisms for smooth operation.

## 🛠️ Installation

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/your-username/medical-report-analysis.git
cd medical-report-analysis
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

1. Create a `.env` file in the root directory.
2. Add your API keys and necessary configurations:

```plaintext
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL_NAME=your_openai_model_name
OPENAI_API_BASE=your_openai_api_base
```

### Run the Application

Launch the Streamlit application:

```bash
streamlit run main.py
```

This will start a local server. Open the provided URL in your browser to use the application.

## 🚀 Usage

1. **Upload a PDF**: Click on "Choose a PDF file" to upload your blood test report.
2. **Analyze Report**: Click on "Analyze Report" to process and analyze the data.
3. **View Results**: After analysis, view the summary of your blood test, related medical articles, and personalized health recommendations.

## 📂 Project Structure

- **`main.py`**: The main application script. Handles PDF uploads, text extraction, and analysis coordination.
- **`agents.py`**: Defines AI agents and their roles in the project.
- **`tasks.py`**: Specifies the tasks each agent will perform.
- **`tools.py`**: Contains tools used by agents to perform searches and gather data.
- **`requirements.txt`**: Lists all Python dependencies for the project.
- **`.env`**: Stores environment variables like API keys (not included in the repository).

## 🧠 How It Works

1. **PDF Text Extraction**: The application uses `pypdf` to extract text from uploaded PDFs.
2. **Agent-Based Processing**:
   - **Blood Test Analyst**: Analyzes the text, identifies key values, and compares them to normal ranges.
   - **Medical Research Specialist**: Searches for relevant medical articles.
   - **Holistic Health Advisor**: Provides personalized health recommendations.
3. **CrewAI Orchestration**: Manages task sequences and agent interactions for a smooth workflow.

## 🤝 Contributions

Contributions are welcome. Please submit a pull request or report any issues.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for more details.