# What is it?

This tool analyses a given text and suggests improvements based on the cosine similarity to a list of "standardised" phrases.

Phrases are located in StandardisedTerms.csv and can be modified at any time. 

### Usage

1. Install requirements

```python
pip install -r requirements.txt
```

2. Run from CLI

```python
python main.py <path to your txt file>
```

default threshold is set to 0.4, you can change it by adding --threshold 
