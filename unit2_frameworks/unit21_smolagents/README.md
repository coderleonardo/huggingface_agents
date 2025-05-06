# UNIT 2.1. INTRODUCTION TO SMOLAGENTS

## Introduction to smolagents

### Some resources

- [smolagents Documentation](https://huggingface.co/docs/smolagents)
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Agent Guidelines](https://huggingface.co/docs/smolagents/tutorials/building_good_agents)
- [LangGraph Agents](https://langchain-ai.github.io/langgraph/)
- [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [RAG Best Practices](https://www.pinecone.io/learn/retrieval-augmented-generation/)

## Why use smolagents?

### What is smolagents?

#### Key Advantages of smolagents

- **Simplicity**: Minimal code complexity and abstractions, to make the framework easy to understand, adopt and extend
- **Flexible** LLM Support: Works with any LLM through integration with Hugging Face tools and external APIs
- **Code-First Approach**: First-class support for Code Agents that write their actions directly in code, removing the need for parsing and simplifying tool calling
- **HF Hub Integration**: Seamless integration with the Hugging Face Hub, allowing the use of Gradio Spaces as tools

#### smolagents is ideal when:

- You need a lightweight and minimal solution.
- You want to experiment quickly without complex configurations.
- Your application logic is straightforward.

### Code vs. JSON Actions

![Code Agent](../../images/code-vs-json-actions.png)

## Small Quiz 

- Q1: What is one of the primary advantages of choosing smolagents over other frameworks?
    - It supports a code-first approach with minimal abstractions, letting agents interact directly via Python function calls

- Q2: In which scenario would you likely benefit most from using smolagents?
    - Prototyping or experimenting quickly with agent logic, particularly when your application is relatively straightforward

- Q3: smolagents offers flexibility in model integration. Which statement best reflects its approach?
    - It can be used with a wide range of LLMs, offering predefined classes like TransformersModel, HfApiModel, and LiteLLMModel

- Q4: How does smolagents handle the debate between code-based actions and JSON-based actions?
    - It focuses on code-based actions via a CodeAgent but also supports JSON-based tool calls with a ToolCallingAgent

- Q5: How does smolagents integrate with the Hugging Face Hub for added benefits?
    - It allows you to push and share agents or tools, making them easily discoverable and reusable by other developers

## Building Agents That Use Code

### Why Code Agents?

Writing actions in code rather than JSON offers several key advantages:
- Composability: Easily combine and reuse actions
- Object Management: Work directly with complex structures like images
- Generality: Express any computationally possible task
- Natural for LLMs: High-quality code is already present in LLM training data

### How Does a Code Agent Work?

![Code Agent Docs](../../images/codeagent_docs.png)

CodeAgent is a special kind of MultiStepAgent. A CodeAgent performs actions through a cycle of steps, with existing variables and knowledge being incorporated into the agent’s context, which is kept in an execution log:

1. The system prompt is stored in a SystemPromptStep, and the user query is logged in a TaskStep.

2. Then, the following while loop is executed:

    - Method agent.write_memory_to_messages() writes the agent’s logs into a list of LLM-readable chat messages.

    - These messages are sent to a Model, which generates a completion.

    - The completion is parsed to extract the action, which, in our case, should be a code snippet since we’re working with a CodeAgent.

    - The action is executed.

    - The results are logged into memory in an ActionStep.

At the end of each step, if the agent includes any function calls (in agent.step_callback), they are executed.

### Examples

See [notebook examples](./code_agents.ipynb).

See also [secure code execution](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution).

In summary, smolagents specializes in agents that write and execute Python code snippets, offering sandboxed execution for security. It supports both local and API-based language models, making it adaptable to various development environments.