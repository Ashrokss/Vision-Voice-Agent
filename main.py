import logging
from dotenv import load_dotenv
from vision_agents.core import User, Agent, cli
from vision_agents.core.agents import AgentLauncher
from vision_agents.plugins import getstream, gemini

load_dotenv()
logging.basicConfig(level=logging.INFO)


async def create_agent(**kwargs) -> Agent:
    return Agent(
        edge=getstream.Edge(),
        agent_user=User(name="AI Assistant", id="agent"),
        instructions="You're a friendly voice assistant.",
        llm=gemini.Realtime(),
    )


async def join_call(agent: Agent, call_type: str, call_id: str, **kwargs):
    await agent.create_user()
    call = await agent.create_call(call_type, call_id)

    with await agent.join(call):
        await agent.llm.simple_response(text="Hello! How can I help?")
        await agent.finish()
        await agent.close()

if __name__ == "__main__":
    cli(AgentLauncher(create_agent=create_agent, join_call=join_call))
