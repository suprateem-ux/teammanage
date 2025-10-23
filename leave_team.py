import os
import requests

def leave_team(team_id: str, token: str) -> None:
    """Leave a Lichess team using the official API."""
    url = f"https://lichess.org/team/{team_id}/quit"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print(f"Leaving team: {team_id}")
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ Successfully left team '{team_id}'.")
    elif response.status_code == 404:
        print(f"⚠️ Not a member of team '{team_id}' or team not found.")
    elif response.status_code == 401:
        print("❌ Invalid or unauthorized API token.")
    else:
        print(f"⚠️ Unexpected response: {response.status_code} - {response.text}")

def main():
    token = os.getenv("LICHESS_KEY")
    if not token:
        raise EnvironmentError("LICHESS_KEY not found in environment variables.")

    team_id = "indicheck-_hu"
    leave_team(team_id, token)

if __name__ == "__main__":
    main()
