# Third Party Stuff
from django.conf import settings


def resolve_frontend_url(name, site_id="frontend", **kwargs):
    """Returns the absolute url for the frontend site
    resolve_front_urls('password-confirm', token="xyz", uuid="abc")
    """
    urls = settings.FRONTEND_URLS
    path = urls[name].format(**kwargs)
    return path
