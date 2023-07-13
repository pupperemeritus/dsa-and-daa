from typing import List


class Job:
    def __init__(self, item_number: int, deadline, profit):
        self.item_number = item_number + 1
        self.deadline = deadline
        self.profit = profit

    def __repr__(self) -> str:
        return f"Item Number : {self.item_number}\nDeadline : {self.deadline}\nProfit : {self.profit}\n"


def job_sequencer(jobs: List[Job]):
    """
    Sorts a list of jobs by non-increasing profit and schedules them based on their deadlines.

    Parameters:
        jobs (List[Job]): A list of Job objects representing the jobs to be scheduled.

    Returns:
        List[Job]: A list of Job objects representing the schedule of jobs.
    """
    # Sort jobs by non-increasing profit
    jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)
    # Find the maximum deadline
    max_deadline = max(job.deadline for job in jobs)
    # Initialize the schedule
    schedule = [None] * max_deadline
    # Iterate over each job in order of decreasing profit
    for job in jobs:
        # Find the latest available slot before the job's deadline
        for i in range(job.deadline - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = job
                break

    # Remove any empty slots from the schedule
    schedule = [job for job in schedule if job is not None]

    return schedule


if __name__ == "__main__":
    profit = [100, 19, 27, 25, 15]
    deadline = [2, 1, 2, 1, 3]
    jobs = [Job(i, deadline[i], profit[i]) for i in range(len(deadline))]
    print(job_sequencer(jobs))
