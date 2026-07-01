Final project
Toni Falodun
February 19, 2026

Purpose:
This project will be a system that monitors a set of network targets, records results, and produces structured results.


Final Project Reflection: 

My program is a system that checks the status of network targets on a network and records the results log files. 
Each device is represented as a target, and the program checks whether it is up or down. After collecting this 
information, the program formats the results and saves them into a log and JSON file for later use. This makes it easier 
to track the status of multiple devices without checking each one manually.

The program is organized into multiple files, each responsible for a specific part of the network scanning process. 
This separation helps keep the code clean, easier to manage, and simpler to debug. The program starts in main.py, which
is responsible for running the program and coordinating the different parts of the system. It brings everything together
by calling functions from the other modules. The network_client.py file handles the network-related logic. This is where
the program would connect to or simulate checking devices on the network and determine their status (such as UP or DOWN).
It performs the pinging of the target to determine the status. The engine.py module contains the main processing logic.
It takes the results from the network checks and creates a log file with structured data, including target name, status,
and timestamps. The datastore.py file is responsible for loading and storing the list of target devices used in the
program. It contains a class called TargetList, which is used to manage all the devices in one central place. Last, 
the models.py file defines the data structure used throughout the program. It contains a class called Target, which
represents a single device on the network.

The hardest part of this project was making sure all the different parts worked together correctly. Even though
individual sections of the code might work on their own, the program would break if even one small part had an error. 
Debugging felt like a scavenger hunt because fixing one issue sometimes caused another problem to appear. A lot of time
was spent running the program, finding errors, and then trying to understand what caused them. This cycle repeated many 
times, and it showed how important it is for all parts of a program to be connected correctly and written carefully.
This also showed me the importance of working in small steps, which allowed me to debug at every stage, rather than
having a whole mess to debug when I finished. This definitely made the process much simpler and quicker. 

One of the main things I learned was how useful classes are. Before this project, classes were not very clear to me, but
now I understand that they help organize data in a structured way. Instead of handling separate variables, I can group 
related information together in an object, which makes the code cleaner and easier to manage. I also learned how
important working with files is. Writing data to a JSON file allows the program to store results in a format that can be
reused or analyzed later. This is especially useful for real-world applications where data needs to be saved instead of
just displayed temporarily. I also learned more about networking concepts through the idea of scanning devices on a
network. This project helped me understand how information about multiple machines can be collected efficiently and
simultaneously. Error handling turned out to be very important in this project. Before, I did not fully understand its
purpose, but now I see that it helps prevent programs from crashing and makes errors easier to understand. Instead of
confusing Python error messages, proper error handling can explain what went wrong in a clearer way. It also helps the
program continue running instead of stopping completely when something goes wrong, which is very useful.

If I had more time, I would improve the program by adding a graphical user interface using the tools we learned 
in class. This would make the program feel more like a real network scanning application instead of just a capstone
project. The GUI would allow users to interact with the program through buttons, windows, and visual results, making it
much easier to view and understand the status of each device on the network. Adding a GUI would also make the results 
more organized and visually clear, since users could see device status updates in real time instead of reading raw text
output or a JSON file. This would make the program feel closer to a real-world IT or cybersecurity tool, where
professionals rely on dashboards and visual interfaces to monitor systems efficiently.

Overall, this project helped me understand how automation can be used to monitor systems in a network. It shows how
professionals in IT or cybersecurity can quickly scan multiple machines and collect data at a fast speed without doing
everything manually, saving time. Even though the program is simple, it represents real-world ideas like automation,
efficiency, and system monitoring. It also showed me how important it is for all parts of a program to work together 
correctly in order for the whole system to function.