import json

from core.ai_service import AIService
from core.tool_registry import TOOL_REGISTRY


class Agent:

    def __init__(self):

        self.ai = AIService()

    def run(self, user_message):

        response = self.ai.process(
            user_message
        )

        candidate = response.candidates[0]

        for part in candidate.content.parts:

            if part.function_call:

                function_call = part.function_call

                tool_name = function_call.name

                arguments = dict(
                    function_call.args
                )

                tool = TOOL_REGISTRY.get(
                    tool_name
                )

                if tool is None:

                    print(
                        f"Unknown tool: {tool_name}"
                    )

                    continue

                result = tool(
                    **arguments
                )

                print(
                    "Tool:",
                    tool_name
                )

                print(
                    "Arguments:",
                    arguments
                )

                print(
                    "Result:",
                    result
                )

            elif part.text:

                print(
                    "Vantis:",
                    part.text
                )

        return response