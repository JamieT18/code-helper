#!/usr/bin/env python3
"""
Advanced Code Helper AI
A Streamlit web application for bioinformatics and coding support.
Provides intelligent assistance using OpenAI API for code explanation,
debugging, bioinformatics analysis, and general programming help.
Author: Advanced Code Helper AI
Python Version: 3.9+
Dependencies: streamlit, openai, matplotlib
"""

import os
import sys
import streamlit as st
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json
import re

# Import the gene sequence analyzer
try:
    from gene_sequence_analyzer import FastaParser, SequenceAnalyzer
except ImportError:
    pass  # Will handle gracefully in the app

# OpenAI import
try:
    from openai import OpenAI
except ImportError:
    st.error("⚠️ OpenAI package not installed. Please run: pip install openai")
    st.stop()


# Constants
APP_TITLE = "🧬 Advanced Code Helper AI"
APP_SUBTITLE = "Intelligent Bioinformatics & Coding Support"

# Bioinformatics file extensions
BIO_EXTENSIONS = {
    '.fasta': 'FASTA sequence file',
    '.fa': 'FASTA sequence file',
    '.fna': 'FASTA nucleic acid file',
    '.faa': 'FASTA amino acid file',
    '.vcf': 'Variant Call Format file',
    '.csv': 'Comma-separated values file',
    '.tsv': 'Tab-separated values file',
    '.txt': 'Text file',
    '.py': 'Python script',
    '.r': 'R script',
    '.R': 'R script'
}

# Programming languages supported
LANGUAGES = ['Python', 'R', 'Java', 'C++', 'JavaScript', 'Shell', 'SQL', 'Other']


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'uploaded_file_content' not in st.session_state:
        st.session_state.uploaded_file_content = None
    if 'uploaded_file_name' not in st.session_state:
        st.session_state.uploaded_file_name = None
    if 'api_key' not in st.session_state:
        st.session_state.api_key = os.getenv('OPENAI_API_KEY', '')


def get_openai_client() -> Optional[OpenAI]:
    """Get OpenAI client with API key."""
    if not st.session_state.api_key:
        return None
    try:
        return OpenAI(api_key=st.session_state.api_key)
    except Exception as e:
        st.error(f"Error initializing OpenAI client: {str(e)}")
        return None


def detect_file_type(filename: str, content: str) -> str:
    """Detect the type of file based on extension and content."""
    ext = Path(filename).suffix.lower()

    if ext in ['.fasta', '.fa', '.fna', '.faa']:
        return 'fasta'
    elif ext == '.vcf':
        return 'vcf'
    elif ext in ['.csv', '.tsv']:
        return 'csv'
    elif ext in ['.py']:
        return 'python'
    elif ext in ['.r', '.R']:
        return 'r'
    elif content.startswith('>'):
        return 'fasta'
    else:
        return 'text'


def analyze_fasta_file(content: str, filename: str) -> str:
    """Analyze FASTA file content and return summary."""
    try:
        # Save to temporary file
        temp_path = Path(f"/tmp/{filename}")
        with open(temp_path, 'w') as f:
            f.write(content)

        # Parse the file
        sequences = FastaParser.parse_file(temp_path)

        summary = f"**FASTA File Analysis: {filename}**\n\n"
        summary += f"- Number of sequences: {len(sequences)}\n"

        for seq_id, seq in sequences.items():
            seq_len = len(seq)
            gc_count = seq.count('G') + seq.count('C')
            gc_content = (gc_count / seq_len * 100) if seq_len > 0 else 0

            summary += f"\n**Sequence: {seq_id}**\n"
            summary += f"  - Length: {seq_len} bp\n"
            summary += f"  - GC Content: {gc_content:.1f}%\n"
            summary += f"  - First 50 bases: {seq[:50]}...\n"

        # Clean up temp file
        temp_path.unlink()

        return summary
    except Exception as e:
        return f"Error analyzing FASTA file: {str(e)}"


def analyze_vcf_file(content: str, filename: str) -> str:
    """Analyze VCF file content and return summary."""
    lines = content.split('\n')
    header_lines = [l for l in lines if l.startswith('##')]
    column_line = [l for l in lines if l.startswith('#CHROM')]
    variant_lines = [l for l in lines if l and not l.startswith('#')]

    summary = f"**VCF File Analysis: {filename}**\n\n"
    summary += f"- Header lines: {len(header_lines)}\n"
    summary += f"- Variant records: {len(variant_lines)}\n"

    if column_line:
        columns = column_line[0].split('\t')
        summary += f"- Columns: {len(columns)}\n"
        summary += f"- Sample columns: {len(columns) - 9}\n"

    if variant_lines:
        summary += f"\n**First variant:**\n```\n{variant_lines[0]}\n```\n"

    return summary


def analyze_csv_file(content: str, filename: str) -> str:
    """Analyze CSV/TSV file content and return summary."""
    lines = content.split('\n')
    non_empty_lines = [l for l in lines if l.strip()]

    summary = f"**CSV/TSV File Analysis: {filename}**\n\n"
    summary += f"- Total lines: {len(non_empty_lines)}\n"

    if non_empty_lines:
        # Detect delimiter
        first_line = non_empty_lines[0]
        if '\t' in first_line:
            delimiter = '\t'
            summary += f"- Format: TSV (tab-separated)\n"
        else:
            delimiter = ','
            summary += f"- Format: CSV (comma-separated)\n"

        columns = first_line.split(delimiter)
        summary += f"- Columns: {len(columns)}\n"
        summary += f"- Column headers: {', '.join(columns[:5])}"
        if len(columns) > 5:
            summary += f" ... ({len(columns) - 5} more)"
        summary += "\n"

        if len(non_empty_lines) > 1:
            summary += f"- Data rows: {len(non_empty_lines) - 1}\n"
            summary += f"\n**First row:**\n```\n{non_empty_lines[1]}\n```\n"

    return summary


def analyze_code_file(content: str, filename: str, language: str) -> str:
    """Analyze code file content and return summary."""
    lines = content.split('\n')
    non_empty_lines = [l for l in lines if l.strip()]
    comment_lines = []

    if language == 'python':
        comment_lines = [l for l in lines if l.strip().startswith('#')]
    elif language == 'r':
        comment_lines = [l for l in lines if l.strip().startswith('#')]

    summary = f"**{language.upper()} Code Analysis: {filename}**\n\n"
    summary += f"- Total lines: {len(lines)}\n"
    summary += f"- Non-empty lines: {len(non_empty_lines)}\n"
    summary += f"- Comment lines: {len(comment_lines)}\n"

    # Extract function/class definitions
    if language == 'python':
        functions = [l.strip() for l in lines if l.strip().startswith('def ')]
        classes = [l.strip() for l in lines if l.strip().startswith('class ')]
        imports = [l.strip() for l in lines if l.strip().startswith(('import ', 'from '))]

        if imports:
            summary += f"- Import statements: {len(imports)}\n"
        if classes:
            summary += f"- Classes defined: {len(classes)}\n"
        if functions:
            summary += f"- Functions defined: {len(functions)}\n"
            summary += f"\n**Functions:**\n"
            for func in functions[:5]:
                summary += f"  - {func}\n"
            if len(functions) > 5:
                summary += f"  ... ({len(functions) - 5} more)\n"

    return summary


def analyze_uploaded_file(filename: str, content: str) -> str:
    """Analyze uploaded file and return summary based on type."""
    file_type = detect_file_type(filename, content)

    if file_type == 'fasta':
        return analyze_fasta_file(content, filename)
    elif file_type == 'vcf':
        return analyze_vcf_file(content, filename)
    elif file_type == 'csv':
        return analyze_csv_file(content, filename)
    elif file_type == 'python':
        return analyze_code_file(content, filename, 'python')
    elif file_type == 'r':
        return analyze_code_file(content, filename, 'r')
    else:
        lines = content.split('\n')
        return f"**Text File Analysis: {filename}**\n\n- Lines: {len(lines)}\n- Characters: {len(content)}\n"


def get_system_prompt() -> str:
    """Get the system prompt for the AI assistant."""
    return """You are an expert AI assistant specialized in bioinformatics and software development. 
You provide helpful, accurate, and detailed assistance with:
1. **Bioinformatics:**
   - DNA/RNA sequence analysis
   - Gene annotation and analysis
   - Protein structure and function
   - Genomic data formats (FASTA, VCF, BAM, etc.)
   - Common bioinformatics workflows and pipelines
   - Tools like BLAST, BWA, SAMtools, BioPython, etc.
2. **Programming:**
   - Python, R, and other languages
   - Code explanation, debugging, and optimization
   - Algorithm design and implementation
   - Library recommendations
   - Best practices and design patterns
3. **Data Analysis:**
   - Statistical analysis
   - Data visualization
   - Machine learning applications
   - Data processing and transformation
Provide clear, concise, and practical answers. Include code examples when relevant.
Format code blocks properly with language specifications.
When analyzing files or code, provide specific insights and actionable suggestions.
"""


def build_context_message(file_content: Optional[str], file_name: Optional[str], 
                         code_snippet: Optional[str]) -> str:
    """Build context message from uploaded files and code snippets."""
    context_parts = []

    if file_content and file_name:
        file_analysis = analyze_uploaded_file(file_name, file_content)
        context_parts.append(f"**Uploaded File Context:**\n{file_analysis}\n\n**File Content:**\n```\n{file_content[:2000]}{'...' if len(file_content) > 2000 else ''}\n```")

    if code_snippet and code_snippet.strip():
        context_parts.append(f"**Code Snippet:**\n```\n{code_snippet}\n```")

    return "\n\n".join(context_parts) if context_parts else ""


def get_ai_response(client: OpenAI, user_message: str, context: str = "") -> str:
    """Get response from OpenAI API."""
    try:
        # Build messages
        messages = [
            {"role": "system", "content": get_system_prompt()}
        ]

        # Add conversation history (last 5 exchanges to manage token limits)
        for msg in st.session_state.messages[-10:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Add context if available
        if context:
            messages.append({
                "role": "user",
                "content": f"Context:\n{context}"
            })

        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=2000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error getting AI response: {str(e)}\n\nPlease check your API key and try again."


def render_sidebar():
    """Render the sidebar with help and settings."""
    with st.sidebar:
        st.title("⚙️ Settings")

        # API Key input
        api_key = st.text_input(
            "OpenAI API Key",
            value=st.session_state.api_key,
            type="password",
            help="Enter your OpenAI API key. Get one at https://platform.openai.com/api-keys"
        )
        if api_key != st.session_state.api_key:
            st.session_state.api_key = api_key
            st.rerun()

        st.divider()

        # Clear conversation button
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.uploaded_file_content = None
            st.session_state.uploaded_file_name = None
            st.rerun()

        st.divider()

        # Help section
        st.title("📖 Help & Usage")

        with st.expander("🧬 Bioinformatics Support"):
            st.markdown("""
            **Supported Formats:**
            - FASTA (.fasta, .fa, .fna, .faa)
            - VCF (Variant Call Format)
            - CSV/TSV data files
            
            **Example Questions:**
            - "Explain the ORF finding algorithm"
            - "How do I calculate GC content?"
            - "What's the best way to parse FASTA files in Python?"
            - "Suggest a workflow for RNA-seq analysis"
            """)

        with st.expander("💻 Coding Support"):
            st.markdown("""
            **Languages:**
            - Python (primary)
            - R (primary)
            - General programming help
            
            **What I Can Help With:**
            - Explain code functionality
            - Debug errors and issues
            - Suggest improvements and optimizations
            - Recommend libraries and tools
            - Refactor code for better quality
            """)

        with st.expander("📤 File Upload"):
            st.markdown("""
            **Upload Files For:**
            - Automatic analysis and insights
            - Context-aware assistance
            - File format conversion help
            - Code review and suggestions
            
            **Supported Files:**
            - Scripts (.py, .r, .R)
            - Data files (.fasta, .vcf, .csv, .tsv)
            - Text files (.txt)
            """)

        with st.expander("💡 Tips"):
            st.markdown("""
            - Be specific in your questions
            - Upload relevant files for context
            - Paste code snippets for analysis
            - Use the conversation history
            - Clear context when switching topics
            """)


def render_main_content():
    """Render the main content area."""
    st.title(APP_TITLE)
    st.markdown(f"*{APP_SUBTITLE}*")

    # Check if API key is set
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to start using the assistant.")
        st.info("💡 You can get an API key at https://platform.openai.com/api-keys")
        return

    # Multi-modal input section
    st.header("📝 Input")

    # Create tabs for different input modes
    tab1, tab2, tab3 = st.tabs(["💬 Question", "📄 Code Snippet", "📁 File Upload"])

    with tab1:
        st.markdown("**Ask any bioinformatics or coding question:**")
        question_input = st.text_area(
            "Your Question",
            height=100,
            placeholder="e.g., How do I find open reading frames in a DNA sequence using Python?",
            label_visibility="collapsed"
        )

    with tab2:
        st.markdown("**Paste code for explanation, debugging, or improvement:**")
        language = st.selectbox("Language", LANGUAGES, index=0)
        code_input = st.text_area(
            "Code Snippet",
            height=200,
            placeholder="Paste your code here...",
            label_visibility="collapsed"
        )

    with tab3:
        st.markdown("**Upload scripts or bioinformatics data files:**")
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=list(BIO_EXTENSIONS.keys()),
            help="Upload FASTA, VCF, CSV, Python, R, or text files"
        )

        if uploaded_file is not None:
            try:
                content = uploaded_file.read().decode('utf-8')
                st.session_state.uploaded_file_content = content
                st.session_state.uploaded_file_name = uploaded_file.name

                st.success(f"✅ File uploaded: {uploaded_file.name}")

                # Show file preview
                with st.expander("Preview uploaded file"):
                    st.text(content[:1000] + ('...' if len(content) > 1000 else ''))
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")

    # Submit button
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        submit = st.button("🚀 Get Help", type="primary", use_container_width=True)

    # Process input when submitted
    if submit:
        # Build the user message
        user_message = ""
        context = ""

        # Collect inputs from different sources
        if question_input and question_input.strip():
            user_message = question_input.strip()

        # Build context from code snippet and uploaded file
        context = build_context_message(
            st.session_state.uploaded_file_content,
            st.session_state.uploaded_file_name,
            code_input if code_input and code_input.strip() else None
        )

        # If only code or file provided without question, create a default question
        if not user_message and context:
            if code_input and code_input.strip():
                user_message = f"Please explain and analyze this {language} code. Suggest any improvements or potential issues."
            elif st.session_state.uploaded_file_content:
                user_message = f"Please analyze this file and provide relevant insights and suggestions."

        if not user_message:
            st.error("Please enter a question or provide code/file to analyze.")
            return

        # Get OpenAI client
        client = get_openai_client()
        if not client:
            st.error("Please configure your OpenAI API key in the sidebar.")
            return

        # Add user message to history
        display_message = user_message
        if context:
            display_message = f"{user_message}\n\n{context}"

        st.session_state.messages.append({
            "role": "user",
            "content": display_message
        })

        # Show loading spinner
        with st.spinner("🤔 Thinking..."):
            # Get AI response
            ai_response = get_ai_response(client, user_message, context)

        # Add assistant response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response
        })

        # Rerun to display the new messages
        st.rerun()

    # Display conversation history
    if st.session_state.messages:
        st.header("💬 Conversation")

        for idx, message in enumerate(st.session_state.messages):
            if message["role"] == "user":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(message["content"])
            else:
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(message["content"])


def main():
    """Main application entry point."""
    # Page config
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🧬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize session state
    initialize_session_state()

    # Render sidebar
    render_sidebar()

    # Render main content
    render_main_content()

    # Footer
    st.divider()
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px;'>
        <small>Advanced Code Helper AI | Powered by OpenAI GPT-4 | 
        Built with Streamlit | Specialized in Bioinformatics & Software Development</small>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
