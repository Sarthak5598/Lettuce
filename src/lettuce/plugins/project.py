import json

from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import command

project_json_path = "Lettuce/projects.json"
with open(project_json_path) as f:
    project_data = json.load(f)


class ProjectPlugin(MachineBasePlugin):
    @command("/project")
    async def project(self, command):
        text = command.text.strip()
        user_name = command.user_name
        project_name = text.strip().lower()

        project = project_data.get(project_name)

        if project:
            project_list = "\n".join(project)
            message = f"Hello {user_name}, here the information about '{project_name}':\n{project_list}"
        else:
            message = f"Hello {user_name}, the project '{project_name}' is not recognized. Please try different query."

        await command.say(message)
