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

There are 3 folders in this repository: 
1) [data](/Data)
    is where local data is stored
2) [connection](/Connection)
    is where the log of the messages in and out of the private node are stored
3) [Kernel](/Kernel)
    is where the Modules are stores.


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

A module is the foundamental unit of the Private node
A module has the folloing elements:
- main.py file where the module class is implemented 
- config.json where the module core informations are stored

## tests

We use the pytest library for tests. All of them are located in the `tests/` directory. First `pip install pytest` if you haven't already, then:

```bash
$ pytest -v .
```

to run the tests. (-v is verbose, slightly prettier).

## todos

- video coming soon :)

## License

MIT