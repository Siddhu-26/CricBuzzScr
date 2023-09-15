# CricBuzzScr

A python library to get live score from [Cricbuzz](https://www.cricbuzz.com)

## Installation

```bash
pip install CricBuzzScr
```

## Usage

### Importing the package

```python

import CricBuzzScr.match as cbs

```

### Methods available

* get_match - This method will give links of the matches listed in the website and will return the url of the match you select.

* get_commentary - This method will give you the Score, Batsman's name, Bowler's name, key stats, recent balls, and the commentary of last 2 overs.

* get_scorecard - This method will give you the Scorecard of the match.

#### get_match
```python

match = cbs.get_match() # This will have the link of the match which you will be using for the get_commentary and get_scorecard methods
```

#### get_commentary

If you are not using in jupyter notebook.

```python
cbs.get_commentary(match) 
```

If you are using jupyter notebook.

```python
from IPython.display import clear_output

while True:
    clear_output(wait= False)
    cbs.get_commentary(match)
    time.sleep(10)
```
This will clear the cell output and will be running till you interrupt.

#### get_scorecard

```python
cbs.get_commentary(match)
```
This will give the scorecard of the match.