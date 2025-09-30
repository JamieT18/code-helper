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
   git clone https://github.com/JamieT18/gene-sequence-analysis.git
   cd gene-sequence-analysis
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
Question: "Why is this code throwing an error and how can I fix it?"
```

#### 5. Get Workflow Suggestions
```
Question: "What's the best workflow for analyzing RNA-seq data in Python?"
```

## Architecture

The application is built with modularity and extensibility in mind:

### Core Components

1. **Session Management** (`initialize_session_state()`):
   - Manages conversation history
   - Stores uploaded file content
   - Handles API key configuration

2. **File Analysis** (`analyze_uploaded_file()`):
   - Automatic file type detection
   - Format-specific analysis
   - Integration with existing gene sequence analyzer

3. **AI Integration** (`get_ai_response()`):
   - OpenAI GPT-4 API calls
   - Context building from multiple sources
   - Conversation history management

4. **UI Components**:
   - `render_sidebar()`: Settings and help documentation
   - `render_main_content()`: Main interaction interface

### File Type Handlers

- **FASTA Files**: Sequence analysis, GC content, length statistics
- **VCF Files**: Variant count, header analysis, format validation
- **CSV/TSV Files**: Column detection, data preview, format analysis
- **Code Files**: Function/class detection, import analysis, line counting

## Extending the Application

### Adding New File Types

1. Add file extension to `BIO_EXTENSIONS` dictionary
2. Create an analyzer function following the pattern:
   ```python
   def analyze_new_file_type(content: str, filename: str) -> str:
       # Analysis logic
       return summary
   ```
3. Add detection logic in `detect_file_type()`
4. Call analyzer in `analyze_uploaded_file()`

### Adding New Languages

1. Add language to `LANGUAGES` list
2. Update `analyze_code_file()` with language-specific patterns
3. Update system prompt in `get_system_prompt()` if needed

### Integrating External Tools

The app can be extended to call external bioinformatics tools:
```python
def run_external_tool(input_file: str, tool: str) -> str:
    # Run tool (e.g., BLAST, BWA, etc.)
    # Parse output
    # Return formatted results
    pass
```

## Integration with Gene Sequence Analyzer

The app integrates with the existing `gene_sequence_analyzer.py` module:
- Automatically analyzes uploaded FASTA files
- Provides detailed sequence statistics
- Leverages existing FastaParser functionality

## Security Notes

- API keys are stored in session state (not persisted)
- Use environment variables for production deployments
- Never commit API keys to version control
- Consider rate limiting for production use

## Troubleshooting

### "OpenAI package not installed"
```bash
pip install openai
```

### "Please enter your OpenAI API key"
- Enter API key in the sidebar
- Or set environment variable: `export OPENAI_API_KEY='your-key'`

### "Error getting AI response"
- Check your API key is valid
- Ensure you have API credits available
- Check your internet connection

### File upload errors
- Ensure file is in a supported format
- Check file encoding (UTF-8 recommended)
- Try with a smaller file if very large

## Contributing

Contributions are welcome! Areas for improvement:
- Additional file format support (BAM, SAM, GFF, GTF, etc.)
- More programming language support
- Integration with bioinformatics databases (NCBI, UniProt, etc.)
- Caching for faster responses
- Export conversation history
- Custom model selection (GPT-3.5, GPT-4, etc.)

## License

See the main repository LICENSE file.

## Author

Advanced Code Helper AI - Built for bioinformatics and software development support

## Acknowledgments

- OpenAI for GPT-4 API
- Streamlit for the web framework
- Gene Sequence Analysis Tool (existing module)
