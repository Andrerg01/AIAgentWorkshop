# Developing a Basic AI Agent with Python (ZN1628 AMN)

**Course Material Repository**

This repository contains the complete course material for "Developing a Basic AI Agent with Python" - a Michelin internal training course designed and delivered by **Dr. Andre Guimaraes** and the **GOAATS Squad** (Business Intelligence & Analytics North America).

🔗 **Course Link**: [Workday Learning Portal](https://wd3.myworkday.com/michelinhr/learning/course/edaca063e04f10015ecd64a067690000?type=9882927d138b100019b6a2df1a46018b)

## 📋 Course Overview

This hands-on course takes you from basic LLM API calls to building sophisticated AI agents capable of:
- 🤖 **Intelligent conversation** with context management
- 🛠️ **Tool integration** for enhanced capabilities
- 🔍 **Smart data querying** with SQL generation
- 🌐 **MCP (Model Context Protocol)** server integration
- 📊 **Multi-agent orchestration** with conditional routing

### What You'll Learn
- Direct API communication with Large Language Models
- LangChain/LangGraph for agent orchestration
- Tool development and integration patterns
- Database querying with AI-generated SQL
- Model Context Protocol (MCP) concepts and usage
- Production-ready agent architecture patterns

## 📚 Course Structure

### Module 1: Introduction (`1 - introduction.ipynb`)
**Foundation: Basic LLM Communication**
- Learn how to make direct API calls to LLMs
- Understand message formats and conversation management
- Set up Azure OpenAI integration
- Handle authentication and environment configuration
- Parse and process LLM responses

**Key Concepts**: API calls, message roles, response handling, environment setup

### Module 2: Simple Chat (`2 - simple_chat.ipynb`)
**Framework: LangGraph Introduction**
- Introduction to LangChain/LangGraph ecosystem
- Build your first stateful agent using StateGraph
- Implement conversation memory and context management
- Create interactive chat loops with personality
- Understand nodes, edges, and graph compilation

**Key Concepts**: StateGraph, AgentState, nodes/edges, conversation flow

### Module 3: Introducing Tools (`3 - introducing_tools.ipynb`)
**Enhancement: Tool Integration & Routing**
- Transform simple chat into a tool-enabled agent
- Implement intelligent routing with conditional logic
- Build email search tool using MCP servers
- Learn router agent patterns for tool selection
- Understand tool context management

**Key Concepts**: Tool integration, conditional routing, MCP servers, context management

### Module 4: Final Agent (`4 - final_agent.ipynb`)
**Advanced: Smart Data Querying**
- Build agents that generate SQL queries dynamically
- Implement intelligent database interactions
- Use DuckDB for local data processing
- Advanced MCP integration for remote databases
- Multi-layer agent architecture

**Key Concepts**: SQL generation, data querying, DuckDB, advanced MCP usage

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ 
- Jupyter Notebook or VS Code with Jupyter extension
- Access to Azure OpenAI or compatible LLM service

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://gitlab.michelin.com/amer-goaats/ai_agents/ai_agent_course_i.git
   cd ai_agent_course_i
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Configure environment variables**:
   ```bash
   cp course_material/.env.example course_material/.env
   # Edit .env file with your API credentials
   ```

4. **Start learning**:
   ```bash
   jupyter notebook course_material/
   ```

### Configuration Files
- **`.env.example`**: Template for environment variables
- **`my_functions.py`**: Utility functions for LLM communication
- **`my_mcp_functions.py`**: MCP server integration helpers

## 🗂️ Repository Structure

```
course_material/
├── 1 - introduction.ipynb          # Basic LLM API communication
├── 2 - simple_chat.ipynb           # LangGraph fundamentals  
├── 3 - introducing_tools.ipynb     # Tool integration & routing
├── 4 - final_agent.ipynb           # Advanced agents with SQL
├── my_functions.py                 # Core utility functions
├── my_mcp_functions.py             # MCP integration helpers
├── .env.example                    # Environment template
└── data/
    ├── mock_emails.json            # Sample email data
    └── mock_sales_data.csv         # Sample sales data
```

## 🔧 Technical Stack

- **🐍 Python**: Core programming language
- **📊 Jupyter**: Interactive development environment  
- **🦜 LangChain/LangGraph**: Agent orchestration framework
- **🤖 Azure OpenAI**: LLM service provider
- **🗄️ DuckDB**: Local SQL query engine
- **🐼 Pandas**: Data manipulation and analysis
- **🌐 MCP**: Model Context Protocol for tool integration

## 🏗️ Platform Support

### ✅ Local Development
- **Full Support**: All modules work completely
- **MCP Integration**: Fully functional
- **Database Operations**: DuckDB and Pandas integration
- **Interactive Notebooks**: Complete Jupyter experience

### 🔄 Databricks Environment  
- **Core Modules**: Modules 1-4 core functionality works
- **⚠️ MCP Limitation**: MCP server functionality not yet supported
- **Database**: Native Databricks integration available
- **Deployment**: Cloud-based execution

## 👨‍🏫 About the Instructor

**Dr. Andre Guimaraes**  
andre.guimaraes1@michelin.com  
Senior Data Scientist, Michelin North America  
GOAATS Squad (Business Intelligence & Analytics)

Specializing in AI/ML applications for industrial and business intelligence use cases.

## 🤝 Support & Contribution

This is an internal Michelin training resource. For questions or improvements:
- Contact the GOAATS Squad
- Submit issues via GitLab
- Join our internal [AI Agents Dev Network](https://michelingroup.sharepoint.com/sites/AIAgentsinMichelin)

## 📄 License

Internal Michelin training material. All rights reserved.

---

**Happy Learning!** 🎉 Build your first AI agent and join the future of intelligent automation.
