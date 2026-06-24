from apscheduler.schedulers.blocking import BlockingScheduler
import os

scheduler = BlockingScheduler()


@scheduler.scheduled_job("interval", minutes=1)
def run_report():
    print("Running scheduled report generation...")
    os.system("py run_final_report.py")


if __name__ == "__main__":
    print("Scheduler started...")
    scheduler.start()