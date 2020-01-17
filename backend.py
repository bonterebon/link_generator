import requests
import clipboard
from requests import auth


class BearerAuth(auth.AuthBase):
    token = None

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['authorization'] = 'Bearer ' + self.token
        return r


def get_token(cluster, username, password):
    endpoint = f'http://{cluster}-user.olacamera.com/connect/token'
    data = {'grant_type': 'password',
            'client_id': f'{cluster}_ro.client',
            'userName': username,
            'password': password}
    resp = requests.post(endpoint, data=data)
    resp_body = resp.json()

    return resp_body['access_token']


def get_feed_id(cluster, token):
    endpoint = f'http://{cluster}-user.olacamera.com/api/FeedsManager/GetFeeds'
    resp = requests.get(endpoint, auth=BearerAuth(token))
    resp_body = resp.json()

    return resp_body['feeds'][0]['feedId']


def generate_link(cluster, feed_id, start, end, token):
    link = f'https://{cluster}-user.olacamera.com/api/FeedStreamingManager/{feed_id}/instantplayback/' \
           f'index.m3u8?from={start}Z&to={end}Z&access_token={token}'
    clipboard.copy(link)
    return link
