# Note Convertor

## About

**Note Convertor** is a small desktop application with a graphical interface (Python/Tkinter) that converts a grade from one scale to another. You enter your grade, the maximum of its original scale, and the scale you want to convert it to. The result is displayed instantly. The interface is in French.

For example, a grade of 15/25 converted to a scale of 20 gives 12/20.

## Getting started

### Installation

1. Download and launch [NoteConvertor.exe](NoteConvertor.exe)
2. Else, download [note_convertor.py](note_convertor.py) and launch it with python 3.13
## Features

- Convert a grade to any scale (out of 20, 10, 100...)
- Simple interface with three fields and an instant result

## Usage

1. In **Convertir la note sur**, enter the scale you want to convert to (e.g. `20`).
2. In **Note actuelle**, enter your current grade (e.g. `15`).
3. In **Note maximale**, enter the maximum of the original scale (e.g. `25`).
4. The result appears under **Le résultat est** (e.g. `12.0 / 20`).

The result is calculated as: `current grade ÷ maximum grade × target scale`.

### 2. Set the delay and the timer
- **Delta minimum / Delta maximum (sec):** the program waits a random time between these two values before switching to the next page. A very small gap between the two is not recommended, since the pattern would be too regular and could be spotted more easily by browsers.
- **AutoStop (optional):** tick the box and enter a duration in minutes. The program stops by itself when the time is up.

### 3. Run
1. Click **Start** to launch.
2. Click **Stop** to end the program. A page confirms that it has stopped.

## Credits

- **Author**: [MarceauMRS](https://github.com/MarceauMRS)

## License

Distributed under the [GNU GPL v3.0](LICENSE).
