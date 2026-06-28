# BPE Tokenizer from Scratch

This is a work-in-progress implementation of Byte Pair Encoding tokenization, built for learning purpose.

Current status: Training loop functional (merges character pairs iteratively). Encode/decode coming next.

To run: python bpe.py (after downloading tinyshakespeare input.txt)

## Dataset

This project uses a text dataset for training the BPE tokenizer.

You can download the dataset from Kaggle:

**Dataset:** [kaggle](https://www.kaggle.com/datasets/timothypaendongg/tinyshakespeareandrej-karpathy?resource=download)

After downloading, place the file as:

```
input.txt
```

in the project's root directory before running:

```bash
python bpe.py
```
