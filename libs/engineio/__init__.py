import sys

from .middleware import Middleware
from .server import Server
if sys.version_info >= (3, 5):  # pragma: no cover
    from .asyncio_server import AsyncServer
    from .async_tornado import get_tornado_handler
else:  # pragma: no cover
    AsyncServer = None

__version__ = '2.3.1'

__all__ = ['__version__', 'Middleware', 'Server']
if AsyncServer is not None:  # pragma: no cover
    __all__ += ['AsyncServer', 'get_tornado_handler']
