@@ -2,6 +2,25 @@

A comprehensive Python tool for analyzing DNA sequences from FASTA files. Features include ORF finding, codon usage analysis, and visualization.

## 🆕 Advanced Code Helper AI

**New!** We now include a powerful Streamlit web application that provides intelligent bioinformatics and coding assistance powered by OpenAI GPT-4!

- 🧬 **Bioinformatics Support**: FASTA, VCF, CSV analysis with AI-powered insights
- 💻 **Coding Help**: Code explanation, debugging, refactoring for Python, R, and more
- 📁 **File Analysis**: Automatic analysis of uploaded bioinformatics files
- 💬 **Interactive Chat**: Maintain conversation context for better assistance

[**➡️ See Advanced Code Helper AI Documentation**](ADVANCED_CODE_HELPER_README.md)

### Quick Start
```bash
pip install -r requirements.txt
streamlit run advanced_code_helper.py
```

---

## Features

- **Robust FASTA parsing**: Supports multiline sequences, ignores headers, handles whitespace and non-standard characters gracefully
@@ -95,3 +114,15 @@ The code is modular with clear separation of concerns:
- `SequenceAnalyzer`: Main analysis orchestration
- `Visualizer`: Plot generation with colorblind-friendly design
- `OutputFormatter`: Console and JSON output formatting

## Repository Contents

- **`gene_sequence_analyzer.py`**: Command-line tool for DNA sequence analysis
- **`advanced_code_helper.py`**: Streamlit web application for AI-powered bioinformatics and coding assistance
- **`requirements.txt`**: Python package dependencies
- **`ADVANCED_CODE_HELPER_README.md`**: Detailed documentation for the AI assistant app
- **`sample_sequence.fasta`**: Example FASTA file for testing

## License

See LICENSE file for details.
