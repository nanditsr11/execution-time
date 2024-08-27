## Introduction
Decorators in Python provide a powerful way to modify or enhance the behavior of a function. This script introduces a timer decorator that measures the time a function takes to execute and prints it to the console. This is particularly useful for performance testing and optimization.

## Installation
To use this script, you need to have Python installed on your system. The script uses the time module, which is included in Python’s standard library, so no additional installations are required.

## Clone this repository or download the script.
Ensure Python is installed on your system (Python 3.x recommended).

## Usage
You can use the timer decorator to measure the execution time of any function. Simply apply the @timer decorator above the function definition.

## Example
In this example, the execution_time function is decorated with the timer decorator. When called, the function will pause for 1 second (using time.sleep(1)), and the timer decorator will print the time taken to execute the function.

## Output
  The function -execution_time took 1.0001s

## Explanation
timer decorator: This decorator captures the current time before and after the execution of the decorated function. The difference between the start and end times is calculated to determine how long the function took to run.
time.sleep(1): This line in the execution_time function causes the function to pause for 1 second, simulating a time-consuming operation.

