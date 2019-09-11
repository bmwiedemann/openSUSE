/*
 * wrapper.c - wrapper program around man and mandb
 *
 * Copyright (C) 2000 Fabrizio Polacco <fpolacco@debian.org>
 * Copyright (C) 2001, 2002 Colin Watson.
 *
 * This file is part of man-db.
 *
 * man-db is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * man-db is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with man-db; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */

#ifdef HAVE_CONFIG_H
#  include "config.h"
#endif /* HAVE_CONFIG_H */

#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <grp.h>
#include <pwd.h>
#include <grp.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>

#include "dirname.h"

#include "gettext.h"
#include <locale.h>
#define _(Text) gettext (Text)

#include "manconfig.h"


/* this list is used to authenticate the program running.
 * it is fixed at compile time to avoid a full class of 
 * dangers ...
 */
static struct {
	const char *prog;
	const char *run;
	const char *user;
} *wlp, wrapped_list[] =
{ /* prog	run				user	*/
#ifdef DEBUG
  { "_man",	"src/man",	"man"	},
  { "_mandb",	"src/mandb",	"man"	},
#endif
  { "man",	"/usr/lib/man-db/man",		"man"	},
  { "mandb",	"/usr/lib/man-db/mandb",	"man"	},
  { 0,		0,				0,	}};

char *program_name;

int main (int argc, char **argv, char *envp[])
{
	extern char **environ;
	uid_t ruid, euid;
	gid_t rgid;

	argc = argc; /* not used */

	/* We don't warn about this setlocale() call failing, as the program
	 * we call will do that.
	 */
	setlocale (LC_ALL, "");
	bindtextdomain (PACKAGE, LOCALEDIR);
	bindtextdomain (PACKAGE "-gnulib", LOCALEDIR);
	textdomain (PACKAGE);

	/* this wrapper can be run as "man" or as "mandb" */
	program_name = base_name (argv[0]);

	ruid = getuid ();
	euid = geteuid();
	rgid = getgid ();

	/* The various preprocessors should be in standard path */
	environ = envp;
	setenv("PATH", "/bin:/usr/bin", 1); 
	envp = environ;

#ifdef DEBUG
	printf ("%s:\n", program_name);
#endif

	for (wlp = wrapped_list; wlp->prog && strcmp (program_name, wlp->prog); ++wlp)
		/* __asm__ __volatile__("": : :"memory") */;
	if (!wlp->prog) {
		fprintf (stderr, _("Don't know which program should I run being >%s<\n"),
			 program_name);
		return -ENOENT;
	}
#ifdef DEBUG
	printf ("%s\n", wlp->run);
#endif
	if (strcmp("man", wlp->prog) == 0)
		/* Short cut: do not map man command to an other user */
		goto man;

	if (ruid == 0 || euid == 0) {
		static char *dummy_environ[] = { NULL };
		extern char **environ;
		struct passwd *pwd;
		char *cwd;

		pwd = getpwnam (wlp->user);
		if (!pwd) {
			fprintf (stderr, _("%s: Failed su to user %s\n"), wlp->prog, wlp->user);
			return -EACCES;
		}
		if (ruid == 0) {
			ruid = pwd->pw_uid;
			rgid = pwd->pw_gid;
		} else {
#ifndef MAN_CATS
			/* No permissions required to create files
			 * under the sub directories of /var/cache/man */
			pwd->pw_uid = ruid;
			pwd->pw_gid = rgid;
#endif
		}
		if ((cwd = get_current_dir_name()) == NULL) {
			fprintf (stderr, _("%s: Failed su to user %s\n"), wlp->prog, wlp->user);
			return -EACCES;
		}
		if (setregid (rgid, pwd->pw_gid)) {
			fprintf (stderr, _("%s: Failed su to user %s\n"), wlp->prog, wlp->user);
			return -EACCES;
		}
		if (initgroups (wlp->user, rgid)) {
			fprintf (stderr, _("%s: Failed su to user %s\n"), wlp->prog, wlp->user);
			return -EACCES;
		}
		if (setreuid (ruid, pwd->pw_uid)) {
			fprintf (stderr, _("%s: Failed su to user %s\n"), wlp->prog, wlp->user);
			return -EACCES;
		}
		if (access(cwd, X_OK) < 0 && chdir(pwd->pw_dir)) {
			fprintf (stderr, _("%s: Failed su to user %s\n"), wlp->prog, wlp->user);
			return -EACCES;
		}
		free(cwd);

		cwd = getenv("TERM");
		environ = dummy_environ;
		setenv("HOME", pwd->pw_dir, 1);
		setenv("PATH", "/bin:/usr/bin", 1);
		setenv("USER", pwd->pw_name, 1);
		setenv("LOGNAME", pwd->pw_name, 1);
		if (cwd)
			setenv("PWD", cwd, 1);
		envp = environ;
	}
man:
	execve (wlp->run, argv, envp);
	perror ("execve");
	return -errno;
}
