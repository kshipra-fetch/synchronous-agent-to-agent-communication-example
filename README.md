# **uAgents Example: Synchronous Agent Communication**

This example demonstrates **synchronous agent-to-agent communication** using the `uAgents` library. Two agents, **Alice** and **Bob**, communicate by exchanging messages. Alice sends a message to Bob, and Bob responds.

## **Installation**

Ensure you have `uAgents` installed:

```bash
pip install uagents
```

## **Usage**

1. **Run Agent 2 (`bob`)** first:
   ```bash
   python agent2.py
   ```
   Copy Bob's agent address from the logs.

2. **Run Agent 1 (`alice`)** and update `agent2_address`:
   - Open `agent1.py`
   - Replace `agent2_address = ""` with Bob’s actual address.
   - Run Alice:
     ```bash
     python agent1.py
     ```

## **How It Works**
- **Alice (`agent1.py`)** sends a message to Bob (`agent2.py`) every **30 seconds**.
- **Bob (`agent2.py`)** receives the message and replies with `"hello from agent2"`.
- Alice logs the response from Bob.

## **Agent1 Log Output**
```
(venv) kshipra@MacBook-Pro-2 global-ai-agents-league-workshop % python3 agent1.py 
INFO:     [alice]: Starting agent with address: agent1q2lkha7n60pljqjyv7ehft8lr54eljwd2m8zkqmm362wck2v3qgrz90nlsd
INFO:     [alice]: Agent inspector available at https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A5001&address=agent1q2lkha7n60pljqjyv7ehft8lr54eljwd2m8zkqmm362wck2v3qgrz90nlsd
INFO:     [alice]: Starting server on http://0.0.0.0:5001 (Press CTRL+C to quit)
INFO:     [alice]: Received awaited response from bob: hello from agent2
INFO:     [uagents.registration]: Registration on Almanac API successful
INFO:     [uagents.registration]: Almanac contract registration is up to date!
INFO:     [alice]: Received awaited response from bob: hello from agent2
```


## **Agent2 Log Output**
```
(venv) kshipra@MacBook-Pro-2 global-ai-agents-league-workshop % python3 agent2.py
INFO:     [  bob]: Starting agent with address: agent1qd06kekp5zrsdquaj69t93vkxdwscllyasdx0aunx0s9rexpxx7ez9u5cfq
INFO:     [  bob]: Agent inspector available at https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A5002&address=agent1qd06kekp5zrsdquaj69t93vkxdwscllyasdx0aunx0s9rexpxx7ez9u5cfq
INFO:     [  bob]: Starting server on http://0.0.0.0:5002 (Press CTRL+C to quit)
INFO:     [uagents.registration]: Registration on Almanac API successful
INFO:     [uagents.registration]: Almanac contract registration is up to date!
INFO:     [  bob]: Received message: hello from agent1
INFO:     [  bob]: Response sent
```

