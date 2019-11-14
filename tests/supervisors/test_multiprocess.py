from uvicorn import Config
from uvicorn.supervisors import Multiprocess


def test_multiprocess_run():
    """
    A basic sanity check.

    Simply run the supervisor against a no-op server, and signal for it to
    quit immediately.
    """
    config = Config(app=None, workers=2)
    supervisor = Multiprocess(config, sockets=[])
    supervisor.startup()
    supervisor.shutdown(hard=True)
