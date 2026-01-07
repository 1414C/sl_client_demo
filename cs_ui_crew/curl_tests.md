# Some Curl Tests

## A nicely formed example that should give a good result
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
<br>


## A nicely formatted example that should give a negative result
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
