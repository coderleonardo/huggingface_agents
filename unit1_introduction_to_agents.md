# UNIT 1. INTRODUCTION TO AGENTS

## What is an Agent?

An Agent is: an **AI model capable of reasoning, planning, and interacting with its environment**. 

We call it Agent because it has agency, aka it has the ability to interact with the environment.

Steps: 
1. Think and Plan
2. Act using Tools

### More formal 
---

*An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks*.

---

We can think an Agent having 2 parts:
1. The Brain (AI Model)
    - This is where all the thinking happens. The AI model handles reasoning and planning. It decides which Actions to take based on the situation.
2. The Body (Capabilities and Tools)
    - This part represents everything the Agent is equipped to do. The scope of possible actions depends on what the agent has been equipped with

([smolagents conceptual guide](https://huggingface.co/docs/smolagents/conceptual_guides/intro_agents))

###  How does an AI take action on its environment?

Agents are powered by **Tools**, which add functionalities that enable them to perform specific actions.

### What type of tasks can an Agent do?

An Agent can perform any task we implement via **Tools** to complete Actions.

- Example 1: Personal Virtual Assistants

    Virtual assistants like Siri, Alexa, or Google Assistant, work as agents when they interact on behalf of users using their digital environments.

    They take user queries, analyze context, retrieve information from databases, and provide responses or initiate actions (like setting reminders, sending messages, or controlling smart devices).

---

To summarize, an Agent is a system that uses an AI Model (typically an LLM) as its core reasoning engine, to:

- Understand natural language: Interpret and respond to human instructions in a meaningful way.

- Reason and plan: Analyze information, make decisions, and devise strategies to solve problems.

- Interact with its environment: Gather information, take actions, and observe the results of those actions.


## Quick Quiz 1

- Q1: What is an Agent?
    - An AI model that can reason, plan, and use tools to interact with its environment to achieve a specific goal.

- Q2: Why does an Agent need to plan before taking an action?
    - To decide on the sequence of actions and select appropriate tools needed to fulfill the user’s request.

- Q3: Why are tools essential for an Agent?
    - Tools provide the Agent with the ability to execute actions a text-generation model cannot perform natively, such as making coffee or generating images.

- Q4: What is the key difference between Actions and Tools?
    -  Actions are the steps the Agent takes, while Tools are external resources the Agent can use to perform those actions.

-  Q5: What Role Do Large Language Models (LLMs) Play in Agents?
    -  LLMs serve as the reasoning 'brain' of the Agent, processing text inputs to understand instructions and plan actions.

## [What are LLMs?](https://huggingface.co/learn/agents-course/unit1/what-are-llms)

([NLP course](https://huggingface.co/learn/nlp-course/chapter1/1))

### What is a Large Language Model?

An LLM is a type of AI model that excels at **understanding and generating human language**. They are trained on vast amounts of text data, allowing them to learn patterns, structure, and even nuance in language. 

Most LLMs nowadays are built on the **Transformer architecture**.

**There are 3 types of transformers**:
1. *Encoders*: An encoder-based Transformer takes text (or other data) as input and outputs a dense representation (or embedding) of that text.
    - Use Cases: Text classification, semantic search, Named Entity Recognition

2. *Decoders*: A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time.
    - Use Cases: Text generation, chatbots, code generation

3. *Seq2Seq (Encoder–Decoder)*: A sequence-to-sequence Transformer combines an encoder and a decoder. The encoder first processes the input sequence into a context representation, then the decoder generates an output sequence.
    - Use Cases: Translation, Summarization, Paraphrasing

The main objective of a LLM is to predict the next token, given a sequence of previous tokens. A “token” is the unit of information an LLM works with. You can think of a “token” as if it was a “word”, but for efficiency reasons LLMs don’t use whole words.

Each LLM has some special tokens specific to the model. The LLM uses these tokens to open and close the structured components of its generation. The most important of those is the **End of sequence token** (EOS).

### [Understanding next token prediction]

LLMs are said to be autoregressive, meaning that **the output from one pass becomes the input for the next one**. In other words, an LLM will decode text until it reaches the EOS. 

![Next Token Prediction](images/AutoregressionSchema.gif)






