from pynetbox.core.query import RequestError, AllocationError, ContentError
from pynetbox.core.api import Api as api

try:
    from pkg_resources import get_distribution, DistributionNotFound

    __version__ = get_distribution(__name__).version
except ModuleNotFoundError:
    pass
except DistributionNotFound:
    pass
