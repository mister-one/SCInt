# SCInt (Super Collective Intelligence)

This repository contains the source code (src) of the SCInt PrivateNode.

SCInt is a system designed to facilitate the emergence of a Super Collective Intelligence that helps humanity as a whole in the pursuit of knowledge and understanding.
The system is comprised of 3 core elements:
1. PrivateNode
2. OpenRegistry
3. TruthCertify

The system is govered by a [Constitution](https://docs.google.com/document/d/1ktIPsv0NkotT9ihCdLxaCJkEQ9Kh12R5zb3aqeBpGQk/edit#heading=h.qac0b2w95mhh) and by specific codes that regulate each of the 3 core elements:
- [Code Of Conduct](https://docs.google.com/document/d/1GcxW_d6yM1EUgexUrHy8h6u4Y8F9ER1zOpm0WQKJ5ac/edit#heading=h.z4ii25jmc5sn) relevant for PrivateNode
- [Code Of Information](https://docs.google.com/document/d/13_CACOXRjZBQqwn62qOxpuiqW4l_4x_I5xe6kEeSvME/edit#heading=h.z4ii25jmc5sn) relevant for OpenRegistry
- [Code Of Truth](https://docs.google.com/document/d/1aXai_SLiGqyyuuUWQPVmqyKV6DUiRjZklrfNQ4KM3k8/edit) relevant for TruthCertify

the funcioning of each of the 3 elementsthe associated GPT-2 [code release](https://github.com/openai/gpt-2) from OpenAI. [Sennrich et al. 2015](https://arxiv.org/abs/1508.07909) is cited as the original reference for the use of BPE in NLP applications. Today, all modern LLMs (e.g. GPT, Llama, Mistral) use this algorithm to train their tokenizers.

There are two Tokenizers in this repository, both of which can perform the 3 primary functions of a Tokenizer: 1) train the tokenizer vocabulary and merges on a given text, 2) encode from text to tokens, 3) decode from tokens to text. The files of the repo are as follows:

1. [minbpe/base.py](minbpe/base.py): Implements the `Tokenizer` class, which is the base class. It contains the `train`, `encode`, and `decode` stubs, save/load functionality, and there are also a few common utility functions. This class is not meant to be used directly, but rather to be inherited from.
2. [minbpe/basic.py](minbpe/basic.py): Implements the `BasicTokenizer`, the simplest implementation of the BPE algorithm that runs directly on text.
3. [minbpe/regex.py](minbpe/regex.py): Implements the `RegexTokenizer` that further splits the input text by a regex pattern, which is a preprocessing stage that splits up the input text by categories (think: letters, numbers, punctuation) before tokenization. This ensures that no merges will happen across category boundaries. This was introduced in the GPT-2 paper and continues to be in use as of GPT-4. This class also handles special tokens, if any.
4. [minbpe/gpt4.py](minbpe/gpt4.py): Implements the `GPT4Tokenizer`. This class is a light wrapper around the `RegexTokenizer` (2, above) that exactly reproduces the tokenization of GPT-4 in the [tiktoken](https://github.com/openai/tiktoken) library. The wrapping handles some details around recovering the exact merges in the tokenizer, and the handling of some unfortunate (and likely historical?) 1-byte token permutations.

Finally, the script [train.py](train.py) trains the two major tokenizers on the input text [tests/taylorswift.txt](tests/taylorswift.txt) (this is the Wikipedia entry for her kek) and saves the vocab to disk for visualization. This script runs in about 25 seconds on my (M1) MacBook.

All of the files above are very short and thoroughly commented, and also contain a usage example on the bottom of the file.

## quick start

As the simplest example, we can call the Core module with the following input:

```python
from Kernel.Modules._Core.main import Core

your_input = 'Order my favoirite pizza that cost less than 10£'

core_module = Core()

core_module.execute(your_input)

```

What the Core module does is given an input it predict and execute the most suited module to complete the task untill the end_of_task

`(input)--> || __pred__ | __exec__ || --> (output)`

## Deep dive

The PrivateNode is comprised of 3 folders:
- data
    is where local data is stored
- connection
    is where the log of the messages in and out of the private node are stored
- Kernel
    is where the Modules are stores.

### What is a module

A module is the foundamental unit of the Private node
A module has the folloing elements:
- main.py file where the module is run
- config.json where the module core informations are stored

## tests

We use the pytest library for tests. All of them are located in the `tests/` directory. First `pip install pytest` if you haven't already, then:

```bash
$ pytest -v .
```

to run the tests. (-v is verbose, slightly prettier).

## todos

- write a more optimized Python version that could run over large files and big vocabs
- write an even more optimized C or Rust version (think through)
- rename GPT4Tokenizer to GPTTokenizer and support GPT-2/GPT-3/GPT-3.5 as well?
- write a LlamaTokenizer similar to GPT4Tokenizer (i.e. attempt sentencepiece equivalent)
- video coming soon ;)

## License

MIT