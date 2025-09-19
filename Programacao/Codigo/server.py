import asyncio
import os
from mcp_use import MCPAgent, MCPClient
from langchain_ollama import ChatOllama

async def main():
    config_path = os.path.join(os.path.dirname(__file__), "..\Json/mcp-config.json")
    client = MCPClient.from_config_file(config_path)

    llm = ChatOllama(model="qwen3:1.7b")

    agent = MCPAgent(
        llm=llm,
        client=client,
        system_prompt="Assistant that can help answer user queries",
        memory_enabled=True,
        max_steps=30
    )

    result = await agent.run("Fetch the latest news headlines for me.")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
