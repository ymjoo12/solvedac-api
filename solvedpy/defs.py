import requests
# from bs4 import BeautifulSoup as bs


class Config:
    
    session = None
    base_url = None
    urls = {}
    
    def __init__(self, base_url: str, urls: dict={}, headers: dict={}, cookies: dict={}):
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=50, pool_maxsize=50)
        self.session.mount('https://', adapter)
        self.session.headers.update(headers)
        self.session.cookies.update(cookies)
        
        self.base_url = base_url
        self.urls = { **urls, 'base': base_url }
        
    def requests(self, path='', url_key='base', **kwargs):
        if path:
            kwargs['url'] = self.urls[url_key] + path
        response = self.session.request(**kwargs)
        if response.status_code >= 400:
            if response.headers['Content-Type'].startswith('application/json'):
                raise Exception(f'API error: {response.status_code} {response.reason} / {response.url}\n{response.json()}')
            else:
                raise Exception(f'HTTP error: {response.status_code} {response.reason} / {response.url}')
        if response.headers['Content-Type'].startswith('application/json'):
            return response.json()
        # elif response.headers['Content-Type'].startswith('text/html'):
        #     return bs(response.text, 'lxml')
        else:
            return response.content


class Model:
    
    def __init__(self, config: Config, name: str=None, pre_path: str=None):
        self.name = (f'/{pre_path}' if pre_path else '') + (f'/{name}' if name else '')
        self.config = config
        
    def api(self, method: str, path: str='', **kwargs):
        return self.config.requests(method=method, path=f'{self.name}{path}', **kwargs)
    

class Utils:
    
    @staticmethod
    def get_file_from_url(url: str, file_name: str, file_type: str):
        response = requests.get(url, stream=True)
        if response.status_code >= 400:
            raise Exception(f'Failed to download image "{url}": {response.status_code} {response.reason}')
        return (file_name, response.content, file_type)
