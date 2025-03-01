@tool
def create_trello_board(board_name: str) -> str:
    """Create a new Kanban board in Trello."""
    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")
    url = f"https://api.trello.com/1/boards/?name={board_name}&key={api_key}&token={token}"
    response = requests.post(url)
    return f"Board '{board_name}' created: {response.json().get('shortUrl', 'N/A')}"
