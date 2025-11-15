# 🎥🎙️ Vision Voice Agent

> **A real-time AI-powered voice and video agent built with Vision Agents**

Transform your applications with intelligent, real-time voice and video interactions. This project leverages the powerful [Vision Agents](https://github.com/getstream/vision-agents/) framework to create an AI assistant that can see, hear, and respond in real-time using Stream's edge network and Google's Gemini AI.

## 🎬 Demo Video


https://github.com/user-attachments/assets/c9feaed1-e047-4720-b082-fd01183b901e



---

## ✨ Features

- 🎯 **Real-time Voice Interaction** - Natural conversations with AI using Gemini's realtime API
- 📹 **Video Support** - Built on Stream Video for low-latency video streaming
- 🧠 **Intelligent Responses** - Powered by Google Gemini for context-aware conversations
- 🚀 **Edge-Optimized** - Leverages Stream's global edge network for minimal latency
- 🔌 **Extensible Architecture** - Easy to customize and extend with additional AI providers

---

## 🛠️ Tech Stack

- **Framework**: [Vision Agents](https://visionagents.ai/) by Stream
- **Edge/Transport**: [Stream Video](https://getstream.io/video/)
- **LLM/Realtime**: Google Gemini
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (ultra-fast Python package installer)
- **Python**: 3.12+

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.12 or higher** installed
- **uv** package manager installed ([Installation Guide](https://github.com/astral-sh/uv#installation))
- **Stream Account** with API credentials
- **Google Gemini API Key** with access to the Realtime API

---

# Installation

To get started with the [Vision Agents](https://github.com/getstream/vision-agents/) framework, developers can install the package from [pypi](https://pypi.org/). We recommend using `uv` as the package manager which is also open-source and free to use. To get started run:

```bash  theme={null}
uv add vision-agents 
```

By default, the SDK does not install with any packages. To install packages, you can run the following:

```bash  theme={null}
uv add "vision-agents[getstream, gemini, openai, elevenlabs, deepgram]"
```

Before running, you will also need a free API key from [Stream](https://getstream.io/try-for-free). Developers building with Stream each receive 333,000 participant minutes free each month and indie developers and small businesses can apply to our [Maker Program](https://getstream.io/chat/pricing/#free-for-maker) which includes an additional \$500 worth of credits each month. Each provider also provides free development keys on their respective websites.


### Step 2: Clone and Setup Project

```bash
# Clone the repository
git clone <your-repo-url>
cd Vision-Voice-Agent

# Create virtual environment and install dependencies with uv
uv sync
```

This will:
- Create a virtual environment (`.venv`)
- Install all project dependencies
- Set up the project for development

### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

---

## 🔑 API Keys Setup

### Getting Stream API Keys

1. **Sign up for Stream**
   - Visit [https://getstream.io/](https://getstream.io/)
   - Click "Sign Up" or "Get Started"
   - Create a new account or log in

2. **Create a New Application**
   - Once logged in, navigate to your [Dashboard](https://dashboard.getstream.io/)
   - Click "Create App" or select an existing app
   - Choose "Video" as the app type

3. **Get Your Credentials**
   - In your app dashboard, go to the **"Overview"** or **"Keys"** section
   - You'll need:
     - **API Key** (starts with something like `mmhfdzb5evj2`)
     - **API Secret** (keep this secure!)
   - Copy both values for the next step


### Getting Google Gemini API Key

1. **Access Google AI Studio**
   - Visit [https://aistudio.google.com/](https://aistudio.google.com/)
   - Sign in with your Google account

2. **Get API Key**
   - Click on "Get API Key" in the left sidebar
   - If prompted, create a new Google Cloud Project or select an existing one
   - Click "Create API Key" in new project or "Create API Key in existing project"
   - Copy the generated API key (starts with `AIza...`)

3. **Enable Gemini Realtime API** (if required)
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Navigate to "APIs & Services" > "Library"
   - Search for "Generative Language API" or "Gemini API"
   - Ensure the API is enabled for your project

4. **Set Usage Limits** (Recommended)
   - In Google AI Studio, go to "Settings" > "Usage and limits"
   - Set appropriate rate limits to avoid unexpected charges

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Create .env file
touch .env  # On Windows: type nul > .env
```

Add your API keys to the `.env` file:

```env
# Stream API Credentials
STREAM_API_KEY=your_stream_api_key_here
STREAM_API_SECRET=your_stream_api_secret_here

# Google Gemini API Key
GOOGLE_API_KEY=your_gemini_api_key_here
```

**⚠️ Important Security Notes:**
- Never commit your `.env` file to version control (it's already in `.gitignore`)
- Keep your API keys secure and don't share them publicly
- Rotate keys if they're accidentally exposed

---

## 🎮 Usage

### Running the Agent

Once your environment is set up and API keys are configured:

```bash
# Make sure virtual environment is activated
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

# Run the agent
python main.py
```

### Command Line Options

The agent supports various CLI options. Run with `--help` to see available options:

```bash
python main.py --help
```

### Example: Joining a Call

The agent will automatically:
1. Create a user session
2. Join the specified call
3. Greet users with "Hello! How can I help?"
4. Process voice and video interactions in real-time

---

## 📁 Project Structure

```
Vision-Voice-Agent/
├── main.py              # Main agent implementation
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock             # Locked dependency versions
├── .env                # Environment variables (create this)
├── .venv/              # Virtual environment (created by uv)
└── README.md           # This file
```

---

## 🔧 Customization

### Modify Agent Instructions

Edit the `instructions` parameter in `main.py`:

```python
instructions="You're a friendly voice assistant.",  # Change this!
```

### Add Additional AI Providers

The project includes support for multiple providers. Check `pyproject.toml` for available extras:

- `deepgram` - Speech-to-Text
- `elevenlabs` - Text-to-Speech
- `gemini` - LLM and Realtime API
- `getstream` - Video transport
- `openai` - Alternative LLM provider

### Extend Functionality

You can extend the agent by:
- Adding custom processors using `BaseProcessor`
- Implementing video analysis with `VideoProcessorMixin`
- Integrating additional AI services
- Customizing the call flow in `join_call()`

---

## 📚 Resources

- [Vision Agents Documentation](https://visionagents.ai/)
- [Vision Agents GitHub](https://github.com/getstream/vision-agents/)
- [Stream Video Docs](https://getstream.io/video/docs/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [uv Documentation](https://github.com/astral-sh/uv)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests with improvements
- Share your use cases and examples

---

## 🙏 Acknowledgments

- Built with [Vision Agents](https://github.com/getstream/vision-agents/) by [Stream](https://getstream.io/)
- Powered by [Google Gemini](https://ai.google.dev/)
- Package management by [uv](https://github.com/astral-sh/uv)

---

**Ready to build something amazing? Start your agent and let the conversations begin! 🚀**

