# Advanced Code Helper AI 🧬

A powerful Streamlit web application that provides intelligent assistance for bioinformatics and software development tasks using OpenAI's GPT-4.

## Features

### 🎯 Multi-Modal Input
- **Text Questions**: Ask any bioinformatics or coding question
- **Code Snippets**: Paste code for explanation, debugging, or improvement
- **File Upload**: Upload scripts and bioinformatics data files for analysis

### 🧠 Intelligent Assistance
- **OpenAI GPT-4 Integration**: Leverages advanced AI for accurate and detailed responses
- **Conversation History**: Maintains context across multiple questions
- **Context-Aware**: Uses uploaded files and code snippets to provide relevant answers

### 🧬 Bioinformatics Support
- **File Format Analysis**:
  - FASTA sequence files (.fasta, .fa, .fna, .faa)
  - VCF (Variant Call Format) files
  - CSV/TSV data files
- **Specific Bioinformatics Help**:
  - Sequence analysis techniques
  - Gene annotation workflows
  - ORF finding and analysis
  - Algorithm recommendations
  - Library suggestions (BioPython, etc.)

### 💻 Coding Support
- **Languages**: Python (primary), R (primary), and general programming
- **Capabilities**:
  - Code explanation and documentation
  - Debugging assistance
  - Performance optimization suggestions
  - Refactoring recommendations
  - Library and tool recommendations
  - Best practices guidance

### 🎨 User Experience
- **Modern UI**: Clean, responsive interface built with Streamlit
- **Interactive Sidebar**: Easy access to settings and help documentation
- **Conversation Management**: Clear context and start fresh anytime
- **File Preview**: Preview uploaded files before analysis
- **Real-time Analysis**: Instant file analysis and insights

## Requirements

- Python 3.9+
- streamlit >= 1.28.0
- openai >= 1.0.0
- matplotlib >= 3.7.0 (for gene sequence analyzer integration)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JamieT18/code-helper.git
   cd code-helper
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API Key**:
   - Get your API key from https://platform.openai.com/api-keys
   - Either:
     - Enter it in the app's sidebar when you launch it, or
     - Set as environment variable: `export OPENAI_API_KEY='your-key-here'`

## Usage

### Running the Application

```bash
streamlit run advanced_code_helper.py
```

The app will open in your default web browser at `http://localhost:8501`

### Example Use Cases

#### 1. Ask Bioinformatics Questions
```
Question: "How do I calculate GC content in a DNA sequence using Python?"
```

#### 2. Explain Code
```
Code Snippet:
def find_orfs(sequence, min_length=75):
    orfs = []
    for frame in range(3):
        # ... code ...
    return orfs
Question: "Explain this ORF finding function"
```

#### 3. Analyze Files
Upload a FASTA file and ask:
```
"Analyze this sequence and suggest potential genes of interest"
```

#### 4. Debug Code
```
Code Snippet: [Your Python/R code with an error]
```
