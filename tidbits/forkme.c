/*-------------------------------------------------------------------------*/
/* forkme.c -- help perforce put a forking trigger in the background       */
/*                                                                         */
/* author: Mark Harrison, Pixar Animation Studios, mh@pixar.com            */
/*                                                                         */
/* This program is necessary because the perforce trigger mechanism hangs  */
/* a read on the triggered process, so that the typical means of putting   */
/* a process in the background won't work, since the child process         */
/* inherits the file descriptor being read.  So, in addition to the        */
/* usual fork/fork we need to close stdin and stderr.  Since this means    */
/* the trigger would lose the ability to write output, we open our own     */
/* and capture the output there.                                           */
/*                                                                         */
/* usage: forkme logfile cmdline...                                        */
/*-------------------------------------------------------------------------*/

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(argc, argv)
int argc;
char **argv;
{
    int fd;

    if (argc < 3) {
        fprintf(stderr, "usage: forkme logfile cmd...\n");
        return 1;
    }

    if ((fd = open(argv[1], O_WRONLY|O_APPEND|O_CREAT, 0666)) < 0) {
        perror(argv[1]);
        return 2;
    }

    /* create a child */
    if (fork() == 0) {
        /* create a grandchild */
        if (fork() == 0) {
            /* perforce, we shall not be foiled by your dastardly file */
            /* machinations!  We shall close stdin and stdout so that  */
            /* your hanging read will get an eof and you will contine  */
            /* your processing, and then capture stdin and stdout      */
            /* for our own logfile!                                    */
            close(1);
            close(2);
            dup(fd);
            dup(fd);
            argv += 2;
            argc -= 2;
            execvp(argv[0], argv);
            perror(argv[0]);
        }
        else {
            /* child dies */
            return 0;
        }
    }
    /* wait for the child to die, to ensure the granchild is adopted */
    wait(0);
    return 0;
}
