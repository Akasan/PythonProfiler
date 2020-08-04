import cProfile
import pstats


def profiler(func):
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        profile.runcall(func, *args, **kwargs)
        ps = pstats.Stats(profile)
        ps.print_stats()

    return wrapper
