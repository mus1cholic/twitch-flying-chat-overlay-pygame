# Twitch Flying Chat Overlay Pygame v0.5.0

Insert gif here

A streaming overlay to display chat that scrolls horizontally, similar to niconico and bilibili, built with Pygame

Instructions:

- `cd` into this directory
- `python main.py`

In OBS:
- Add a **Window Capture** source to your scene
- Name it whatever
- For **Window**, select `pygame window`
- For **Capture Method**, select `Windows 10`
- Right click on your **Window Capture** under `Sources` and select `Filters`
- Add a **Color Key** filter
- Select the filter and select `Custom` for the **Key Color Type**
- Press **Select Color** and type `#000000` under **HTML**
- Don't forget to drag your window (under `Sources`) all the way to the top of the list