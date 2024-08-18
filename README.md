Here’s the updated README with the usage and benefits of using CrewAI:

```markdown
# 🧪 Medical Report Analysis with Google Gemini API

This project leverages the power of Google Gemini API, Streamlit, and advanced AI agents powered by CrewAI to analyze medical reports, particularly blood test PDFs, and provide detailed insights, related articles, and health recommendations. With an intuitive interface and robust backend, this application is designed to help users understand their medical data in simple terms.

## ✨ Features

- **PDF Upload & Text Extraction**: Upload blood test reports in PDF format. The application extracts text from these reports for further analysis.
- **Automated Analysis**: AI agents analyze the blood test data, comparing values against normal ranges, highlighting any abnormal values, and explaining potential health implications.
- **Health Research**: The application searches for relevant medical articles related to the blood test results, summarizing the findings to enhance understanding.
- **Personalized Recommendations**: Based on the analysis and research, users receive health recommendations tailored to their specific results.
- **Streamlit Interface**: An easy-to-use web interface built with Streamlit, making the application accessible to non-technical users.

## 🚀 The Power of CrewAI

### What is CrewAI?

CrewAI is a framework designed to manage and orchestrate multiple AI agents working together to achieve complex tasks. It allows for the creation of specialized agents that can handle different aspects of a project, ensuring that each component is handled by an expert agent.

### Usage and Benefits of CrewAI

- **Specialized Agents**: CrewAI enables the creation of specialized agents, each focused on a particular task, such as analyzing medical data, conducting research, or providing recommendations. This specialization ensures high accuracy and relevance in the outputs.
  
- **Task Orchestration**: CrewAI manages the sequence and interaction between tasks, ensuring that the output of one agent can be effectively used by another. This orchestration is crucial for complex workflows like medical report analysis, where each step depends on the previous one.

- **Scalability**: With CrewAI, it's easy to add more agents to handle additional tasks or to scale the existing tasks. This makes the framework adaptable to more complex projects or additional features.

- **Parallel Processing**: CrewAI can manage agents in a parallel processing mode, where multiple tasks can be handled simultaneously, speeding up the overall process.

- **Error Handling and Resilience**: CrewAI's structure allows for robust error handling and fallback mechanisms, ensuring that the project can continue smoothly even if one part encounters an issue.

## 🛠️ Installation

To set up the project on your local machine, follow these steps:

### Prerequisites

- **Python 3.8+**
- **pip (Python package installer)**

### Clone the Repository

```bash
git clone https://github.com/your-username/medical-report-analysis.git
cd medical-report-analysis
```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

1. Create a `.env` file in the root directory of the project.
2. Add your API keys and other necessary configurations:

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
2. **Analyze Report**: After uploading, click on "Analyze Report." The application will take a few moments to process and analyze the data.
3. **View Results**: Once the analysis is complete, view the results including a summary of your blood test, related medical articles, and personalized health recommendations.

## 📂 Project Structure

- **`main.py`**: The main entry point of the application. Handles PDF upload, text extraction, and coordinates the analysis process.
- **`agents.py`**: Defines the AI agents used in the project, including their roles, goals, and behaviors.
- **`tasks.py`**: Defines the tasks that each agent will perform during the analysis process.
- **`tools.py`**: Contains tools used by the agents to perform searches and gather data.
- **`requirements.txt`**: Lists all the Python dependencies needed for the project.
- **`.env`**: Stores environment variables like API keys (not included in the repository).

## 🧠 How It Works

1. **PDF Text Extraction**: The application uses `pypdf` to extract text from the uploaded PDF.
2. **Agent-Based Processing**:
   - **Blood Test Analyst**: Analyzes the extracted text, identifying key values and comparing them to normal ranges.
   - **Medical Research Specialist**: Searches for relevant medical articles based on the blood test results.
   - **Holistic Health Advisor**: Provides personalized health recommendations based on the analysis and research findings.
3. **CrewAI Orchestration**: Manages the sequence of tasks and agent interactions, ensuring a smooth and coherent workflow.

## 🤝 Contributions

Contributions to this project are welcome. Please feel free to submit a pull request or report any issues.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for more details.
```
## Made by Suryansh Dubey