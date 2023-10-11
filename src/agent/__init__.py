from uagents import Agent,Context


# Initialize your CurrencyWhisper agent
CurrencyWhisper = Agent(
    name="CurrencyWhisper",
    port=8000,
    endpoint=["http://127.0.0.1:8000"],
    seed="CurrencyWhisper recovery phrase"
)
