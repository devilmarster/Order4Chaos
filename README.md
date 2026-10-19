# Order4Chaos

A Python tool for reorganising Spotify collaborative playlists based on who added each track.

Order4Chaos takes a playlist exported from Exportify, rearranges the songs according to user-defined contributor patterns, and generates a new CSV file that can be imported back into Spotify using Soundiiz.

This allows collaborative playlists to feel fairer, giving each contributor regular turns instead of allowing one person's songs to dominate large sections of the playlist.

---

## The Problem

Collaborative playlists can become unbalanced when contributors add different numbers of songs at different times.

For example, a playlist may end up looking like:

```text
P1
P1
P1
P1
P1
P2
P2
P3
P4
```

This can make listening less enjoyable, as songs from some contributors are clustered together rather than being spread throughout the playlist.

---

## The Solution

Order4Chaos redistributes tracks based on the contributor who added them.

Example:

Original playlist:

```text
P1
P1
P1
P2
P2
P3
P4
P4
```

Reordered playlist:

```text
P1
P2
P3
P4
P1
P2
P4
P1
```

This creates a more balanced listening experience and ensures contributors are represented more evenly throughout the playlist.

---

## Features

- Import Spotify playlist exports from Exportify
- Automatic contributor detection
- Create custom contributor sequences
- Randomise contributor placement
- Mix fixed and random contributor positions
- Preserve original song order within contributor playlists
- Randomise song order within contributor playlists
- Configure ordering behaviour per contributor
- Built-in file picker for selecting playlist exports
- Export reordered playlists as CSV
- Compatible with Soundiiz playlist importing

---

## Workflow

### 1. Export a Playlist

Export your Spotify playlist using Exportify:

https://exportify.app/

Download the generated CSV file.

### 2. Load Into Order4Chaos

Launch the application and select the exported playlist CSV using the file picker.

Order4Chaos identifies which contributor added each track and groups songs accordingly.

### 3. Choose a Playlist Pattern

Specify how contributors should be arranged throughout the playlist.

Example:

```text
P1 → P2 → P3 → P4
```

Generated sequence:

```text
P1
P2
P3
P4
P1
P2
P3
P4
...
```

Order4Chaos supports several approaches:

- Fully custom contributor ordering
- Completely random contributor ordering
- Hybrid ordering, where some contributors are assigned fixed positions while the remaining positions are filled randomly

For example:

```text
P1 → Random → P3 → Random
```

When the playlist order is generated, the random positions are filled once using the remaining contributors.

One possible result could be:

```text
P1 → P4 → P3 → P2
```

This generated contributor sequence then becomes the fixed rotation used when building the playlist:

```text
P1
P4
P3
P2
P1
P4
P3
P2
...
```

The random positions are not recalculated for each cycle. They are only used when creating the contributor sequence, ensuring a consistent listening experience throughout the playlist.

### 4. Choose Song Ordering

Tracks within each contributor's collection can be configured independently.

Options include:

- Keeping a contributor's songs in the order they were originally added
- Randomising a contributor's songs
- Mixing ordered and randomised contributors within the same playlist

For example:

```text
Alice    → Original order
Bob      → Randomised
Charlie  → Original order
Dan      → Randomised
```

This allows some contributors' playlists to preserve their intended flow while introducing variety to others.

### 5. Export

Order4Chaos generates a new CSV playlist file containing the reordered tracks.

### 6. Import Back Into Spotify

Upload the generated CSV file using Soundiiz:

https://soundiiz.com/

The reordered playlist can then be recreated in Spotify.

---

## Example

Given contributors:

```text
Alice
Bob
Charlie
Dan
```

And a generated contributor sequence:

```text
Alice → Dan → Charlie → Bob
```

The playlist will be constructed by taking one available track from each contributor in turn until all tracks have been used.

Result:

```text
Alice Song
Dan Song
Charlie Song
Bob Song
Alice Song
Dan Song
Charlie Song
Bob Song
...
```

---

## Technologies Used

- Python
- Pandas
- CSV Processing
- Tkinter
- Data Manipulation Algorithms

---

## Installation

### Prerequisites

- Python 3.9 or newer
- pandas 1.5.3

### Clone the Repository

```bash
git clone https://github.com/devilmarster/Order4Chaos.git
```

### Install Dependencies

Using requirements.txt:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas==1.5.3
```

> **Note**
>
> This project was developed and tested using pandas 1.5.3. Later versions of pandas may introduce changes or deprecations that affect compatibility.

### Run

```bash
python Order4Chaos.py
```

---

## Why I Made This

I regularly use Spotify collaborative playlists and found that they often become dominated by whichever contributor recently added a large batch of songs.

Order4Chaos was created as a way to rebalance playlists automatically while still respecting who added each track.

The project also provided an opportunity to work with data processing, file handling, algorithm design, and playlist generation logic.

---

## Future Improvements

Potential future enhancements include:

- Direct Spotify API integration
- Playlist preview interface
- Saveable ordering presets
- Contributor weighting options
- Automatic playlist recreation through Spotify
- Web-based interface

---

## Author

**Greg**

GitHub: https://github.com/devilmarster

---

## Licence

This project is provided for educational, personal, and portfolio purposes.
