from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool
from dotenv import load_dotenv
import os
import requests
import rich

# 🔑 Load .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please check your .env file")

# 🔧 Setup OpenAI Client for Gemini
external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client
)
config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

# use a function tool to search products
@function_tool
def get_products():
    """
   Get all available products from the online source.
    """
    url = "https://template6-six.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return products
    except requests.RequestException as e:
        return {"error": str(e)}
    

# 🤖 Agent setup
agent = Agent(
    name = "Shopping Agent",
    instructions = 
    """You're a helpful shopping assistant. Display the available products and recommend one that's
    practical or likely to be popular.""",
    tools = [get_products]
)
# 🚀 Launch Agent – Synchronous Execution
result = Runner.run_sync(
    agent,
    #input = input("\033[1;36m Which thing you want to buy?\033[0m "),
    input = "Show me all the products to buy with name and their prices? ",
    run_config = config
)

# Testing Queries
test_query = [
    "[green] Show me all the products available, including their names, prices & discounted prices in PKR[/green]",
    "[green] What would you suggest for upgrading my living room?[/green]",
    "[green] What do you think is a smart purchase right now?[/green]"
    "[green] What kind of furniture would best suit my space[/green]",
    "[green] Can you recommend something special for my mother?[/green]",
    "[green] Which furniture piece do you need — sofa, table, or chair?[/green]"
    
]
# Loop through all test queries
for query in test_query:
    rich.print(f"\n[b cyan] 🤺 User Prompt:[/b cyan] {query}")
    result = Runner.run_sync(
        agent, 
        input = query,
        run_config = config
    )

# 🔗 Display the result
rich.print(f"[blue] Agent Response:[/blue] {result.final_output}")
