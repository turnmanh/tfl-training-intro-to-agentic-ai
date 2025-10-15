# Task: Tool Creation 

We have outlined the tasks on writing tools for the agent. In general, tools
serve as external functions that the agent can call to perform specific actions
with - so called **actuators**.

They can also be helpful to break down complex problems into smaller, more
manageable and provide specific functionalities that the agent can leverage to
achieve its goals. E.g., instead of using a complex web interface, the agent can
call simple, well-defined functions to perform specific tasks. This mitigates
any confusions that may arise from the complexity of the web interface and thus,
requiring lots of tokens.

## Task 1 - Writing regular tools 

You can find a sample tool in `./weather_tools.py`, which is essentially just a
placeholder as it cannot do anything useful up to now. The tool itself is
provided to the agent via the list of `tools`, created in `./__init__.py`.

Your **task** is to implement a useful tool that can be used by the agent. Feel
free to tackle any problem you like, not necessarily related to weather. 

In case you don't know where to start, here are some ideas:
- A tool for integer calculations (e.g., addition, subtraction, multiplication,
  division)
- A tool for unit conversions (e.g., kilometers to miles, Celsius to Fahrenheit)
- A tool for date and time manipulations (e.g., calculating the difference
  between two dates, adding days to a date)
- ...
- And if you're curious, write a tool for searching the web (e.g., using a search engine API s.a. tavily)

## Task 2 - Adding tools to a toolkit 

