# SL_CLIENT_DEMO

## What is this?
This is a super-simple set of python scripts that illustrate the creation of a 
basic Agent, Task and Crew using the crewai Agent framework.  There are two modes 
of operation in this demo:

1. Run an agent from the console and look at the trace info to see what is going on
2. Run a small server to expose an Agent via an end-point and connect via a simple streamlit app

The app_crew.py files are mostly hard-coded and the folder structure doesn't conform to the 
crewai tool standard.  This was done for clarity.  Typically you would expect to see .yaml
files in a config folder to setup the Agent(s) and Task(s).

The project expects the use of uv and you will have to install crewai and uvicorn if you don't
have them on your system.  Installation can be accomplished as follows:

```bash
uv tool install crewai
uv pip install uvicorn
```

To run the programs it is best if you setup your OPENAI_API_KEY and/or your ANTHROPIC_API_KEY
as environment variables.  

 
## Simple Single Agent via Console

This is a single agent example that makes use of the crewai RagTool to vectorize/add
the sample pdf (data/RBH_J1_AAAI10.pdf) to a chromadb database.  This is the crewai
standard and works out of the box without any real config.  Exploring options would 
be interesting.

```terminal
  cd sl_client_demo/stdout_crew
  uv run main.py
```
The single-agent console example can be run as shown above.
Code in the repo is setup to use public "anthropic/claude-3-7-sonnet-latest",
but you can change this to pretty much whatever you like within reason.  There
are a couple of commented out examples specifying openai and a local LLM in the
app_crew.py file.


## Simple Single Agent via Server / Client UI

This is the same example as above but split into a primitive web service with
an accompanying streamlit client UI.

### Start the Server
```terminal
cd sl_client_demo/cs_ui_crew
uv run uvicorn serve_agent:app --reload

INFO:     Will watch for changes in these directories: ['/Users/stevem/python/ui/sl_client_demo/cs_ui_crew']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12555] using WatchFiles
INFO:     Started server process [12557]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
This should start a local server that exposes end-point  http://localhost:8000/run_crew.

### A nicely formed curl test that should give a good result
```bash
curl -X POST 127.0.0.1:8000/run_crew \
     -H "Content-Type: application/json" \
     -d '{"topic": "The cost of hearing aids"}'
```

```text
Crew Execution Completed                                                                                                       
  Name: crew                                                                                                                     
  ID: 192e70c3-487e-4ee0-aebc-702824397db8
  Tool Args:
  Final Output: For hearing aids, the policy indicates a 12-month waiting period before coverage begins. The annual benefit      
  limit is $1,088 per policy, with sub-limits applying. The maximum benefit example shown is $2,720.00 for a hearing aid.        
                                                                                                                                 
  The policy also notes that the hearing aids benefit accumulates over time, with a limit of $5,440 in any 5-year period.
```
<br></br>

### A nicely formed curl example that should give a negative result
```bash
curl -X POST 127.0.0.1:8000/run_crew \
     -H "Content-Type: application/json" \
     -d '{"topic": "The cost of hearing a zebra"}'
```

```text
|  Crew Execution Completed                                                                                                       
│  Name: crew                                                                                                                     
│  ID: 43873667-77fc-4305-b234-b7d5f8daff2d                                                                                       
│  Tool Args:                                                                                                                     
│  Final Output: I'm sorry, but I don't have any information about the cost of zebra insurance, including waiting periods or      
│  annual costs. The knowledge base I have access to contains information about human health insurance policies, but nothing      
│  related to exotic animals like zebras. If you're interested in obtaining insurance for a zebra, I'd recommend contacting       
│  specialized exotic animal insurance providers who can provide you with specific details about coverage options, waiting        
│  periods, and costs for zebra insurance.  
```

## Testing with the World's Worst Web Client
``` terminal
cd sl_client_demo
uv run streamlit run client_app.py
```
This will start a very crappy streamlit application in your default browser.
You can enter an item or topic for the Agent to research/lookup in the vector
store.  The return is not well-formatted.  There are ways to get an agent to 
return well-formatted json in a repeatable manner, but the goal here was to 
simply illustrate that it is quite easy to call an agent (or Agentic workflow)
via a hosted service.  You can do all sorts of things such as tracking conversation
ids and contexts, do web research through the use of the WebScrape and 
SerperAPI or Tavily web-search tools, compare the web results with the info in 
vector store etc. 