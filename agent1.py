from uagents import Agent, Bureau, Context, Model


class Message(Model):
    message: str

class Response(Model):
    number: int

agent = Agent(name="alice", port=5001, endpoint = 'http://localhost:5001/submit')

agent2_address = ""       #run agent2.py, copy the agent's address and paste here

@agent.on_interval(period=30.0)
async def send_message(ctx: Context):
    msg = Message(message="hello from alice!")
    reply, status = await ctx.send_and_receive(agent2_address, msg, response_type=Message)
    if isinstance(reply, Message):
        ctx.logger.info(f"Received awaited response from bob: {reply.message}")
    else:
        ctx.logger.info(f"Failed to receive response from bob: {status}")



if __name__ == "__main__":
    agent.run()
