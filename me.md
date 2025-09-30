# Resource

[https://youtu.be/YIT-pWEbgCc?si=ErjmqICShaTtY6QV](https://youtu.be/YIT-pWEbgCc?si=ErjmqICShaTtY6QV)

# Generate prompt

use ChatGPT:

    Help me create a prompt for a web app for a to-do-list

# Install Specify

Install once and use everywhere:

    uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

Then use the tool directly:

    specify init <PROJECT_NAME>

    specify check

# Setup: API Key

Before using the slash commands, you need to configure an API key for your chosen AI agent. The tool expects the key to be in an environment variable.

For example, if you are using Google's Gemini:

```powershell
# In PowerShell, this sets the key for the current session
$env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

```bash
# In Bash/Zsh, this sets the key for the current session
export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

Replace `GOOGLE_API_KEY` with the correct variable for your agent (e.g., `ANTHROPIC_API_KEY` for Claude) and `"YOUR_API_KEY_HERE"` with your actual key. To make it permanent, add it to your shell profile file (e.g., `~/.bash_profile`, `~/.zshrc`, or PowerShell's `$PROFILE`).

# Next Steps

1.  `cd speckit_hr`
2.  Start using slash commands with your AI agent:
    - `/constitution` - Establish project principles
    - `/specify` - Create specifications
    - `/plan` - Create implementation plans
    - `/tasks` - Generate actionable tasks
    - `/implement` - Execute implementation
