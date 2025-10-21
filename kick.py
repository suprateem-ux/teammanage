import os
import requests
import sys

def kick_user(team_id: str, user_id: str, token: str):
    url = f"https://lichess.org/api/team/{team_id}/kick/{user_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"✅ Kicked {user_id}")
    else:
        print(f"❌ Failed to kick {user_id} (status {response.status_code}) -> {response.text}")

def main():
    token = os.getenv("LICHESS_KEY")
    team_id = "bharat-royals"

    if not token:
        print("❌ Missing LICHESS_KEY environment variable.")
        sys.exit(1)

    # Read usernames from kick.txt
    try:
        with open("kick.txt", "r", encoding="utf-8") as f:
            users = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ kick.txt not found in repository root.")
        sys.exit(1)

    if not users:
        print("⚠️ kick.txt is empty — no users to kick.")
        sys.exit(0)

    print(f"🚀 Starting to kick {len(users)} users from team '{team_id}'...")
    for user in users:
        kick_user(team_id, user, token)

    print("✅ All users processed.")

if __name__ == "__main__":
    main()
