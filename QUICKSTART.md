# Quick Start Guide - Advanced Code Helper AI

Get started with the Advanced Code Helper AI in 5 minutes!

## Prerequisites

- Python 3.9 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/JamieT18/code-helper.git
cd code-helper
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web framework)
- openai (AI integration)
- matplotlib (for gene sequence analyzer)

### Step 3: Get Your OpenAI API Key

1. Visit https://platform.openai.com/api-keys
2. Sign up or log in
3. Create a new API key
4. Copy the key (you'll need it in the next step)

## Running the Application

### Launch the App

```bash
streamlit run advanced_code_helper.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Configure Your API Key

1. Look at the **Settings** section in the left sidebar
2. Paste your OpenAI API key in the "OpenAI API Key" field
3. The app is now ready to use!

> **Note:** Your API key is stored only in your browser session and is never saved to disk.

## First Steps

### Try These Examples

#### 1. Ask a Question

Go to the **💬 Question** tab and try:
```
What's the best way to parse FASTA files in Python?
```

#### 2. Analyze Code

Go to the **📄 Code Snippet** tab, select "Python", and paste:
```python
def gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100
```

Then ask: "Explain this function and suggest improvements"

#### 3. Upload a File

Go to the **📁 File Upload** tab and upload `sample_sequence.fasta` (included in the repository).

The app will automatically analyze it and provide insights!

## What Can You Do?

### Bioinformatics Tasks
- Understand sequence analysis algorithms
- Get help with FASTA, VCF, CSV files
- Learn about ORF finding, GC content, etc.
- Design analysis workflows
- Get tool and library recommendations

### Coding Tasks
- Explain complex code
- Debug errors
- Optimize performance
- Refactor code
- Learn best practices
- Get library suggestions

### Supported File Types
- **FASTA** (.fasta, .fa, .fna, .faa) - DNA/RNA sequences
- **VCF** (.vcf) - Variant calls
- **CSV/TSV** (.csv, .tsv) - Tabular data
- **Scripts** (.py, .r, .R) - Python and R code
- **Text** (.txt) - Any text files

## Tips for Success

1. **Be Specific**: The more context you provide, the better the response
2. **Upload Files**: Give the AI actual data to analyze
3. **Use Conversation History**: Ask follow-up questions
4. **Combine Inputs**: Upload a file AND ask a specific question
5. **Explore Help**: Check the sidebar help sections for more examples

## Troubleshooting

### "Please enter your OpenAI API key"
- Make sure you've entered your API key in the sidebar
- Check that the key is valid and has credits

### "Error getting AI response"
- Verify your API key is correct
- Check your internet connection
- Ensure you have API credits remaining

### File Upload Issues
- Make sure the file is in a supported format
- Check that the file is UTF-8 encoded
- Try with a smaller file if it's very large

## Next Steps

- Read the [Full Documentation](ADVANCED_CODE_HELPER_README.md)
- Check out [Usage Examples](USAGE_EXAMPLES.md)
- Try the [Gene Sequence Analyzer](README.md) CLI tool

## Need Help?

- Check the **Help & Usage** section in the app sidebar
- Review the usage examples
- Read the full documentation

## Environment Variables (Optional)

If you don't want to enter your API key each time, you can set it as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
streamlit run advanced_code_helper.py
```

On Windows:
```cmd
set OPENAI_API_KEY=your-api-key-here
streamlit run advanced_code_helper.py
```

---

**Enjoy using the Advanced Code Helper AI!** 🧬🤖
