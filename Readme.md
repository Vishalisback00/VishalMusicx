
<!-- ✨ Animated Header (Top) -->

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" />
</p>

<!-- 👤 Avatar + Typing Banner -->

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://files.catbox.moe/r2ga8f.jpg" width="90px" style="border-radius: 50%;" />
      </td>
      <td>
        <img src="https://readme-typing-svg.herokuapp.com?color=00BFFF&width=600&lines=Hey+There,+This+is+Vishal+%F0%9F%A5%80+%E2%9D%97%EF%B8%8F" />
      </td>
    </tr>
  </table>
</div>

<!-- 👁 Visitor Counter -->

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=ItsMeVishal0&style=flat-square" />
</p>

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=FF69B4&width=500&lines=Welcome+to+Shruti+Music+%F0%9F%8E%B6+The+Robot;Your+Ultimate+Telegram+Music+Bot" />
</h1>

<p align="center">
  <a href="https://t.me/Its_me_Vishall">
    <img src="https://files.catbox.moe/eh780q.jpg" width="600">
  </a>
</p>

<p align="center">
  <a href="https://t.me/Shrutimusic_bot"><img src="https://img.shields.io/badge/Try%20Bot-@Shrutimusic_bot-blue?style=for-the-badge&logo=telegram"/></a>
</p>


<p align="center">
  <a href="https://github.com/ItsMeVishal0/VishalMusic/stargazers"><img src="https://img.shields.io/github/stars/ItsMeVishal0/VishalMusic?style=flat-square"/></a>
  <a href="https://github.com/ItsMeVishal0/VishalMusic/network/members"><img src="https://img.shields.io/github/forks/ItsMeVishal0/VishalMusic?style=flat-square"/></a>
  <a href="https://github.com/ItsMeVishal0/VishalMusic/issues"><img src="https://img.shields.io/github/issues/ItsMeVishal0/VishalMusic?style=flat-square"/></a>
  <a href="https://github.com/ItsMeVishal0/VishalMusic/commits/main"><img src="https://img.shields.io/github/last-commit/ItsMeVishal0/VishalMusic?style=flat-square"/></a>
  <a href="https://github.com/ItsMeVishal0/VishalMusic/actions"><img src="https://img.shields.io/badge/CI-Status-grey?style=flat-square"/></a>
</p>

## 🌟 What is Shruti Music Bot?

**Shruti Music Bot** is a modern Telegram bot that streams **high-quality music** into group voice chats.
Powered by **Pyrogram + PyTgCalls**, it supports multiple platforms like **YouTube, Spotify, Apple Music, SoundCloud, Resso, and more**.
It also includes **basic group management features** for convenience.

## 🚀 Features
<table>
<tr>
<td>
  <img src="https://files.catbox.moe/la0sxq.jpg" width="300" />
</td>
<td>

| 🌟 Feature                | 🔎 Description                              |
| ------------------------- | ------------------------------------------- |
| 🎶 HQ Music Streaming     | Lag‑free HD audio in group voice chats      |
| 🌐 Multi‑Platform Sources | YouTube, Spotify, Apple Music, Resso, etc.  |
| 👮 Group Management Tools | Promote/demote, mute/kick, etc.     |
| ⚡ Fast Setup              | One‑click Heroku, VPS, or Docker deployment |
| 🔄 Auto Config            | Quick setup script with pre‑checks          |

</td>
</tr>
</table>

## 🔑 Environment Variables

Below are the required and optional environment variables for deployment.

```env
API_ID=              # Required - Get from https://my.telegram.org
API_HASH=            # Required - From https://my.telegram.org
BOT_TOKEN=           # Required - Get t.me/BotFather
OWNER_ID=            # Required - Your Telegram user ID
LOGGER_ID=           # Required - Log group/channel ID
STRING_SESSION=      # Required - Generate from @SessionBuilderbot
MONGO_DB_URI=        # Required - MongoDB connection string
COOKIE_URL=          # Required - YT Cookies url

DEEP_API=            # Optional - Get from https://deepai.org
API_KEY=             # Optional - External API key for music Download
API_URL=             # Optional - External API url for music Download
```

⚠️ Never expose raw cookies or tokens in public repos. Use safe paste services like Pastebin or Batbin.



<details>
  <summary><b>Where do I get each key?</b></summary>

  <br/>

  <table>
    <thead>
      <tr>
        <th>Key</th>
        <th>Where to Get It</th>
        <th>Steps</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>API_ID</code> &amp; <code>API_HASH</code></td>
        <td><a href="https://my.telegram.org" target="_blank">my.telegram.org</a> → <i>API Development Tools</i></td>
        <td>
          1) Log in with Telegram →
          2) Open <b>API Development Tools</b> →
          3) Create app →
          4) Copy values
        </td>
        <td>Keep these private. Needed by both userbot &amp; bot client.</td>
      </tr>
      <tr>
        <td><code>BOT_TOKEN</code></td>
        <td><a href="https://t.me/BotFather" target="_blank">@BotFather</a></td>
        <td>
          1) <b>/newbot</b> →
          2) Set name &amp; username →
          3) Copy the token
        </td>
        <td>Rotate if leaked. Store in <code>.env</code>.</td>
      </tr>
      <tr>
        <td><code>STRING_SESSION</code></td>
        <td><a href="https://t.me/SessionBuilderbot" target="_blank">@SessionBuilderbot</a></td>
        <td>
          1) Start bot →
          2) Provide <code>API_ID</code>/<code>API_HASH</code> →
          3) Complete login →
          4) Copy string
        </td>
        <td>Userbot auth for Pyrogram.</td>
      </tr>
      <tr>
        <td><code>LOGGER_ID</code></td>
        <td>Telegram <b>Channel/Group</b> you own</td>
        <td>
          1) Create private channel/group →
          2) Add your bot as admin →
          3) Get ID via <code>@Shrutimusic_bot</code> or <code>@MissRose_Bot</code>
        </td>
        <td>Use a private space so logs aren't public.</td>
      </tr>
      <tr>
        <td><code>MONGO_DB_URI</code></td>
        <td><a href="https://www.mongodb.com/atlas/database" target="_blank">MongoDB Atlas</a></td>
        <td>
          1) Create free cluster →
          2) Add database user &amp; IP allowlist →
          3) Copy connection string (<code>mongodb+srv://...</code>)
        </td>
        <td>Required for persistence (queues, configs, etc.).</td>
      </tr>
      <tr>
        <td><code>COOKIE_URL</code></td>
        <td>Any secure host (e.g., <a href="https://pastebin.com" target="_blank">Pastebin</a>, <a href="https://batbin.me" target="_blank">Batbin</a>)</td>
        <td>
          1) Upload your <code>cookies.txt</code> privately →
          2) Set paste visibility to <b>Unlisted</b> →
          3) Copy the <b>raw</b> URL
        </td>
        <td>Improves YouTube reliability. Never commit raw cookies.</td>
      </tr>
      <tr>
        <td><code>DEEP_API</code> / <code>API_KEY</code> / <code>API_URL</code></td>
        <td>Provider of your choice</td>
        <td>Sign up → generate key → paste here</td>
        <td>Optional integrations (AI/extras).</td>
      </tr>
    </tbody>
  </table>

  <br/>
</details>



☕ VPS Setup Guide

<img src="https://img.shields.io/badge/Show%20/Hide-VPS%20Steps-0ea5e9?style=for-the-badge" alt="Toggle VPS Steps"/>
<div align="left">
  <details>

```bash
🎵 Deploy Shruti Music Bot on VPS

### Step 1: Update & Install Packages
sudo apt update && sudo apt upgrade -y
sudo apt install git curl python3-pip python3-venv ffmpeg -y
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
npm install -g npm

### Step 2: Clone Repo
git clone https://github.com/ItsMeVishal0/VishalMusic.git
cd VishalMusic
tmux new -s Shruti

### Step 3: Setup & Run
python3 -m venv venv
source venv/bin/activate
pip install -U pip && pip install -r requirements.txt
bash setup   # Fill environment variables
bash start   # Start bot

### Useful Commands
tmux detach         # Use Ctrl+B, then D
tmux attach-session -t Shruti # Attach to Running Bot session
tmux kill-session -t Shruti # to kill the running bot session
rm -rf VishalMusic  # Uninstall the repo
```

  </details>
</div>



🐳 Docker Deployment

<img src="https://img.shields.io/badge/Show%20/Hide-Docker%20Steps-10b981?style=for-the-badge" alt="Toggle Docker Steps"/>

<div align="left">
  <details>

```bash
### Step 1: Clone Repo
git clone https://github.com/ItsMeVishal0/VishalMusic.git
cd VishalMusic

### Step 2: Create .env File
nano .env
# Paste your environment variables here and save (Ctrl+O, Enter, Ctrl+X)

### Step 3: Build Image
docker build -t shrutimusicbot .

### Step 4: Run Container
docker run -d --name shruti --env-file .env --restart unless-stopped shrutimusicbot

### Step 5: Manage Container
docker logs -f shruti        # View logs (Ctrl+C to exit)
docker stop shruti           # Stop container
docker start shruti          # Start again
docker rm -f shruti          # Remove container
docker rmi shrutimusicbot    # Remove image
```

  </details>
</div>



☁️ Quick Deploy

Platform Deploy Link
🔑 Generate Session <a href="https://t.me/SessionBuilderbot"><img src="https://img.shields.io/badge/Session%20-Generator-blue?style=for-the-badge&logo=telegram"/></a>
🌍 Heroku Deploy <a href="http://dashboard.heroku.com/new?template=https://github.com/ItsMeVishal0/VishalMusic"><img src="https://img.shields.io/badge/Deploy%20to-Heroku-purple?style=for-the-badge&logo=heroku"/></a>

💬 Community & Support

<p align="center">
  <a href="https://t.me/ItsMeVishalSupport">
    <img src="https://img.shields.io/badge/Support_Group-Telegram-0088cc?style=for-the-badge&logo=telegram&logoColor=white" />
  </a>
  <a href="https://t.me/ItsMeVishalBots">
    <img src="https://img.shields.io/badge/Updates_Channel-Telegram-6A5ACD?style=for-the-badge&logo=telegram&logoColor=white" />
  </a>
  <a href="https://t.me/Its_me_Vishall">
    <img src="https://img.shields.io/badge/Contact_Owner-Telegram-4CAF50?style=for-the-badge&logo=telegram&logoColor=white" />
  </a>
  <a href="https://t.me/Shrutimusic_bot">
    <img src="https://img.shields.io/badge/Use_Bot-Telegram-FF69B4?style=for-the-badge&logo=telegram&logoColor=white" />
  </a>
</p>

---

<p align="center">
  <i>✨ Made with ❤️ by <a href="https://t.me/Its_me_Vishall">Vishal</a> ✨</i>
</p>

<!-- ✨ Animated Footer (Bottom) -->

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" />
</p>