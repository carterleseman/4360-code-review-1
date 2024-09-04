from message import Message

class UserInterface:
    def __init__(self):
        self.commands = {}
        self.message = Message()

    def show_commands(self):
        if not self.commands:
            self.message.print("No commands registered")
            return
        for key,val in self.commands.items():
            description = val.get("description", "No description available")
            message = f"{key} - {description}"
            self.message.print(message)    

    def register_command(self, command, callback, description=""):
        self.commands[command] = {
            "callback": callback,   
            "description": description
        }

    def deregister_command(self, command):
        if command in self.commands:
            self.commands.pop(command)
        else:
            self.message.print(f"Command '{command}' not found")

    def execute_command(self, command, args):
        func_info = self.commands.get(command)
        if func_info:
            try:
                func = func_info["callback"]
                return func(args)
            except Exception as e:
                self.message.print(f"An error occured while executing the command: {e}")
        else:
            self.message.print(f"Command '{command}' not found")