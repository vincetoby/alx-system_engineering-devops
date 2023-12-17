# READ ME

## STEPS for doing the cmd challenge tasks
- go through this link [CMD_CHALLENGE](https://cmdchallenge.com/#/files_starting_with_a_number)
- read the tasks, write code that solves the task andit keeps moving.

## STEPS for uploading screenshots with sftp
- Open your terminal
- get your username, hostname and password
	- to get username: type "whoami" on your terminal
	- to get hostname: type "hostname" on terminal
	- to create password: passwd (if you dont already have a password)

- run on the terminal: <pre><code> sftp username@hostname </pre></code>
replace username with actual username, also do the same for hostname

- input your password: note that while inputing password on terminal, it will be invisible and also case-sensitive
- navigate to the directory containing the file you need and run; 
	<pre><code> get file_name </pre></code>

- navigate to your repo/directory and do;
	<pre><code> put file_name </pre></code>
- do exit, when done, then push to Github
