# solvedpy
Unofficial [solved.ac](https://solved.ac) API Client for Python

### Basic Usage
```python3
from solvedpy import Client

cl = Client()
cl.set_token('YOUR_SOLVEDAC_TOEKEN_FROM_BROWSER_COOKIE')

user_info = cl.User.show('USER_HANDLE')
problems_d5 = cl.Search.problem('solvable:true+tier:21', sort='solved')
```
