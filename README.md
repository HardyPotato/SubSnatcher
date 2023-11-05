# Subtitle Downloader

Subtitle Downloader is a Python-based graphical user interface (GUI) application that leverages the OpenSubtitles XML-RPC API to search for and download movie subtitles.

## Features

- **Search**: Look up subtitles by movie titles.
- **List Subtitles**: View a list of available subtitles after searching.
- **Download**: Select and download subtitles to your computer.
- **GUI**: A simple and intuitive graphical interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x installed on your system. If you do not have Python installed, download it from [python.org](https://www.python.org/downloads/).

Additionally, the `requests` module is required which can be installed using pip:

```shell
pip install requests
```

## Installing
First, clone this repository to your local machine:

```shell
git clone https://github.com/<your-github-username>/subtitle-downloader.git
```

Navigate to the directory where you cloned the repository:

```shell
cd subtitle-downloader
```

Run the application:

```shell
python subtitle_downloader.py
```

The GUI should appear where you can start interacting with the application.

## Usage
To download subtitles:

- Enter the movie name in the text field.
- Click 'Search Subtitles' to display a list of available subtitles.
- Select the desired subtitle from the list.
- Click 'Download Selected Subtitle' to save the subtitle to your machine.
