import requests

class Discofy:
    def __init__(self, discord_token: str):
        self.discord_token = discord_token
        self.headers = {
            "Authorization": f"{self.discord_token}",
            "Content-Type": "application/json"
        }

    def get_spotify_token(self):
        url = "https://discord.com/api/v9/users/@me/connections"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            connections = response.json()
            for conn in connections:
                if conn["type"] == "spotify":
                    return conn["access_token"]
        return None

    def send_spotify_request(self, method, endpoint, data=None, params=None):
        spotify_token = self.get_spotify_token()
        if not spotify_token:
            print("Exception: Failed to retrieve Spotify token")
            return None

        spotify_headers = {
            "Authorization": f"Bearer {spotify_token}",
            "Content-Type": "application/json"
        }

        url = f"https://api.spotify.com/v1/me/player/{endpoint}"
        response = requests.request(method, url, headers=spotify_headers, json=data, params=params)

        if response.status_code not in [200, 204]: 
            print(f"Exception: {response.status_code} - {response.text}")
            return None

        try:
            return response.json() if response.text else None
        except requests.exceptions.JSONDecodeError:
            return None  


    def pause_track(self):
        self.send_spotify_request("PUT", "pause")
        
    def resume_track(self):
        self.send_spotify_request("PUT", "play")

    def next_track(self):
        self.send_spotify_request("POST", "next")

    def previous_track(self):
        self.send_spotify_request("POST", "previous")

    def play_track(self, track_uri: str):
        data = {"uris": [track_uri]}
        self.send_spotify_request("PUT", "play", data=data)

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            params = {"volume_percent": volume}
            self.send_spotify_request("PUT", "volume", params=params)
        else:
            print("Exception: Volume must be between 0 and 100")

    def get_current_track(self):
        track_info = self.send_spotify_request("GET", "currently-playing")
        if track_info and "item" in track_info:
            track = track_info["item"]
            return track
        else:
            print("Exception: No track is currently playing")
            return None

    def shuffle(self, state: bool):
        params = {"state": str(state).lower()}
        self.send_spotify_request("PUT", "shuffle", params=params)

    def repeat(self, state: str):
        if state not in ["track", "context", "off"]:
            print("Exception: Repeat state must be 'track', 'context', or 'off'")
            return
        params = {"state": state}
        self.send_spotify_request("PUT", "repeat", params=params)

    def is_playing(self):
        track_info = self.send_spotify_request("GET", "currently-playing")
        return track_info.get("is_playing", False) if track_info else False

    def get_playback_state(self):
        playback_state = self.send_spotify_request("GET", "")
        return playback_state

    def transfer_playback(self, device_id: str, play: bool):
        data = {"device_ids": [device_id], "play": play}
        self.send_spotify_request("PUT", "transfer", data=data)

    def get_available_devices(self):
        devices = self.send_spotify_request("GET", "devices")
        return devices.get("devices", []) if devices else []

    def seek_to_position(self, position_ms: int):
        params = {"position_ms": position_ms}
        self.send_spotify_request("PUT", "seek", params=params)

    def add_to_playback_queue(self, track_uri: str):
        data = {"uris": [track_uri]}
        self.send_spotify_request("POST", "queue", data=data)
