# 0x05. Processes and Signals

## A project on:
- What is a process, signal and PID
- How to find the PID
- How to start and kill processes
- How to work with background processes

## Requirements
- All  files are interpreted/compiled on Ubuntu 14.04 LTS
- Bash script must pass Shellcheck

## Challenges
- **[0-what-is-my-pid](0-what-is-my-pid)**: Bash script that displays its PID
- **[1-list_your_processes](1-list_your_processes)**: Bash script that displays a list of currently running processes in user oriented format wit process hierarchy
- **[2-show_your_bash_pid](2-show_your_bash_pid)**: Bash script that displays currently running process containing `bash`
- **[3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy)**: Bash script that displays the PID, along with the process name, of processes which name contains the word bash
- **[4-to_infinity_and_beyond](4-to_infinity_and_beyond)**: Bash script that displays `To infinity and beyond` indefinitely
- **[5-kill_me_now](5-kill_me_now)**: Bash script that kills `4-to_infinity_and_beyond` process
- **[6-kill_me_now_made_easy](6-kill_me_now_made_easy)**: Bash script that kills `4-to_infinity_and_beyond` process
- **[7-highlander](7-highlander)**: Infinate process killed by `67-kill_me_now_made_easy`
- **[8-beheaded_process](8-beheaded_process)**: Bash script that kills the process `7-highlander`
- **[100-process_and_pid_file](100-process_and_pid_file)**: Bash script that:

	- Creates the file `/var/run/holbertonscript.pid` containing its PID
	- Displays `To infinity and beyond` indefinitely
	- Displays `I hate the kill command` when receiving a SIGTERM signal
	- Displays `Y U no love me?!` when receiving a SIGINT signal
	- Deletes the file `/var/run/holbertonscript.pid` and terminate itself when receiving a SIGQUIT or SIGTERM signal

- **[101-manage_my_process](101-manage_my_process)**: Very basic init script that manages `manage_my_process`
