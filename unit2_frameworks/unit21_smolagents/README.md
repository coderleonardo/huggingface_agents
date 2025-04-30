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