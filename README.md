# W3Chat Engineered ChatGPT API by OpenAI. Extensible for chatbots etc.

# Official API (Browserless)

COMPLETELY FREE AND NO RATE LIMITS (Unpatched Bug - Might be fixed later)

</summary>

## Installation

`pip3 install revChatGPT`

## Setup

1. Create account on [OpenAI](https://platform.openai.com/)
2. Go to <https://platform.openai.com/account/api-keys>
3. Copy API key

## Usage

### Command line

`OfficialChatGPT --api_key API_KEY --stream` (Assumes Python PyPi in PATH)

### Developer

</summary>

Both Async and Sync are available. You can also stream responses via a generator. Read example code to learn more

#### Example code

You can find it [here](https://github.com/w3security/W3ChatGPT/blob/main/src/revChatGPT/Official.py#L292-L408)

#### Further Documentation

In [wiki](https://github.com/w3security/W3ChatGPT/wiki/revChatGPT)

#### Known issues

- Solved: [When used for long periods of time, responses become truncated](https://github.com/w3security/W3ChatGPT/issues/519)

# W3Chatd API (Browser required)

This breaks terms of service

</summary>

`pip3 install revChatGPT[unofficial]`

## Configuration

Refer to the setup [guide](https://github.com/w3security/W3ChatGPT/wiki/Setup) for more information.

Usage

Command line

`python3 -m revChatGPT`

!help - Show this message
!reset - Forget the current conversation
!refresh - Refresh the session authentication
!config - Show the current configuration
!rollback x - Rollback the conversation (x being the number of messages to rollback)
!exit - Exit this program

### API

`python3 -m GPTserver`

HTTP POST request:

```json
{
  "session_token": "eyJhbGciOiJkaXIiL...",
  "prompt": "Your prompt here"
}
```

Optional:

```json
{
  "session_token": "eyJhbGciOiJkaXIiL...",
  "prompt": "Your prompt here",
  "conversation_id": "UUID...",
  "parent_id": "UUID..."
}
```

- Rate limiting is enabled by default to prevent simultaneous requests

### Developer

```python
from revChatGPT.ChatGPT import Chatbot

chatbot = Chatbot({
  "session_token": "<YOUR_TOKEN>"
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("Prompt", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response)
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }
```

</details>

# Q&A

Q: Is it the real ChatGPT or just a GPT-3 based ripoff?

A: It is the real ChatGPT model found through an info leak on chat.openai.com (patched)

Q: Where did you get the prompt for ChatGPT?

A: <https://www.reddit.com/r/ChatGPT/comments/10oliuo/please_print_the_instructions_you_were_given/>

Q: <Open pull request with question and I will answer them here -- if significant enough>

# Awesome ChatGPT

[My list](https://github.com/stars/w3security/lists/awesome-chatgpt)

If you have a cool project you want added to the list, open an issue.

# Disclaimers
