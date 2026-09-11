from core.ai_service import AIService
from core.tool_registry import TOOL_REGISTRY


class Agent:

    def __init__(self):

        self.ai = AIService()

    def run(self, user_message):

        messages = [
            user_message
        ]

        max_steps = 10

        for step in range(max_steps):

            response = self.ai.process(
                messages
            )

            candidate = response.candidates[0]

            function_call_found = False

            for part in candidate.content.parts:

                if part.function_call:

                    function_call_found = True

                    function_call = part.function_call

                    tool_name = function_call.name

                    arguments = dict(
                        function_call.args
                    )

                    print()
                    print("Tool:", tool_name)
                    print("Arguments:", arguments)

                    tool = TOOL_REGISTRY.get(
                        tool_name
                    )

                    if tool is None:

                        print(
                            f"Unknown tool: {tool_name}"
                        )

                        return response

                    result = tool(
                        **arguments
                    )

                    print(
                        "Result:",
                        result
                    )

                    messages.append({
                        "tool": tool_name,
                        "result": result
                    })

            if not function_call_found:

                for part in candidate.content.parts:

                    if part.text:

                        print(
                            "Vantis:",
                            part.text
                        )

                return response

        print(
            "Vantis: I could not complete the task."
        )

        return None 