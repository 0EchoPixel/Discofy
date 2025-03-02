# Discofy  

Wanna control Spotify playback API but you don't want to pay for a Spotify Premium? No problem!  
`Discofy` is a Python library that allows you to control Spotify playback **for free, without a premium subscription** — just by using your Discord account.  

## Requirements  

- Your Spotify account have to be connected to your Discord account (in Discord settings under "Connections").  
- You must enable "Display Spotify as your status" in Discord.  
- You need your Discord account token (check online resources on how to get it).  
- Discofy will stop working shortly after you close the Discord app.  

## Features  

- Spotify Integration: Control your Spotify playback through your Discord connection.  
- Playback Control: Pause, resume, skip tracks, or go back to the previous one.  
- Track Management: Play a specific song or add it to the queue.  
- Volume Adjustment: Set the volume between 0 and 100.  
- Shuffle & Repeat Modes: Enable or disable shuffle and repeat functions.  
- Playback Monitoring: Get information about the currently playing track.  
- Device Management: Transfer playback to another linked device.  
- Seek to Position: Jump to a specific time in a track.  
- Add to Queue: Queue tracks for playback.  

## Installation  

To install Discofy, simply use pip:
`pip install discofy`

## Available Commands  

- pause_track() - Pauses the currently playing track.  
- resume_track() - Resumes playback if paused.  
- next_track() - Skips to the next track.  
- previous_track() - Goes back to the previous track.  
- play_track(track_uri: str) - Plays a specific track. Example:  
  `client.play_track("spotify:track:PASTE_TRACK_ID")`
- set_volume(volume: int) - Changes the playback volume (0-100%). Example:  
  `client.set_volume(10)`  # Sets volume to 10%  
- get_current_track() - Returns information about the currently playing track.  
- shuffle(state: bool) - Toggles shuffle mode.  
- repeat(state: str) - Changes the repeat mode ('track', 'context', or 'off').  
- is_playing() - Returns True if music is playing, otherwise False.  
- get_playback_state() - Retrieves information about the user's current playback state (track, progress, active device, etc.).  
- transfer_playback(device_id: str, play: bool) - Moves playback to another device.  
- get_available_devices() - Lists available Spotify Connect devices (some may not be supported).  
- seek_to_position(position_ms: int) - Moves playback to a specific position in milliseconds.  
- add_to_playback_queue(track_uri: str) - Adds a track to the queue. Example:  
  `client.add_to_playback_queue("spotify:track:PASTE_TRACK_ID")`

## Example Usage  

Basic Python script to control Spotify playback with Discofy:  
```
from discofy import Discofy  

# Set your Discord token  
discord_token = "PASTE_YOUR_TOKEN_HERE"  

client = Discofy(discord_token)  

# Set volume to 10%  
client.set_volume(10)  

# Pause playback  
client.pause_track()  

# Print info about the currently playing track  
print(client.get_current_track())  

# Shows if something is being played
if judeify.is_playing():
    print("Something is being played")
else:
    print("Nothing is being played!")

```
## License  

Discofy is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.  
For more details, visit: https://creativecommons.org/licenses/by-sa/4.0/  
