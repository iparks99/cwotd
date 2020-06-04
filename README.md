# Chinese Word of the Day
#### v1.0.0

Chinese word of the day (cwotd) is a Python script that chooses a random word from HSK lists (or any CSV) on a daily basis.

## Installation

Simply download the Python script. I have also included the HSK1-6 word lists as appropriate CSV files.

## Usage

cwotd reads all the arguments as files, except for the ```-r``` flag, which means to use a random seed instead of the current date. Excluding this flag gives a constant word throughout the day.

Custom CSV files should follow this format:
```<simplified>,<traditional>,<pinyin_numbers>,<pinyin>,<english>```
An example would be:
```不客气,不客氣,bu2 ke4qi5,bú kèqi,you're welcome; don't be polite```

```
python cwotd.py HSK1.csv HSK2.csv
./cwotd.py my_words.csv -r
```
