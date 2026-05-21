# Name: YOUR NAME
# Student Number: 23XXXXXX

class Leaderboard:
    """A leaderboard of speedrunning record times.

    Each entry has a time in seconds and a runner name.
    Runners may submit multiple runs.
    The leaderboard is ranked fastest run first.
    Ties receive the same rank as each other, so for example if runners submit
    the times 10, 20, 20, and 30, they will have the ranks 1, 2, 2, and 4.
    """

    def __init__(self, runs=[]):
        """Constructs a leaderboard with the given runs.

        The given list of runs is not required to be in order.

        Args:
            runs: Initial leaderboard entries as list of (time, name) pairs.
        """
        pass

    def get_runs(self):
        """Returns the current leaderboard.

        Leaderboard is given in rank order, tie-broken by runner name.

        Returns:
            The current leaderboard as a list of (time, name) pairs.
        """
        pass

    def submit_run(self, time, name):
        """Adds the given run to the leaderboard

        Args:
            time: The run time in seconds.
            name: The runner's name.
        """
        pass

    def get_rank_time(self, rank):
        """Get the time required to achieve at least a given rank.

        For example, `get_rank_time(5)` will give the maximum possible time
        that would be ranked fifth.

        Args:
            rank: The rank to look up.

        Returns:
            The time required to place `rank`th or better.
        """
        pass

    def get_possible_rank(self, time):
        """Determine what rank the run would get if it was submitted.

        Does not actually submit the run.

        Args:
            time: The run time in seconds.

        Returns:
            The rank this run would be if it were to be submitted.
        """
        pass

    def count_time(self, time):
        """Count the number of runs with the given time.

        Args:
            time: The run time to count, in seconds.

        Returns:
            The number of submitted runs with that time.
        """
        pass
