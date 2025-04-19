# 🎸 Guitar Tab Maker

**Guitar Tab Maker** is a modern, interactive tool for creating guitar tablature using a virtual fretboard interface. Click on frets to add notes, insert pauses, undo changes, and (soon) play back your tabs with real audio samples. Inspired by tools like [tab-maker.com](https://tab-maker.com), this app aims to be the most intuitive and feature-rich way to write and hear your guitar ideas.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%A8-lightgrey)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Features

- 🎛 **Clickable Fretboard UI:**  
  Write tabs by simply clicking on frets in a grid-based fretboard layout (0–21 frets across 6 strings).

- 🎼 **Auto-Generating Tab Output:**  
  Tabs are formatted and aligned as you click. Notes appear in the order they are played.

- ↩️ **Undo Functionality:**  
  Easily undo the most recent note or pause with a single click.

- ⏸ **Insert Pauses:**  
  Add spacing (pauses) in the tab to reflect timing and rhythm.

- 📏 **Standardized Output Formatting:**  
  Clean, consistent tab formatting for easy reading and copying.

---

## 🔜 Upcoming Features

### 🎧 Audio Playback
- Play back individual notes when selected on the fretboard.
- Full tab playback so you can hear your composition in real time.
- Ability to adjust playback **tempo** and **loop** specific sections.
> 🎵 Audio playback will require high-quality guitar note samples.  
> I'm currently evaluating the best sample sets to include.


### 🧠 Tab Editing
- Click any cell in the tab to edit the note directly from the fretboard.
- Visual indicator for selected cell and auto-return to append mode afterward.
- Support for **chords** by allowing multiple notes in the same column.

### 📝 Guitar Techniques
Add special notation for techniques like:
- **Muted hit** (`x`)
- **Hammer-on** (`h`)
- **Pull-off** (`p`)
- **Bend** (`b`)
- **Vibrato** (`~`)
- **Slide up** (`/`)
- **Slide down** (`\`)
- **Tap** (`t`)
- All with in-app documentation and example formatting.

### 💾 Tab Persistence & Organization
- Save tabs so they persist between sessions.
- Allow users to:
  - Name their tabs
  - Reorder tabs
  - Delete with confirmation prompts
  - Group tabs into **folders/directories** (e.g., "Choruses," "Verses," or "Songs")

### 🧪 Stretch Goals
- **Export to .txt or .pdf**
- **YouTube sync** (playback to backing tracks)
- **Mobile support**
- **Multi-instrument support** (bass, ukulele, etc.)

---

## 🧱 Tech Stack

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – UI and app framework

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/guitar-tab-maker.git
   cd guitar-tab-maker
   ```

2. Install the required python packages:
   ```bash
   pip install -r requirements.txt
   ```
   > `requirements.txt` includes all the necessary Python libraries to run the app (e.g., Streamlit).


3. Run the app:
   ```bash
   streamlit run tab_writer_app.py
   ```

## 📄 License

MIT License. Use freely and contribute to improve!

## 💡 Credits

Built and maintained by Darius Dahl

Inspired by: [tab-maker.com](https://tab-maker.com/en)
