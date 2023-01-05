# solvedpy
unofficial [solved.ac](https://solved.ac) API client for python

### Basic Usage
```python3
from solvedac import Solvedac

sa = Solvedac()
sa.set_token('YOUR_SOLVEDAC_TOEKEN_FROM_BROWSER_COOKIE')

user_info = sa.User.show('USER_HANDLE')
problems_d5 = sa.Search.problem('solvable:true+tier:21', sort='solved')
```
