#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - entry point
 *
 * Description: makes five zombies
 * Return: 0 for success
 */

int main(void)
{
	int i;
	pid_t mypid;

	i = 0;
	while (i < 5)
	{
		mypid = fork();
		if (mypid)
			printf("Zombie process created, PID: %i\n", mypid);
		else
			exit(0);
		i++;
	}
	sleep(100);
	return (0);
}
