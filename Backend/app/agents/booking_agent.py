import json, os

from langchain_openai import ChatOpenAI

from app.tools.booking_tools import (
    check_booking_tool,
    cancel_booking_tool,
    update_booking_tool,
    check_room_availability_tool,
    create_booking_tool
)

tools = [
    check_booking_tool,
    cancel_booking_tool,
    update_booking_tool,
    check_room_availability_tool,
    create_booking_tool
]

tool_map = {tool.name: tool for tool in tools}

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=api_key,
    base_url=base_url,
    temperature=0
).bind_tools(tools)


async def run_agent(user_input: str):

    response = await llm.ainvoke(user_input)
    print("###############response: ", response)

    if response.tool_calls:

        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]

        args = tool_call["args"]

        tool = tool_map[tool_name]

        result = await tool.ainvoke(args)

        print("############### tool call response ################", result)

        return result

    return response.content