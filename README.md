# DiscoHook

A powerful and flexible Python library for sending Discord webhooks with rich content support.

## Installation

You can install DiscoHook directly from GitHub:

```bash
pip install git+https://github.com/MildThrone/discohook.git
```

## Basic Usage

```python
from discohook import Discohook

# Initialize the webhook
webhook = Discohook(url="YOUR_WEBHOOK_URL")

# Send a simple message
webhook.set_content("Hello from DiscoHook!")
response = webhook.execute()

# Edit a message
webhook.set_content("Updated message content")
webhook.edit(response)

# Delete a message
webhook.delete(response)
```

## Features

### Rich Embeds

```python
from discohook import Discohook, DiscohookEmbed

# Create webhook instance
webhook = Discohook(url="YOUR_WEBHOOK_URL")

# Create embed
embed = DiscohookEmbed(
    title="Embed Title",
    description="This is an embed description",
    color=0x00ff00  # Green color
)

# Set author info
embed.set_author(
    name="Author Name",
    url="https://example.com",
    icon_url="https://example.com/avatar.png"
)

# Set footer
embed.set_footer(text="Footer text", icon_url="https://example.com/footer.png")

# Add fields
embed.add_embed_field(name="Field 1", value="Value 1", inline=True)
embed.add_embed_field(name="Field 2", value="Value 2", inline=True)

# Add timestamp
embed.set_timestamp()

# Add the embed to the webhook
webhook.add_embed(embed)

# Execute the webhook
webhook.execute()
```

### File Attachments

```python
# Create webhook with file attachment
webhook = Discohook(url="YOUR_WEBHOOK_URL")
webhook.set_content("Here's a file attachment")

# Add a file
with open("example.txt", "rb") as f:
    webhook.add_file(file=f.read(), filename="example.txt")

# Execute the webhook
webhook.execute(remove_files=True)
```

### Advanced Options

```python
# Create webhook with advanced options
webhook = Discohook(
    url="YOUR_WEBHOOK_URL",
    content="Advanced webhook example",
    username="Custom Username",
    avatar_url="https://example.com/custom_avatar.png",
    tts=False,
    allowed_mentions={"parse": ["users"]},
    rate_limit_retry=True
)

# Execute the webhook
webhook.execute()
```

## API Reference

### Discohook Class

The main class for creating and sending Discord webhooks.

#### Parameters:
- `url`: Webhook URL (string or list of URLs)
- `content`: Message content (optional)
- `username`: Override the default username (optional)
- `avatar_url`: Override the default avatar (optional)
- `tts`: Enable text-to-speech (optional, default: False)
- `files`: Dictionary of files to attach (optional)
- `embeds`: List of embeds to include (optional)
- `allowed_mentions`: Control which mentions are parsed (optional)
- `proxies`: Dictionary of proxies to use (optional)
- `timeout`: Request timeout in seconds (optional)
- `rate_limit_retry`: Whether to retry on rate limits (optional)

### DiscohookEmbed Class

Class for creating rich embeds for Discord webhooks.

#### Parameters:
- `title`: Title of the embed (optional)
- `description`: Description of the embed (optional)
- `url`: URL of the embed (optional)
- `timestamp`: Timestamp of the embed content (optional)
- `color`: Color code of the embed as int (optional)
- `hex_color`: Color code of the embed as hex string (optional)
- `footer`: Footer information (optional)
- `image`: Image information (optional)
- `thumbnail`: Thumbnail information (optional)
- `video`: Video information (optional)
- `provider`: Provider information (optional)
- `author`: Author information (optional)
- `fields`: Fields information (optional)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

- Aaron (mildthrone@proton.me)
- JanakXD (janak@panarastudios.in)