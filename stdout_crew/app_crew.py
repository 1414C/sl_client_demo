import os
import warnings

from crewai import LLM, Agent, Crew, Task
from crewai.rag.embeddings.providers.openai.types import OpenAIProviderSpec
from crewai_tools import RagTool
from crewai_tools.rag.data_types import DataType

# from crewai_tools.vectordbs.faiss import FaissVectorDbConfig
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

# uncomment to use local model via ollama / lm studio
# local_llm = LLM(
#     model="openai/gpt-oss-20b",
#     base_url="http://localhost:1234/v1",
#     api_key="lm-studio",
#     provider="openai"
# )

# llm = LLM(model="openai/gpt-4", max_tokens=1024)
llm = LLM(model="anthropic/claude-3-7-sonnet-latest", max_tokens=1024)


rag_tool = RagTool(
    description="A quick and dirty rag implementation using chromadb under the covers",
    similarity_threshold=0.6,
    limit=5,
)
rag_tool.add("../data/RBH_J1_AAAI10.pdf", data_type=DataType.PDF_FILE)
# print(rag_tool)

# define the one and only agent
insurance_agent = Agent(
    role="Senior Insurance Coverage Assistant",
    goal="Determine whether something is covered or not",
    backstory="You are an expert insurance agent designed to assist with coverage queries",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[rag_tool],
    max_retry_limit=5,
)

# define a Task for the Agent
task1 = Task(
    description="What is the waiting period for {topic} and how what is their annual benfit limit?",
    expected_output="A comprehensive response as to the users question",
    agent=insurance_agent,
)

app_crew = Crew(agents=[insurance_agent], tasks=[task1], verbose=True)


def run_crew():
    """Function to run the crew agent."""
    load_dotenv()
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    serper_api_key = os.getenv("SERPER_DEV_API_KEY")
    # print("Anthropic API Key:", anthropic_api_key)
    # print("OpenAI API Key:", openai_api_key)
    # print("Serper Dev API Key:", serper_api_key)
    result = app_crew.kickoff()
    # print(result)
    return result


# def run_crew2(topic: str):
#     """Function to run the crew agent."""
#     load_dotenv()
#     anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
#     openai_api_key = os.getenv("OPENAI_API_KEY")
#     serper_api_key = os.getenv("SERPER_DEV_API_KEY")
#     # print("Anthropic API Key:", anthropic_api_key)
#     # print("OpenAI API Key:", openai_api_key)
#     # print("Serper Dev API Key:", serper_api_key)
#     result = app_crew.kickoff(inputs={"topic": topic})
#     # print(result)
#     return result
