# Advanced Code Helper AI - Usage Examples

This document provides practical examples of how to use the Advanced Code Helper AI for various bioinformatics and coding tasks.

## Example 1: Understanding ORF Finding

**Question Tab:**
```
How does the ORF (Open Reading Frame) finding algorithm work? 
Explain it for someone learning bioinformatics.
```

**Expected Response:**
The AI will explain the concept of ORFs, start/stop codons, reading frames, and provide code examples.

---

## Example 2: Analyzing a FASTA File

**File Upload Tab:**
1. Upload `sample_sequence.fasta`
2. Ask: "What are the key characteristics of this sequence?"

**Expected Response:**
- Automatic analysis showing sequence length, GC content
- AI suggestions about potential genes, sequence features
- Recommendations for further analysis

---

## Example 3: Debugging Python Code

**Code Snippet Tab:**
```python
def calculate_gc_content(sequence):
    gc = sequence.count('G') + sequence.count('C')
    return gc / len(sequence)

result = calculate_gc_content("ATGC")
print(f"GC Content: {result}%")
```

**Question:**
```
Is this code correct? What improvements can be made?
```

**Expected Response:**
- Points out the percentage calculation is correct
- Suggests adding input validation
- Recommends handling edge cases (empty sequences)
- Suggests adding a docstring
- Mentions the missing multiplication by 100 for percentage display

---

## Example 4: Workflow Suggestions

**Question Tab:**
```
I have RNA-seq data and want to identify differentially expressed genes. 
What's the recommended workflow in Python?
```

**Expected Response:**
- Overview of RNA-seq analysis pipeline
- Tool recommendations (DESeq2, edgeR via rpy2, or Python alternatives)
- Step-by-step workflow with code snippets
- Library suggestions (pandas, numpy, matplotlib, seaborn)

---

## Example 5: Code Explanation

**Code Snippet Tab:**
```python
def find_orfs(sequence, min_length=75):
    orfs = []
    for frame in range(3):
        for i in range(frame, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon == 'ATG':
                start = i
                for j in range(i+3, len(sequence) - 2, 3):
                    stop_codon = sequence[j:j+3]
                    if stop_codon in ['TAA', 'TAG', 'TGA']:
                        if j - start >= min_length:
                            orfs.append((start, j+3, frame+1))
                        break
    return orfs
```

**Question:**
```
Explain what this function does step by step.
```

**Expected Response:**
- Detailed explanation of the ORF finding logic
- Explanation of reading frames
- Description of start and stop codon detection
- Analysis of the minimum length filter

---

## Example 6: Library Recommendations

**Question Tab:**
```
What Python libraries should I use for:
1. Parsing FASTA files
2. Multiple sequence alignment
3. Phylogenetic tree construction
```

**Expected Response:**
- BioPython for FASTA parsing and general bioinformatics tasks
- MUSCLE, Clustal Omega (via subprocess or biopython)
- ETE3 or Dendropy for phylogenetics
- Code examples for each

---

## Example 7: Format Conversion Help

**Question Tab:**
```
How do I convert a VCF file to a pandas DataFrame in Python?
```

**Expected Response:**
- Code example using pandas
- Explanation of VCF format
- Tips for handling large files
- Suggestions for specific columns to extract

---

## Example 8: Algorithm Implementation

**Question Tab:**
```
Implement the Needleman-Wunsch algorithm for global sequence alignment in Python.
```

**Expected Response:**
- Complete implementation with dynamic programming
- Explanation of the algorithm steps
- Example usage
- Suggestions for optimization

---

## Example 9: File Analysis with Context

**File Upload Tab:**
1. Upload a CSV file with gene expression data
2. **Question:**
```
Analyze this data and suggest appropriate visualization techniques 
and statistical tests.
```

**Expected Response:**
- Data structure analysis
- Visualization suggestions (heatmap, volcano plot, PCA)
- Statistical test recommendations
- Code examples for implementation

---

## Example 10: R Code Help

**Code Snippet Tab:**
Select Language: **R**

```r
library(ggplot2)

# Load data
data <- read.csv("expression_data.csv")

# Create plot
ggplot(data, aes(x=gene, y=expression)) +
  geom_bar(stat="identity")
```

**Question:**
```
This code works but the gene names overlap on the x-axis. How can I fix this?
```

**Expected Response:**
- Suggestions to rotate x-axis labels
- Alternative visualization methods
- Code to implement the fix
- Best practices for displaying many categories

---

## Tips for Best Results

1. **Be Specific**: Provide context about your data and goals
2. **Upload Files**: Give the AI actual data to work with
3. **Follow Up**: Ask clarifying questions based on responses
4. **Combine Inputs**: Upload a file AND paste code for comprehensive help
5. **Use Conversation History**: Build on previous responses for complex problems

## Common Use Cases

- **Learning**: Understanding bioinformatics concepts and algorithms
- **Debugging**: Finding and fixing code errors
- **Optimization**: Improving code performance and quality
- **Discovery**: Finding the right tools and libraries for your task
- **Workflow Design**: Planning analysis pipelines
- **Code Review**: Getting feedback on your implementation
- **Format Conversion**: Converting between different file formats
- **Visualization**: Creating effective plots and figures
