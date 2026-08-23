# Flash Card Learning App

A Python desktop application that helps users learn French vocabulary through interactive flash cards. The application displays a French word, automatically flips the card after a few seconds to reveal the English translation, and tracks learning progress between sessions.

## Features

- Randomly displays French vocabulary words
- Automatically flips cards after 3 seconds
- Tracks learned words
- Saves progress between sessions
- Interactive graphical user interface built with Tkinter
- Reads and writes data using Pandas and CSV files

## Technologies Used

- Python
- Tkinter
- Pandas

## Project Structure

```text
flash-card-app/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   └── french_words.csv
│
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    ├── wrong.png
    ├── front.png
    └── back.png
```

## Screenshots

### Front of Flash Card

![Front of flash card app](images/front.png)

### Back of Flash Card

![Back of flash card app](images/back.png)

## Installation

Clone the repository:

```bash
git https://github.com/Brendo101/flash-card-app.git
cd flash-card-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## What I Learned

This project helped me gain practical experience with:

- Building desktop applications using Tkinter
- Managing application state
- Working with CSV files using Pandas
- Reading and writing persistent data
- Exception handling with try/except
- Event-driven programming
- Using timers with Tkinter's `after()` method
- Organising Python projects for source control


## Author

**Brandon Dyer-Smith**

Data & Paid Search Specialist with a growing focus on Python, analytics and data science.