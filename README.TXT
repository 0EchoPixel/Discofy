<div class="vertical-tabs__panel">
        <!-- mobile menu -->
        

        <div id="description" data-project-tabs-target="content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="description-tab mobile-description-tab" tabindex="-1" style="display: block;">
          
          <div class="project-description">
            <h1>Discofy</h1>
<p>Wanna control Spotify playback API but you don't want to pay for a Spotify Premium? No problem!<br>
<code>Discofy</code> is a Python library that allows you to control Spotify playback <strong>for free, without a premium subscription</strong> — just by using your Discord account.</p>
<h2>Requirements</h2>
<ul>
<li>Your Spotify account have to be connected to your Discord account (in Discord settings under "Connections").</li>
<li>You must enable "Display Spotify as your status" in Discord.</li>
<li>You need your Discord account token (check online resources on how to get it).</li>
<li>Discofy will stop working shortly after you close the Discord app.</li>
</ul>
<h2>Features</h2>
<ul>
<li>Spotify Integration: Control your Spotify playback through your Discord connection.</li>
<li>Playback Control: Pause, resume, skip tracks, or go back to the previous one.</li>
<li>Track Management: Play a specific song or add it to the queue.</li>
<li>Volume Adjustment: Set the volume between 0 and 100.</li>
<li>Shuffle &amp; Repeat Modes: Enable or disable shuffle and repeat functions.</li>
<li>Playback Monitoring: Get information about the currently playing track.</li>
<li>Device Management: Transfer playback to another linked device.</li>
<li>Seek to Position: Jump to a specific time in a track.</li>
<li>Add to Queue: Queue tracks for playback.</li>
</ul>
<h2>Installation</h2>
<p>To install Discofy, simply use pip:
<code>pip install discofy</code></p>
<h2>Available Commands</h2>
<ul>
<li>pause_track() - Pauses the currently playing track.</li>
<li>resume_track() - Resumes playback if paused.</li>
<li>next_track() - Skips to the next track.</li>
<li>previous_track() - Goes back to the previous track.</li>
<li>play_track(track_uri: str) - Plays a specific track. Example:<br>
<code>client.play_track("spotify:track:PASTE_TRACK_ID")</code></li>
<li>set_volume(volume: int) - Changes the playback volume (0-100%). Example:<br>
<code>client.set_volume(10)</code>  # Sets volume to 10%</li>
<li>get_current_track() - Returns information about the currently playing track.</li>
<li>shuffle(state: bool) - Toggles shuffle mode.</li>
<li>repeat(state: str) - Changes the repeat mode ('track', 'context', or 'off').</li>
<li>is_playing() - Returns True if music is playing, otherwise False.</li>
<li>get_playback_state() - Retrieves information about the user's current playback state (track, progress, active device, etc.).</li>
<li>transfer_playback(device_id: str, play: bool) - Moves playback to another device.</li>
<li>get_available_devices() - Lists available Spotify Connect devices (some may not be supported).</li>
<li>seek_to_position(position_ms: int) - Moves playback to a specific position in milliseconds.</li>
<li>add_to_playback_queue(track_uri: str) - Adds a track to the queue. Example:<br>
<code>client.add_to_playback_queue("spotify:track:PASTE_TRACK_ID")</code></li>
</ul>
<h2>Example Usage</h2>
<p>Basic Python script to control Spotify playback with Discofy:</p>
<pre><code>from discofy import Discofy  

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

</code></pre>
<h2>License</h2>
<p>Discofy is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.<br>
For more details, visit: <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="nofollow">https://creativecommons.org/licenses/by-sa/4.0/</a></p>
<h1>Change Log</h1>
<h2>1.2 (02/03/2025)</h2>
<ul>
<li>First release</li>
</ul>

          </div>
        </div>

        

        

          




      </div>
