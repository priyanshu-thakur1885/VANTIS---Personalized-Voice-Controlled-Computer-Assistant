from google.genai import types


TOOLS = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="type_text",
                description="Type text into the currently focused application.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "text": types.Schema(
                            type="STRING",
                            description="The text to type."
                        )
                    },
                    required=["text"]
                )
            ),

            types.FunctionDeclaration(
                name="press_key",
                description="Press a keyboard key.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "key": types.Schema(
                            type="STRING",
                            description="The key to press."
                        )
                    },
                    required=["key"]
                )
            ),

            types.FunctionDeclaration(
                name="scroll",
                description="Scroll the screen up or down.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "direction": types.Schema(
                            type="STRING",
                            enum=["up", "down"]
                        ),
                        "amount": types.Schema(
                            type="INTEGER",
                            description="Number of scroll units."
                        )
                    },
                    required=["direction"]
                )
            ),

            types.FunctionDeclaration(
                name="click",
                description="Click at the current mouse position."
            ),

            types.FunctionDeclaration(
                name="double_click",
                description="Double click at the current mouse position."
            ),

            types.FunctionDeclaration(
                name="right_click",
                description="Right click at the current mouse position."
            ),

            types.FunctionDeclaration(
                name="open_application",
                description="Open an application on the Windows computer.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "name": types.Schema(
                            type="STRING",
                            description="Application name."
                        )
                    },
                    required=["name"]
                )
            ),
            types.FunctionDeclaration(
                name="close_application",
                description="Close an application on the Windows computer.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "name": types.Schema(
                            type="STRING",
                            description="Application name."
                        )
                    },
                    required=["name"]
                )
            ),

            types.FunctionDeclaration(
                name="open_url",
                description="Open a URL in the default browser.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "url": types.Schema(
                            type="STRING",
                            description="URL to open."
                        )
                    },
                    required=["url"]
                )
            ),

            types.FunctionDeclaration(
                name="open_folder",
                description="Open a folder in Windows File Explorer. Accept either an absolute path or a folder name to search for on the local system.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "path": types.Schema(
                            type="STRING",
                            description="Absolute folder path or folder name to search for on the system."
                        )
                    },
                    required=["path"]
                )
            ),

            types.FunctionDeclaration(
                name="increase_volume",
                description="Increase system volume.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "amount": types.Schema(
                            type="INTEGER"
                        )
                    }
                )
            ),

            types.FunctionDeclaration(
                name="decrease_volume",
                description="Decrease system volume.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "amount": types.Schema(
                            type="INTEGER"
                        )
                    }
                )
            ),

            types.FunctionDeclaration(
                name="mute",
                description="Mute the computer."
            ),
            types.FunctionDeclaration(
                name="click_at",
                description="Click at specific screen coordinates.",
                parameters= types.Schema(
                    type="OBJECT",
                    properties={
                        "x": types.Schema(
                            type="INTEGER",
                            description="X coordinate on the screen."
                        ),
                        "y": types.Schema(
                            type="INTEGER",
                            description="Y coordinate on the screen."
                        )
                    },
                    required=["x", "y"]
                )
            ),
            types.FunctionDeclaration(
                name="click_element",
                description="Find a visible screen element from a screenshot and click its center.",
                parameters=types.Schema(
                    type="OBJECT",
                    properties={
                        "description": types.Schema(
                            type="STRING",
                            description="Description of the visible element to click."
                        )
                    },
                    required=["description"]
                )
            )
        ]
    )
]