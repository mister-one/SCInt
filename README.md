# SCInt (Super Collective Intelligence)

This repository contains the source code (src) of the SCInt PrivateNode.

SCInt is a system designed to facilitate the emergence of a Super Collective Intelligence that helps humanity as a whole in the pursuit of knowledge and understanding.
The system is comprised of 3 core elements:
1. PrivateNode
2. OpenRegistry
3. TruthCertify


![overview_image_of_system](/_documentation/images/overview.png)

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


## Manifesto

The current tech industry is broken. It's fragmented and wastes an insane amount of resources. It's dominated by Venture capitalists who splash money to lock you in renting solutions called saas with the objective of extracting as much value from you as possible.
The industry is crowded with white collar people who add Zero value and stand on the shoulders of few hard core engineers/creators who actually build and create value for us all. Most of the time this creator gets a small share of the value they create as business weasels, sales geezers, and banker wankers eat the bigger portion of the pie by creating artificial barriers.
SCInt is here to knock these walls down and build the best open source system built for Humans.
SCInt is essentially build on the belief that with these 3 core elements:

1. Openness
2. Truth
3. Fair reward

We can deliver a fully functioning Super Collective Intelligence that helps humanity as a whole in the pursuit of knowledge and understanding.

In the system im proposing there are 3 agents:
- `Truth Certifiers`
Imagine this as a simple API that given a statement tells you if your statement is true or false. Collectively they vote and decide if something is true or false. To prevent bad actors these TruthCertifiers must have truth_liability_policies that make sure they have skin in the game should they lie

- `Open Registry`
This could be for example BigQuery and is a big queryable collection of public data. The idea is that if you have a central repository of well structured information that is impartially organised (not for example skewed by marketing ads) information can flow faster and more effectively. (For example if you take an Uber you really want to create a public record that says “I need to go from A to B” and this should be accessible to anyone who can take you from A to B rather than just to Uber.

- `Private Nodes`
It’s just a source code that runs on private computers and has some predefined methods to interact with other private nodes, to notarize information and to publish public information. It contains a bunch of modules that solve specific problems and by combining multiple modules it can become intelligent.

## Visual Assets
- `system_interaction`
![system_interaction](/_documentation/images/system_interaction.jpeg)

- `Code Structure`
![folder_structure](/_documentation/images/folder_structure.jpeg)