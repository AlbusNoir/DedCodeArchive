# TODO: make gui?
# TODO: add wav files to winsound so that it's not just beeps
# TODO: test snd_nostop to see if this plays while other stuff is

from datetime import datetime
from datetime import timedelta
import winsound

class Pomodoro():
    # define timer types
    TIMER_NONE = 0
    TIMER_TASK = 1
    TIMER_SHORT_BREAK = 2
    TIMER_LONG_BREAK = 3

    def __init__(self, tl, sb, lb, tg, lbg):
        # define goals
        self.task_goal = tg
        self.task_count = 0
        self.long_break_goal = lbg

        # define task length
        #self.task_length = timedelta(minutes=25)
        self.task_length = timedelta(minutes=tl)  # testing

        # define break periods
        self.short_break = timedelta(minutes=sb)  # testing
        #self.short_break = timedelta(minutes=5)
        self.long_break = timedelta(minutes=lb)

        # initialize timer
        self.timer_type = self.TIMER_NONE

    def start_task(self):
        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.task_length
        self.timer_type = self.TIMER_TASK

        print(f'\n---- begin task {self.task_count+1} ----\n')

    def start_short_break(self):
        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.short_break
        self.timer_type = self.TIMER_SHORT_BREAK
        for i in range(0, 3):
            winsound.Beep(700, 100)
        print('\n---- break ----\n')


    def start_long_break(self):
        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.long_break
        self.timer_type = self.TIMER_LONG_BREAK

        for i in range(0, 5):
            winsound.Beep(700, 100)
        print('\n---- BREEEEEEEEEEEEEEAK ----\n')

    def complete_task(self):
        # increase task counter
        self.task_count+=1

    def done(self):
        '''
            Denotes whether the Pomodoro task goal has been met.
            Returns True if task goal has been met.  False otherwise.
        '''
        return self.task_count == self.task_goal

    def get_time_remaining(self):
        '''
            returns the amount of time remaining in the current timer in the form of a timedelta object.
        '''
        return self.timer_end - datetime.now()

    def format_timedelta(self, td):
        '''
            Formats a timedelta object to a string displaying minutes & seconds.
        '''

        # find seconds
        total_seconds = int(td.total_seconds())

        # 3600 seconds in an hour
        hours, remainder = divmod(total_seconds,3600)

        # 60 seconds in a minute
        minutes, seconds = divmod(remainder,60)

        return (f'{minutes} mins {seconds} secs')

    def print_summary(self):
        '''
            Prints a summary of the current timer type & time remaining.
        '''

        task_name = 'none'

        # format timer output
        if self.timer_type == self.TIMER_TASK:
            task_name = 'Pomo'
        elif self.timer_type == self.TIMER_SHORT_BREAK:
            task_name = 'SHORT BREAK'
        elif self.timer_type == self.TIMER_LONG_BREAK:
            task_name = 'LONG BREAK'

        # format time remaining output
        time_remaining = self.format_timedelta(self.get_time_remaining())

        print(f'\r{task_name} | time remaining: {time_remaining}', end='')

def main():
    # get some info
    task_goal = int(input('How many tasks are we doing: '))
    task_length = int(input('Enter time for Pomo: '))
    short_break = int(input('Enter short break time: '))
    long_break = int(input('Enter long break time: '))
    lbreak_goal = int(input('How many long breaks should we aim for: '))
    # create pomodoro & begin first task
    pomodoro = Pomodoro(task_length, short_break, long_break, task_goal, lbreak_goal)
    pomodoro.start_task()

    while True:

        # Initialize last_summary variable to 10 seconds in the past
        last_summary = pomodoro.timer_start - timedelta(seconds=10)

        # while the timer is running
        while pomodoro.get_time_remaining() > timedelta(seconds=0):

            current_time = datetime.now()

            # print a summary of the current timer every 10 seconds
            if (current_time - last_summary) > timedelta(seconds=10):
                pomodoro.print_summary()

                # update timer to track when the last summary was printed
                last_summary = current_time

        # if we are on a task, complete the task.  Otherwise, we start the task timer
        if pomodoro.timer_type == Pomodoro.TIMER_TASK:

            # complete the task
            pomodoro.complete_task()

            # check to see if need to continue to a break or stop the pomodoro
            if pomodoro.done():
                break
            elif pomodoro.task_count % pomodoro.long_break_goal == 0:
                pomodoro.start_long_break()
            else:
                pomodoro.start_short_break()
        else:
            pomodoro.start_task()

    # we have met our pomodoro goal
    for i in range(0, 10):
        winsound.Beep(700, 100)
    print('\nPomo Dono!')


if __name__ == '__main__':
    main()