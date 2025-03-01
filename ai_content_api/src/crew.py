import os
from crewai import Agent, Task, Crew, Process
from tools.custom_tool import serper_tool, social_media_tool
from tools.kanban_tool import create_trello_board

os.environ["SERPER_API_KEY"] = "your-serper-key"

researcher = Agent.from_config("config/agents.yaml", "researcher")
writer = Agent.from_config("config/agents.yaml", "writer")
developer = Agent.from_config("config/agents.yaml", "developer")
media_creator = Agent.from_config("config/agents.yaml", "media_creator")

tasks = [
    Task.from_config("config/tasks.yaml", "research_trends_task", tools=[serper_tool]),
    Task.from_config("config/tasks.yaml", "create_content_task"),
    Task.from_config("config/tasks.yaml", "predict_post_success_task"),
    Task.from_config("config/tasks.yaml", "schedule_and_post_task", tools=[social_media_tool]),
    Task.from_config("config/tasks.yaml", "manage_project_tasks", tools=[create_trello_board]),
]

crew = Crew(
    agents=[researcher, writer, developer, media_creator],
    tasks=tasks,
    process=Process.sequential
)

result = crew.kickoff()
print(result)
