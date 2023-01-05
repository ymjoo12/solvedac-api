from defs import Config, Model, Utils
from typing import List, Tuple, Literal, LiteralString


class Solvedac:
    
    def __init__(self, token: str=None):
        self.config = SolvedacConfig(token)
        
        self.User = User(self.config)
        self.Search = Search(self.config)
        self.Problem = Problem(self.config)
        self.Tag = Tag(self.config)
        self.Ranking = Ranking(self.config)
        
        self.Account = Account(self.config)
        self.Coins = Coins(self.config)
        self.Badge = Badge(self.config)
        self.Background = Background(self.config)
        
        self.Site = Site(self.config)
        self.Event = Event(self.config)
        self.Post = Post(self.config)


class SolvedacConfig(Config):
    
    API_URL = 'https://solved.ac/api/v3'
    
    def __init__(self, token: str=None):
        self.token = token
        super().__init__(
            base_url=self.API_URL,
            cookies={ 'solvedacToken': token } if token else None,
        )
    
    def set_token(self, token: str=None):
        self.token = token
        self.session.cookies.update({ 'solvedacToken': token })


class User(Model):
    
    HistoryTopic = Literal['rating', 'ratingRank', 'exp', 'solvedCount', 'voteCount']
    
    def __init__(self, config: Config):
        super().__init__(config, 'user')
    
    def show(self, handle: str):
        return self.api('GET', f'/show', params={ 'handle': handle })
    
    def problem_stats(self, handle: str):
        return self.api('GET', f'/problem_stats', params={ 'handle': handle })
    
    def class_stats(self, handle: str):
        return self.api('GET', f'/class_stats', params={ 'handle': handle })
    
    def contribution_stats(self, handle: str):
        return self.api('GET', f'/contribution_stats', params={ 'handle': handle })
    
    def problem_tag_stats(self, handle: str):
        return self.api('GET', f'/problem_tag_stats', params={ 'handle': handle })
    
    def top_ratings(self, handle: str):
        return self.api('GET', f'/top_ratings', params={ 'handle': handle })
    
    def top_100(self, handle: str):
        return self.api('GET', f'/top_100', params={ 'handle': handle })
    
    def grass(self, handle: str, topic: str='today-solved'):
        return self.api('GET', f'/grass', params={ 'handle': handle, 'topic': topic })
    
    def history(self, handle: str, topic: HistoryTopic='solved'):
        return self.api('GET', f'/history', params={ 'handle': handle, 'topic': topic })
    
    def votes(self, handle: str, page: int=1):
        return self.api('GET', f'/votes', params={ 'handle': handle, 'page': page })
    
    def available_badges(self, handle: str):
        return self.api('GET', f'/available_badges', params={ 'handle': handle })
    
    def available_backgrounds(self, handle: str):
        return self.api('GET', f'/available_backgrounds', params={ 'handle': handle })
    
    def bans(self, handle: str):
        return self.api('GET', f'/bans', params={ 'handle': handle })


class Search(Model):
    
    SortType = Literal['id', 'level', 'title', 'solved', 'average_try', 'random']
    
    def __init__(self, config: Config):
        super().__init__(config, 'search')
        
    def problem(self, query: str, page: int=1, sort: SortType='id', asc: bool=True):
        return self.api('GET', f'/problem', params={ 
            'query': query, 'page': page,
            'sort': sort,'direction': 'asc' if asc else 'desc', 
        })
    
    def suggestion(self, query: str=''):
        self.api('GET', f'/suggestion', params={ 'query': query })
    
    def tag(self, query: str, page=1):
        self.api('GET', f'/tag', params={ 'query': query, 'page': page })
    
    def user(self, query: str, page=1):
        self.api('GET', f'/user', params={ 'query': query, 'page': page })


class Problem(Model):
    
    def __init__(self, config: Config):
        super().__init__(config, 'problem')
    
    def show(self, problem_id: int):
        return self.api('GET', f'/show', params={ 'problemId': problem_id })
    
    def lookup(self, problem_ids: List[int]):
        return self.api('GET', f'/lookup', params={ 'problemIds': ','.join(map(str, problem_ids)) })
    
    def sprout(self):
        return self.api('GET', f'/sprout_lookup')
    
    def count_by_class(self):
        return self.api('GET', f'/class')
    
    def count_by_level(self):
        return self.api('GET', f'/level')


class Tag(Model):
    
    def __init__(self, config: Config):
        super().__init__(config, 'tag')
    
    def list(self):
        return self.api('GET', '/list')
    
    def show(self, tag_id: int):
        return self.api('GET', f'/{tag_id}/show')
    

class Ranking(Model):
    
    IndvType = Literal['tier', 'class', 'streak', 'contribution', 'rival', 'reverse_rival']
    OrgType = Literal['university', 'company', 'community', 'high_school', 'middle_school', 'elementary_school', 'undefined']

    def __init__(self, config: Config):
        super().__init__(config, 'ranking')

    def indivisual(self, type: IndvType, page: int=1):
        return self.api('GET', f'/{type}', params={ 'page': page })

    def organization(self, type: OrgType, page: int=1):
        return self.api('GET', f'/organization', params={ 'type': type, 'page': page })


class Account(Model):
        
    def __init__(self, config: Config):
        super().__init__(config, 'account')
            
    def verify_credentials(self):
        return self.api('GET', '/verify_credentials')
        
    def inventory(self):
        return self.api('GET', '/inventory')
    
    def use_item(self, item_id: str):
        return self.api('POST', '/use_item', data={ 'itemId': item_id })
    
    def coin_history(self, year: int=None, month: int=None):
        return self.api('GET', '/coin_history', params={ 'year': year, 'month': month })
    
    def coin_exchange(self, amount: int, to_coin: bool=True):
        return self.api('POST', '/coin_exchange', data={ 'amount': amount, 'to': 'coin' if to_coin else 'stardusts' })

    def redeem(self, code: str):
        return self.api('POST', '/redeem', data={ 'code': code })
    
    def update_bio(self, bio: str):
        return self.api('PATCH', '/update_bio', data={ 'bio': bio })
    
    def update_badge(self, badge_id: int):
        return self.api('PATCH', '/update_badge', data={ 'badgeId': badge_id })
    
    def update_background(self, background_id: str):
        return self.api('PATCH', '/update_background', data={ 'backgroundId': background_id })
    
    def update_picture(self, picture: Tuple[LiteralString, bytes, LiteralString]):
        return self.api('PATCH', '/update_picture', files={ 'picture': picture })
    
    def update_picture_by_url(self, image_url: str):
        file = Utils.get_file_from_url(image_url)
        return self.change_profile_image(file)
    
    
class Coins(Model):
    
    def __init__(self, config: Config):
        super().__init__(config, 'coins')
        
    def shop_list(self):
        return self.api('GET', '/shop/list')
    
    def shop_buy(self, sku_id: int):
        return self.api('POST', '/shop/buy', data={ 'skuId': sku_id })
    
    def exchange_rate(self):
        return self.api('GET', '/exchange_rate')
    
    def exchange_rate_history(self):
        return self.api('GET', '/exchange_rate_history')

    
class Achivement(Model):
    
    SortType = Literal['added', 'unlockedUserCount']
    
    def __init__(self, config: Config, name: str):
        super().__init__(config, name)
        
    def list(self, page: int = 1, sort: SortType = 'added', asc: bool = True):
        return self.api('GET', '/list', params={ 'page': page, 'sort': sort, 'direction': 'asc' if asc else 'desc' })
    
    def show(self, badge_id: str):
        return self.api('GET', f'/show', params={ 'badgeId': badge_id })
    
    def unlocked_users(self, badge_id: str, page: int=1, sort: str='unlocked', asc: bool=True):
        return self.api('GET', f'/unlocked_users', params={ 
            'badgeId': badge_id, 'page': page, 
            'sort': sort, 'direction': 'asc' if asc else 'desc' 
        })


class Badge(Achivement):
    
    def __init__(self, config: Config):
        super().__init__(config, 'badge')


class Background(Achivement):
    
    def __init__(self, config: Config):
        super().__init__(config, 'background')


class Site(Model):
    
    def __init__(self, config: Config):
        super().__init__(config, 'site')
        
    def stats(self):
        return self.api('GET', '/stats')
    

class Event(Model):
    
    def __init__(self, config: Config):
        super().__init__(config, 'event')
    
    def status(self, event_id: int):
        return self.api('GET', f'/{event_id}/status')
    

class Post(Model):
    
    def __init__(self, config: Config):
        super().__init__(config, 'post')
    
    def show(self, post_id: str):
        return self.api('GET', f'/show', params={ 'postId': post_id })