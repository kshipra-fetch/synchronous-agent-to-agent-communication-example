from uagents import Agent, Bureau, Context, Model


class Message(Model):
    message: str

class Response(Model):
    response: str

agent = Agent(name="bob", port=5002, endpoint = 'http://localhost:5002/submit')

@agent.on_message(model=Message)
async def handle_message_and_reply(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message: {msg.message}")
    await ctx.send(sender,message= Response(response="hello from agent2"))
    ctx.logger.info("Response sent")


if __name__ == "__main__":
    agent.run()
